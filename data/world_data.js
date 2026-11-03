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
    reliefExaggeration: 8,
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
    brockenhexe: {"name": "Hexenkönigin vom Brocken", "side": "enemy", "faction": "WITCHES", "rank": "UNIQUE", "role": "CASTER", "hp": 90, "initiative": 8, "move": 4, "damage": 14, "range": 4, "power": "CHAOS", "counter": true, "defense": "DIVINE", "magicResist": 6, "soulShield": 6, "sight": 8, "hear": 8, "smell": 8, "size": 3, "spectral": false, "flying": true, "abilities": [], "shape": "octahedron", "color": "#1d1d1d", "desc": "Herrin der Walpurgisnacht, Finale der Kampagne."}
  },
  // </GEN:UNITS>

  // ---------------------------------------------------------------------------
  // Factions (names match Enums.Faction; ASKANIER is an addition Kevin allowed)
  // ---------------------------------------------------------------------------
  factions: {
    UNDEAD:   { name: "Untote",            color: "#5a2d82" },
    HANSE:    { name: "Hanse",             color: "#8a2f2f" },
    GUELPHS:  { name: "Welfen",            color: "#c9a227" },
    ASKANIER: { name: "Askanier",          color: "#2f5f8a" },
    CLERGY:   { name: "Klerus",            color: "#e6e0cc" },
    WITCHES:  { name: "Hexen und Haine",   color: "#3e5a3a" }
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
      garrison: { stadtwache: 16, armbrust: 8, bauer: 8 }, desc: "Erste Menschenhauptstadt, durch den Erbfolgekrieg geschwächt." },
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
