import json
import os
from pathlib import Path
from typing import Iterator
import typer
from typing_extensions import Annotated
from rich import print

from mapper.json_mapper import JSONMapper
from organizer import Organizer
from constants import JSON_DIR, JSON_ENV

# App
app = typer.Typer()


def validate_env() -> bool:
    """Checks if the JSON_ENV has been defined"""
    if not os.getenv(JSON_ENV):
        print(f"{JSON_ENV} has not been set... set it to a directory in the home directory containing your custom mapping in JSON format")
        return False
    return True


@app.command()
def default(
    directory: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=False,
            dir_okay=True,
            writable=True,
            readable=True,
            help="Specify the directory to organize"
        )
    ],
    verbose: Annotated[
        bool,
        typer.Option(
            help="Determines if the organization output should be displayed"
        )
    ] = False,
):
    """Runs organizer using the default mapping"""
    organizer = Organizer(directory, verbose)
    organizer.organize()


@app.command()
def list_custom():
    """Displays the custom JSON mappings found at the JSON_ENV directory"""

    if not validate_env():
        return

    json_files: Iterator[Path] = filter(
        lambda x: x.is_file() and x.suffix == ".json",
        JSON_DIR.iterdir()
    )

    print(f"Found the following at {JSON_DIR}\n")

    # Show the JSON files
    for json_file in json_files:
        print(f"- {json_file.name}")

@app.command()
def run_custom(
    custom_mapper: Annotated[
        str,
        typer.Option(
            help="Name of the custom mapper to use EXCLUDING the .json suffix, to view all available custom mappers use the list-custom command"
        )
    ],
    directory: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=False,
            dir_okay=True,
            writable=True,
            readable=True,
            help="Specify the directory to organize"
        )
    ],
    verbose: Annotated[
        bool,
        typer.Option(
            help="Determines if the organization output should be displayed"
        )
    ] = False,
):
    """Runs the organizer using the custom mapper specified"""

    if not validate_env():
        return

    mapper_path = JSON_DIR / f"{custom_mapper}.json"  # JSON mapper to use

    if not mapper_path.exists():
        print(f"{custom_mapper} DOES NOT EXIST")
        return

    JSONMapper.parse_json(mapper_path)
    organizer = Organizer(directory, verbose)
    organizer.organize(JSONMapper)