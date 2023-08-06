#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click

from database import (User, add_new_user, db, get_all_users,
                      get_user_by_api_key, get_user_by_id, initialize_database,
                      update_user_token_usage)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", prompt=True, help="Name of the user")
@click.option("--limit", prompt=True, help="Token limit of the user")
def create_user(name, limit):
    """Creates a new user"""
    user = add_new_user(name, limit)
    click.echo(
        f"User {user.name} created with ID {user.id} and API key {user.api_key}"
    )


@cli.command()
@click.option("--id", prompt=True, help="ID of user to retrieve")
def get_user_by_id_cmd(id):
    """Retrieves a user by ID"""
    user = get_user_by_id(id)
    if user:
        click.echo(
            f"User {user.id}: {user.name}, usage: {user.token_usage}/{user.token_limit}"
        )
    else:
        click.echo(f"No user found with ID={id}")


@cli.command()
@click.option("--key", prompt=True, help="API key of user to retrieve")
def get_user_by_key(key):
    """Retrieves a user by API key"""
    user = get_user_by_api_key(key)
    if user:
        click.echo(
            f"User {user.id}: {user.name}, usage: {user.token_usage}/{user.token_limit}"
        )
    else:
        click.echo(f"No user found with API key={key}")


@cli.command()
@click.option("--id", prompt=True, help="ID of user to update")
@click.option("--used",
              prompt=True,
              help="Number of tokens used in the session")
def update_user_usage(id, used):
    """Updates the token usage of a user"""
    user = get_user_by_id(id)
    if user:
        update_user_token_usage(user, used)
        click.echo(f"User {user.name} updated with {used} tokens used")
    else:
        click.echo(f"No user found with ID={id}")


@cli.command()
def list_users():
    """List all users"""
    users = get_all_users()
    for user in users:
        click.echo(
            f"User {user.id}: {user.name}, usage: {user.token_usage}/{user.token_limit}, API key: {user.api_key}"
        )


if __name__ == "__main__":
    cli()
