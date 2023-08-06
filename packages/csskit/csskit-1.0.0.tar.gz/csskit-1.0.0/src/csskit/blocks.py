from .common import CSSUnitValue, CSSVariable, CSSUnits, CSSEdges, CSSObjectFitType, SideType, CSSObjectPosition, \
    AspectRatio, ASPECT_RATIO_SQUARE, CSSObjectFitCover, SideTop

__all__ = []

try:

    from wagtail import __semver__
    from wagtail import blocks

    from django.utils.functional import cached_property
    import django.core.validators

    css_compatible_identifier_validator = django.core.validators.RegexValidator(
       '^[A-Za-z_][A-Za-z_0-9-]*$',
       code='invalid_identifier',
       message='A valid identifier starts with an alphanumeric letter or underscore and contains '
               'only alphanumeric letters, underscores, digits or hyphens.')


    class CSSUnitValueWrapper(blocks.StructValue):

        @property
        def as_common_value(self):
            return CSSUnitValue(self['value'], CSSUnits.map_identifier_to_value(self['unit']))


    class CSSUnitValueBlock(blocks.StructBlock):

        class Meta:
            value_class = CSSUnitValueWrapper
            accepted_css_units = CSSUnits.choices()

        def __init__(self, **kwargs):

            accepted_css_units = kwargs.pop('accepted_css_units', None)

            if accepted_css_units is None:
                meta = self._meta_class() # noqa
                accepted_css_units = meta.accepted_css_units

            local_blocks = kwargs.pop('local_blocks', [])

            value_block = blocks.FloatBlock()
            choice_block = blocks.ChoiceBlock(choices=accepted_css_units,
                                              default=accepted_css_units[0][0],
                                              required=False)

            local_blocks.insert(0, ('value', value_block))
            local_blocks.insert(1, ('unit', choice_block))

            super().__init__(local_blocks=local_blocks, **kwargs)

        def deconstruct(self):
            return blocks.Block.deconstruct(self)


    class CSSVariableWrapper(blocks.StructValue):

        @property
        def as_common_value(self):
            return CSSVariable(self['identifier'])


    class CSSVariableBlock(blocks.StructBlock):

        class Meta:
            value_class = CSSVariableWrapper

        identifier = blocks.CharBlock(default='', required=True, validators=(css_compatible_identifier_validator,))

        def deconstruct(self):
            return blocks.Block.deconstruct(self)


    __all__.extend(['CSSUnitValueBlock', 'CSSVariableBlock']) # noqa

    try:

        from wagtail_switch_block.blocks import SwitchBlock, SwitchValue, TYPE_FIELD_NAME

        COMPLEX_CSS_UNIT_VALUE_BLOCK_CHOICES = {
            'undefined': (blocks.StaticBlock, {}),
            'value': (CSSUnitValueBlock, {'default': {'value': 0, 'unit': None}}),
            'variable': (CSSVariableBlock, {})
        }

        class ComplexCSSUnitValueWrapper(SwitchValue):

            @property
            def as_common_value(self):

                if self.type == 'undefined':
                    return self.block.meta.undefined_value

                return self.value.as_common_value

        class ComplexCSSUnitValueBlock(SwitchBlock):

            class Meta:
                value_class = ComplexCSSUnitValueWrapper
                accepted_css_units = CSSUnits.choices()
                choices = ['undefined', 'value', 'variable']
                default_block_name = 'undefined'
                undefined_value = None

            def __init__(self, **kwargs):

                meta = self._meta_class()  # noqa

                choices = kwargs.get('choices', None)

                if choices is None:
                    choices = meta.choices

                accepted_css_units = kwargs.pop('accepted_css_units', None)

                if accepted_css_units is None:
                    accepted_css_units = meta.accepted_css_units

                kwargs.pop('local_blocks', None)

                local_blocks = []

                for choice in choices:
                    block_type, block_kwargs = COMPLEX_CSS_UNIT_VALUE_BLOCK_CHOICES.get(choice, (None, None))

                    if block_type is None:
                        raise RuntimeError(f'Undefined block choice: {choice}')

                    if block_type is CSSUnitValueBlock:
                        block_kwargs = dict(block_kwargs)
                        block_kwargs['accepted_css_units'] = accepted_css_units

                    block_def = block_type(**block_kwargs)
                    local_blocks.append((choice, block_def))

                super().__init__(local_blocks=local_blocks, **kwargs)

            def deconstruct(self):

                path, args, kwargs = blocks.Block.deconstruct(self)
                return path, args, kwargs

        def get_identifier_property(obj):
            return obj.identifier

        def return_value(value):
            return value

        class ObjectChoiceBlock(blocks.ChoiceBlock):
            choices = []

            class Meta:
                default = None
                from_identifier = return_value
                to_identifier = return_value

            @cached_property
            def objects_by_identifier(self):

                result = {}

                for identifier, value in self.field.choices:

                    if isinstance(value, (list, tuple)):

                        for nested_identifier, nested_value in value:
                            result[nested_identifier] = self.meta.from_identifier(nested_identifier)

                    else:
                        result[identifier] = self.meta.from_identifier(identifier)

                return result

            def to_python(self, value):

                if not isinstance(value, str):
                    return value

                return self.value_from_form(value)

            def get_prep_value(self, value):
                return self.value_for_form(value)

            def value_from_form(self, value):
                value = self.objects_by_identifier.get(value, None)
                return value

            def value_for_form(self, value):
                if not value:
                    return value

                return value.identifier

            def get_searchable_content(self, value):
                return super().get_searchable_content(value.identifier if value else value)

        class AspectRatioBlock(ObjectChoiceBlock):

            choices = AspectRatio.choices

            class Meta:
                default = ASPECT_RATIO_SQUARE
                from_identifier = AspectRatio.from_identifier
                to_identifier = get_identifier_property

        class CSSObjectFitBlock(ObjectChoiceBlock):

            choices = CSSObjectFitType.choices

            class Meta:
                default = CSSObjectFitCover
                from_identifier = CSSObjectFitType.from_identifier
                to_identifier = get_identifier_property

        class SideBlock(ObjectChoiceBlock):

            choices = SideType.choices

            class Meta:
                default = SideTop
                from_identifier = SideType.from_identifier
                to_identifier = get_identifier_property


        class CSSObjectPositionWrapper(blocks.StructValue):

            @property
            def as_common_value(self):

                x = self['x']
                y = self['y']

                return CSSObjectPosition(x=x.as_common_value, y=y.as_common_value)


        class CSSObjectPositionBlock(blocks.StructBlock):

            class Meta:
                value_class = CSSObjectPositionWrapper
                accepted_css_units = CSSUnits.choices()

            def __init__(self, local_blocks=None, **kwargs):

                accepted_css_units = kwargs.pop('accepted_css_units', None)

                if accepted_css_units is None:
                    meta = self._meta_class()  # noqa
                    accepted_css_units = meta.accepted_css_units

                if local_blocks is None:
                    local_blocks = []

                x = ComplexCSSUnitValueBlock(choices=['undefined', 'value'], accepted_css_units=accepted_css_units)
                y = ComplexCSSUnitValueBlock(choices=['undefined', 'value'], accepted_css_units=accepted_css_units)

                local_blocks.insert(0, ('x', x))
                local_blocks.insert(1, ('y', y))

                super().__init__(local_blocks, accepted_css_units=accepted_css_units, **kwargs)

            def deconstruct(self):

                path, args, kwargs = blocks.Block.deconstruct(self)
                return path, args, kwargs


        class CSSGapBlock(ComplexCSSUnitValueBlock):

            class Meta:
                choices = ['undefined', 'value']
                undefined_value = 'normal'

            def deconstruct(self):

                path, args, kwargs = blocks.Block.deconstruct(self)
                return path, args, kwargs


        class CSSEdgesBlockValue(blocks.StructValue):

            @property
            def as_common_value(self):

                top = self['top'].as_common_value
                right = self['right'].as_common_value
                bottom = self['bottom'].as_common_value
                left = self['left'].as_common_value

                return CSSEdges(top, right, bottom, left)


        class CSSEdgesBlock(blocks.StructBlock):

            class Meta:
                value_class = CSSEdgesBlockValue
                accepted_css_units = CSSUnits.choices()

            def __init__(self,
                         choices=None,
                         default_top=None,
                         default_right=None,
                         default_bottom=None,
                         default_left=None,
                         **kwargs):

                if choices is None:
                    choices = ['undefined', 'value', 'variable']

                accepted_css_units = kwargs.pop('accepted_css_units', None)

                if accepted_css_units is None:
                    meta = self._meta_class()  # noqa
                    accepted_css_units = meta.accepted_css_units

                local_blocks = kwargs.pop('local_blocks', [])
                required = kwargs.pop('required', True)

                if default_top is None:
                    default_top = {}

                if default_left is None:
                    default_left = {}

                if default_right is None:
                    default_right = {}

                if default_bottom is None:
                    default_bottom = {}

                top = ComplexCSSUnitValueBlock(choices=choices, accepted_css_units=accepted_css_units, default=default_top, required=required)
                right = ComplexCSSUnitValueBlock(choices=choices, accepted_css_units=accepted_css_units, default=default_right, required=required)
                bottom = ComplexCSSUnitValueBlock(choices=choices, accepted_css_units=accepted_css_units, default=default_bottom, required=required)
                left = ComplexCSSUnitValueBlock(choices=choices, accepted_css_units=accepted_css_units, default=default_left, required=required)

                local_blocks.insert(0, ('top', top))
                local_blocks.insert(1, ('right', right))
                local_blocks.insert(2, ('bottom', bottom))
                local_blocks.insert(3, ('left', left))

                super().__init__(local_blocks, required=required, **kwargs)

            def deconstruct(self):

                path, args, kwargs = blocks.Block.deconstruct(self)
                return path, args, kwargs

            @classmethod
            def undefined_default_edge_value(cls):
                return {TYPE_FIELD_NAME: 'undefined'}

            @classmethod
            def value_default_edge_value(cls, value, unit):
                return {TYPE_FIELD_NAME: 'value', 'value': {'value': value, 'unit': unit}}

            @classmethod
            def variable_default_edge_value(cls, identifier):
                return {TYPE_FIELD_NAME: 'variable', 'variable': {'identifier': identifier}}


        __all__.extend(['COMPLEX_CSS_UNIT_VALUE_BLOCK_CHOICES',
                        'ComplexCSSUnitValueBlock',
                        'CSSGapBlock',
                        'AspectRatioBlock',
                        'CSSObjectFitBlock',
                        'SideBlock',
                        'CSSObjectPositionBlock',
                        'CSSEdgesBlock']) # noqa

    except ImportError:
        pass

except ImportError:
    pass
