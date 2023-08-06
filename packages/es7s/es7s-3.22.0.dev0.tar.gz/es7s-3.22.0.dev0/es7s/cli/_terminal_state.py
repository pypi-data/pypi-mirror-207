# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import sys

import pytermor as pt

from es7s.shared import IoProxy, get_stdout


class TerminalStateController:
    def __init__(self, io_proxy: IoProxy = None):
        self._io_proxy: IoProxy = io_proxy or get_stdout()
        self._restore_callbacks: list[callable] = []
        self._terminal_orig_settings: list|None = None

    def enable_alt_screen_buffer(self):
        self._restore_callbacks.append(self._disable_alt_screen_buffer)
        self._restore_callbacks.append(self._restore_cursor_position)
        self._io_proxy.echo(pt.make_save_cursor_position())
        self._io_proxy.echo(pt.make_enable_alt_screen_buffer())

    def hide_cursor(self):
        self._restore_callbacks.append(self._show_cursor)
        self._io_proxy.echo(pt.make_hide_cursor())

    def disable_input(self):
        import tty
        import termios
        self._restore_callbacks.append(self._restore_input)
        self._terminal_orig_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)

    def restore_state(self):
        while self._restore_callbacks:
            self._restore_callbacks.pop()()

    def _disable_alt_screen_buffer(self):
        self._io_proxy.echo(pt.make_disable_alt_screen_buffer())

    def _restore_cursor_position(self):
        self._io_proxy.echo(pt.make_restore_cursor_position())

    def _show_cursor(self):
        self._io_proxy.echo(pt.make_show_cursor())

    def _restore_input(self):
        import termios
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self._terminal_orig_settings)
