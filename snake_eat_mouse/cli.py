"""Console script for snake_eat_mouse."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for snake_eat_mouse."""
    click.echo("Replace this message by putting your code into "
               "snake_eat_mouse.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
