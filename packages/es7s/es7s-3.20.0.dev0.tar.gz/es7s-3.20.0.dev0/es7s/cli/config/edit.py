# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

import os
import subprocess

from .._decorators import cli_command, _catch_and_log_and_exit
from ...shared import get_user_config_filepath, get_stdout


@cli_command(name="edit")
@_catch_and_log_and_exit
class EditCommand:
    """Open current user config in text editor."""

    def __init__(self):
        self._run()

    def _run(self):
        user_config_filepath = get_user_config_filepath()
        editor = os.getenv("EDITOR", "xdg-open")
        subprocess.run(f"{editor} {user_config_filepath}", shell=True)
        get_stdout().echo("Done")
