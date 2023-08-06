""" Implements Maturin as a build system for kraken-std. """

from __future__ import annotations

import logging
import os
import shutil
import subprocess as sp
from pathlib import Path
from typing import Collection

from kraken.common.path import is_relative_to
from kraken.common.pyenv import VirtualEnvInfo, get_current_venv

from ...cargo.manifest import CargoMetadata
from ..pyproject import Pyproject
from ..settings import PythonSettings
from . import ManagedEnvironment
from .poetry import PoetryManagedEnvironment, PoetryPythonBuildSystem

logger = logging.getLogger(__name__)


class MaturinPythonBuildSystem(PoetryPythonBuildSystem):
    """A maturin-backed version of the Poetry build system, that invokes the maturin build-backend.
    Can be enabled by adding the following to the local pyproject.yaml:
    ```toml
    [tool.poetry.dev-dependencies]
    maturin = "0.13.7"

    [build-system]
    requires = ["maturin>=0.13,<0.14"]
    build-backend = "maturin"
    ```
    """

    name = "Maturin"

    def __init__(self, project_directory: Path) -> None:
        super().__init__(project_directory)
        self._default_build = True
        self._zig_targets: Collection[str] = ()
        self._zig_features: Collection[str] = ()
        self._macos_sdk_root: Path | None = None

    def disable_default_build(self) -> None:
        self._default_build = False

    def enable_zig_build(
        self,
        targets: Collection[str] = (),
        features: Collection[str] = (),
        macos_sdk_root: Path | None = None,
    ) -> None:
        """
        :param targets: list of Rust targets to cross-compile to using zig.
                        For example "x86_64-unknown-linux-gnu" or "aarch64-apple-darwin".
                        Requires the `maturin[zig]` pip package.
                        These targets should be installed with Cargo.
        :param features: Cargo features to enable for zig builds. If zig is used, it should be at least `pyo3/abi3`
                         or another feature depending on `pyo3/abi3` (`pyo3/abi3-py38`...).
        :param macos_sdk_root: For zig builds targeting macOS, the path to the MacOS SDK to use.
                               By default, the `SDKROOT` environment variable is used as a fallback.
                               Not useful when compiling from macOS.
        """
        self._zig_targets = targets
        self._zig_features = features
        self._macos_sdk_root = macos_sdk_root

    def get_managed_environment(self) -> ManagedEnvironment:
        return MaturinManagedEnvironment(self.project_directory)

    def update_pyproject(self, settings: PythonSettings, pyproject: Pyproject) -> None:
        super().update_pyproject(settings, pyproject)
        pyproject.synchronize_project_section_to_poetry_state()

    def build(self, output_directory: Path, as_version: str | None = None) -> list[Path]:
        # We set the version
        old_poetry_version = None
        old_project_version = None
        pyproject_path = self.project_directory / "pyproject.toml"
        if as_version is not None:
            pyproject = Pyproject.read(pyproject_path)
            old_poetry_version = pyproject.set_poetry_version(as_version)
            old_project_version = pyproject.set_core_metadata_version(as_version)
            pyproject.save()

        # We cleanup target dir
        metadata = CargoMetadata.read(self.project_directory)
        dist_dir = metadata.target_directory / "wheels"
        if dist_dir.exists():
            shutil.rmtree(dist_dir)

        # We enable virtualenv
        env = os.environ.copy()
        if get_current_venv(env) is None:
            VirtualEnvInfo(self.get_managed_environment().get_path()).activate(env)

        # We run the actual build
        if self._default_build:
            command = ["maturin", "build", "--release"]
            logger.info("%s", command)
            sp.check_call(command, cwd=self.project_directory, env=env)
        for target in self._zig_targets:
            command = [
                "maturin",
                "build",
                "--release",
                "--zig",
                "--target",
                target,
                "--features",
                ",".join(self._zig_features),
            ]
            logger.info("%s", command)
            if target.endswith("-apple-darwin"):
                if self._macos_sdk_root is not None:
                    env["SDKROOT"] = str(self._macos_sdk_root.resolve())
                elif "SDKROOT" not in env:
                    logger.error(f"No macOS SDKROOT set for the target {target}")
            sp.check_call(command, cwd=self.project_directory, env=env)

        # We get the output files
        src_files = list(dist_dir.iterdir())
        dst_files = [output_directory / path.name for path in src_files]
        for src, dst in zip(src_files, dst_files):
            shutil.move(str(src), dst)

        # Unless the output directory is a subdirectory of the dist_dir, we remove the dist dir again.
        if not is_relative_to(output_directory, dist_dir):
            shutil.rmtree(dist_dir)

        if as_version is not None:
            # We roll back the version
            pyproject = Pyproject.read(pyproject_path)
            pyproject.set_poetry_version(old_poetry_version)
            pyproject.set_core_metadata_version(old_project_version)
            pyproject.save()

        return dst_files


class MaturinManagedEnvironment(PoetryManagedEnvironment):
    def install(self, settings: PythonSettings) -> None:
        command = ["poetry", "run", "maturin", "develop"]
        logger.info("%s", command)
        sp.check_call(command, cwd=self.project_directory)

    def always_install(self) -> bool:
        return True
