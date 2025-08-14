# dictionary for pulsars used for XNAV

# The following values are taken from the ATNF Pulsar Catalogue
# https://www.atnf.csiro.au/research/pulsar/psrcat/

# Note that "B1821-24", "XTE_J1751-305" are not available names in ATNF
# Includes right_ascension & declination (at the recommendation to use ATNF, not SIMBAD coordinates)
# Frequency Epoch is expected in NICERTIME, not MJD. Old entries may have MJD and a # DANGER

pulsar_coords = {
    "B0531+21": {
        "ra": 83.63322,
        "dec": 22.014461,
        "frequency": 29.6236103456,
        "f_dot": -368596.16e-15,
        "frequency_epoch": 157075202.020201,
    },
    "B0531+21_3013010102": {
        "ra": 83.63322,
        "dec": 22.014461,
        "frequency": 29.6095750017,
        "f_dot": -3.6817457e-10,
        "frequency_epoch": 195177602.025552,
    },
    "B1937+21": {
        "ra": 294.91067,
        "dec": 21.583089,
        "frequency": 641.92822124440,
        "f_dot": -4.33083e-14,
        "frequency_epoch": 163646615.238,
    },  # from Sun & co., 2025
    "B1937+21_OG": {
        "ra": 294.9105,
        "dec": 21.58419,
        "frequency": 641.928244534462,
        "f_dot": -4.331046e-14,
        "frequency_epoch": -327456000.000,
    },
    "J0218+4232": {
        "ra": 34.526494038,
        "dec": 42.53815976,
        "frequency": 430.461054546,
        "f_dot": -1.4e-14,
        "frequency_epoch": 55000,  # DANGER
    },
    "J0030+0451": {
        "ra": 7.61426435,
        "dec": 4.8610320,
        "frequency": 205.530695938456,
        "f_dot": -4.29770e-16,
        "frequency_epoch": 55000,  # DANGER
    },
    "J0437-4715": {
        "ra": 69.316872576,
        "dec": -47.252783951,
        "frequency": 173.6879456649439,
        "f_dot": -1.728367e-15,
        "frequency_epoch": 55486,  # DANGER
    },
    "J1012+5307": {
        "ra": 153.13932687,
        "dec": 53.11729541,
        "frequency": 190.2678344415654,
        "f_dot": -6.20041e-16,
        "frequency_epoch": 55000,  # DANGER
    },
    "J2124-3358": {
        "ra": 321.182646430,
        "dec": -33.97930438,
        "frequency": 202.793893746013,
        "f_dot": -8.45900e-16,
        "frequency_epoch": 55000,  # DANGER
    },
    "J2214+3000": {
        "ra": 333.66189047,
        "dec": 30.01060878,
        "frequency": 320.5922923290326,
        "f_dot": -1.51379e-15,
        "frequency_epoch": 56885,  # DANGER
    },
    "J0751+1807": {
        "ra": 117.78814720,
        "dec": 18.12735717,
        "frequency": 287.4578539951060,
        "f_dot": -6.43455e-16,
        "frequency_epoch": 55000,  # DANGER
    },
    "J1024-0719": {
        "ra": 156.161034971,
        "dec": -7.32221654,
        "frequency": 193.715683448548,
        "f_dot": -6.9593e-16,
        "frequency_epoch": 55000,  # DANGER
    },
    "B1957+20": {
        "ra": 299.9032078,
        "dec": 20.80420061,
        "frequency": 622.122030512,
        "f_dot": -6.5e-15,
        "frequency_epoch": 48196,  # DANGER
    },
    "B0540-69": {
        "ra": 85.04667,
        "dec": -69.331714,
        "frequency": 19.7746860321,
        "f_dot": -1.8727175e-10,
        "frequency_epoch": 52910,  # DANGER
    },
}
