// Harmbringer – game data for the one-shot prototype.
// Loaded via <script src="data/world_data.js"> before the game module.
// All numbers are starting values for balancing; rules that use them are defined in PROMPT.md.
// Values marked "source: design notes" come from Kevin's design document; everything else is a
// first proposal and may be tuned freely.

window.HARMBRINGER_DATA = {

  // ---------------------------------------------------------------------------
  // Map and geometry
  // ---------------------------------------------------------------------------
  map: {
    // Campaign grid ETRS89 / UTM 32N (tools/build_game_map.py). One hex tile = 247 m column spacing,
    // 285 m row spacing, so tiles have the same size in meters in both directions.
    // Tile (q, r) center: E = eMin + q * colMeters, N = nMax - (r + 0.5 * (q & 1)) * rowMeters.
    // Positions from lat/lon: python tools/build_game_map.py --tile <lat> <lon>
    width: 2017,               // tiles, Q axis, west -> east
    height: 1583,              // tiles, R axis, north -> south (R = 0 is the north edge)
    // Heights come in meters (data/heightmap.js, 16 bit). Battle tiles use a compressed height:
    // sign(s) * sqrt(|s|) * hex.heightPerStep with s = meters / metersPerStep.
    metersPerStep: 508 / 255,
    // World map relief: height in world units = meters / colMeters * columnSpacing * reliefExaggeration.
    // 1 = true scale (~55 m per unit). Battles use the compressed hex heights (hex.heightPerStep).
    reliefExaggeration: 6,
    utm: { eMin: 370354.257, nMax: 6093532.332, colMeters: 247.1460, rowMeters: 285.3797 },
    startDate: { year: 1371, month: 5, day: 1 }
  },

  hex: {
    circumradius: 3.0,         // center to corner, world units (1 unit = 1 m)
    // Derived values (compute in code, do not round):
    //   inradius      = circumradius * sqrt(3) / 2   (~2.598)
    //   columnSpacing = 1.5 * circumradius           (4.5)
    //   rowSpacing    = 2 * inradius                 (~5.196)
    heightPerStep: 1.0,        // battle tile height = sign(s) * sqrt(|s|) * heightPerStep, s = meters / map.metersPerStep
    tileDepth: 20.0,           // tiles are tall prisms so height steps never show gaps
    waterLevel: -0.5           // y of the water plane
  },

  streaming: {
    radius: 32                 // visible window = (2 * radius + 1)^2 tiles around the camera pivot
  },

  camera: {
    minZoom: 10, maxZoom: 160, startZoom: 60,
    pitchDegrees: 55,          // looking down at the board
    minPitchDegrees: 15, maxPitchDegrees: 85,   // tilt range for right mouse button dragging
    moveSpeed: 20,             // world units per second at minZoom, scales with zoom
    rotateSpeed: 2.0,          // radians per second for Q/E
    heightSmoothing: 5.0
  },

  // ---------------------------------------------------------------------------
  // Floor types (names match the Godot enum Enums.FloorType)
  // moveCost: battle movement points to enter; null = impassable for walking units.
  // ---------------------------------------------------------------------------
  floorTypes: {
    DEEP_WATER:        { name: "Tiefes Wasser",    color: "#22364f", moveCost: null, water: true },
    SHALLOW_WATER:     { name: "Seichtes Wasser",  color: "#3f6478", moveCost: 3,    water: true },
    SAND:              { name: "Sand",             color: "#cbb98a", moveCost: 2 },
    WET_EARTH:         { name: "Feuchte Erde",     color: "#5e5236", moveCost: 2 },
    MUD:               { name: "Schlamm",          color: "#4a3f2b", moveCost: 3 },
    BOG:               { name: "Moor",             color: "#3d4430", moveCost: 3 },
    SWAMP:             { name: "Sumpf",            color: "#36442f", moveCost: 3 },
    GRASS_SHORT:       { name: "Kurzes Gras",      color: "#6f7f45", moveCost: 1 },
    GRASS_TALL:        { name: "Hohes Gras",       color: "#5d6e38", moveCost: 1 },
    HEATHER:           { name: "Heide",            color: "#7a5a6e", moveCost: 1 },
    DRY_EARTH:         { name: "Trockene Erde",    color: "#8a7650", moveCost: 1 },
    GRAVEL:            { name: "Kies",             color: "#8c8679", moveCost: 1 },
    RAW_STONE:         { name: "Fels",             color: "#77746c", moveCost: 2 },
    COBBLESTONE:       { name: "Kopfsteinpflaster",color: "#6b6660", moveCost: 1 },
    STONE_FLOOR:       { name: "Steinboden",       color: "#8d867a", moveCost: 1 },
    WOOD_FLOOR:        { name: "Holzboden",        color: "#7b5a3a", moveCost: 1 },
    HOLY_GROUND:       { name: "Geweihter Boden",  color: "#c9c2a3", moveCost: 1, effect: { damageUndeadPerRound: 2 } },
    GRAVEYARD_GROUND:  { name: "Friedhofserde",    color: "#4b463c", moveCost: 1, effect: { healUndeadPerRound: 2 } },
    PAGAN_GROUND:      { name: "Heidnischer Boden",color: "#5b5a3a", moveCost: 1 }
  },

  // Rule-based floor assignment for the world (see PROMPT.md, section "Bodentypen").
  // Bands are in meters above sea level. "mix" lists [floorType, weight] picked by value noise.
  floorRules: {
    noiseCellSize: 15,         // tiles per value-noise cell (larger = bigger patches), noise seed 1
    // Lueneburger Heide: inside this soft region "heathMix" replaces "mix".
    // d = distance / radius; weight = smoothstep from 1 (d <= fullUntil) to 0 (d >= fadeOut);
    // a tile is "heath" when valueNoise(cell = edgeNoiseCellSize, seed 4) < weight.
    heathRegion: { q: 844, r: 787, radius: 130, fullUntil: 0.6, fadeOut: 1.4, edgeNoiseCellSize: 13 },
    bands: [
      { maxMeters: -6,       floor: "DEEP_WATER" },
      { maxMeters: -0.2,     floor: "SHALLOW_WATER" },
      { maxMeters: 4,        mix: [["WET_EARTH", 4], ["SAND", 3], ["MUD", 2], ["GRASS_SHORT", 3]] },
      { maxMeters: 50,       mix: [["GRASS_SHORT", 5], ["GRASS_TALL", 3], ["WET_EARTH", 2], ["BOG", 1], ["HEATHER", 1]],
                             heathMix: [["HEATHER", 6], ["SAND", 2], ["GRASS_SHORT", 2], ["BOG", 1]] },
      { maxMeters: 150,      mix: [["GRASS_SHORT", 4], ["DRY_EARTH", 3], ["HEATHER", 2], ["SAND", 1]],
                             heathMix: [["HEATHER", 7], ["SAND", 2], ["DRY_EARTH", 1]] },
      { maxMeters: 350,      mix: [["DRY_EARTH", 4], ["GRASS_SHORT", 3], ["GRAVEL", 2]] },
      { maxMeters: Infinity, mix: [["RAW_STONE", 5], ["GRAVEL", 3], ["DRY_EARTH", 1]] }
    ]
  },

  // ---------------------------------------------------------------------------
  // Combat rules data
  // ---------------------------------------------------------------------------
  // <GEN:RULES>
  // Generated by tools/gen_data.py from design/data/*.csv and tools/rules.py - do not edit by hand.
  // Percent of damage that arrives. HEAL is not in the matrix: it restores HP to an ally.
  powerDefense: {
    PIERCE: {"UNARMORED": 100, "LIGHT": 100, "MEDIUM": 100, "HEAVY": 75, "FORTIFIED": 50, "DIVINE": 50},
    BLUNT: {"UNARMORED": 100, "LIGHT": 100, "MEDIUM": 75, "HEAVY": 100, "FORTIFIED": 75, "DIVINE": 50},
    REND: {"UNARMORED": 125, "LIGHT": 100, "MEDIUM": 75, "HEAVY": 50, "FORTIFIED": 25, "DIVINE": 50},
    SIEGE: {"UNARMORED": 100, "LIGHT": 75, "MEDIUM": 75, "HEAVY": 100, "FORTIFIED": 150, "DIVINE": 50},
    FIRE: {"UNARMORED": 100, "LIGHT": 125, "MEDIUM": 100, "HEAVY": 75, "FORTIFIED": 50, "DIVINE": 75},
    POISON: {"UNARMORED": 100, "LIGHT": 100, "MEDIUM": 100, "HEAVY": 75, "FORTIFIED": 0, "DIVINE": 50},
    ARCANE: {"UNARMORED": 100, "LIGHT": 100, "MEDIUM": 100, "HEAVY": 100, "FORTIFIED": 75, "DIVINE": 75},
    SOUL: {"UNARMORED": 150, "LIGHT": 125, "MEDIUM": 100, "HEAVY": 75, "FORTIFIED": 0, "DIVINE": 50},
    HOLY: {"UNARMORED": 150, "LIGHT": 125, "MEDIUM": 100, "HEAVY": 75, "FORTIFIED": 50, "DIVINE": 100},
    CHAOS: {"UNARMORED": 100, "LIGHT": 100, "MEDIUM": 100, "HEAVY": 100, "FORTIFIED": 100, "DIVINE": 100}
  },
  // Corpse quality per killing power type (0..1)
  corpseQuality: {"PIERCE": 1.0, "BLUNT": 0.7, "REND": 0.4, "SIEGE": 0.3, "FIRE": 0.2, "POISON": 0.5, "ARCANE": 0.8, "CHAOS": 0.8, "SOUL": 1.0, "HOLY": 0.0},
  // Combat rules: tick cost per turn = tickBase / initiative; one round = roundTicks (ini 2.5).
  // Magic power types are reduced by magicResist * mrPerPoint (capped). soulShield is a pool that absorbs any damage first.
  rules: {"tickBase": 2520, "roundTicks": 1008, "magicPowers": ["ARCANE", "CHAOS", "HOLY", "SOUL"], "mrPerPoint": 0.05, "mrCap": 0.5},
  // </GEN:RULES>

  // <GEN:UNITS>
  // Generated by tools/gen_data.py from design/data/*.csv and tools/rules.py - do not edit by hand.
  units: {
    lich: {"name": "Lich", "side": "undead", "faction": "UNDEAD", "rank": "UNIQUE", "role": "COMMANDER", "hp": 40, "initiative": 6, "move": 3, "damage": 8, "range": 3, "power": "SOUL", "counter": false, "defense": "UNARMORED", "magicResist": 8, "soulShield": 10, "sight": 5, "hear": 4, "smell": 2, "size": 2, "spectral": false, "flying": false, "abilities": ["LichSoulDrain", "LichRetreat"], "commandPoints": 0, "cost": {}, "shape": "octahedron", "color": "#5a2d82", "desc": "Untoter Herrscher. Fällt er, ist der Kampf verloren und er kehrt ins Hügelgrab zurück."},
    ghul: {"name": "Ghul", "side": "undead", "faction": "UNDEAD", "rank": "CANNON_FODDER", "role": "MELEE", "hp": 18, "initiative": 5, "move": 3, "damage": 6, "range": 1, "power": "REND", "counter": true, "defense": "UNARMORED", "magicResist": 1, "soulShield": 0, "sight": 3, "hear": 2, "smell": 4, "size": 2, "spectral": false, "flying": false, "abilities": ["GhoulCorpseEater"], "commandPoints": 2, "cost": {"corpses": 1}, "shape": "capsule", "color": "#6b7d4a", "desc": "Billig, zäh, zerfleischt seine Opfer (schlechte Leichen)."},
    skelett: {"name": "Skelett", "side": "undead", "faction": "UNDEAD", "rank": "CANNON_FODDER", "role": "MELEE", "hp": 10, "initiative": 5, "move": 3, "damage": 5, "range": 1, "power": "PIERCE", "counter": true, "defense": "LIGHT", "magicResist": 0, "soulShield": 0, "sight": 3, "hear": 2, "smell": 0, "size": 1, "spectral": false, "flying": false, "abilities": ["SkeletonReassemble"], "commandPoints": 1, "cost": {"bones": 120}, "shape": "cone", "color": "#d8d0b8", "desc": "Sauberer Stich, gute Leichen."},
    bogner: {"name": "Skelett-Bogenschütze", "side": "undead", "faction": "UNDEAD", "rank": "CANNON_FODDER", "role": "RANGED", "hp": 9, "initiative": 4, "move": 3, "damage": 4, "range": 4, "power": "PIERCE", "counter": false, "defense": "LIGHT", "magicResist": 0, "soulShield": 0, "sight": 5, "hear": 2, "smell": 1, "size": 1, "spectral": false, "flying": false, "abilities": [], "commandPoints": 2, "cost": {"bones": 150}, "shape": "cylinder", "color": "#ece4cc", "desc": "Fernkampf ohne Wissen. Schwach, trifft aus der Deckung."},
    leichenhund: {"name": "Leichenhund", "side": "undead", "faction": "UNDEAD", "rank": "CANNON_FODDER", "role": "SCOUT", "hp": 10, "initiative": 7, "move": 5, "damage": 4, "range": 1, "power": "REND", "counter": false, "defense": "UNARMORED", "magicResist": 0, "soulShield": 0, "sight": 4, "hear": 4, "smell": 6, "size": 1, "spectral": false, "flying": false, "abilities": [], "commandPoints": 1, "cost": {"corpses": 1}, "shape": "box", "color": "#5a4a3a", "desc": "Schnell und früh am Zug. Erreicht Schützen hinter der Front."},
    zombie: {"name": "Zombie", "side": "undead", "faction": "UNDEAD", "rank": "CANNON_FODDER", "role": "MELEE", "hp": 20, "initiative": 3, "move": 2, "damage": 6, "range": 1, "power": "BLUNT", "counter": true, "defense": "UNARMORED", "magicResist": 0, "soulShield": 0, "sight": 2, "hear": 2, "smell": 3, "size": 2, "spectral": false, "flying": false, "abilities": ["ZombieInfect"], "commandPoints": 1, "cost": {"corpses": 1}, "shape": "capsule", "color": "#7f8f62", "desc": "Langsam und zäh. Hält Türen und Engstellen."},
    schleuderer: {"name": "Knochenschleuderer", "side": "undead", "faction": "UNDEAD", "rank": "WARRIOR", "role": "RANGED", "hp": 10, "initiative": 4, "move": 3, "damage": 6, "range": 4, "power": "BLUNT", "counter": false, "defense": "LIGHT", "magicResist": 0, "soulShield": 0, "sight": 5, "hear": 2, "smell": 1, "size": 1, "spectral": false, "flying": false, "abilities": [], "commandPoints": 2, "cost": {"bones": 180}, "requiresKnowledge": 2, "shape": "cylinder", "color": "#bfb59a", "desc": "Fernkampf. Wirft Knochensplitter."},
    geist: {"name": "Geist", "side": "undead", "faction": "UNDEAD", "rank": "WARRIOR", "role": "SCOUT", "hp": 10, "initiative": 8, "move": 5, "damage": 8, "range": 1, "power": "SOUL", "counter": false, "defense": "UNARMORED", "magicResist": 4, "soulShield": 6, "sight": 5, "hear": 4, "smell": 0, "size": 1, "spectral": true, "flying": true, "abilities": [], "commandPoints": 3, "cost": {"souls": 2}, "requiresKnowledge": 3, "shape": "sphere", "color": "#a9c7d6", "desc": "Lautlos, fliegt, geht durch Wände. Seelenschaden bringt Seelen."},
    bauer: {"name": "Bauer", "side": "enemy", "faction": "HANSE", "rank": "CANNON_FODDER", "role": "MELEE", "hp": 10, "initiative": 4, "move": 3, "damage": 4, "range": 1, "power": "PIERCE", "counter": true, "defense": "UNARMORED", "magicResist": 0, "soulShield": 0, "sight": 4, "hear": 3, "smell": 2, "size": 2, "spectral": false, "flying": false, "abilities": ["PeasantMob"], "shape": "cone", "color": "#a08a5a", "desc": "Mistgabel, rot-weißer Wappenrock."},
    stadtwache: {"name": "Stadtwache", "side": "enemy", "faction": "HANSE", "rank": "WARRIOR", "role": "MELEE", "hp": 18, "initiative": 5, "move": 3, "damage": 6, "range": 1, "power": "PIERCE", "counter": true, "defense": "MEDIUM", "magicResist": 0, "soulShield": 0, "sight": 5, "hear": 3, "smell": 2, "size": 2, "spectral": false, "flying": false, "abilities": [], "shape": "box", "color": "#8a2f2f", "desc": "Spieß und Kettenhemd, bewacht Tore und Märkte."},
    armbrust: {"name": "Lüneburger Armbrustschütze", "side": "enemy", "faction": "HANSE", "rank": "CANNON_FODDER", "role": "RANGED", "hp": 15, "initiative": 4, "move": 3, "damage": 9, "range": 5, "power": "PIERCE", "counter": false, "defense": "MEDIUM", "magicResist": 1, "soulShield": 0, "sight": 6, "hear": 3, "smell": 2, "size": 2, "spectral": false, "flying": false, "abilities": ["CrossbowPavise"], "shape": "cylinder", "color": "#9a5a2a", "desc": "Armbrust mit Setzschild."},
    ritter: {"name": "Ritter", "side": "enemy", "faction": "GUELPHS", "rank": "WARRIOR", "role": "TANK", "hp": 30, "initiative": 6, "move": 4, "damage": 9, "range": 1, "power": "PIERCE", "counter": true, "defense": "HEAVY", "magicResist": 1, "soulShield": 1, "sight": 5, "hear": 2, "smell": 2, "size": 2, "spectral": false, "flying": false, "abilities": [], "shape": "box", "color": "#c2c2c8", "desc": "Gepanzerter Vasall der Welfen."},
    balliste: {"name": "Stadtballiste", "side": "enemy", "faction": "HANSE", "rank": "MACHINE", "role": "SIEGE", "hp": 25, "initiative": 2, "move": 1, "damage": 20, "range": 6, "power": "SIEGE", "counter": false, "defense": "FORTIFIED", "magicResist": 0, "soulShield": 0, "sight": 6, "hear": 3, "smell": 1, "size": 3, "spectral": false, "flying": false, "abilities": [], "shape": "box", "color": "#6e5536", "desc": "Geschütz auf Mauern und Türmen der Städte."},
    moench: {"name": "Mönch", "side": "enemy", "faction": "CLERGY", "rank": "WARRIOR", "role": "CASTER", "hp": 12, "initiative": 5, "move": 3, "damage": 6, "range": 3, "power": "HOLY", "counter": false, "defense": "UNARMORED", "magicResist": 3, "soulShield": 3, "sight": 5, "hear": 4, "smell": 3, "size": 1, "spectral": false, "flying": false, "abilities": [], "shape": "cone", "color": "#5b4632", "desc": "Wirft heilige Worte wie Steine."},
    priester: {"name": "Priester", "side": "enemy", "faction": "CLERGY", "rank": "WARRIOR", "role": "SUPPORT", "hp": 16, "initiative": 4, "move": 3, "damage": 6, "range": 3, "power": "HEAL", "counter": false, "defense": "UNARMORED", "magicResist": 4, "soulShield": 4, "sight": 5, "hear": 4, "smell": 3, "size": 1, "spectral": false, "flying": false, "abilities": [], "shape": "cone", "color": "#e6e0cc", "desc": "Heilt Verbündete. Ohne Verwundete greift er mit 3 Heilig-Schaden an."},
    hexe: {"name": "Hexe", "side": "enemy", "faction": "WITCHES", "rank": "WARRIOR", "role": "CASTER", "hp": 14, "initiative": 5, "move": 3, "damage": 7, "range": 4, "power": "ARCANE", "counter": false, "defense": "LIGHT", "magicResist": 5, "soulShield": 2, "sight": 4, "hear": 3, "smell": 3, "size": 2, "spectral": false, "flying": false, "abilities": ["WitchHex"], "shape": "cone", "color": "#3e5a3a", "desc": "Kräuterbündel-Stab, violettes Licht."},
    irrlicht: {"name": "Irrlicht", "side": "enemy", "faction": "HEATH_SPIRITS", "rank": "CANNON_FODDER", "role": "SCOUT", "hp": 6, "initiative": 9, "move": 5, "damage": 3, "range": 1, "power": "ARCANE", "counter": false, "defense": "UNARMORED", "magicResist": 6, "soulShield": 4, "sight": 6, "hear": 3, "smell": 0, "size": 1, "spectral": true, "flying": true, "abilities": ["WispConfusion", "WispFalseLight"], "shape": "sphere", "color": "#d9e86a", "desc": "Schwebende Lichtkugel."},
    moorgeist: {"name": "Moorgeist", "side": "enemy", "faction": "HEATH_SPIRITS", "rank": "WARRIOR", "role": "TANK", "hp": 30, "initiative": 3, "move": 2, "damage": 8, "range": 1, "power": "BLUNT", "counter": true, "defense": "UNARMORED", "magicResist": 3, "soulShield": 2, "sight": 3, "hear": 4, "smell": 2, "size": 3, "spectral": false, "flying": false, "abilities": ["MoorGrip", "FromThePeat"], "shape": "capsule", "color": "#3a4a3a", "desc": "Torfkörper, wächst aus dem Boden."},
    rattenfaenger: {"name": "Rattenfänger", "side": "enemy", "faction": "WITCHES", "rank": "UNIQUE", "role": "CASTER", "hp": 35, "initiative": 8, "move": 4, "damage": 9, "range": 4, "power": "ARCANE", "counter": false, "defense": "LIGHT", "magicResist": 5, "soulShield": 3, "sight": 7, "hear": 7, "smell": 3, "size": 2, "spectral": false, "flying": false, "abilities": [], "shape": "octahedron", "color": "#b0422e", "desc": "Der Rattenfänger von Hameln. Seine Flöte lenkt Ratten und Kinder."},
    brockenhexe: {"name": "Hexenkönigin vom Brocken", "side": "enemy", "faction": "WITCHES", "rank": "UNIQUE", "role": "CASTER", "hp": 90, "initiative": 8, "move": 4, "damage": 14, "range": 4, "power": "CHAOS", "counter": true, "defense": "DIVINE", "magicResist": 6, "soulShield": 6, "sight": 8, "hear": 8, "smell": 8, "size": 3, "spectral": false, "flying": true, "abilities": [], "shape": "octahedron", "color": "#1d1d1d", "desc": "Herrin der Walpurgisnacht, Finale der Kampagne."},
    kleriker: {"name": "Kleriker", "side": "enemy", "faction": "CLERGY", "rank": "WARRIOR", "role": "SUPPORT", "hp": 14, "initiative": 5, "move": 3, "damage": 4, "range": 2, "power": "HOLY", "counter": false, "defense": "LIGHT", "magicResist": 4, "soulShield": 6, "sight": 4, "hear": 3, "smell": 2, "size": 2, "spectral": false, "flying": false, "abilities": ["ClericCenser"], "shape": "cone", "color": "#cfc6a8", "desc": "Weihrauchfass und Buch."},
    heideschwester: {"name": "Heideschwester", "side": "enemy", "faction": "CLERGY", "rank": "WARRIOR", "role": "SUPPORT", "hp": 14, "initiative": 5, "move": 3, "damage": 4, "range": 2, "power": "HOLY", "counter": false, "defense": "LIGHT", "magicResist": 4, "soulShield": 6, "sight": 4, "hear": 3, "smell": 2, "size": 2, "spectral": false, "flying": false, "abilities": ["SisterHolyWater", "SisterConsecrate"], "shape": "cone", "color": "#9a7a8a", "desc": "Nonne mit Laterne und Kräuterkorb."},
    druide: {"name": "Druide", "side": "enemy", "faction": "WITCHES", "rank": "WARRIOR", "role": "SUPPORT", "hp": 16, "initiative": 4, "move": 3, "damage": 5, "range": 3, "power": "ARCANE", "counter": false, "defense": "LIGHT", "magicResist": 5, "soulShield": 3, "sight": 4, "hear": 3, "smell": 3, "size": 2, "spectral": false, "flying": false, "abilities": ["DruidMistletoe"], "shape": "cone", "color": "#4f6a3a", "desc": "Geweih-Kopfschmuck, Mistelkranz."},
    druidin: {"name": "Hügelgrab-Druidin", "side": "enemy", "faction": "WITCHES", "rank": "WARRIOR", "role": "CASTER", "hp": 16, "initiative": 6, "move": 3, "damage": 7, "range": 4, "power": "ARCANE", "counter": false, "defense": "LIGHT", "magicResist": 5, "soulShield": 3, "sight": 4, "hear": 3, "smell": 4, "size": 2, "spectral": false, "flying": false, "abilities": ["DruidessGraveRest", "DruidessEarthBind"], "shape": "cone", "color": "#6a8a4a", "desc": "Rentiergeweih-Haube, Mooreichenstab."},
    schwarzer_hund: {"name": "Schwarzer Hund", "side": "enemy", "faction": "HEATH_SPIRITS", "rank": "CANNON_FODDER", "role": "SCOUT", "hp": 8, "initiative": 7, "move": 5, "damage": 4, "range": 1, "power": "REND", "counter": false, "defense": "UNARMORED", "magicResist": 3, "soulShield": 2, "sight": 4, "hear": 4, "smell": 6, "size": 2, "spectral": true, "flying": false, "abilities": ["HoundPack"], "shape": "box", "color": "#202020", "desc": "Hund der Wilden Jagd. Nur beschworen."},
    wode: {"name": "Der Wode", "side": "enemy", "faction": "HEATH_SPIRITS", "rank": "UNIQUE", "role": "MELEE", "hp": 55, "initiative": 8, "move": 6, "damage": 12, "range": 1, "power": "PIERCE", "counter": true, "defense": "DIVINE", "magicResist": 5, "soulShield": 6, "sight": 6, "hear": 5, "smell": 5, "size": 3, "spectral": false, "flying": false, "abilities": ["WodeWildHunt", "WodeRideThrough", "WodeHorn"], "shape": "octahedron", "color": "#3a4a6a", "desc": "Anführer der Wilden Jagd. Pantheon der Heide."},
    zwergenkoenig: {"name": "Hügelgrab-Zwergenkönig", "side": "enemy", "faction": "HEATH_SPIRITS", "rank": "UNIQUE", "role": "TANK", "hp": 50, "initiative": 3, "move": 2, "damage": 11, "range": 1, "power": "BLUNT", "counter": true, "defense": "DIVINE", "magicResist": 6, "soulShield": 4, "sight": 4, "hear": 6, "smell": 4, "size": 2, "spectral": false, "flying": false, "abilities": ["DwarfKingForge", "DwarfKingTreasureCurse", "DwarfKingStoneSkin"], "shape": "octahedron", "color": "#8a6a3a", "desc": "Hüter der Gräber. Pantheon der Heide."},
    heidekoenigin: {"name": "Die Heidekönigin", "side": "enemy", "faction": "WITCHES", "rank": "UNIQUE", "role": "CASTER", "hp": 60, "initiative": 6, "move": 2, "damage": 10, "range": 4, "power": "ARCANE", "counter": false, "defense": "DIVINE", "magicResist": 8, "soulShield": 10, "sight": 6, "hear": 5, "smell": 5, "size": 3, "spectral": false, "flying": false, "abilities": ["HeathQueenLeyBond", "HeathQueenBloom", "HeathQueenThorns"], "shape": "octahedron", "color": "#a0607a", "desc": "Herrin des Wilseder Bergs. Pantheon der Heide."}
  },
  // </GEN:UNITS>

  // ---------------------------------------------------------------------------
  // Special places (node.special): owning them gives daily income or a lasting buff,
  // conquering them gives an artifact. Effect keys are explained at "artifacts".
  // ---------------------------------------------------------------------------
  specials: {
    lueneburg_saline: { name: "Saline", income: { corpses: 2 }, text: "Salz hält Leichen frisch: +2 Leichen pro Tag." },
    luebeck_kontor:   { name: "Kontor der Hanse", buff: { travelPct: 0.2 }, text: "Die Handelswege der Hanse: Reisen 20 % schneller." },
    segeberg_kalk:    { name: "Kalkberg", income: { bones: 60 }, text: "Kalkbrüche bleichen Gebeine: +60 Knochen pro Tag." },
    rungholt:         { name: "Glocken von Rungholt", artifact: "glocken_rungholt" },
    doberan:          { name: "Klosterapotheke", buff: { healPct: 0.1 }, text: "Kräuter der Zisterzienser: nach einem Sieg +10 % mehr Heilung." },
    arkona:           { name: "Tempel des Svantevit", artifact: "svantevit_horn" },
    vineta:           { name: "Versunkene Stadt", income: { souls: 1 }, text: "Die Glocken rufen Seelen: +1 Seele pro Tag." },
    lehnin:           { name: "Lehniner Weissagung", artifact: "lehniner_weissagung" },
    spreewald:        { name: "Hort des Schlangenkönigs", artifact: "schlangenkrone" },
    halle_saline:     { name: "Saline Halle", income: { corpses: 3 }, text: "Die Halloren sieden Salz: +3 Leichen pro Tag." },
    merseburg:        { name: "Merseburger Zaubersprüche", artifact: "merseburger_sprueche" },
    mansfeld_kupfer:  { name: "Kupferschiefer", income: { bones: 60 }, text: "Bergleute sterben jung: +60 Knochen pro Tag." },
    kyffhaeuser:      { name: "Kaiser im Berg", artifact: "reichsschwert" },
    rammelsberg:      { name: "Rammelsberg", income: { bones: 120 }, text: "Tausend Jahre Bergbau: +120 Knochen pro Tag." },
    quedlinburg:      { name: "Domschatz", artifact: "reliquienkasten" },
    hexentanzplatz:   { name: "Hexentanzplatz", buff: { travelPct: 0.2 }, text: "Die Besen der Hexen tragen auch Untote: Reisen 20 % schneller." },
    teufelsmauer:     { name: "Teufelsmauer", buff: { undeadDamagePct: 0.05 }, text: "Der Teufel steht auf eurer Seite: Untote +5 % Schaden." },
    iberg:            { name: "Zwergenschmiede", artifact: "zwergenhammer" },
    hackelberg:       { name: "Wilde Jagd", artifact: "jagdhorn" },
    corvey:           { name: "Bibliothek von Corvey", artifact: "codex_corvey" },
    externsteine:     { name: "Ley-Knoten", income: { souls: 1 }, buff: { undeadMr: 1 }, text: "Ein uralter Ley-Knoten: +1 Seele pro Tag, Untote +1 Magieresistenz." },
    pestrup:          { name: "Gräberfeld", buff: { lootBonesPct: 0.5 }, text: "Fünfhundert Hügelgräber: +50 % Knochen aus Kämpfen." },
    duemmer:          { name: "Moorleichen", income: { corpses: 2 }, text: "Der Torf gibt seine Toten: +2 Leichen pro Tag." },
    steinhaeuser:     { name: "Großsteingräber", artifact: "huenenknochen" },
    heidekoenigin:    { name: "Hof der Heidekönigin", artifact: "herz_der_heide" },
    arendsee:         { name: "Versunkene Burg", buff: { lootCorpsesPct: 0.25 }, text: "Die Ertrunkenen dienen gern: +25 % Leichen aus Kämpfen." }
  },

  // Artifacts: found at special places, kept in the inventory; only equipped ones work
  // (artifactSlots). Effects: lichHp/lichDamage/lichShield (flat), undeadHpPct/undeadDamagePct (share),
  // undeadMr/undeadIni (flat), travelPct, commandLimit, healPct, soulsPerVictory, knowledgePerVictory,
  // lootBonesPct, lootCorpsesPct.
  artifactSlots: 3,
  artifacts: {
    reichsschwert:        { name: "Reichsschwert Barbarossas", effect: { lichDamage: 6 }, text: "Der Lich führt die Klinge des schlafenden Kaisers: +6 Schaden." },
    glocken_rungholt:     { name: "Glocke von Rungholt", effect: { soulsPerVictory: 2 }, text: "Ihr Läuten fängt Seelen: +2 Seelen pro Sieg." },
    svantevit_horn:       { name: "Trinkhorn des Svantevit", effect: { undeadIni: 1 }, text: "Der vierköpfige Gott sieht in alle Richtungen: Untote +1 Initiative." },
    schlangenkrone:       { name: "Krone des Schlangenkönigs", effect: { lichShield: 10 }, text: "Ein Schild aus Schlangenhaut: Lich +10 Seelenschild." },
    lehniner_weissagung:  { name: "Lehniner Weissagung", effect: { knowledgePerVictory: 1 }, text: "Wer das Ende kennt, lernt schneller: +1 Wissen pro Sieg." },
    merseburger_sprueche: { name: "Merseburger Zaubersprüche", effect: { healPct: 0.15 }, text: "„Bein zu Bein, Blut zu Blut“: nach einem Sieg +15 % mehr Heilung." },
    reliquienkasten:      { name: "Reliquienkasten der Ottonen", effect: { undeadMr: 1 }, text: "Heilige Knochen, unheilig benutzt: Untote +1 Magieresistenz." },
    zwergenhammer:        { name: "Zwergenhammer", effect: { undeadDamagePct: 0.1 }, text: "Geschmiedet unter dem Iberg: Untote +10 % Schaden." },
    jagdhorn:             { name: "Horn der Wilden Jagd", effect: { travelPct: 0.25 }, text: "Hackelbergs Horn: Reisen 25 % schneller." },
    codex_corvey:         { name: "Codex von Corvey", effect: { commandLimit: 8 }, text: "Karolingische Kriegskunst: +8 Kommando." },
    huenenknochen:        { name: "Hünenknochen", effect: { undeadHpPct: 0.1 }, text: "Knochen eines Riesen, zu Pulver gemahlen: Untote +10 % Lebenspunkte." },
    herz_der_heide:       { name: "Herz der Heide", effect: { lichHp: 30, undeadHpPct: 0.05 }, text: "Die Heide lebt im Lich weiter: Lich +30 LP, Untote +5 % LP." }
  },

  // ---------------------------------------------------------------------------
  // Factions (names match Enums.Faction; ASKANIER is an addition Kevin allowed)
  // ---------------------------------------------------------------------------
  factions: {
    UNDEAD:   { name: "Untote",            color: "#5a2d82" },
    HANSE:    { name: "Hanse",             color: "#8a2f2f" },
    GUELPHS:  { name: "Welfen",            color: "#c9a227" },
    ASKANIER: { name: "Askanier",          color: "#2f5f8a" },
    CLERGY:   { name: "Klerus",            color: "#e6e0cc" },
    WITCHES:  { name: "Hexen und Haine",   color: "#3e5a3a" },
    GRAFEN:   { name: "Grafen",            color: "#c0603a" },   // Holstein, Oldenburg, Hoya, Mansfeld, Hessen …
    MECKLENBURG: { name: "Mecklenburg",    color: "#3b8fb0" },
    WETTINER: { name: "Wettiner",          color: "#9a7a2a" }
  },

  // ---------------------------------------------------------------------------
  // Nodes: places on the world map. q/r computed with the calibrated formula in map.
  // type: PHYLACTERY | MYTHIC | WORLDLY | CHRISTIAN | VILLAGE. size = battle area edge in tiles (16 / 32 / 64).
  // garrison: enemy units placed at battle start (before threat bonus).
  // ---------------------------------------------------------------------------
  nodes: [
    { id: "wilseder_berg", name: "Wilseder Berg", q: 777,  r: 709, type: "PHYLACTERY", faction: "UNDEAD", size: 16,
      garrison: {}, desc: "Hügelgrab und Phylakterium des Lichs. Hier wird rekrutiert." },

    { id: "soltau",        name: "Soltau",            q: 754,  r: 780, type: "WORLDLY",   faction: "GUELPHS",  size: 16,
      garrison: { bauer: 16 } },
    { id: "medingen",      name: "Kloster Medingen",  q: 940,  r: 736, type: "CHRISTIAN", faction: "CLERGY",   size: 16,
      garrison: { moench: 8, priester: 4 } },
    { id: "walsrode",      name: "Kloster Walsrode",  q: 687,  r: 829, type: "CHRISTIAN", faction: "CLERGY",   size: 16,
      garrison: { moench: 8, priester: 4, bauer: 8 } },
    { id: "ebstorf",       name: "Kloster Ebstorf",   q: 910,  r: 760, type: "CHRISTIAN", faction: "CLERGY",   size: 16,
      garrison: { moench: 8, priester: 8, bauer: 8 } },
    { id: "uelzen",        name: "Uelzen",            q: 948,  r: 785, type: "WORLDLY",   faction: "HANSE",    size: 16,
      garrison: { bauer: 12, stadtwache: 8 } },
    { id: "teufelsmoor",   name: "Teufelsmoor",       q: 506,  r: 685, type: "MYTHIC",    faction: "WITCHES",  size: 16,
      garrison: { irrlicht: 12, moorgeist: 8 } },
    { id: "verden",        name: "Verden",            q: 589,  r: 805, type: "CHRISTIAN", faction: "CLERGY",   size: 16,
      garrison: { moench: 12, priester: 4, stadtwache: 8 } },
    { id: "hameln",        name: "Hameln",            q: 624,  r: 1125, type: "MYTHIC",    faction: "WITCHES",  size: 16,
      garrison: { rattenfaenger: 1, hexe: 8, irrlicht: 8 } },
    { id: "wittenberg",    name: "Wittenberg",        q: 1541, r: 1195, type: "WORLDLY",   faction: "ASKANIER", size: 16,
      garrison: { ritter: 8, armbrust: 8, stadtwache: 8 } },

    { id: "lueneburg",     name: "Lüneburg",          q: 907,  r: 673, type: "WORLDLY",   faction: "HANSE",    size: 32,
      garrison: { stadtwache: 16, armbrust: 8, bauer: 8 }, special: "lueneburg_saline", desc: "Erste Menschenhauptstadt, durch den Erbfolgekrieg geschwächt." },
    { id: "celle",         name: "Celle",             q: 821,  r: 920, type: "WORLDLY",   faction: "GUELPHS",  size: 32,
      garrison: { ritter: 8, stadtwache: 12, armbrust: 8 } },
    { id: "bremen",        name: "Bremen",            q: 471,  r: 745, type: "WORLDLY",   faction: "HANSE",    size: 32,
      garrison: { stadtwache: 16, armbrust: 12, balliste: 4, priester: 4 } },
    { id: "hannover",      name: "Hannover",          q: 726,  r: 1017, type: "WORLDLY",   faction: "GUELPHS",  size: 32,
      garrison: { ritter: 12, stadtwache: 12, armbrust: 8 } },
    { id: "braunschweig",  name: "Braunschweig",      q: 946,  r: 1056, type: "WORLDLY",   faction: "GUELPHS",  size: 32,
      garrison: { ritter: 16, armbrust: 8, balliste: 4 } },
    { id: "magdeburg",     name: "Magdeburg",         q: 1253, r: 1107, type: "CHRISTIAN", faction: "CLERGY",   size: 32,
      garrison: { moench: 12, priester: 8, stadtwache: 12, balliste: 4 } },

    { id: "hamburg",       name: "Hamburg",           q: 791,  r: 558, type: "WORLDLY",   faction: "HANSE",    size: 64,
      garrison: { stadtwache: 24, armbrust: 16, balliste: 8 } },
    { id: "berlin",        name: "Berlin",            q: 1734, r: 931, type: "WORLDLY",   faction: "ASKANIER", size: 64,
      garrison: { stadtwache: 20, armbrust: 16, ritter: 8, balliste: 4 } },
    { id: "brocken",       name: "Brocken",           q: 975,  r: 1239, type: "MYTHIC",    faction: "WITCHES",  size: 64,
      garrison: { brockenhexe: 1, hexe: 16, irrlicht: 16, moorgeist: 8 }, finale: true,
      desc: "Mächtigster Ley-Knoten. Sieg hier gewinnt das Spiel." },

    // --- Villages: small named places between the larger ones (easier than Soltau). First proposal. ---
    { id: "undeloh", name: "Undeloh", q: 789, r: 698, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "egestorf", name: "Egestorf", q: 813, r: 697, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "bispingen", name: "Bispingen", q: 795, r: 741, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "schneverdingen", name: "Schneverdingen", q: 740, r: 728, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "amelinghausen", name: "Amelinghausen", q: 854, r: 725, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "munster", name: "Munster", q: 820, r: 779, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "hermannsburg", name: "Hermannsburg", q: 822, r: 839, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "bergen", name: "Bergen", q: 787, r: 847, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "salzhausen", name: "Salzhausen", q: 841, r: 686, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "hanstedt", name: "Hanstedt", q: 799, r: 672, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "bienenbuettel", name: "Bienenbüttel", q: 927, r: 715, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "suderburg", name: "Suderburg", q: 919, r: 813, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "unterluess", name: "Unterlüß", q: 876, r: 835, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "fallingbostel", name: "Fallingbostel", q: 715, r: 827, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "visselhoevede", name: "Visselhövede", q: 683, r: 780, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 8 } },
    { id: "tostedt", name: "Tostedt", q: 716, r: 665, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 8, moench: 4 } },
    { id: "zeven", name: "Zeven", q: 600, r: 659, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 8, moench: 4 } },
    { id: "buxtehude", name: "Buxtehude", q: 712, r: 588, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 8, moench: 4 } },
    { id: "achim", name: "Achim", q: 533, r: 769, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "syke", name: "Syke", q: 478, r: 808, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "schwarmstedt", name: "Schwarmstedt", q: 694, r: 900, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "burgdorf", name: "Burgdorf", q: 802, r: 990, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "wittingen", name: "Wittingen", q: 999, r: 876, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "dannenberg", name: "Dannenberg", q: 1093, r: 729, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "hitzacker", name: "Hitzacker", q: 1078, r: 709, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "bleckede", name: "Bleckede", q: 992, r: 657, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "lauenburg", name: "Lauenburg", q: 944, r: 626, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 12 } },
    { id: "bergedorf", name: "Bergedorf", q: 850, r: 582, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 12 } },
    { id: "neustadt", name: "Neustadt am Rübenberge", q: 651, r: 967, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "peine", name: "Peine", q: 864, r: 1038, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 8, moench: 4 } },
    { id: "wolfenbuettel", name: "Wolfenbüttel", q: 949, r: 1098, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "harzburg", name: "Harzburg", q: 959, r: 1207, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },
    { id: "ilsenburg", name: "Ilsenburg", q: 993, r: 1213, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 8, moench: 4 } },
    { id: "schierke", name: "Schierke", q: 990, r: 1252, type: "VILLAGE", faction: "WITCHES", size: 16, garrison: { irrlicht: 8 } },
    { id: "oschersleben", name: "Oschersleben", q: 1144, r: 1145, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 8, moench: 4 } },
    { id: "haldensleben", name: "Haldensleben", q: 1190, r: 1043, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 8, moench: 4 } },
    { id: "gardelegen", name: "Gardelegen", q: 1182, r: 952, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 12 } },
    { id: "salzwedel", name: "Salzwedel", q: 1110, r: 827, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 12 } },
    { id: "tangermuende", name: "Tangermünde", q: 1339, r: 940, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 8, armbrust: 4 } },
    { id: "burg", name: "Burg", q: 1313, r: 1045, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 8, moench: 4 } },
    { id: "genthin", name: "Genthin", q: 1395, r: 990, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 8, armbrust: 4 } },
    { id: "zerbst", name: "Zerbst", q: 1381, r: 1163, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 8, armbrust: 4 } },
    { id: "belzig", name: "Belzig", q: 1519, r: 1089, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 8, armbrust: 4 } },
    { id: "nauen", name: "Nauen", q: 1588, r: 904, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 8, armbrust: 4 } },
    { id: "bernau", name: "Bernau", q: 1780, r: 865, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 8, armbrust: 4 } },
    { id: "koenigswusterhausen", name: "Wusterhausen", q: 1802, r: 1013, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 8, armbrust: 4 } },
    { id: "rathenow", name: "Rathenow", q: 1439, r: 910, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 8, armbrust: 4 } },
    { id: "nienburg", name: "Nienburg", q: 581, r: 915, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 12 } },

    // --- Added 2026-11: wider map (north, west, south, east); lat/lon for reference ---
    { id: "luebeck", name: "Lübeck", q: 973, r: 433, type: "WORLDLY", faction: "HANSE", size: 64,
      garrison: { stadtwache: 24, armbrust: 16, ritter: 4, balliste: 8 }, special: "luebeck_kontor", desc: "Königin der Hanse. Ihr Kontor kennt jeden Handelsweg.", lat: 53.866, lon: 10.687 },
    { id: "kiel", name: "Kiel", q: 824, r: 257, type: "WORLDLY", faction: "HANSE", size: 16,
      garrison: { stadtwache: 12, armbrust: 8, bauer: 4 }, lat: 54.323, lon: 10.139 },
    { id: "schleswig", name: "Schleswig", q: 673, r: 184, type: "CHRISTIAN", faction: "CLERGY", size: 32,
      garrison: { moench: 12, priester: 8, kleriker: 8, stadtwache: 8 }, desc: "Dom und Bischofssitz an der Schlei.", lat: 54.515, lon: 9.565 },
    { id: "husum", name: "Husum", q: 538, r: 200, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 54.477, lon: 9.051 },
    { id: "rendsburg", name: "Rendsburg", q: 699, r: 266, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 54.304, lon: 9.664 },
    { id: "itzehoe", name: "Itzehoe", q: 662, r: 414, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.925, lon: 9.516 },
    { id: "neumuenster", name: "Neumünster", q: 785, r: 356, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 54.071, lon: 9.985 },
    { id: "segeberg", name: "Segeberg", q: 872, r: 408, type: "WORLDLY", faction: "GRAFEN", size: 16,
      garrison: { ritter: 4, stadtwache: 8, bauer: 8 }, special: "segeberg_kalk", desc: "Burg auf dem Kalkberg, Sitz der Schauenburger Grafen.", lat: 53.936, lon: 10.309 },
    { id: "ploen", name: "Plön", q: 900, r: 319, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 54.162, lon: 10.421 },
    { id: "oldesloe", name: "Oldesloe", q: 891, r: 456, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.811, lon: 10.374 },
    { id: "ratzeburg", name: "Ratzeburg", q: 994, r: 498, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, desc: "Inseldom des Bistums Ratzeburg.", lat: 53.699, lon: 10.757 },
    { id: "moelln", name: "Mölln", q: 977, r: 526, type: "VILLAGE", faction: "HANSE", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.627, lon: 10.69 },
    { id: "rungholt", name: "Rungholt", q: 472, r: 167, type: "MYTHIC", faction: "WITCHES", size: 32,
      garrison: { moorgeist: 16, irrlicht: 12 }, special: "rungholt", desc: "Vor neun Jahren in der Groten Mandränke versunken. Bei Ebbe läuten unter dem Watt die Glocken.", lat: 54.56, lon: 8.8 },
    { id: "wismar", name: "Wismar", q: 1180, r: 418, type: "WORLDLY", faction: "HANSE", size: 32,
      garrison: { stadtwache: 16, armbrust: 12, balliste: 4 }, lat: 53.892, lon: 11.465 },
    { id: "rostock", name: "Rostock", q: 1355, r: 335, type: "WORLDLY", faction: "HANSE", size: 32,
      garrison: { stadtwache: 16, armbrust: 12, balliste: 4 }, lat: 54.088, lon: 12.14 },
    { id: "stralsund", name: "Stralsund", q: 1599, r: 238, type: "WORLDLY", faction: "HANSE", size: 32,
      garrison: { stadtwache: 16, armbrust: 12, balliste: 4 }, desc: "Vor einem Jahr hat sie Dänemark den Frieden diktiert.", lat: 54.309, lon: 13.081 },
    { id: "greifswald", name: "Greifswald", q: 1683, r: 316, type: "WORLDLY", faction: "HANSE", size: 16,
      garrison: { stadtwache: 12, armbrust: 8, bauer: 4 }, lat: 54.096, lon: 13.378 },
    { id: "anklam", name: "Anklam", q: 1772, r: 406, type: "VILLAGE", faction: "HANSE", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.856, lon: 13.69 },
    { id: "schwerin", name: "Schwerin", q: 1170, r: 521, type: "WORLDLY", faction: "MECKLENBURG", size: 32,
      garrison: { ritter: 8, stadtwache: 12, armbrust: 8 }, desc: "Residenz der Herzöge von Mecklenburg.", lat: 53.629, lon: 11.414 },
    { id: "guestrow", name: "Güstrow", q: 1371, r: 449, type: "WORLDLY", faction: "MECKLENBURG", size: 16,
      garrison: { ritter: 4, stadtwache: 8, bauer: 8 }, lat: 53.794, lon: 12.175 },
    { id: "doberan", name: "Kloster Doberan", q: 1293, r: 330, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, special: "doberan", desc: "Zisterzienser, Grablege der Mecklenburger Fürsten.", lat: 54.106, lon: 11.906 },
    { id: "parchim", name: "Parchim", q: 1290, r: 596, type: "VILLAGE", faction: "MECKLENBURG", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.426, lon: 11.849 },
    { id: "waren", name: "Waren", q: 1512, r: 551, type: "VILLAGE", faction: "MECKLENBURG", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.519, lon: 12.68 },
    { id: "neubrandenburg", name: "Neubrandenburg", q: 1666, r: 529, type: "WORLDLY", faction: "MECKLENBURG", size: 16,
      garrison: { ritter: 4, stadtwache: 8, bauer: 8 }, lat: 53.557, lon: 13.261 },
    { id: "demmin", name: "Demmin", q: 1599, r: 395, type: "VILLAGE", faction: "MECKLENBURG", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.905, lon: 13.043 },
    { id: "wolgast", name: "Wolgast", q: 1789, r: 327, type: "VILLAGE", faction: "MECKLENBURG", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 54.053, lon: 13.774 },
    { id: "pasewalk", name: "Pasewalk", q: 1863, r: 537, type: "VILLAGE", faction: "MECKLENBURG", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.506, lon: 13.99 },
    { id: "bergen_ruegen", name: "Bergen auf Rügen", q: 1688, r: 192, type: "VILLAGE", faction: "MECKLENBURG", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 54.416, lon: 13.433 },
    { id: "barth", name: "Barth", q: 1504, r: 219, type: "VILLAGE", faction: "MECKLENBURG", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 54.369, lon: 12.725 },
    { id: "gadebusch", name: "Gadebusch", q: 1090, r: 495, type: "VILLAGE", faction: "MECKLENBURG", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.7, lon: 11.115 },
    { id: "hagenow", name: "Hagenow", q: 1113, r: 599, type: "VILLAGE", faction: "MECKLENBURG", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.431, lon: 11.189 },
    { id: "boizenburg", name: "Boizenburg", q: 989, r: 621, type: "VILLAGE", faction: "MECKLENBURG", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.381, lon: 10.724 },
    { id: "arkona", name: "Kap Arkona", q: 1681, r: 89, type: "MYTHIC", faction: "WITCHES", size: 32,
      garrison: { druide: 12, druidin: 8, schwarzer_hund: 12 }, special: "arkona", desc: "Ruinen des Svantevit-Tempels. Die Ranen haben ihren Gott nie ganz vergessen.", lat: 54.677, lon: 13.433 },
    { id: "vineta", name: "Vineta", q: 1829, r: 318, type: "MYTHIC", faction: "WITCHES", size: 16,
      garrison: { moorgeist: 12, irrlicht: 8 }, special: "vineta", desc: "Die versunkene Stadt vor Usedom. Wer ihre Glocken hört, hört die Toten.", lat: 54.072, lon: 13.93 },
    { id: "prenzlau", name: "Prenzlau", q: 1835, r: 613, type: "WORLDLY", faction: "ASKANIER", size: 16,
      garrison: { ritter: 4, stadtwache: 8, bauer: 8 }, lat: 53.316, lon: 13.862 },
    { id: "templin", name: "Templin", q: 1743, r: 696, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 53.118, lon: 13.502 },
    { id: "angermuende", name: "Angermünde", q: 1880, r: 728, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 53.016, lon: 13.997 },
    { id: "eberswalde", name: "Eberswalde", q: 1838, r: 802, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 52.833, lon: 13.82 },
    { id: "chorin", name: "Kloster Chorin", q: 1853, r: 779, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, lat: 52.89, lon: 13.883 },
    { id: "strausberg", name: "Strausberg", q: 1863, r: 900, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 52.579, lon: 13.884 },
    { id: "fuerstenwalde", name: "Fürstenwalde", q: 1919, r: 982, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, desc: "Bischofssitz von Lebus.", lat: 52.361, lon: 14.062 },
    { id: "neuruppin", name: "Neuruppin", q: 1559, r: 780, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 52.925, lon: 12.804 },
    { id: "wittstock", name: "Wittstock", q: 1467, r: 691, type: "VILLAGE", faction: "CLERGY", size: 16,
      garrison: { bauer: 12 }, lat: 53.163, lon: 12.484 },
    { id: "havelberg", name: "Havelberg", q: 1363, r: 827, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, desc: "Dom auf dem Berg über der Havel.", lat: 52.826, lon: 12.074 },
    { id: "perleberg", name: "Perleberg", q: 1300, r: 733, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 53.074, lon: 11.861 },
    { id: "brandenburg", name: "Brandenburg", q: 1503, r: 983, type: "WORLDLY", faction: "ASKANIER", size: 32,
      garrison: { ritter: 8, stadtwache: 12, armbrust: 8 }, desc: "Die alte Hauptstadt der Mark.", lat: 52.412, lon: 12.554 },
    { id: "lehnin", name: "Kloster Lehnin", q: 1557, r: 1017, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, special: "lehnin", desc: "Hauskloster der Askanier. Seine Weissagung kennt das Ende jedes Fürstenhauses.", lat: 52.32, lon: 12.745 },
    { id: "potsdam", name: "Potsdam", q: 1642, r: 982, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 52.4, lon: 13.06 },
    { id: "spandau", name: "Spandau", q: 1678, r: 927, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 52.535, lon: 13.205 },
    { id: "jueterbog", name: "Jüterbog", q: 1656, r: 1140, type: "VILLAGE", faction: "CLERGY", size: 16,
      garrison: { bauer: 12 }, lat: 51.993, lon: 13.073 },
    { id: "treuenbrietzen", name: "Treuenbrietzen", q: 1597, r: 1102, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 52.098, lon: 12.871 },
    { id: "luebben", name: "Lübben", q: 1885, r: 1148, type: "VILLAGE", faction: "WETTINER", size: 16,
      garrison: { bauer: 12 }, lat: 51.941, lon: 13.893 },
    { id: "luckau", name: "Luckau", q: 1836, r: 1186, type: "VILLAGE", faction: "WETTINER", size: 16,
      garrison: { bauer: 12 }, lat: 51.852, lon: 13.707 },
    { id: "spreewald", name: "Spreewald", q: 1920, r: 1174, type: "MYTHIC", faction: "WITCHES", size: 32,
      garrison: { moorgeist: 12, irrlicht: 12, hexe: 8 }, special: "spreewald", desc: "Hunderte Fließe im Erlenbruch. Hier herrscht der Schlangenkönig mit seiner Krone.", lat: 51.87, lon: 14.01 },
    { id: "herzberg", name: "Herzberg", q: 1708, r: 1256, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 51.691, lon: 13.234 },
    { id: "torgau", name: "Torgau", q: 1648, r: 1310, type: "VILLAGE", faction: "WETTINER", size: 16,
      garrison: { bauer: 12 }, lat: 51.561, lon: 13.006 },
    { id: "meissen", name: "Meißen", q: 1790, r: 1458, type: "WORLDLY", faction: "WETTINER", size: 32,
      garrison: { ritter: 8, stadtwache: 12, armbrust: 8 }, desc: "Burgberg der Markgrafen von Meißen.", lat: 51.163, lon: 13.473 },
    { id: "dresden", name: "Dresden", q: 1868, r: 1497, type: "WORLDLY", faction: "WETTINER", size: 16,
      garrison: { ritter: 4, stadtwache: 8, bauer: 8 }, lat: 51.051, lon: 13.738 },
    { id: "dessau", name: "Dessau", q: 1429, r: 1212, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 51.833, lon: 12.243 },
    { id: "koethen", name: "Köthen", q: 1354, r: 1247, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 51.752, lon: 11.97 },
    { id: "bernburg", name: "Bernburg", q: 1289, r: 1232, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 51.795, lon: 11.738 },
    { id: "halle", name: "Halle", q: 1359, r: 1352, type: "WORLDLY", faction: "CLERGY", size: 32,
      garrison: { ritter: 8, stadtwache: 12, armbrust: 8 }, special: "halle_saline", desc: "Salzstadt des Erzbischofs von Magdeburg.", lat: 51.482, lon: 11.97 },
    { id: "merseburg", name: "Merseburg", q: 1368, r: 1402, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, special: "merseburg", desc: "Hier liegen die Merseburger Zaubersprüche.", lat: 51.355, lon: 11.993 },
    { id: "leipzig", name: "Leipzig", q: 1476, r: 1403, type: "WORLDLY", faction: "WETTINER", size: 32,
      garrison: { ritter: 8, stadtwache: 12, armbrust: 8 }, desc: "Messestadt an der Kreuzung der Handelsstraßen.", lat: 51.34, lon: 12.375 },
    { id: "delitzsch", name: "Delitzsch", q: 1463, r: 1331, type: "VILLAGE", faction: "WETTINER", size: 16,
      garrison: { bauer: 12 }, lat: 51.526, lon: 12.342 },
    { id: "weissenfels", name: "Weißenfels", q: 1364, r: 1462, type: "VILLAGE", faction: "WETTINER", size: 16,
      garrison: { bauer: 12 }, lat: 51.2, lon: 11.969 },
    { id: "naumburg", name: "Naumburg", q: 1320, r: 1482, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, desc: "Dom mit den zwölf Stifterfiguren.", lat: 51.152, lon: 11.81 },
    { id: "eisleben", name: "Eisleben", q: 1240, r: 1338, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 51.528, lon: 11.548 },
    { id: "mansfeld", name: "Mansfeld", q: 1212, r: 1313, type: "WORLDLY", faction: "GRAFEN", size: 16,
      garrison: { ritter: 4, stadtwache: 8, bauer: 8 }, special: "mansfeld_kupfer", desc: "Kupferschiefer, Stollen und Schlackenhalden.", lat: 51.594, lon: 11.454 },
    { id: "sangerhausen", name: "Sangerhausen", q: 1171, r: 1361, type: "VILLAGE", faction: "WETTINER", size: 16,
      garrison: { bauer: 12 }, lat: 51.473, lon: 11.3 },
    { id: "kyffhaeuser", name: "Kyffhäuser", q: 1118, r: 1386, type: "MYTHIC", faction: "WITCHES", size: 32,
      garrison: { ritter: 8, stadtwache: 12, zwergenkoenig: 1 }, special: "kyffhaeuser", desc: "Im Berg schläft Kaiser Friedrich am Steintisch. Sein Bart ist schon zweimal herumgewachsen.", lat: 51.413, lon: 11.108 },
    { id: "goslar", name: "Goslar", q: 922, r: 1198, type: "WORLDLY", faction: "HANSE", size: 32,
      garrison: { stadtwache: 16, armbrust: 12, balliste: 4 }, special: "rammelsberg", desc: "Kaiserpfalz und Silber aus dem Rammelsberg.", lat: 51.906, lon: 10.429 },
    { id: "halberstadt", name: "Halberstadt", q: 1095, r: 1198, type: "CHRISTIAN", faction: "CLERGY", size: 32,
      garrison: { moench: 12, priester: 8, kleriker: 8, stadtwache: 8 }, desc: "Bischofssitz am Nordrand des Harzes.", lat: 51.896, lon: 11.048 },
    { id: "quedlinburg", name: "Quedlinburg", q: 1122, r: 1240, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, special: "quedlinburg", desc: "Damenstift mit dem Domschatz der Ottonen.", lat: 51.789, lon: 11.141 },
    { id: "hexentanzplatz", name: "Hexentanzplatz", q: 1092, r: 1262, type: "MYTHIC", faction: "WITCHES", size: 32,
      garrison: { hexe: 16, irrlicht: 8, heideschwester: 8 }, special: "hexentanzplatz", desc: "Felsplateau über dem Bodetal. In der Walpurgisnacht fliegen von hier die Hexen zum Brocken.", lat: 51.735, lon: 11.03 },
    { id: "teufelsmauer", name: "Teufelsmauer", q: 1076, r: 1239, type: "MYTHIC", faction: "WITCHES", size: 16,
      garrison: { hexe: 8, schwarzer_hund: 8 }, special: "teufelsmauer", desc: "Der Teufel baute die Mauer, um sein Reich vom Gottes abzugrenzen.", lat: 51.795, lon: 10.975 },
    { id: "wernigerode", name: "Wernigerode", q: 1022, r: 1224, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 51.835, lon: 10.785 },
    { id: "nordhausen", name: "Nordhausen", q: 1028, r: 1353, type: "WORLDLY", faction: "HANSE", size: 16,
      garrison: { stadtwache: 12, armbrust: 8, bauer: 4 }, lat: 51.503, lon: 10.791 },
    { id: "osterode", name: "Osterode", q: 874, r: 1269, type: "VILLAGE", faction: "GUELPHS", size: 16,
      garrison: { bauer: 12 }, lat: 51.728, lon: 10.252 },
    { id: "iberg", name: "Zwergenlöcher am Iberg", q: 903, r: 1237, type: "MYTHIC", faction: "WITCHES", size: 16,
      garrison: { zwergenkoenig: 1, stadtwache: 8 }, special: "iberg", desc: "Tropfsteinhöhlen, in denen die Bergleute nachts Hämmern hören.", lat: 51.807, lon: 10.358 },
    { id: "hackelberg", name: "Hackelbergs Grab", q: 975, r: 1178, type: "MYTHIC", faction: "WITCHES", size: 32,
      garrison: { wode: 1, schwarzer_hund: 16, irrlicht: 8 }, special: "hackelberg", desc: "Der Oberjägermeister, der lieber jagen als in den Himmel wollte. Seither reitet er mit der Wilden Jagd.", lat: 51.955, lon: 10.62 },
    { id: "gandersheim", name: "Stift Gandersheim", q: 810, r: 1214, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, lat: 51.87, lon: 10.026 },
    { id: "seesen", name: "Seesen", q: 853, r: 1205, type: "VILLAGE", faction: "GUELPHS", size: 16,
      garrison: { bauer: 12 }, lat: 51.891, lon: 10.179 },
    { id: "goettingen", name: "Göttingen", q: 787, r: 1345, type: "WORLDLY", faction: "GUELPHS", size: 32,
      garrison: { ritter: 8, stadtwache: 12, armbrust: 8 }, lat: 51.534, lon: 9.935 },
    { id: "northeim", name: "Northeim", q: 804, r: 1278, type: "VILLAGE", faction: "GUELPHS", size: 16,
      garrison: { bauer: 12 }, lat: 51.706, lon: 9.999 },
    { id: "einbeck", name: "Einbeck", q: 767, r: 1234, type: "WORLDLY", faction: "GUELPHS", size: 16,
      garrison: { ritter: 4, stadtwache: 8, bauer: 8 }, desc: "Sein Bier trinkt man bis nach Lübeck.", lat: 51.818, lon: 9.868 },
    { id: "muenden", name: "Münden", q: 709, r: 1391, type: "VILLAGE", faction: "GUELPHS", size: 16,
      garrison: { bauer: 12 }, lat: 51.418, lon: 9.654 },
    { id: "kassel", name: "Kassel", q: 665, r: 1431, type: "WORLDLY", faction: "GRAFEN", size: 32,
      garrison: { ritter: 8, stadtwache: 12, armbrust: 8 }, desc: "Residenz der Landgrafen von Hessen.", lat: 51.315, lon: 9.497 },
    { id: "muehlhausen", name: "Mühlhausen", q: 935, r: 1470, type: "WORLDLY", faction: "WETTINER", size: 16,
      garrison: { ritter: 4, stadtwache: 8, bauer: 8 }, lat: 51.208, lon: 10.453 },
    { id: "corvey", name: "Kloster Corvey", q: 639, r: 1251, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, special: "corvey", desc: "Reichsabtei mit einer Bibliothek aus karolingischer Zeit.", lat: 51.778, lon: 9.41 },
    { id: "alfeld", name: "Alfeld", q: 754, r: 1169, type: "VILLAGE", faction: "CLERGY", size: 16,
      garrison: { bauer: 12 }, lat: 51.986, lon: 9.826 },
    { id: "hildesheim", name: "Hildesheim", q: 788, r: 1105, type: "CHRISTIAN", faction: "CLERGY", size: 32,
      garrison: { moench: 12, priester: 8, kleriker: 8, stadtwache: 8 }, desc: "Bischofsstadt mit dem tausendjährigen Rosenstock.", lat: 52.15, lon: 9.951 },
    { id: "paderborn", name: "Paderborn", q: 456, r: 1275, type: "CHRISTIAN", faction: "CLERGY", size: 32,
      garrison: { moench: 12, priester: 8, kleriker: 8, stadtwache: 8 }, lat: 51.719, lon: 8.754 },
    { id: "externsteine", name: "Externsteine", q: 502, r: 1216, type: "MYTHIC", faction: "WITCHES", size: 32,
      garrison: { druide: 16, druidin: 8, irrlicht: 8 }, special: "externsteine", desc: "Sandsteinfelsen im Teutoburger Wald. Ein uralter Ley-Knoten, den die Mönche nur übermalt haben.", lat: 51.869, lon: 8.918 },
    { id: "lemgo", name: "Lemgo", q: 497, r: 1154, type: "VILLAGE", faction: "HANSE", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 52.028, lon: 8.901 },
    { id: "herford", name: "Herford", q: 433, r: 1120, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, lat: 52.115, lon: 8.671 },
    { id: "bielefeld", name: "Bielefeld", q: 395, r: 1156, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 52.021, lon: 8.532 },
    { id: "minden", name: "Minden", q: 502, r: 1052, type: "CHRISTIAN", faction: "CLERGY", size: 32,
      garrison: { moench: 12, priester: 8, kleriker: 8, stadtwache: 8 }, desc: "Bistum an der Weserpforte.", lat: 52.289, lon: 8.918 },
    { id: "stadthagen", name: "Stadthagen", q: 581, r: 1038, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 52.325, lon: 9.206 },
    { id: "rinteln", name: "Rinteln", q: 546, r: 1092, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 52.188, lon: 9.079 },
    { id: "osnabrueck", name: "Osnabrück", q: 262, r: 1055, type: "CHRISTIAN", faction: "CLERGY", size: 32,
      garrison: { moench: 12, priester: 8, kleriker: 8, stadtwache: 8 }, lat: 52.279, lon: 8.047 },
    { id: "muenster", name: "Münster", q: 143, r: 1176, type: "CHRISTIAN", faction: "CLERGY", size: 32,
      garrison: { moench: 12, priester: 8, kleriker: 8, stadtwache: 8 }, desc: "Fürstbistum, das größte im Westen.", lat: 51.962, lon: 7.626 },
    { id: "oldenburg", name: "Oldenburg", q: 312, r: 719, type: "WORLDLY", faction: "GRAFEN", size: 32,
      garrison: { ritter: 8, stadtwache: 12, armbrust: 8 }, desc: "Sitz der Grafen von Oldenburg.", lat: 53.141, lon: 8.214 },
    { id: "delmenhorst", name: "Delmenhorst", q: 425, r: 755, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.051, lon: 8.632 },
    { id: "wildeshausen", name: "Wildeshausen", q: 370, r: 815, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 52.898, lon: 8.433 },
    { id: "pestrup", name: "Pestruper Gräberfeld", q: 378, r: 824, type: "MYTHIC", faction: "WITCHES", size: 16,
      garrison: { druide: 8, schwarzer_hund: 8 }, special: "pestrup", desc: "Fünfhundert Grabhügel in der Heide. Hier liegen mehr Knochen als in jeder Stadt.", lat: 52.875, lon: 8.46 },
    { id: "vechta", name: "Vechta", q: 329, r: 880, type: "VILLAGE", faction: "CLERGY", size: 16,
      garrison: { bauer: 12 }, lat: 52.729, lon: 8.286 },
    { id: "cloppenburg", name: "Cloppenburg", q: 264, r: 833, type: "VILLAGE", faction: "CLERGY", size: 16,
      garrison: { bauer: 12 }, lat: 52.847, lon: 8.045 },
    { id: "duemmer", name: "Dümmer-Moor", q: 341, r: 963, type: "MYTHIC", faction: "WITCHES", size: 16,
      garrison: { moorgeist: 12, irrlicht: 8 }, special: "duemmer", desc: "Weites Moor am See. Der Torf gibt seine Toten nicht her – es sei denn, man fragt richtig.", lat: 52.515, lon: 8.33 },
    { id: "diepholz", name: "Diepholz", q: 352, r: 928, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 52.607, lon: 8.37 },
    { id: "hoya", name: "Hoya", q: 562, r: 850, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 52.808, lon: 9.137 },
    { id: "aurich", name: "Aurich", q: 117, r: 587, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.471, lon: 7.483 },
    { id: "emden", name: "Emden", q: 42, r: 627, type: "WORLDLY", faction: "GRAFEN", size: 16,
      garrison: { ritter: 4, stadtwache: 8, bauer: 8 }, lat: 53.367, lon: 7.206 },
    { id: "jever", name: "Jever", q: 229, r: 549, type: "VILLAGE", faction: "GRAFEN", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.574, lon: 7.898 },
    { id: "stade", name: "Stade", q: 652, r: 541, type: "WORLDLY", faction: "HANSE", size: 16,
      garrison: { stadtwache: 12, armbrust: 8, bauer: 4 }, lat: 53.6, lon: 9.476 },
    { id: "otterndorf", name: "Otterndorf", q: 498, r: 460, type: "VILLAGE", faction: "HANSE", size: 16,
      garrison: { bauer: 12, armbrust: 4 }, lat: 53.809, lon: 8.899 },
    { id: "sieben_steinhaeuser", name: "Sieben Steinhäuser", q: 760, r: 833, type: "MYTHIC", faction: "WITCHES", size: 16,
      garrison: { druide: 8, druidin: 4 }, special: "steinhaeuser", desc: "Fünf Großsteingräber im Wald. Die Druiden behaupten, es seien einmal sieben gewesen.", lat: 52.85, lon: 9.865 },
    { id: "oldendorf", name: "Oldendorfer Totenstatt", q: 879, r: 714, type: "MYTHIC", faction: "WITCHES", size: 32,
      garrison: { heidekoenigin: 1, heideschwester: 12, druidin: 8 }, special: "heidekoenigin", desc: "Hünenbetten im Luhetal. Hier hält die Heidekönigin Hof.", lat: 53.15, lon: 10.31 },
    { id: "stendal", name: "Stendal", q: 1308, r: 916, type: "WORLDLY", faction: "HANSE", size: 16,
      garrison: { stadtwache: 12, armbrust: 8, bauer: 4 }, lat: 52.604, lon: 11.858 },
    { id: "osterburg", name: "Osterburg", q: 1276, r: 846, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 52.787, lon: 11.753 },
    { id: "arendsee", name: "Arendsee", q: 1199, r: 808, type: "MYTHIC", faction: "WITCHES", size: 16,
      garrison: { moorgeist: 8, irrlicht: 8 }, special: "arendsee", desc: "Im See versank eine Burg samt ihrer Besatzung. Manchmal steigen Blasen auf, als atme jemand.", lat: 52.888, lon: 11.478 },
    { id: "kloetze", name: "Klötze", q: 1117, r: 913, type: "VILLAGE", faction: "ASKANIER", size: 16,
      garrison: { bauer: 12 }, lat: 52.627, lon: 11.164 },
    { id: "gifhorn", name: "Gifhorn", q: 950, r: 974, type: "VILLAGE", faction: "GUELPHS", size: 16,
      garrison: { bauer: 12 }, lat: 52.481, lon: 10.547 },
    { id: "fallersleben", name: "Fallersleben", q: 998, r: 997, type: "VILLAGE", faction: "GUELPHS", size: 16,
      garrison: { bauer: 12 }, lat: 52.418, lon: 10.722 },
    { id: "helmstedt", name: "Helmstedt", q: 1080, r: 1070, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, lat: 52.228, lon: 11.01 },
    { id: "koenigslutter", name: "Königslutter", q: 1027, r: 1061, type: "CHRISTIAN", faction: "CLERGY", size: 16,
      garrison: { moench: 8, priester: 4, kleriker: 4 }, desc: "Kaiserdom über dem Grab Lothars III.", lat: 52.251, lon: 10.818 }
  ],

  // ---------------------------------------------------------------------------
  // Buildings on battlefields (first proposal).
  // tiles: each tile is a path of direction steps from the anchor (0=N, 1=NE, 2=SE, 3=S, 4=SW, 5=NW);
  //        [] is the anchor itself. The whole shape is rotated by a random multiple of 60 degrees.
  // floor: floor type inside. doors: open edges to the outside. windows: outer walls that become
  // WALL_TRANSPARENT (block movement and melee, not sight or missiles). wall: edge type of the outer walls.
  // ---------------------------------------------------------------------------
  buildings: {
    hut:       { name: "Kate",        tiles: [[]],                                   floor: "WOOD_FLOOR",  doors: 1, windows: 0 },
    house:     { name: "Haus",        tiles: [[], [0], [1]],                         floor: "STONE_FLOOR", doors: 1, windows: 1 },
    longhouse: { name: "Langhaus",    tiles: [[], [0], [0, 0], [0, 0, 0]],           floor: "WOOD_FLOOR",  doors: 2, windows: 0 },
    manor:     { name: "Gutshof",     tiles: [[], [0], [1], [0, 1]],                 floor: "STONE_FLOOR", doors: 1, windows: 2 },
    hall:      { name: "Gildehalle",  tiles: [[], [0], [0, 0], [0, 0, 2], [0, 0, 2, 2]], floor: "STONE_FLOOR", doors: 2, windows: 2 },
    tower:     { name: "Wachturm",    tiles: [[]],                                   floor: "STONE_FLOOR", doors: 1, windows: 0, wall: "WALL_TRANSPARENT" },
    chapel:    { name: "Kapelle",     tiles: [[], [0]],                              floor: "STONE_FLOOR", doors: 1, windows: 1 },
    church:    { name: "Kirche",      tiles: [[], [0], [1], [2], [3], [4], [5]],     floor: "STONE_FLOOR", doors: 2, windows: 2 }
  },
  // Which buildings appear where. count = fixed number, countPer16 = per 16 tiles of field edge.
  // first: placed before the random mix. mix: [building, weight].
  buildingSets: {
    VILLAGE:   { count: 2, fences: 1, mix: [["hut", 3], ["house", 3], ["longhouse", 2], ["chapel", 1]] },
    WORLDLY:   { countPer16: 3, fencesPer16: 2, mix: [["house", 4], ["longhouse", 2], ["manor", 2], ["hall", 2], ["tower", 1], ["hut", 1]],
                 // Fields of at least this size get a city wall: a ring at cityWallRadius tiles with open gates.
                 cityWallMinSize: 32, cityWallRadius: 9, gates: 4 },
    CHRISTIAN: { countPer16: 3, fencesPer16: 2, first: "church", mix: [["house", 3], ["hut", 2], ["longhouse", 1], ["chapel", 1]],
                 holyRadius: 3, graveyardRadius: 2 }
  },

  // ---------------------------------------------------------------------------
  // Campaign economy
  // ---------------------------------------------------------------------------
  // Bone amounts are scaled x60 against the first proposal (30 bones per kill); costs scaled alike.
  economy: {
    startResources: { corpses: 24, bones: 960, souls: 0, knowledge: 0 },   // x4 with the stack system (knowledge unchanged)
    startArmy: ["lich", ...Array(12).fill("ghul"), ...Array(8).fill("skelett")],
    commandLimitBase: 60,              // the Lich as leader grants this (x4 with the stack system)
    commandLimitPerMythicNode: 12,     // each conquered MYTHIC node raises the limit
    corpsesPerKill: 1,                 // multiplied by corpse quality, summed, rounded down at battle end
    bonesPerKill: 30,                  // independent of quality (a skeleton yields its bones either way)
    soulsPerSoulKill: 1,               // extra souls when the killing blow was SOUL damage
    travelTilesPerDay: 39,
    // The Lich draws strength from his army: bonus per command point in use at battle start
    // (start army: 32 points -> +64 HP, +8 damage, +8 soul shield).
    lichArmyBonus: { hpPerCommand: 2, damagePerCommand: 0.25, shieldPerCommand: 0.25 },
    lichDeathDays: 3,                  // days lost when the Lich falls and returns to the phylactery
    // Loot for conquering a node, by type and size.
    nodeRewards: {
      // Materials x4 with the stack system; knowledge unchanged.
      MYTHIC:    { 16: { knowledge: 3, souls: 8, corpses: 4 }, 32: { knowledge: 4, souls: 12, corpses: 8 }, 64: { knowledge: 6, souls: 16, corpses: 12 } },
      WORLDLY:   { 16: { corpses: 16, bones: 720 },          32: { corpses: 32, bones: 1200 },         64: { corpses: 56, bones: 1920 } },
      // Monasteries keep books: conquering a christian place grants knowledge.
      CHRISTIAN: { 16: { corpses: 8, knowledge: 1 },         32: { corpses: 12, knowledge: 2 },        64: { corpses: 20, knowledge: 3 } },
      VILLAGE:   { 16: { corpses: 8, bones: 240 } }
    },
    // After a won battle every survivor regains this share of its max HP (rounded up).
    postBattleHealShare: 0.25
  },

  // Enemy stacks: a garrison type may be split into several stacks (like Heroes of Might and Magic).
  // maxStacks needs at least fullStacksFromTypes different types; with fewer types the limit is
  // stacksPerTypeFew per type. A stack is only split while every part keeps minStackSize units.
  stacks: { maxStacks: 8, maxPerType: 3, fullStacksFromTypes: 4, stacksPerTypeFew: 2, minStackSize: 4 },

  threat: {
    attackOwnNode: 25,       // faction of the attacked node
    attackOwnVillage: 10,    // faction of an attacked village (small places cause less alarm)
    attackOtherFaction: 5,   // every other living faction
    dailyDecay: 0.05,        // 5 % of the current value per day (source: design notes)
    reinforcementPer: 25,    // per full 25 % threat of the defending faction ...
    reinforcementUnits: 4    // ... this many extra units of its most numerous type
  }
};
