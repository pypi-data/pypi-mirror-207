"""
2022, March 12
"""

import importlib_resources as ir
import json
import math
import warnings


# Load JSON files in dictionaries for fast access
# see https://importlib-resources.readthedocs.io/en/latest/using.html
def getdict(filename: str) -> dict:
    source = ir.files('stringunitconverter').joinpath(filename)
    with ir.as_file(source) as filepath:
        with open(filepath, 'r') as f:
            a = json.load(f)
    return a


prefixes = getdict('prefixes.json')
units = getdict('units.json')

operators_and_brackets = frozenset(('*', '/', '^', '-', '+', '(', ')', ' ',
                                    '·', '.'))
digits = frozenset(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
nonunits = operators_and_brackets.union(digits)


def add_unit(unit: str, multiplier: str):
    """Add a unit and its multiplier

    For the parameter 'multiplier',
    We want a string here because we substitute strings
    and don't care about the actual mathematical value.

    :param unit: base unit string, e.g. 'ft'
    :param multiplier: corresponding multiplier, e.g. '0.3048'
    """
    # Check multiplier of correct type
    if not isinstance(multiplier, str):
        msg = f"The argument for parameter 'multiplier' must be " + \
              f"of type str, not {type(multiplier)}."
        raise ValueError(msg)
    # Check whether unit isn't registered yet
    if unit in units:
        if units[unit] == multiplier:
            msg = f'The unit {unit} is already present with the same multiplier.'
            warnings.warn(msg, UserWarning, stacklevel=2)
            return None
        else:
            msg = f'The unit {unit} is already present ' + \
                  f'with the multiplier {units[unit]}, which differs from ' + \
                  f'the given multiplier {multiplier}.'
            raise Exception(msg)
    # Ok, unit not yet preset => add it
    else:
        units[unit] = multiplier


def add_json(filename: str, add_to_existing=False):
    """Add JSON file with units and multipliers

    Example of the used formatting:
    ```
    {
      "oz": "0.02834952",
      "gf": "9.80665e-6",
      "ft": "0.3048"
    }
    ```

    :param filename: filepath of the JSON file
    :param add_to_existing: Whether to add the units to the already present
                            ones (common ones will be overwritten), or to
                            let them replace the already present ones.
    """
    units_new = getdict(filename)
    units = units.update(units_new) if add_to_existing \
        else units_new


def multiplier(a: str, b: str, *args, **kwargs) -> float:
    """Get float multiplier from two unitstrings

    Multiplying the returned value with
    a value of a quantity expressed in unit 'a'
    gives the value of that quantity expressed in unit 'b'.
    Any additional parameters are passed to ``get_factor``.

    :param a: input unitstring
    :param b: output unitstring
    :return: multiplier
    """
    return get_factor(a, *args, **kwargs) / get_factor(b, *args, **kwargs)


def get_factor(a: str, unsafe=False) -> float:
    """Get float multiplier to convert to base SI

    Multiplying the returned value with
    a value of a quantity expressed in unit 'a'
    gives the value of that quantity expressed in
    (a combinatione of) base SI units, i.e. g, N, m/s etc.

    :param a: input unit
    :param unsafe: set to 'True' to disable protection against malicious code
    :return: multiplier
    """
    # Replace each hat with two asterisks
    # and replace multiplication dot with asterisk
    # and replace ² and ³ with **2 and **3 respectively
    for i in range(len(a)-1, -1, -1):
        if a[i] == '^':
            a = a[:i] + '**' + a[i+1:]
        elif a[i] == '·':
            a = a[:i] + '*' + a[i+1:]
        elif a[i] == '²':
            a = a[:i] + '**2' + a[i+1:]
        elif a[i] == '³':
            a = a[:i] + '**3' + a[i+1:]

    # Replace every unit-with-prefix with its appropriate multiplier
    # iterate over input string from back to front
    # `ks` = start index, `ke` = end index
    ke = len(a) - 1
    while True:
        # Search for end index `ke`
        # character in known non-units -> nothing to replace -> skip these indices
        while ke > -1 and a[ke] in nonunits:
            ke -= 1
        # found end of unit string on index `ke`
        # or if before start of the string, end processing
        if ke < 0:
            break
        # Search for start index `ks`
        ks = ke
        while ks > -1 and a[ks] not in nonunits:
            ks -= 1
        # found start of unit string on index `ke + 1`
        # Extract the string and replace it
        detected_unit_string = a[ks+1:ke+1]
        #print('  detected_unit_string: <' + detected_unit_string + '>')
        #print('  ks:', ks, ', ke:', ke)
        # Substitute
        a = a[:ks+1] + unit_to_factor_string(detected_unit_string) + a[ke+1:]
        # If at start of the string, end processing
        if ks < 0:
            break
        # If space between two units, replace it with a multiplier
        if ks > 0 and a[ks] == ' ' and a[ks-1] not in operators_and_brackets:
            a = a[:ks] + '*' + a[ks+1:]
        # Move end index to start index
        ke = ks
    # Before evaluating the string, search for suspicious code,
    # unless unsafe mode has been enabled
    if unsafe is False:
        if 'import' in a or 'eval' in a:
            msg = 'The string may not contain "import" or "eval". ' + \
                  'Add argument "unsafe=True" to circumvent protection.'
            raise Exception(msg)
    # Evaluate string
    a = eval(a)
    # Return outcome
    return a


def unit_to_factor_string(a: str) -> str:
    """single unit with prefix => multiplier string

    Convert string with a single unit and prefix, e.g. 'kPa',
    to its multiplier string, e.g. '(1e3*1)'.

    :param a: single unit
    :return: multiplier
    """
    # assume no prefix
    if a in units:
        return units[a]
    # doesn't work, so assume prefix and split it
    p = a[0]
    u = a[1:]
    if p in prefixes and u in units:
        return '(' + prefixes[p] + '*' + units[u] + ')'
    # neither of the two worked, so error out
    print('Failed to decode string: <' + a + '>')
    # doesn't work either, so it's not a known unitstring
    return a


if __name__ == '__main__':
    pass
