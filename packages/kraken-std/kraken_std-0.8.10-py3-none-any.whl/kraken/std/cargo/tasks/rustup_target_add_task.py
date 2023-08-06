from __future__ import annotations

import subprocess as sp

from kraken.core import Property, Task, TaskStatus


class RustupTargetAddTask(Task):
    description = "Installs a given target for Cargo"

    target: Property[str]

    def execute(self) -> TaskStatus:
        command = ["rustup", "target", "add", self.target.get()]
        result = sp.call(command, cwd=self.project.directory)
        return TaskStatus.from_exit_code(command, result)
