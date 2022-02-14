from doom.models import User
import click


@click.command()
@click.option(
    "-u",
    "--username",
    default="admin",
    is_flag=False,
    help="admin username"
)
@click.option(
    "-p",
    "--password",
    default="123456",
    is_flag=False,
    help="admin password"
)
def create_admin_user(username, password):
    """run demo command"""
    from doom.app import create_app
    app = create_app()
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User.create(username=username)
        user.set_password(password)
        user.update()
        print("Admin user created!")
