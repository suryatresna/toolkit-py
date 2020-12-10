import click

@click.command()
def testRedis():
    """Test connection Redis, e.g PING"""
    click.echo("Test redis connection")