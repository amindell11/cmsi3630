
def prefix_to_value(prefix_str):
    """
    Converts a metric prefix string to its corresponding value.
    
    Args:
    prefix_str (str): The metric prefix abbreviation.
    
    Returns:
    float: The value corresponding to the metric prefix, or None if the prefix is not recognized.
    """
    prefix_map = {
        "Y": 1e24,  # yotta
        "Z": 1e21,  # zetta
        "E": 1e18,  # exa
        "P": 1e15,  # peta
        "T": 1e12,  # tera
        "G": 1e9,   # giga
        "M": 1e6,   # mega
        "k": 1e3,   # kilo
        "h": 1e2,   # hecto
        "da": 1e1,  # deka
        "d": 1e-1,  # deci
        "c": 1e-2,  # centi
        "m": 1e-3,  # milli
        "µ": 1e-6,  # micro
        "u": 1e-6,  # micro (alternative symbol)
        "n": 1e-9,  # nano
        "p": 1e-12, # pico
        "f": 1e-15, # femto
        "a": 1e-18, # atto
        "z": 1e-21, # zepto
        "y": 1e-24  # yocto
    }

    return prefix_map.get(prefix_str)