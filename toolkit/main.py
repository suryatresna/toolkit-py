import click

from cmd.database import database
from cmd.redis import redis
from cmd.hello import hello

@click.group()
def cli():
    pass

cli.add_command(database.testDB)
cli.add_command(redis.testRedis)
cli.add_command(hello.hello)

if __name__ == '__main__':
    cli()