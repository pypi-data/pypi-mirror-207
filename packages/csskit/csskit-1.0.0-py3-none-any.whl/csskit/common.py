from collections import namedtuple
from .auxiliaries import classproperty

__all__ = ['CSSTextAlignment', 'CSSUnits', 'CSSUnitValue', 'AspectRatio',
           'ASPECT_RATIO_SQUARE', 'ASPECT_RATIO_LANDSCAPE_2_1', 'ASPECT_RATIO_LANDSCAPE_3_2',
           'ASPECT_RATIO_LANDSCAPE_4_3', 'ASPECT_RATIO_LANDSCAPE_16_10', 'ASPECT_RATIO_LANDSCAPE_16_9',
           'ASPECT_RATIO_LANDSCAPE_21_9', 'ASPECT_RATIO_PORTRAIT_2_1', 'ASPECT_RATIO_PORTRAIT_3_2',
           'ASPECT_RATIO_PORTRAIT_4_3', 'ASPECT_RATIO_PORTRAIT_16_10', 'ASPECT_RATIO_PORTRAIT_16_9',
           'ASPECT_RATIO_PORTRAIT_21_9', 'ASPECT_RATIO_VIEWPORT',
           'CSSObjectFitType', 'CSSObjectFitNone', 'CSSObjectFitCover', 'CSSObjectFitContain', 'CSSObjectFitFill',
           'SideType', 'SideLeft', 'SideRight', 'SideTop', 'SideBottom',
           'CSSObjectPosition', 'CSSEdges', 'CSSMathExpr', 'CSSVariable']


class CSSTextAlignment:

    ALIGN_START = 'start'
    ALIGN_START_IDENTIFIER = 'start'
    ALIGN_START_LABEL = 'Start'

    ALIGN_END = 'end'
    ALIGN_END_IDENTIFIER = 'end'
    ALIGN_END_LABEL = 'End'

    ALIGN_CENTRE = 'center'
    ALIGN_CENTRE_IDENTIFIER = 'centre'
    ALIGN_CENTRE_LABEL = 'Centre'

    ALIGN_JUSTIFY = 'justify'
    ALIGN_JUSTIFY_IDENTIFIER = 'justify'
    ALIGN_JUSTIFY_LABEL = 'Justify'

    ALIGN_LEFT = 'left'
    ALIGN_LEFT_IDENTIFIER = 'left'
    ALIGN_LEFT_LABEL = 'Left'

    ALIGN_RIGHT = 'right'
    ALIGN_RIGHT_IDENTIFIER = 'right'
    ALIGN_RIGHT_LABEL = 'Right'

    @classmethod
    def choices(cls):
        return [(cls.ALIGN_START_IDENTIFIER, cls.ALIGN_START_LABEL),
                (cls.ALIGN_END_IDENTIFIER, cls.ALIGN_END_LABEL),
                (cls.ALIGN_CENTRE_IDENTIFIER, cls.ALIGN_CENTRE_LABEL),
                (cls.ALIGN_JUSTIFY_IDENTIFIER, cls.ALIGN_JUSTIFY_LABEL),
                (cls.ALIGN_LEFT_IDENTIFIER, cls.ALIGN_LEFT_LABEL),
                (cls.ALIGN_RIGHT_IDENTIFIER, cls.ALIGN_RIGHT_LABEL)]

    @classmethod
    def map_identifier_to_value(cls, identifier, default=None):
        return CSS_TEXT_ALIGNMENT_BY_IDENTIFIER.get(identifier, default)


CSS_TEXT_ALIGNMENT_BY_IDENTIFIER = {

    CSSTextAlignment.ALIGN_START_IDENTIFIER: CSSTextAlignment.ALIGN_START,
    CSSTextAlignment.ALIGN_END_IDENTIFIER: CSSTextAlignment.ALIGN_END,
    CSSTextAlignment.ALIGN_CENTRE_IDENTIFIER: CSSTextAlignment.ALIGN_CENTRE,
    CSSTextAlignment.ALIGN_JUSTIFY_IDENTIFIER: CSSTextAlignment.ALIGN_JUSTIFY,
    CSSTextAlignment.ALIGN_LEFT_IDENTIFIER: CSSTextAlignment.ALIGN_LEFT,
    CSSTextAlignment.ALIGN_RIGHT_IDENTIFIER: CSSTextAlignment.ALIGN_RIGHT,
}


class CSSUnits:

    PIXEL_UNIT = 'px'
    PIXEL_UNIT_IDENTIFIER = 'px'
    PIXEL_UNIT_LABEL = 'Pixels'

    POINT_UNIT = 'pt'
    POINT_UNIT_IDENTIFIER = 'pt'
    POINT_UNIT_LABEL = 'Points'

    EM_UNIT = 'em'
    EM_UNIT_IDENTIFIER = 'em'
    EM_UNIT_LABEL = 'EMs'

    REM_UNIT = 'rem'
    REM_UNIT_IDENTIFIER = 'rem'
    REM_UNIT_LABEL = 'REMs'

    PERCENTAGE_UNIT = '%'
    PERCENTAGE_UNIT_IDENTIFIER = 'pc'
    PERCENTAGE_UNIT_LABEL = 'Percent'

    VIEW_WIDTH_UNIT = 'vw'
    VIEW_WIDTH_UNIT_IDENTIFIER = 'vw'
    VIEW_WIDTH_UNIT_LABEL = 'View Width'

    VIEW_HEIGHT_UNIT = 'vh'
    VIEW_HEIGHT_UNIT_IDENTIFIER = 'vh'
    VIEW_HEIGHT_UNIT_LABEL = 'View Height'

    VIEW_MIN_UNIT = 'vmin'
    VIEW_MIN_UNIT_IDENTIFIER = 'vmin'
    VIEW_MIN_UNIT_LABEL = 'View Min'

    VIEW_MAX_UNIT = 'vmax'
    VIEW_MAX_UNIT_IDENTIFIER = 'vmax'
    VIEW_MAX_UNIT_LABEL = 'View Max'

    @classproperty
    def ABSOLUTE_UNITS(cls): # noqa
        return cls.PIXEL_UNIT, cls.POINT_UNIT

    @classproperty
    def RELATIVE_UNITS(cls): # noqa
        return cls.EM_UNIT, cls.REM_UNIT, cls.PERCENTAGE_UNIT, cls.VIEW_WIDTH_UNIT, cls.VIEW_HEIGHT_UNIT

    @classmethod
    def is_absolute_unit(cls, unit):
        return unit in cls.ABSOLUTE_UNITS

    @classmethod
    def is_relative_unit(cls, unit):
        return unit in cls.RELATIVE_UNITS

    @classmethod
    def choices(cls):
        return [(identifier, item[1]) for identifier, item in CSS_UNITS_BY_IDENTIFIER.items()]

    @classmethod
    def map_identifier_to_value(cls, identifier, default=None):
        result = CSS_UNITS_BY_IDENTIFIER.get(identifier, default)

        if result is default:
            return result

        unit, label = result
        return unit


CSS_UNITS_BY_IDENTIFIER = {

    CSSUnits.PIXEL_UNIT_IDENTIFIER: (CSSUnits.PIXEL_UNIT, CSSUnits.PIXEL_UNIT_LABEL),
    CSSUnits.EM_UNIT_IDENTIFIER: (CSSUnits.EM_UNIT, CSSUnits.EM_UNIT_LABEL),
    CSSUnits.REM_UNIT_IDENTIFIER: (CSSUnits.REM_UNIT, CSSUnits.REM_UNIT_LABEL),
    CSSUnits.PERCENTAGE_UNIT_IDENTIFIER: (CSSUnits.PERCENTAGE_UNIT, CSSUnits.PERCENTAGE_UNIT_LABEL),
    CSSUnits.VIEW_WIDTH_UNIT_IDENTIFIER: (CSSUnits.VIEW_WIDTH_UNIT, CSSUnits.VIEW_WIDTH_UNIT_LABEL),
    CSSUnits.VIEW_HEIGHT_UNIT_IDENTIFIER: (CSSUnits.VIEW_HEIGHT_UNIT, CSSUnits.VIEW_HEIGHT_UNIT_LABEL),
    CSSUnits.VIEW_MIN_UNIT_IDENTIFIER: (CSSUnits.VIEW_MIN_UNIT, CSSUnits.VIEW_MIN_UNIT_LABEL),
    CSSUnits.VIEW_MAX_UNIT_IDENTIFIER: (CSSUnits.VIEW_MAX_UNIT, CSSUnits.VIEW_MAX_UNIT_LABEL),
}


class CSSMathExpr(namedtuple('CSSMathExpr', ['text'], defaults=('',))):
    __slots__ = ()

    def __str__(self):
        return self.text


class CSSUnitValue(namedtuple('CSSUnitValue', ['value', 'unit'], defaults=(CSSUnits.PIXEL_UNIT,))):
    __slots__ = ()

    def __str__(self):
        unit = self.unit if self.unit else ""
        return format_numeric_value(self.value) + unit


class CSSVariable(namedtuple('CSSVariable', ['identifier'], defaults=())):
    __slots__ = ()

    def __str__(self):
        return f"var(--{str(self)})"


class AspectRatio:

    __REGISTRY = {}

    @property
    def identifier(self):
        return self.__identifier

    @property
    def label(self):
        return self.__label

    @property
    def value(self):
        return self.__value

    def __init__(self, identifier, label, value):
        self.__identifier = identifier
        self.__label = label
        self.__value = value
        self.__REGISTRY[identifier] = self

    def __str__(self):
        return self.__identifier

    @classmethod
    def from_identifier(cls, value):
        return cls.__REGISTRY.get(value, None)

    @classmethod
    def all(cls):
        return list(cls.__REGISTRY.values())

    @classmethod
    def choices(cls):
        return [(identifier, ct.label) for identifier, ct in cls.__REGISTRY.items()]


ASPECT_RATIO_NONE = AspectRatio('none', 'None', None)
ASPECT_RATIO_SQUARE = AspectRatio('square', '1:1', (1,1))

ASPECT_RATIO_LANDSCAPE_2_1 = AspectRatio('landscape-2-1', '2:1', (2,1))
ASPECT_RATIO_LANDSCAPE_3_2 = AspectRatio('landscape-3-2', '3:2', (3,2))
ASPECT_RATIO_LANDSCAPE_4_3 = AspectRatio('landscape-4-3', '4:3', (4,3))
ASPECT_RATIO_LANDSCAPE_16_10 = AspectRatio('landscape-16-10', '16:10', (16,10))
ASPECT_RATIO_LANDSCAPE_16_9 = AspectRatio('landscape-16-9', '16:9', (16,9))
ASPECT_RATIO_LANDSCAPE_21_9 = AspectRatio('landscape-21-9', '21:9', (21,9))

ASPECT_RATIO_PORTRAIT_2_1 = AspectRatio('portrait-1-2', '1:2', (1,2))
ASPECT_RATIO_PORTRAIT_3_2 = AspectRatio('portrait-2-3', '2:3', (2,3))
ASPECT_RATIO_PORTRAIT_4_3 = AspectRatio('portrait-3-4', '3:4', (3,4))
ASPECT_RATIO_PORTRAIT_16_10 = AspectRatio('portrait-10-16', '10:16', (10,16))
ASPECT_RATIO_PORTRAIT_16_9 = AspectRatio('portrait-9-16', '9:16', (9,16))
ASPECT_RATIO_PORTRAIT_21_9 = AspectRatio('portrait-9-21', '9:21', (9,21))

ASPECT_RATIO_VIEWPORT = AspectRatio('viewport', 'Viewport', None)


class CSSObjectFitType:

    __REGISTRY = {}

    @property
    def identifier(self):
        return self.__identifier

    @property
    def label(self):
        return self.__label

    def __init__(self, identifier, label):
        self.__identifier = identifier
        self.__label = label
        self.__REGISTRY[identifier] = self

    def __str__(self):
        return self.__identifier

    @classmethod
    def from_identifier(cls, value):
        return cls.__REGISTRY.get(value, None)

    @classmethod
    def all(cls):
        return list(cls.__REGISTRY.values())

    @classmethod
    def choices(cls):
        return [(identifier, ct.label) for identifier, ct in cls.__REGISTRY.items()]


CSSObjectFitNone = CSSObjectFitType('none', 'None')
CSSObjectFitContain = CSSObjectFitType('contain', 'Contain')
CSSObjectFitCover = CSSObjectFitType('cover', 'Cover')
CSSObjectFitFill = CSSObjectFitType('fill', 'Fill')


class SideType:

    __REGISTRY = {}

    @property
    def identifier(self):
        return self.__identifier

    @property
    def label(self):
        return self.__label

    def __init__(self, identifier, label):
        self.__identifier = identifier
        self.__label = label
        self.__REGISTRY[identifier] = self

    def __str__(self):
        return self.__identifier

    @classmethod
    def from_identifier(cls, value):
        return cls.__REGISTRY.get(value, None)

    @classmethod
    def all(cls):
        return list(cls.__REGISTRY.values())

    @classmethod
    def choices(cls):
        return [(identifier, ct.label) for identifier, ct in cls.__REGISTRY.items()]


SideTop = SideType('top', 'Top')
SideBottom = SideType('bottom', 'Bottom')
SideLeft = SideType('left', 'Left')
SideRight = SideType('right', 'Right')


class CSSObjectPosition(namedtuple('CSSObjectPosition', ['x', 'y'], defaults=(CSSUnitValue(value=0), CSSUnitValue(value=0)))): # noqa
    __slots__ = ()

    def is_defined(self):
        return (self.x and self.x.value) or (self.y and self.y.value)

    def __str__(self):

        result = ''

        if self.x:
            result += ' ' + str(self.x)

        if self.y:
            result += ' ' + str(self.y)

        if result:
            result = result[1:]

        return result


class CSSEdges(namedtuple('CSSEdges', ['top', 'right', 'bottom', 'left'],
                          defaults=(CSSUnitValue(value=0), CSSUnitValue(value=0), # noqa
                                    CSSUnitValue(value=0), CSSUnitValue(value=0)))): # noqa
    __slots__ = ()

    def is_defined(self):
        return (self.top and self.top.value) or (self.right and self.right.value) or \
               (self.bottom and self.bottom.value) or (self.left and self.left.value)

    def __str__(self):
        result = ""

        if self.top is not None:
            result += f" {self.top};"
        else:
            result += " 0"

        if self.right is not None:
            result += f" {self.right};"
        else:
            result += " 0"

        if self.bottom is not None:
            result += f" {self.bottom};"
        else:
            result += " 0"

        if self.left is not None:
            result += f" {self.left};"
        else:
            result += " 0"

        if result:
            result = result[1:]

        return result


def format_numeric_value(value, decimals=3):

    try:
        value = '{:d}'.format(value)
    except ValueError:
        f = '{{:.{:d}f}}'.format(decimals)
        value = f.format(value)

    return value


try:
    from steadfast import *

    decl_serializable(
        CSSUnitValue,
        SaveInitArguments(),
        type_identifier='csskit.css_unit_value'  # noqa
    )

    decl_serializable(
        CSSMathExpr,
        SaveInitArguments(),
        type_identifier='csskit.css_math_expr'  # noqa
    )

    decl_serializable(
        CSSObjectPosition,
        SaveInitArguments(),
        type_identifier='csskit.css_object_position'  # noqa
    )

    decl_serializable(
        CSSEdges,
        SaveInitArguments(),
        type_identifier='csskit.css_edges'  # noqa
    )

except ModuleNotFoundError:
    pass
