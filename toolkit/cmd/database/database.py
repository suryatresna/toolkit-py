import click

@click.command()
def testDB():
    """Test connection Database PostgresSQL, e.g PING and Select Test"""
    click.echo("test database connection")