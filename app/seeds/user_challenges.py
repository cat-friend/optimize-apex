from app.models import db, UserChallenge, UserChallengeDimensionTable

# seeds data for a specific user


def seed_one_user(ids):
    """
    Seeds Season 12 data for a user
    """
    labels = [
        "Deal 1000 damage with pistols",
        "Play 12 matches as Bangalore, Mad Maggie, or Wattson",
        "Deal 5000 damage as Pathfinder, Horizon, or Revenant",
        "Get 40 knockdowns with sub machine guns",
        "Get 20 kills as Wraith, Fuse, or Mirage",
        "Survive 30 ring closings",
        "Finish in the top-3 1 time getting at least 3 kills, knockdowns or assists",
        "Neurolink: Scan 10 enemies as Crypto",
        "Deal 10000 damage with assault rifles",
        "Play 12 matches as Gibraltar, Octane, or Loba",
        "Deal 5000 damage as Pathfinder, Mad Maggie, or Mirage",
        "Get 30 knockdowns with sub machine guns",
        "Win 3 matches as Bangalore, Ash, or Caustic",
        "Deal 500 melee damage",
        "Get 50 kills or assists",
        "Play 10 matches",
        "Deal 3500 damage with shotguns",
        "Play 12 matches as Bangalore, Octane, or Mirage",
        "Deal 5000 damage as Wraith, Wattson, or Fuse",
        "Get 25 knockdowns with sniper rifles",
        "Get 20 kills as Lifeline, Mad Maggie or Caustic",
        "Finish in the top-3 1 time getting at least 3 kills, knockdowns, or assists",
        "Deal 5000 damage",
        "Loot 50 epic items",
        "Deal 3500 damage with marksman weapons",
        "Play 12 matches as Bloodhound, Fuse, or Caustic",
        "Deal 5000 damage as Gibraltar, Valkyrie, or Crypto",
        "Get 40 knockdowns with sub machine guns",
        "Get 15 kills as Wraith, Rampart or Wattson",
        "Get 5 Battle Royale Top 10 finishes or Arenas wins",
        "Win 1 match getting at least five kills, knockdowns, or assists",
        "Deal 1000 damage before the end of the first shrink",
        "Deal 5000 damage with marksman weapons",
        "Play 12 matches as Bloodhound, Seer, or Crypto",
        "Deal 5000 damage as Bangalore, Ash, or Valkyrie",
        "Get 25 knockdowns with shotguns",
        "Finish in the top 3 as Lifeline, Loba, or Fuse",
        "Deal 750 damage in a single match",
        "Get 25 headshots",
        "Revive Squadmates 20 times"
    ]

    value = [
        10,
        10,
        10,
        10,
        5,
        5,
        5,
        2,
        10,
        10,
        10,
        10,
        5,
        5,
        5,
        2,
        10,
        10,
        10,
        10,
        5,
        5,
        5,
        2,
        10,
        10,
        10,
        10,
        5,
        5,
        5,
        2,
        10,
        10,
        10,
        10,
        5,
        5,
        5,
        2
    ]

    modes = [
        [2],
        [1, 2, 3],
        [1],
        [2],
        [2],
        [1, 2, 3],
        [1],
        [1, 2, 3],
        [2],
        [1, 2, 3],
        [1],
        [1],
        [2],
        [1, 2, 3],
        [1],
        [1, 2, 3],
        [2],
        [1, 2, 3],
        [1],
        [1],
        [2],
        [1],
        [1],
        [1],
        [1],
        [1, 2, 3],
        [1],
        [2],
        [1],
        [1, 2],
        [2],
        [1]
    ]

    challenge_types = [
        3,
        8,
        3,
        6,
        6,
        11,
        4,
        1,
        3,
        8,
        3,
        6,
        4,
        3,
        6,
        8,
        3,
        8,
        3,
        6,
        6,
        4,
        3,
        7,
        3,
        8,
        3,
        6,
        6,
        4,
        4,
        3,
        3,
        8,
        3,
        6,
        4,
        3,
        6,
        5
    ]

    legends = [
        [None],
        [6, 20, 10],
        [4, 15, 12],
        [None],
        [16, 5, 9],
        [None],
        [None],
        [11],
        [None],
        [2, 8, 13],
        [4, 20, 9],
        [None],
        [6, 19, 7],
        [None],
        [None],
        [None],
        [None],
        [6, 8, 9],
        [5, 10, 16],
        [None],
        [3, 20, 7],
        [None],
        [None],
        [None],
        [None],
        [1, 16, 7],
        [2, 17, 11],
        [None],
        [5, 14, 10],
        [None],
        [None],
        [None],
        [None],
        [1, 18, 11],
        [6, 19, 17],
        [None],
        [3, 13, 16],
        [None],
        [None],
        [None]
    ]
    weapons = [
        [23, 29, 36],
        [None],
        [None],
        [2, 4, 25, 27, 34, 35],
        [None],
        [None],
        [None],
        [None],
        [10, 11, 14, 15, 26],
        [None],
        [None],
        [2, 4, 25, 27, 34, 35],
        [None],
        [None],
        [None],
        [None],
        [9, 21, 22, 24],
        [None],
        [None],
        [7, 16, 17, 19, 20, 30],
        [None],
        [None],
        [None],
        [None],
        [1, 3, 12, 13, 33],
        [None],
        [None],
        [2, 4, 25, 27, 34, 35],
        [None],
        [None],
        [None],
        [None],
        [1, 3, 12, 13, 33],
        [None],
        [None],
        [9, 21, 22, 24],
        [None],
        [None],
        [None],
        [None]
    ]
    for id in ids:
        for i in range(0, len(labels)):
            entry = UserChallenge(
                user_id=id, challenge_label=labels[i], challenge_type_id=challenge_types[i],
                status="open", value=value[i])
            db.session.add(entry)
            db.session.commit()
            for weapon in weapons[i]:
                for legend in legends[i]:
                    for mode in modes[i]:
                        dim_table_entry = UserChallengeDimensionTable(
                            user_challenge_id=entry.id, weapon_id=weapon, mode_id=mode,
                            legend_id=legend, value=value[i]
                        )
                        db.session.add(dim_table_entry)
                        db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities


def undo_user_challenge():
    db.session.execute('TRUNCATE userchallenges RESTART IDENTITY CASCADE;')
    db.session.commit()
