from flask.cli import AppGroup


from .challenge_types import seed_challenge_types, undo_challenge_types
from .legends import seed_legends, undo_legends
from .modes import seed_modes, undo_modes
from .weapon_types import seed_weapon_types, undo_weapon_types
from .weapons import seed_weapon, undo_weapon
from .users import seed_users, undo_users
from .user_challenges import undo_user_challenge, seed_one_user

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command


@seed_commands.command('all')
# Add other seed functions here
def seed():
    seed_challenge_types()
    seed_users()
    seed_legends()
    seed_weapon_types()
    seed_weapon()
    seed_modes()
    seed_one_user([1])


@seed_commands.command('undo')
def undo():
    undo_challenge_types()
    undo_users()
    undo_legends()
    undo_weapon_types()
    undo_weapon()
    undo_modes()
    undo_user_challenge()


@seed_commands.command('reset')
def reset():
    """
    `flask seed reset` unseeds all of the data and then reseeds
    """
    undo_challenge_types()
    undo_users()
    undo_legends()
    undo_weapon_types()
    undo_weapon()
    undo_modes()
    undo_user_challenge()
    seed_challenge_types()
    seed_users()
    seed_legends()
    seed_weapon_types()
    seed_weapon()
    seed_modes()
    seed_one_user([1])
