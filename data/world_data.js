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
    width: 1704,              // tiles (= heightmap pixels), Q axis, west -> east
    height: 920,              // tiles, R axis, north -> south (R = 0 is the north edge)
    seaLevelGray: 29,         // gray value of 0 m above sea level
    // Gray -> meters is linear: meters = gray * metersPerGray + metersAtGrayZero.
    // Everything above 450 m is capped at gray 255 (the Harz shows as a plateau).
    metersPerGray: 508 / 255,
    metersAtGrayZero: -58,
    // Calibrated georeference (fitted on coastline features, error about +-5 tiles):
    // Q = round((lon - lonLeft) * tilesPerDegree), R = round((latTop - lat) * tilesPerDegree)
    lonLeft: 7.1529,
    latTop: 54.8190,
    tilesPerDegree: 240,       // the heightmap is a native 15 arc-second grid
    startDate: { year: 1371, month: 5, day: 1 }
  },

  hex: {
    circumradius: 3.0,         // center to corner, world units (1 unit = 1 m)
    // Derived values (compute in code, do not round):
    //   inradius      = circumradius * sqrt(3) / 2   (~2.598)
    //   columnSpacing = 1.5 * circumradius           (4.5)
    //   rowSpacing    = 2 * inradius                 (~5.196)
    heightPerStep: 1.0,        // world height = sign(s) * sqrt(|s|) * heightPerStep, s = gray - seaLevelGray
    tileDepth: 20.0,           // tiles are tall prisms so height steps never show gaps
    waterLevel: -0.5           // y of the water plane
  },

  streaming: {
    radius: 32                 // visible window = (2 * radius + 1)^2 tiles around the camera pivot
  },

  camera: {
    minZoom: 10, maxZoom: 160, startZoom: 60,
    pitchDegrees: 55,          // looking down at the board
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
    noiseCellSize: 12,         // tiles per value-noise cell (larger = bigger patches), noise seed 1
    // Lueneburger Heide: inside this soft region "heathMix" replaces "mix".
    // d = distance / radius; weight = smoothstep from 1 (d <= fullUntil) to 0 (d >= fadeOut);
    // a tile is "heath" when valueNoise(cell = edgeNoiseCellSize, seed 4) < weight.
    heathRegion: { q: 725, r: 445, radius: 100, fullUntil: 0.6, fadeOut: 1.4, edgeNoiseCellSize: 10 },
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
  // Percent of damage that arrives. source: design notes ("Power-Defense-Matrix").
  powerDefense: {
    PIERCE: { UNARMORED: 100, LIGHT: 100, MEDIUM: 100, HEAVY: 75,  FORTIFIED: 50,  DIVINE: 50 },
    BLUNT:  { UNARMORED: 100, LIGHT: 100, MEDIUM: 75,  HEAVY: 100, FORTIFIED: 75,  DIVINE: 50 },
    SIEGE:  { UNARMORED: 100, LIGHT: 75,  MEDIUM: 75,  HEAVY: 100, FORTIFIED: 150, DIVINE: 50 },
    FIRE:   { UNARMORED: 100, LIGHT: 125, MEDIUM: 100, HEAVY: 75,  FORTIFIED: 50,  DIVINE: 75 },
    POISON: { UNARMORED: 100, LIGHT: 100, MEDIUM: 100, HEAVY: 75,  FORTIFIED: 0,   DIVINE: 50 },
    ARCANE: { UNARMORED: 100, LIGHT: 100, MEDIUM: 100, HEAVY: 100, FORTIFIED: 75,  DIVINE: 75 },
    SOUL:   { UNARMORED: 150, LIGHT: 125, MEDIUM: 100, HEAVY: 75,  FORTIFIED: 0,   DIVINE: 50 },
    HOLY:   { UNARMORED: 150, LIGHT: 125, MEDIUM: 100, HEAVY: 75,  FORTIFIED: 50,  DIVINE: 100 },
    CHAOS:  { UNARMORED: 100, LIGHT: 100, MEDIUM: 100, HEAVY: 100, FORTIFIED: 100, DIVINE: 100 }
    // HEAL is not in the matrix: it restores its damage value as HP to an ally, capped at max HP.
  },

  // Corpse quality per killing power type (0..1). source: design notes ("Leichen-Ressourcen"),
  // mapped onto the PowerType enum. A unit's corpseQuality overrides this value (e.g. the ghoul rends).
  corpseQuality: { PIERCE: 1.0, BLUNT: 0.7, SIEGE: 0.3, FIRE: 0.2, POISON: 0.5, ARCANE: 0.6, SOUL: 1.0, HOLY: 0.5, CHAOS: 0.5 },

  // ---------------------------------------------------------------------------
  // Units. Stats for ghul, geist and balliste: source: design notes. Others: first proposal.
  // shape: placeholder mesh for the prototype (cone, capsule, box, sphere, cylinder, octahedron).
  // ---------------------------------------------------------------------------
  units: {
    // --- Undead (player) ---
    lich:        { name: "Lich", side: "undead", rank: "UNIQUE", hp: 40, initiative: 6, move: 3, damage: 10, range: 3,
                   power: "ARCANE", counter: false, defense: "MEDIUM", magicResist: 4, soulShield: 4,
                   sight: 6, hear: 3, smell: 3, size: 2, spectral: false, flying: false,
                   commandPoints: 0, cost: {}, shape: "octahedron", color: "#5a2d82",
                   desc: "Untoter Herrscher. Fällt er, ist der Kampf verloren und er kehrt ins Hügelgrab zurück." },
    ghul:        { name: "Ghul", side: "undead", rank: "CANNON_FODDER", hp: 18, initiative: 5, move: 3, damage: 6, range: 1,
                   power: "BLUNT", corpseQuality: 0.4, counter: true, defense: "UNARMORED", magicResist: 1, soulShield: 0,
                   sight: 3, hear: 2, smell: 4, size: 2, spectral: false, flying: false,
                   commandPoints: 2, cost: { corpses: 1 }, shape: "capsule", color: "#6b7d4a",
                   desc: "Billig, zäh, zerfleischt seine Opfer (schlechte Leichen)." },
    skelett:     { name: "Skelett-Speerträger", side: "undead", rank: "CANNON_FODDER", hp: 12, initiative: 4, move: 3, damage: 5, range: 1,
                   power: "PIERCE", counter: true, defense: "LIGHT", magicResist: 0, soulShield: 0,
                   sight: 3, hear: 2, smell: 1, size: 1, spectral: false, flying: false,
                   commandPoints: 1, cost: { bones: 120 }, shape: "cone", color: "#d8d0b8",
                   desc: "Sauberer Stich, gute Leichen." },
    schleuderer: { name: "Knochenschleuderer", side: "undead", rank: "WARRIOR", hp: 10, initiative: 4, move: 3, damage: 6, range: 4,
                   power: "BLUNT", counter: false, defense: "LIGHT", magicResist: 0, soulShield: 0,
                   sight: 5, hear: 2, smell: 1, size: 1, spectral: false, flying: false,
                   commandPoints: 2, cost: { bones: 180 }, requiresKnowledge: 2, shape: "cylinder", color: "#bfb59a",
                   desc: "Fernkampf. Wirft Knochensplitter." },
    geist:       { name: "Geist", side: "undead", rank: "WARRIOR", hp: 10, initiative: 8, move: 5, damage: 8, range: 1,
                   power: "SOUL", counter: false, defense: "UNARMORED", magicResist: 4, soulShield: 6,
                   sight: 5, hear: 4, smell: 0, size: 1, spectral: true, flying: true,
                   commandPoints: 3, cost: { souls: 2 }, requiresKnowledge: 3, shape: "sphere", color: "#a9c7d6",
                   desc: "Lautlos, fliegt, geht durch Wände. Seelenschaden bringt Seelen." },

    // --- Worldly enemies ---
    bauer:       { name: "Bauer", side: "enemy", rank: "CANNON_FODDER", hp: 10, initiative: 4, move: 3, damage: 4, range: 1,
                   power: "PIERCE", counter: true, defense: "UNARMORED", magicResist: 0, soulShield: 0,
                   sight: 4, hear: 3, smell: 2, size: 1, spectral: false, flying: false, shape: "cone", color: "#a08a5a" },
    stadtwache:  { name: "Stadtwache", side: "enemy", rank: "WARRIOR", hp: 18, initiative: 5, move: 3, damage: 6, range: 1,
                   power: "PIERCE", counter: true, defense: "MEDIUM", magicResist: 0, soulShield: 0,
                   sight: 5, hear: 3, smell: 2, size: 2, spectral: false, flying: false, shape: "box", color: "#8a2f2f" },
    armbrust:    { name: "Armbrustschütze", side: "enemy", rank: "WARRIOR", hp: 12, initiative: 5, move: 3, damage: 7, range: 5,
                   power: "PIERCE", counter: false, defense: "LIGHT", magicResist: 0, soulShield: 0,
                   sight: 6, hear: 3, smell: 2, size: 1, spectral: false, flying: false, shape: "cylinder", color: "#9a5a2a" },
    ritter:      { name: "Ritter", side: "enemy", rank: "WARRIOR", hp: 30, initiative: 6, move: 4, damage: 9, range: 1,
                   power: "PIERCE", counter: true, defense: "HEAVY", magicResist: 1, soulShield: 1,
                   sight: 5, hear: 2, smell: 2, size: 2, spectral: false, flying: false, shape: "box", color: "#c2c2c8" },
    balliste:    { name: "Balliste", side: "enemy", rank: "MACHINE", hp: 25, initiative: 2, move: 1, damage: 20, range: 6,
                   power: "SIEGE", counter: false, defense: "FORTIFIED", magicResist: 0, soulShield: 0,
                   sight: 6, hear: 3, smell: 1, size: 3, spectral: false, flying: false, shape: "box", color: "#6e5536" },

    // --- Clergy ---
    moench:      { name: "Mönch", side: "enemy", rank: "WARRIOR", hp: 12, initiative: 5, move: 3, damage: 6, range: 3,
                   power: "HOLY", counter: false, defense: "UNARMORED", magicResist: 3, soulShield: 3,
                   sight: 5, hear: 4, smell: 3, size: 1, spectral: false, flying: false, shape: "cone", color: "#5b4632" },
    priester:    { name: "Priester", side: "enemy", rank: "WARRIOR", hp: 16, initiative: 4, move: 3, damage: 6, range: 3,
                   power: "HEAL", counter: false, defense: "UNARMORED", magicResist: 4, soulShield: 4,
                   sight: 5, hear: 4, smell: 3, size: 1, spectral: false, flying: false, shape: "cone", color: "#e6e0cc",
                   desc: "Heilt Verbündete. Ohne Verwundete greift er mit 3 HOLY-Schaden an." },

    // --- Mythic enemies ---
    hexe:        { name: "Hexe", side: "enemy", rank: "WARRIOR", hp: 14, initiative: 7, move: 4, damage: 8, range: 4,
                   power: "ARCANE", counter: false, defense: "LIGHT", magicResist: 4, soulShield: 2,
                   sight: 6, hear: 5, smell: 5, size: 1, spectral: false, flying: false, shape: "cone", color: "#3e5a3a" },
    irrlicht:    { name: "Irrlicht", side: "enemy", rank: "CANNON_FODDER", hp: 8, initiative: 9, move: 6, damage: 4, range: 2,
                   power: "ARCANE", counter: false, defense: "UNARMORED", magicResist: 3, soulShield: 3,
                   sight: 6, hear: 4, smell: 0, size: 1, spectral: true, flying: true, shape: "sphere", color: "#d9e86a" },
    moorgeist:   { name: "Moorgeist", side: "enemy", rank: "WARRIOR", hp: 20, initiative: 3, move: 2, damage: 7, range: 1,
                   power: "SOUL", counter: true, defense: "UNARMORED", magicResist: 2, soulShield: 5,
                   sight: 3, hear: 5, smell: 6, size: 2, spectral: true, flying: false, shape: "capsule", color: "#3a4a3a" },
    rattenfaenger:{ name: "Rattenfänger", side: "enemy", rank: "UNIQUE", hp: 35, initiative: 8, move: 4, damage: 9, range: 4,
                   power: "ARCANE", counter: false, defense: "LIGHT", magicResist: 5, soulShield: 3,
                   sight: 7, hear: 7, smell: 3, size: 2, spectral: false, flying: false, shape: "octahedron", color: "#b0422e" },
    brockenhexe: { name: "Hexenkönigin vom Brocken", side: "enemy", rank: "UNIQUE", hp: 90, initiative: 8, move: 4, damage: 14, range: 4,
                   power: "CHAOS", counter: true, defense: "DIVINE", magicResist: 6, soulShield: 6,
                   sight: 8, hear: 8, smell: 8, size: 3, spectral: false, flying: true, shape: "octahedron", color: "#1d1d1d" }
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
    WITCHES:  { name: "Hexen und Haine",   color: "#3e5a3a" }
  },

  // ---------------------------------------------------------------------------
  // Nodes: places on the world map. q/r computed with the calibrated formula in map.
  // type: PHYLACTERY | MYTHIC | WORLDLY | CHRISTIAN | VILLAGE. size = battle area edge in tiles (16 / 32 / 64).
  // garrison: enemy units placed at battle start (before threat bonus).
  // ---------------------------------------------------------------------------
  nodes: [
    { id: "wilseder_berg", name: "Wilseder Berg", q: 667,  r: 397, type: "PHYLACTERY", faction: "UNDEAD", size: 16,
      garrison: {}, desc: "Hügelgrab und Phylakterium des Lichs. Hier wird rekrutiert." },

    { id: "soltau",        name: "Soltau",            q: 646,  r: 440, type: "WORLDLY",   faction: "GUELPHS",  size: 16,
      garrison: { bauer: 4 } },
    { id: "medingen",      name: "Kloster Medingen",  q: 811,  r: 415, type: "CHRISTIAN", faction: "CLERGY",   size: 16,
      garrison: { moench: 2, priester: 1 } },
    { id: "walsrode",      name: "Kloster Walsrode",  q: 586,  r: 470, type: "CHRISTIAN", faction: "CLERGY",   size: 16,
      garrison: { moench: 2, priester: 1, bauer: 2 } },
    { id: "ebstorf",       name: "Kloster Ebstorf",   q: 784,  r: 429, type: "CHRISTIAN", faction: "CLERGY",   size: 16,
      garrison: { moench: 2, priester: 2, bauer: 2 } },
    { id: "uelzen",        name: "Uelzen",            q: 817,  r: 445, type: "WORLDLY",   faction: "HANSE",    size: 16,
      garrison: { bauer: 3, stadtwache: 2 } },
    { id: "teufelsmoor",   name: "Teufelsmoor",       q: 427,  r: 381, type: "MYTHIC",    faction: "WITCHES",  size: 16,
      garrison: { irrlicht: 3, moorgeist: 2 } },
    { id: "verden",        name: "Verden",            q: 500,  r: 455, type: "CHRISTIAN", faction: "CLERGY",   size: 16,
      garrison: { moench: 3, priester: 1, stadtwache: 2 } },
    { id: "hameln",        name: "Hameln",            q: 529,  r: 652, type: "MYTHIC",    faction: "WITCHES",  size: 16,
      garrison: { rattenfaenger: 1, hexe: 2, irrlicht: 2 } },
    { id: "wittenberg",    name: "Wittenberg",        q: 1319, r: 709, type: "WORLDLY",   faction: "ASKANIER", size: 16,
      garrison: { ritter: 2, armbrust: 2, stadtwache: 2 } },

    { id: "lueneburg",     name: "Lüneburg",          q: 783,  r: 376, type: "WORLDLY",   faction: "HANSE",    size: 32,
      garrison: { stadtwache: 4, armbrust: 2, bauer: 2 }, desc: "Erste Menschenhauptstadt, durch den Erbfolgekrieg geschwächt." },
    { id: "celle",         name: "Celle",             q: 703,  r: 527, type: "WORLDLY",   faction: "GUELPHS",  size: 32,
      garrison: { ritter: 2, stadtwache: 3, armbrust: 2 } },
    { id: "bremen",        name: "Bremen",            q: 396,  r: 418, type: "WORLDLY",   faction: "HANSE",    size: 32,
      garrison: { stadtwache: 4, armbrust: 3, balliste: 1, priester: 1 } },
    { id: "hannover",      name: "Hannover",          q: 619,  r: 586, type: "WORLDLY",   faction: "GUELPHS",  size: 32,
      garrison: { ritter: 3, stadtwache: 3, armbrust: 2 } },
    { id: "braunschweig",  name: "Braunschweig",      q: 810,  r: 612, type: "WORLDLY",   faction: "GUELPHS",  size: 32,
      garrison: { ritter: 4, armbrust: 2, balliste: 1 } },
    { id: "magdeburg",     name: "Magdeburg",         q: 1074, r: 648, type: "CHRISTIAN", faction: "CLERGY",   size: 32,
      garrison: { moench: 3, priester: 2, stadtwache: 3, balliste: 1 } },

    { id: "hamburg",       name: "Hamburg",           q: 682,  r: 304, type: "WORLDLY",   faction: "HANSE",    size: 64,
      garrison: { stadtwache: 6, armbrust: 4, balliste: 2 } },
    { id: "berlin",        name: "Berlin",            q: 1501, r: 552, type: "WORLDLY",   faction: "ASKANIER", size: 64,
      garrison: { stadtwache: 5, armbrust: 4, ritter: 2, balliste: 1 } },
    { id: "brocken",       name: "Brocken",           q: 831,  r: 725, type: "MYTHIC",    faction: "WITCHES",  size: 64,
      garrison: { brockenhexe: 1, hexe: 4, irrlicht: 4, moorgeist: 2 }, finale: true,
      desc: "Mächtigster Ley-Knoten. Sieg hier gewinnt das Spiel." },

    // --- Villages: small named places between the larger ones (easier than Soltau). First proposal. ---
    { id: "undeloh", name: "Undeloh", q: 678, r: 390, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "egestorf", name: "Egestorf", q: 699, r: 390, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "bispingen", name: "Bispingen", q: 683, r: 417, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "schneverdingen", name: "Schneverdingen", q: 634, r: 408, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "amelinghausen", name: "Amelinghausen", q: 735, r: 407, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "munster", name: "Munster", q: 704, r: 440, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "hermannsburg", name: "Hermannsburg", q: 705, r: 477, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "bergen", name: "Bergen", q: 674, r: 482, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "salzhausen", name: "Salzhausen", q: 724, r: 383, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "hanstedt", name: "Hanstedt", q: 687, r: 374, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "bienenbuettel", name: "Bienenbüttel", q: 800, r: 402, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "suderburg", name: "Suderburg", q: 791, r: 462, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "unterluess", name: "Unterlüß", q: 753, r: 475, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "fallingbostel", name: "Fallingbostel", q: 611, r: 469, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "visselhoevede", name: "Visselhövede", q: 583, r: 440, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 2 } },
    { id: "tostedt", name: "Tostedt", q: 614, r: 369, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 2, moench: 1 } },
    { id: "zeven", name: "Zeven", q: 510, r: 365, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 2, moench: 1 } },
    { id: "buxtehude", name: "Buxtehude", q: 611, r: 322, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 2, moench: 1 } },
    { id: "achim", name: "Achim", q: 451, r: 433, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "syke", name: "Syke", q: 402, r: 457, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "schwarmstedt", name: "Schwarmstedt", q: 592, r: 514, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "burgdorf", name: "Burgdorf", q: 685, r: 570, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "wittingen", name: "Wittingen", q: 860, r: 502, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "dannenberg", name: "Dannenberg", q: 947, r: 413, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "hitzacker", name: "Hitzacker", q: 934, r: 400, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "bleckede", name: "Bleckede", q: 859, r: 367, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "lauenburg", name: "Lauenburg", q: 817, r: 347, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 3 } },
    { id: "bergedorf", name: "Bergedorf", q: 734, r: 319, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 3 } },
    { id: "neustadt", name: "Neustadt am Rübenberge", q: 554, r: 555, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "peine", name: "Peine", q: 739, r: 600, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 2, moench: 1 } },
    { id: "wolfenbuettel", name: "Wolfenbüttel", q: 811, r: 638, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "harzburg", name: "Harzburg", q: 818, r: 705, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
    { id: "ilsenburg", name: "Ilsenburg", q: 847, r: 709, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 2, moench: 1 } },
    { id: "schierke", name: "Schierke", q: 843, r: 733, type: "VILLAGE", faction: "WITCHES", size: 16, garrison: { irrlicht: 2 } },
    { id: "oschersleben", name: "Oschersleben", q: 979, r: 669, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 2, moench: 1 } },
    { id: "haldensleben", name: "Haldensleben", q: 1022, r: 607, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 2, moench: 1 } },
    { id: "gardelegen", name: "Gardelegen", q: 1018, r: 551, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 3 } },
    { id: "salzwedel", name: "Salzwedel", q: 959, r: 473, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 3 } },
    { id: "tangermuende", name: "Tangermünde", q: 1156, r: 547, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 2, armbrust: 1 } },
    { id: "burg", name: "Burg", q: 1129, r: 611, type: "VILLAGE", faction: "CLERGY", size: 16, garrison: { bauer: 2, moench: 1 } },
    { id: "genthin", name: "Genthin", q: 1202, r: 579, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 2, armbrust: 1 } },
    { id: "zerbst", name: "Zerbst", q: 1183, r: 685, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 2, armbrust: 1 } },
    { id: "belzig", name: "Belzig", q: 1305, r: 643, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 2, armbrust: 1 } },
    { id: "nauen", name: "Nauen", q: 1375, r: 531, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 2, armbrust: 1 } },
    { id: "bernau", name: "Bernau", q: 1545, r: 513, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 2, armbrust: 1 } },
    { id: "koenigswusterhausen", name: "Wusterhausen", q: 1555, r: 605, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 2, armbrust: 1 } },
    { id: "rathenow", name: "Rathenow", q: 1244, r: 531, type: "VILLAGE", faction: "ASKANIER", size: 16, garrison: { bauer: 2, armbrust: 1 } },
    { id: "nienburg", name: "Nienburg", q: 493, r: 523, type: "VILLAGE", faction: "GUELPHS", size: 16, garrison: { bauer: 3 } },
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
    startResources: { corpses: 6, bones: 240, souls: 0, knowledge: 0 },
    startArmy: ["lich", "ghul", "ghul", "ghul", "skelett", "skelett"],
    commandLimitBase: 15,              // the Lich as leader grants this
    commandLimitPerMythicNode: 3,      // each conquered MYTHIC node raises the limit
    corpsesPerKill: 1,                 // multiplied by corpse quality, summed, rounded down at battle end
    bonesPerKill: 30,                  // independent of quality (a skeleton yields its bones either way)
    soulsPerSoulKill: 1,               // extra souls when the killing blow was SOUL damage
    travelTilesPerDay: 30,
    lichDeathDays: 3,                  // days lost when the Lich falls and returns to the phylactery
    // Loot for conquering a node, by type and size.
    nodeRewards: {
      MYTHIC:    { 16: { knowledge: 3, souls: 2, corpses: 1 }, 32: { knowledge: 4, souls: 3, corpses: 2 }, 64: { knowledge: 6, souls: 4, corpses: 3 } },
      WORLDLY:   { 16: { corpses: 4, bones: 180 },           32: { corpses: 8, bones: 300 },           64: { corpses: 14, bones: 480 } },
      CHRISTIAN: { 16: { corpses: 2 },                       32: { corpses: 3 },                       64: { corpses: 5 } },
      VILLAGE:   { 16: { corpses: 2, bones: 60 } }
    },
    // After a won battle every survivor regains this share of its max HP (rounded up).
    postBattleHealShare: 0.25
  },

  threat: {
    attackOwnNode: 25,       // faction of the attacked node
    attackOwnVillage: 10,    // faction of an attacked village (small places cause less alarm)
    attackOtherFaction: 5,   // every other living faction
    dailyDecay: 0.05,        // 5 % of the current value per day (source: design notes)
    reinforcementPer: 25     // +1 extra garrison unit per full 25 % threat of the defending faction
  }
};
