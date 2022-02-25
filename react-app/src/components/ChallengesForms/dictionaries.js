const challengeTypeDict = {
    ability: 1,
    collect: 2,
    craft: 2,
    damage: 3,
    finish: 4,
    win: 4,
    restore: 4,
    revive: 4,
    resurrect: 4,
    knockdowns: 6,
    kills: 6,
    assists: 6,
    headshots: 6,
    finishing: 6,
    loot: 7,
    open: 7,
    play: 8,
    capture: 8,
    purchase: 9,
    upgrade: 9,
    'survey beacons': 10,
    outlive: 11,
    survive: 11
}
const legendsDict = {
    bloodhound: [1],
    gibraltar: [2],
    lifeline: [3],
    pathfinder: [4],
    wraith: [5],
    bangalore: [6],
    caustic: [7],
    octane: [8],
    mirage: [9],
    wattson: [10],
    crypto: [11],
    revenant: [12],
    loba: [13],
    rampart: [14],
    horizon: [15],
    fuse: [16],
    valkyrie: [17],
    seer: [18],
    ash: [19],
    'mad maggie': [20],
    recon: [1, 4, 11, 17, 18]
}

const weaponsDict = {
    '30-30': [1],
    alternator: [2],
    bocek: [3],
    car: [4],
    'charge rifle': [7],
    craftable: [11, 19],
    devotion: [8],
    'eva-8': [9],
    flatline: [10, 11],
    g7: [12, 13],
    havoc: [14],
    hemlok: [15],
    kraber: [16, 17],
    'l-star': [18],
    longbow: [19, 20],
    mastiff: [21],
    mozambique: [22],
    p2020: [23],
    peacekeeper: [24],
    prowler: [25],
    'r-301': [26],
    'r-99': [27],
    rampage: [28],
    're-45': [29],
    sentinel: [30],
    spitfire: [31, 32],
    'triple take': [33],
    volt: [34, 35],
    wingman: [36],
    pistol: [23, 29, 36],
    'assault rifle': [10, 11, 14, 15, 26],
    ar: [10, 11, 14, 15, 26],
    smg: [2, 4, 25, 27, 34, 35],
    'sub mach': [2, 4, 25, 27, 34, 35],
    'sub-mach': [2, 4, 25, 27, 34, 35],
    submach: [2, 4, 25, 27, 34, 35],
    'light machine': [8, 18, 28, 31, 32],
    lmg: [8, 18, 28, 31, 32],
    shotgun: [9, 21, 22, 24],
    marksman: [1, 3, 12, 13, 33],
    sniper: [7, 16, 17, 19, 20, 30]
}

export {challengeTypeDict, legendsDict, weaponsDict}
