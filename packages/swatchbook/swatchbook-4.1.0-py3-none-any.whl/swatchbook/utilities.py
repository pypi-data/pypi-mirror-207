import re

from wagtail_switch_block.blocks import TYPE_FIELD_NAME
from model_porter.repository import RepositoryException

__all__ = ['parse_colour_block_value']

COLOUR_RE = re.compile(r'^(?P<type>(rgb|rgba|hsl|hsla))\((?P<values>[^)]*)\)$')
NUMERIC_RE = re.compile(r'^(?P<value>[0-9]+(.[0-9]+)?)(?P<unit>[^.0-9]*)$')


def parse_colour_block_value(*, specifier):

    result = {}
    specifier = specifier.strip()
    match = COLOUR_RE.match(specifier)

    if not match:
        raise RepositoryException("Couldn't parse colour specification.")

    colour_type = match.group('type').lower()
    colour_values = match.group('values').split(',')
    units = []

    for index, value in enumerate(colour_values):
        match = NUMERIC_RE.match(value.lower().strip())

        if not match:
            raise RepositoryException("Couldn't parse colour specification.")

        unit = match.group('unit')
        value = float(match.group('value'))

        if value < 0.0:
            raise RepositoryException("Couldn't parse colour specification.")

        colour_values[index] = value # noqa
        units.append(unit)

    colour_def = {}

    if colour_type == "rgb":
        if len(colour_values) != 3:
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[0] > 255.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[1] > 255.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[2] > 255.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        colour_def['red'] = colour_values[0]
        colour_def['green'] = colour_values[1]
        colour_def['blue'] = colour_values[2]

    elif colour_type == "rgba":
        if len(colour_values) != 4:
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[0] > 255.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[1] > 255.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[2] > 255.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[3] > 1.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        colour_def['red'] = colour_values[0]
        colour_def['green'] = colour_values[1]
        colour_def['blue'] = colour_values[2]
        colour_def['alpha'] = colour_values[3]

    elif colour_type == "hsl":
        if len(colour_values) != 3:
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[0] > 360.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[1] > 100.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[2] > 100.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        colour_def['hue'] = colour_values[0]
        colour_def['saturation'] = colour_values[1]
        colour_def['lightness'] = colour_values[2]

    elif colour_type == "hsla":
        if len(colour_values) != 4:
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[0] > 360.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[1] > 100.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[2] > 100.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        if colour_values[3] > 1.0: # noqa
            raise RepositoryException("Couldn't parse colour specification.")

        colour_def['hue'] = colour_values[0]
        colour_def['saturation'] = colour_values[1]
        colour_def['lightness'] = colour_values[2]
        colour_def['alpha'] = colour_values[3]

    else:
        raise RepositoryException("Couldn't parse colour specification.")

    result[TYPE_FIELD_NAME] = colour_type
    result[colour_type] = colour_def

    return result

