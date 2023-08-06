# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2021-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import logging
import os
import shutil

import pytermor as pt

from es7s import APP_NAME
from .._decorators import _catch_and_log_and_exit, cli_option, cli_command
from ...shared import get_logger, get_stdout
from ...shared.path import RESOURCE_DIR, USER_ES7S_BIN_DIR, USER_ES7S_DATA_DIR


@cli_command(__file__)
@cli_option(
    "-n",
    "--dry-run",
    is_flag=True,
    default=False,
    help="Don't actually do anything, just pretend to.",
)
@cli_option(
    "-s",
    "--symlinks",
    is_flag=True,
    default=False,
    help="Make symlinks to core files instead of copying them. "
    "Useful for es7s development, otherwise unnecessary.",
)
@_catch_and_log_and_exit
class InstallCommand:
    """Install es7s system."""

    def __init__(self, dry_run: bool, symlinks: bool, **kwargs):
        self._dry_run = dry_run
        self._symlinks = symlinks
        self._current_stage: str|None = None
        self._run()

    def _run(self):
        for stage in [
            # self._run_prepare,
            # self._run_copy_core,
            # self._run_inject_bashrc,
            # self._run_inject_gitconfig,
            self._run_copy_data,
            self._run_copy_bin,
            # self._run_install_with_apt,
            # self._run_install_with_pip,
            # self._run_install_x11,
            # self._run_dload_install,
            # self._run_build_install_tmux,
            # self._run_build_install_less,
            # self._run_install_es7s_exts,
            # self._run_install_daemon,
            # self._run_install_shocks_service,
            # self._run_setup_cron,
        ]:
            self._current_stage = stage.__qualname__.split('.')[1].lstrip('_')
            self._log(f"Starting stage: {self._current_stage}")
            try:
                stage()
            except Exception as e:
                raise RuntimeError(self._current_stage + " failed") from e

    def _run_prepare(self):
        # install docker
        # sudo xargs -n1 <<< "docker syslog adm sudo" adduser $(id -nu)
        # ln -s /usr/bin/python3 ~/.local/bin/python
        pass

    def _run_copy_core(self):
        # install i -cp -v
        # git+ssh://git@github.com/delameter/pytermor@2.1.0-dev9
        pass

    def _run_inject_bashrc(self):
        pass

    def _run_inject_gitconfig(self):
        pass

    def _run_copy_data(self):
        import pkg_resources
        count = 0

        dist_dir_relpath = os.path.join(RESOURCE_DIR)
        dist_dir = pkg_resources.resource_listdir(APP_NAME, dist_dir_relpath)

        if os.path.exists(USER_ES7S_DATA_DIR):
            if not self._remove_file_or_dir(USER_ES7S_DATA_DIR):
                raise RuntimeError(f"Failed to remove dir, aborting", [USER_ES7S_DATA_DIR])

        if not self._make_dir(USER_ES7S_DATA_DIR):
            raise RuntimeError(f"Failed to create dir, aborting", [USER_ES7S_DATA_DIR])

        for dist_relpath in dist_dir:
            dist_abspath = pkg_resources.resource_filename(
                APP_NAME, os.path.join(dist_dir_relpath, dist_relpath)
            )
            if not os.path.isfile(dist_abspath):
                continue
            user_abspath = os.path.join(USER_ES7S_DATA_DIR, os.path.basename(dist_relpath))

            if not self._copy_or_symlink(dist_abspath, user_abspath):
                raise RuntimeError(f"Failed to copy file, aborting", [dist_abspath])
            count += 1

        self._echo_success(f"Installed {count} data files")

    def _run_copy_bin(self):
        import pkg_resources
        logger = get_logger()
        count = 0

        dist_dir_relpath = os.path.join(RESOURCE_DIR, "bin")
        dist_dir = pkg_resources.resource_listdir(APP_NAME, dist_dir_relpath)

        if not os.path.exists(USER_ES7S_BIN_DIR):
            if not self._make_dir(USER_ES7S_BIN_DIR):
                raise RuntimeError(f"Failed to create dir, aborting", [USER_ES7S_BIN_DIR])

        for dist_relpath in dist_dir:
            dist_abspath = pkg_resources.resource_filename(
                APP_NAME, os.path.join(dist_dir_relpath, dist_relpath)
            )
            user_abspath = os.path.join(USER_ES7S_BIN_DIR, os.path.basename(dist_relpath))

            if os.path.exists(user_abspath) or os.path.islink(user_abspath):  # may be broken link
                if not self._remove_file_or_dir(user_abspath):
                    logger.warning(f"Failed to remove file: '{user_abspath}', skipping...")
                    continue

            if not self._copy_or_symlink(dist_abspath, user_abspath):
                raise RuntimeError(f"Failed to copy file, aborting", [dist_abspath])
            count += 1

        self._echo_success(f"Installed {count} bin files")

    def _run_install_with_apt(self):
        pass

    def _run_install_with_pip(self):
        pass

    def _run_install_x11(self):
        pass

    def _run_dload_install(self):
        # ginstall exa
        # ginstall bat
        pass

    def _run_build_install_tmux(self):
        # install tmux deps
        # build_tmux
        # ln -s `pwd`/tmux ~/bin/es7s/tmux
        # git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
        # tmux run-shell /home/delameter/.tmux/plugins/tpm/bindings/install_plugins
        pass

    def _run_build_install_less(self):
        # install less deps
        # build_less
        pass

    def _run_install_es7s_exts(self):
        # install i -i -v

        # colors
        # fonts?
        # > pipx install kolombos
        # leo
        # > pipx install macedon
        # watson
        # nalog
        pass

    def _run_install_daemon(self):
        # copy es7s.service to /etc/systemd/system
        # replace USER placeholders
        # enable es7s, reload systemd
        pass

    def _run_install_shocks_service(self):
        # copy es7s-shocks.service to /etc/systemd/system
        # replace USER placeholders
        # enable shocks, reload systemd
        pass

    def _make_dir(self, user_path: str) -> bool:
        self._log_io("Creating", user_path)
        if self._dry_run:
            return True

        try:
            os.makedirs(user_path)
            self._log_io("Created", user_path)
        except Exception as e:
            get_logger().exception(e)
            return False

        return os.path.exists(user_path)

    def _remove_file_or_dir(self, user_path: str) -> bool:
        self._log_io("Removing", user_path)
        if self._dry_run:
            return True

        try:
            if os.path.isfile(user_path) or os.path.islink(user_path):
                os.unlink(user_path)
                self._log_io("Removed", user_path)
            elif os.path.isdir(user_path):
                shutil.rmtree(user_path)
                self._log_io("Removed", user_path)
            else:
                self._log_io("Not found", user_path)

        except Exception as e:
            get_logger().exception(e)
            return False

        return not os.path.exists(user_path)

    def _copy_or_symlink(self, dist_path: str, user_path: str) -> bool:
        action = ("Linking" if self._symlinks else "Copying")

        self._log_io(action, user_path, dist_path)
        if self._dry_run:
            return True

        try:
            if self._symlinks:
                os.symlink(dist_path, user_path)
                self._log_io("Linked", user_path, dist_path)
            else:
                shutil.copy(dist_path, user_path)
                self._log_io("Copied", user_path, dist_path)

        except Exception as e:
            get_logger().exception(e)
            return False

        return True

    def _log_io(self, action: str, target: str, source: str = None):
        prefix = ""
        path = f'"{target}"'
        if source:
            path = f'"{source}" -> {path}'
        self._log(f"{prefix}{action+':':<9s} {path}")

    def _log(self, msg: str):
        prefix = ""
        if self._dry_run:
            prefix += "DRY-RUN|"
        prefix += self._current_stage
        get_logger().info(f'[{prefix}] {msg}')

    def _echo_success(self, msg: str):
        if self._dry_run:
            msg += " [NOT REALLY]"
        self._log(msg)

        stdout = get_stdout()
        if get_logger().verbosity == 0:
            msg = stdout.render(" ⏺ ", pt.cv.GREEN) + msg
        else:
            msg = stdout.render(" ⏺ " + msg, pt.cv.GREEN)
        stdout.echo(msg)
