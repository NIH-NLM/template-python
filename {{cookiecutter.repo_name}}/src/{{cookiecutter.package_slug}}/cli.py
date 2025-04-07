# src/{{cookiecutter.package_slug}}/cli.py
import typer
app = typer.Typer()

@app.command()
def hello(name: str):
    """Say hello."""
    typer.echo(f"Hello {name} 👋")

if __name__ == "__main__":
    app()

# src/{{cookiecutter.package_slug}}/core.py
def do_work():
    return "work done"

# src/{{cookiecutter.package_slug}}/utils.py
def add(x, y):
    return x + y

# tests/test_cli.py
def test_add():
    from {{cookiecutter.package_slug}}.utils import add
    assert add(2, 2) == 4

