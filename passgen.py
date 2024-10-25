import click
import pyperclip
from app import application

logo = """
    +-----------------------------+
    | Thank you for using Genpass |
    +-----------------------------+
    """

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


@cli.command("hello")
@click.option("-n", "--name", type=str, help="Name to greet", default="World")
def hello(name):
    """Say hello to the user.

    Args:
        name (str): The name of the person to greet. Defaults to "World".
    """
    click.echo(f"Hello {name}")
    click.echo(logo)

@cli.command("generate")
@click.option("-l", "--length", type=int, help="Length of password to be generated", default=12)
@click.option(
    "-o",
    "--option",
    type=click.Choice(["1", "2", "3"]),
    default="3",
    help="""Options\n
    1 - alphabetic both cases\n
    2 - alphanumeric\n
    3 - alphanumeric + special characters""",
)
def generate(length, option):
    """Generates a random password of length and type"""

    password = application.generate(int(length), int(option))

    try:
        pyperclip.copy(password)
        click.echo("Password has been copied to clipboard\n")
    except Exception:
        click.echo("Could not copy password to clipboad\n")

    # output password and info to terminal
    click.echo(password)
    click.echo(logo)

@cli.command("generate-strong-password")
@click.option(
    "-l", "--length", type=int, help="Length of password to be generated", default=12
)
def generate_strong_password(length):
    """Generates a strong password of length and type

    Strong password is generated using all options: alphabetic both cases, alphanumeric, alphanumeric + special characters
    """
    password = application.generate_strong_password(int(length))

    try:
        pyperclip.copy(password)
        click.echo("Password has been copied to clipboard\n")
    except Exception:
        click.echo("Could not copy password to clipboad\n")

    # output password and info to terminal
    click.echo(password)
    click.echo(logo)
    
@cli.command("check-password-strength")
@click.option(
    "-p",
    "--password",
    type=str,
    help="Password to be checked",
)
def check_password_strength(password):
    """
    Command to check the strength of a given password.

    This command takes a password as input, checks its strength using the application logic,
    and outputs whether the password is strong or not. If the password is not strong, it
    provides feedback on what is missing.

    Parameters
    ----------
    password : str
        The password to be checked.
    """
    is_strong, message = application.check_password_strength(password)
    if is_strong:
        click.echo("Password is strong")
    else:
        click.echo(message)
