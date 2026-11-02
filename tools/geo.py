"""Geo-Umrechnung ohne Zusatzpakete: Geografisch (GRS80/WGS84) <-> ETRS89 / UTM Zone 32N (EPSG:25832).
Transverse Mercator nach Krüger (Reihen 4. Ordnung, Genauigkeit < 1 mm innerhalb der Zone, < 1 cm bis 6° vom Mittelmeridian)."""
import math

A_GRS80 = 6378137.0
F_GRS80 = 1 / 298.257222101
K0, LON0, FE, FN = 0.9996, 9.0, 500000.0, 0.0   # UTM 32N

n = F_GRS80 / (2 - F_GRS80)
A_ = A_GRS80 / (1 + n) * (1 + n**2 / 4 + n**4 / 64)
alpha = [n/2 - 2*n**2/3 + 5*n**3/16 + 41*n**4/180,
         13*n**2/48 - 3*n**3/5 + 557*n**4/1440,
         61*n**3/240 - 103*n**4/140,
         49561*n**4/161280]
beta = [n/2 - 2*n**2/3 + 37*n**3/96 - n**4/360,
        n**2/48 + n**3/15 - 437*n**4/1440,
        17*n**3/480 - 37*n**4/840,
        4397*n**4/161280]
delta = [2*n - 2*n**2/3 - 2*n**3 + 116*n**4/45,
         7*n**2/3 - 8*n**3/5 - 227*n**4/45,
         56*n**3/15 - 136*n**4/35,
         4279*n**4/630]

def to_utm(lat, lon):
    """Breite/Länge in Grad -> (Ostwert, Nordwert) in Metern, UTM 32N."""
    phi, lam = math.radians(lat), math.radians(lon - LON0)
    e = math.sqrt(F_GRS80 * (2 - F_GRS80))
    t = math.sinh(math.atanh(math.sin(phi)) - e * math.atanh(e * math.sin(phi)))
    xi_ = math.atan2(t, math.cos(lam))
    eta_ = math.atanh(math.sin(lam) / math.sqrt(1 + t * t))
    xi, eta = xi_, eta_
    for j, a in enumerate(alpha, 1):
        xi += a * math.sin(2*j*xi_) * math.cosh(2*j*eta_)
        eta += a * math.cos(2*j*xi_) * math.sinh(2*j*eta_)
    return FE + K0 * A_ * eta, FN + K0 * A_ * xi

def from_utm(E, N):
    """(Ostwert, Nordwert) UTM 32N -> Breite/Länge in Grad."""
    xi, eta = (N - FN) / (K0 * A_), (E - FE) / (K0 * A_)
    xi_, eta_ = xi, eta
    for j, b in enumerate(beta, 1):
        xi_ -= b * math.sin(2*j*xi) * math.cosh(2*j*eta)
        eta_ -= b * math.cos(2*j*xi) * math.sinh(2*j*eta)
    chi = math.asin(math.sin(xi_) / math.cosh(eta_))
    phi = chi
    for j, d in enumerate(delta, 1):
        phi += d * math.sin(2*j*chi)
    lam = math.atan2(math.sinh(eta_), math.cos(xi_))
    return math.degrees(phi), LON0 + math.degrees(lam)

if __name__ == "__main__":
    # Selbsttest: Mittelmeridian -> Ostwert 500 000; Meridianbogen bis 52° (GRS80) = 5 763 343,5 m
    E, N = to_utm(52.0, 9.0)
    assert abs(E - 500000) < 1e-6 and abs(N - 0.9996 * 5763343.5) < 2, (E, N)
    for lat, lon in [(51.7991, 10.6156), (53.55, 9.99), (54.68, 13.43), (51.0, 14.25)]:
        la, lo = from_utm(*to_utm(lat, lon))
        assert abs(la - lat) < 1e-9 and abs(lo - lon) < 1e-9, (lat, lon, la, lo)
    print("geo ok", to_utm(52, 9), to_utm(51.7991, 10.6156))

# ---------- numpy-Variante (für ganze Raster) ----------
def from_utm_np(E, N):
    import numpy as np
    xi, eta = (N - FN) / (K0 * A_), (E - FE) / (K0 * A_)
    xi_, eta_ = xi.copy(), eta.copy()
    for j, b in enumerate(beta, 1):
        xi_ -= b * np.sin(2*j*xi) * np.cosh(2*j*eta)
        eta_ -= b * np.cos(2*j*xi) * np.sinh(2*j*eta)
    chi = np.arcsin(np.sin(xi_) / np.cosh(eta_))
    phi = chi.copy()
    for j, d in enumerate(delta, 1):
        phi += d * np.sin(2*j*chi)
    lam = np.arctan2(np.sinh(eta_), np.cos(xi_))
    return np.degrees(phi), LON0 + np.degrees(lam)
