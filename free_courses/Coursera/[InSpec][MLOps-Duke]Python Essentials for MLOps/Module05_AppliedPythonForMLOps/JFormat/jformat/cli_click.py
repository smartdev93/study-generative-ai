import json
from pathlib import Path
from jformat.core import *

import click

@click.command(context_settings={"help_option_names": ['-h', '--help']})
@click.argument(
    "json_file",
    type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True)
)
@click.option(
    "-r", "--reverse",
    is_flag=True,
    default=False,
    help="Sort by value in descending order (default: ascending)."
)
@click.option(
    "-o", "--output",
    type=click.Path(file_okay=True, dir_okay=False, writable=True),
    default=None,
    help="If given, write the sorted JSON to OUTPUT_FILE; otherwise print to stdout."
)
def jformat(json_file, reverse, output):
    try:
        data = load_json_file(json_file)
    except FileNotFoundError as e:
        click.echo(f"[ERROR] {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"[ERROR] Invalid JSON format: {e}", err=True)
        raise click.Abort()
    except json.JSONDecodeError as e:
        click.echo(f"[ERROR] JSON decode error in '{json_file}': {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"[ERROR] Could not read '{json_file}': {e}", err=True)
        raise click.Abort()

    sorted_data = sort_dict_by_value(data, reverse=reverse)

    sorted_json = rewrite_to_json_file(sorted_data, indent=4)

    if output:
        try:
            Path(output).write_text(sorted_json + "\n", encoding="utf-8")
        except Exception as e:
            click.echo(f"[ERROR] Cannot write to '{output}': {e}", err=True)
            raise click.Abort()
    else:
        click.echo(sorted_json)

if __name__ == "__main__":
    jformat()