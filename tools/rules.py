"""Gemeinsame Spielregeln für Generator und Balancing-Simulation."""
DEFENSES = ["Unarmored", "Light", "Medium", "Heavy", "Fortified", "Divine"]

# Power-Defense-Matrix (Anteil des Schadens, der ankommt) – identisch zum Design-Dokument
MATRIX = {
    "Pierce": [1.00, 1.00, 1.00, 0.75, 0.50, 0.50],
    "Blunt":  [1.00, 1.00, 0.75, 1.00, 0.75, 0.50],
    "Rend":   [1.25, 1.00, 0.75, 0.50, 0.25, 0.50],
    "Siege":  [1.00, 0.75, 0.75, 1.00, 1.50, 0.50],
    "Fire":   [1.00, 1.25, 1.00, 0.75, 0.50, 0.75],
    "Poison": [1.00, 1.00, 1.00, 0.75, 0.00, 0.50],
    "Arcane": [1.00, 1.00, 1.00, 1.00, 0.75, 0.75],
    "Soul":   [1.50, 1.25, 1.00, 0.75, 0.25, 0.50],   # Fortified 25 %: machines have no soul, but their crew does
    "Holy":   [1.50, 1.25, 1.00, 0.75, 0.50, 1.00],
    "Chaos":  [1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
}

# Magische Schadensarten: MagicResist reduziert prozentual (5 % pro Punkt, max. 50 %)
MAGIC = {"Arcane", "Soul", "Holy", "Chaos"}
MR_PER_POINT, MR_CAP = 0.05, 0.50

# Initiative: Tick-Kosten pro Zug. 2520 = kgV(1..10) -> ganzzahlig für jede Initiative 1-10
TICK_BASE = 2520

def mult(power, defense):
    return MATRIX[power][DEFENSES.index(defense)]

def hit_damage(att, dfn):
    """Schaden eines Treffers von att auf dfn (dicts mit CSV-Feldern als int/str)."""
    raw = att["AttackDamage"] * mult(att["PowerType"], dfn["DefenseType"])
    if att["PowerType"] in MAGIC:
        raw *= 1 - min(MR_CAP, dfn["MagicResist"] * MR_PER_POINT)
    if mult(att["PowerType"], dfn["DefenseType"]) == 0:
        return 0
    return max(1, round(raw))

def tick_cost(initiative):
    return TICK_BASE // initiative
