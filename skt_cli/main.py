from __future__ import print_function, unicode_literals

import traceback
from typing import Optional

import typer

from .packages.commands.command import argparse
from .packages.logger import get_logger
from .packages.prompt.factory import CreatePrompt

logger = get_logger()

app = typer.Typer()


@app.command()
def cli(
    path: str = typer.Argument(""),
    type: Optional[str] = typer.Option(None, help="[websocket, socketio, unix]"),
):
    prompt = CreatePrompt(type, path)
    while True:
        try:
            prompt.run_cli()
        except argparse.ArgumentError as exc:
            logger.debug("Error: %r.", exc)
            logger.error("traceback: %r", traceback.format_exc())
            typer.echo(exc.msg, color="red")
        except EOFError:
            prompt.terminate()
            break
        except Exception as exc:
            logger.debug("Exception: %r.", exc)
            logger.error("traceback: %r", traceback.format_exc())
            typer.echo(str(exc), color="red")


if __name__ == "__main__":
    app()
