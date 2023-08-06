import click
from AQAInterpreter.scanner import Scanner
from AQAInterpreter.parser import Parser


def run(source: str, debug: bool = False, transpile: bool = False) -> str:
    """evaluates `source` returning a string"""

    source += "\n"
    if debug:
        click.echo(source)

    tokens = Scanner(source).scan_tokens()
    if debug:
        click.echo(tokens)
        click.echo()

    output: list[str] = []
    statements = Parser(tokens, output).parse()
    if debug:
        click.echo(statements)

    if not transpile:
        for statement in statements:
            statement.interpret(output)

        return "\n".join(output) + "\n"
    else:
        for statement in statements:
            output.append(statement.unparse())

        return "".join(output)


@click.command
@click.argument("filename", required=False)
@click.option("-c", "--cmd")
@click.option("-d", "--debug", is_flag=True, default=False, help="Show tokens and ast")
@click.option(
    "-t", "--transpile", is_flag=True, default=False, help="convert to python"
)
def main(filename: str, cmd: str, debug: bool, transpile: bool):
    """source code can be read in from a file or a string
    if `debug` is True, tokens and ast are also printed"""

    if filename and cmd:
        raise click.UsageError("cannot specify both filename and command")

    if filename:
        with open(filename, encoding="utf-8") as infp:
            click.echo(run(infp.read(), debug=debug, transpile=transpile).rstrip())
    elif cmd:
        click.echo(run(cmd, debug=debug).rstrip())
    else:
        # run REPL
        while True:
            click.echo(run(input("> "), debug=debug, transpile=transpile).rstrip())


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
