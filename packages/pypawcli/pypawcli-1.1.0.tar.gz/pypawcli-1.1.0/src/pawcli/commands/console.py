from __future__ import annotations

from typing import Optional

from pawapi import Shell
from typer import Argument
from typer import Context
from typer import Option
from typer import Typer
from typer import launch

from pawcli.core.callback import init_api
from pawcli.core.path import resolve
from pawcli.core.result import process_result
from pawcli.core.utils import save_config

CONSOLE_ID_ARGUMENT = Argument(
    ...,
    metavar="ID",
    help="Console ID",
)
CONSOLE_ID_OPTION = Option(
    ...,
    "--console",
    "-c",
    metavar="ID",
    help="Console ID",
)

console_app = Typer(help="Manage consoles")


@console_app.callback()
def _init_context(ctx: Context):  # pragma: no cover
    init_api(ctx)

    executable = ctx.obj.config.get("console", "default_shell", fallback=None)
    console_id = ctx.obj.config.get("console", "default_id", fallback=None)
    ctx.default_map = {
        "new": {"executable": executable},
        **{
            k: {"console_id": console_id}
            for k in ("info", "output", "exec", "rm")
            if console_id is not None and console_id
        }
    }  # yapf: disable


@console_app.command()
def ls(
    ctx: Context,
    shared: bool = Option(
        False,
        "--shared",
        "-s",
        is_flag=True,
        help="Shared consoles",
    ),
) -> None:
    """List existing consoles"""

    api = ctx.obj.api.console
    if shared:
        result = api.list_shared()
    else:
        result = api.list()
    process_result(result)


@console_app.command(short_help="Create a new console")
def new(
    ctx: Context,
    executable: Shell = Argument(..., help="Console executable"),
    args: Optional[str] = Option(None, help="Additional arguments"),
    working_dir: Optional[str] = Option(
        None,
        "--working-dir",
        "-d",
        metavar="PATH",
        help="Console working directory",
    ),
    default: bool = Option(
        False,
        "--default",
        "-D",
        is_flag=True,
        help="Use console as default for `console id` argument",
    ),
    open_frame: bool = Option(
        False,
        "--open",
        is_flag=True,
        help="Open a new console in browser",
    ),
) -> None:
    """Create a new console instance.

    NOTE: New console is not actually initialized.
    You need open the console in browser to initialize it.
    """

    result = ctx.obj.api.console.create(
        executable=executable,
        arguments=args,
        working_directory=(
            resolve(ctx, working_dir) if working_dir is not None else None
        ),
    )
    if result is None:
        ctx.exit(1)
    process_result(result)
    if default:
        ctx.obj.config.set("console", "default_id", str(result["id"]))
        save_config(ctx)
    if open_frame:
        frame_path = result["console_frame_url"]
        launch(f"https://www.pythonanywhere.com{frame_path}")


@console_app.command()
def info(
    ctx: Context,
    console_id: int = CONSOLE_ID_ARGUMENT,
) -> None:
    """Console info"""

    result = ctx.obj.api.console.get_info(console_id)
    process_result(result)


@console_app.command()
def rm(
    ctx: Context,
    console_id: int = CONSOLE_ID_ARGUMENT,
) -> None:
    """Remove the console"""

    if not ctx.obj.api.console.kill(console_id):
        ctx.exit(1)

    # try to remove default_id from config
    try:
        default_id = ctx.obj.config.getint(
            "console",
            "default_id",
            fallback=None,
        )
    except ValueError:  # pragma: no cover
        ctx.exit()

    if default_id is not None and default_id == console_id:
        if ctx.obj.config.remove_option("console", "default_id"):
            save_config(ctx)


@console_app.command()
def output(
    ctx: Context,
    console_id: int = CONSOLE_ID_ARGUMENT,
) -> None:
    """Get console output"""

    print(ctx.obj.api.console.get_output(console_id))


@console_app.command()
def exec(
    ctx: Context,
    command: str = Argument(..., metavar="CMD"),
    console_id: int = CONSOLE_ID_OPTION,
    get_output: bool = Option(
        False,
        "--output",
        "-o",
        help="Get console output",
    ),
) -> None:
    """Execute command in console"""

    if not command.endswith("\n"):
        command += "\n"

    result = ctx.obj.api.console.send_input(
        console_id=console_id,
        command=command,
    )
    if not result:
        ctx.exit(1)
    if get_output:
        output(ctx, console_id)
