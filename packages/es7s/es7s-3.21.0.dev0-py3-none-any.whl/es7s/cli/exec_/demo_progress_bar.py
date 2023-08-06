# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import math
import pathlib
import typing
from os import stat_result
from time import sleep

from es7s.cli._base_opts_params import IntRange
from es7s.cli._decorators import cli_argument, cli_command, cli_option, _catch_and_log_and_exit
from es7s.shared import get_stdout, FrozenStyle
from es7s.shared.progress_bar import ProgressBar
from es7s.shared.strutil import cut


@cli_command(__file__, help="Launch a demonstration of ProgressBar CLI component.")
@cli_option(
    "-s",
    "--slow",
    default=1,
    help="Add an artificial delay in eⁿ seconds between operations."
    " With default n=0 delay is disabled. With n=1 delay ≈3ms, "
    "with n=5 ≈140ms, and with 10 ≈21sec. Practical slow levels "
    "are within range [1;4].",
    type=IntRange(_min=0, _max=10),
)
@cli_argument("path", default="/home", type=pathlib.Path)
@_catch_and_log_and_exit
class DemoProgressBarCommand:
    """ """

    def __init__(self, path: pathlib.Path, slow: int):
        self._path = path
        self._slow = slow
        self.run()

    def run(self):
        stdout = get_stdout()
        pathes = [*filter(lambda f: f.is_dir(), self._path.iterdir())]
        pbar = ProgressBar(threshold_count=len(pathes))
        for pidx, path in enumerate(pathes):
            pbar.next_threshold(label=path.absolute().name)
            try:
                children: typing.Sequence[pathlib.Path] = [*path.iterdir()]
            except:
                continue

            for idx, child in enumerate(sorted(children)):
                data = b""
                st: stat_result | None = None
                try:
                    st: stat_result = child.stat()
                    if child.is_file():
                        data = child.open("rb").read(12)
                except FileNotFoundError as e:
                    pbar.echo(
                        get_stdout().render(" ! ", FrozenStyle(fg="yellow", bold=True)) + f"{e}",
                        err=True,
                    )
                except Exception as e:
                    pbar.echo(
                        stdout.render(" × ", FrozenStyle(bg="dark red", fg="bright white", bold=True))
                        + stdout.render(f" {e}", "red"),
                        err=True,
                    )
                    continue
                if not st:
                    continue

                cc = ""
                for c in data:
                    cc += hex(c).removeprefix("0x").zfill(2) + " "
                while len(cc) < 12 * 3:
                    cc += "·· "
                if self._slow:
                    sleep(math.e**self._slow / 1000)
                pbar.echo(  # @todo refactor for fucks sake
                    f"\x1b[2m{idx:6d} \x1b[34m|\x1b[m {cut(str(child.resolve()), 30, '^').strip():30s} {st.st_size:16d} "
                    f"{st.st_blocks:8d} {st.st_ino:12d} {st.st_nlink:4d}"
                    f" \x1b[34;2m|\x1b[0m {cc}\x1b[39m"
                )
                pbar.set(ratio_local=idx / len(children), label=str(path.name))
            pbar.set(finished=True)
        pbar.echo(stdout.render(f" ⏺  ", "green") + "Did a lot of hard (fake) work: WIN")
