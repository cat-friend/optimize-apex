from flask.cli import AppGroup


from .challenge_types import seed_challenge_types, undo_challenge_types
from .clans import seed_clans, undo_clans
from .clan_users import seed_clan_users, undo_clan_users
from .legends import seed_legends, undo_legends
from .messages import seed_messages, undo_messages
from .modes import seed_modes, undo_modes
from .weapon_types import seed_weapon_types, undo_weapon_types
from .weapons import seed_weapon, undo_weapon
from .users import seed_users, undo_users

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
    seed_clans()
    seed_clan_users()
    seed_messages()





# Creates the `flask seed undo` command
@seed_commands.command('undo')
# Add other undo functions here
def undo():
    undo_challenge_types()
    undo_users()
    undo_legends()
    undo_weapon_types()
    undo_weapon()
    undo_modes()
    undo_clans()
    undo_clan_users()
    undo_messages()
