from .utilities import GenericParser
from .utilities import Visitor as BaseVisitor

from antlr4 import Token, RuleNode

__all__ = ['DefinitionsParser']


class Definition(object):
    pass


class OptionalArgument(object):

    @property
    def identifier(self):
        return self._identifier

    @property
    def value(self):
        return self._value

    def __init__(self, identifier, value):
        self._identifier = identifier
        self._value = value


class Command(Definition):

    @property
    def identifier(self):
        return self._identifier

    @property
    def required_arguments(self):
        return self._required_arguments[:]

    @property
    def optional_arguments(self):
        return self._optional_arguments[:]

    def __init__(self, identifier, required_arguments=None, optional_arguments=None):

        super().__init__()

        if required_arguments is None:
            required_arguments = []

        if optional_arguments is None:
            optional_arguments = []

        self._identifier = identifier
        self._required_arguments = list(required_arguments)
        self._optional_arguments = list(optional_arguments)


class Scope(object):

    @property
    def content(self):
        return self._content

    def __init__(self, content=None):

        if content is None:
            content = []

        self._content = list(content)


"""
class Visitor(BaseVisitor):

    def __init__(self, *args, **kwargs):
        super(Visitor, self).__init__(*args, **kwargs)

    def visitCommand(self, ctx):
        cmd = Command(identifier=ctx.identifier,
                      required_arguments=ctx.required_args,
                      optional_arguments=ctx.optional_args)
        return cmd
"""


class DefinitionsParser(GenericParser):

    from .generated.DefinitionTokens import DefinitionTokens
    from .generated.Definitions import Definitions
    from .generated.DefinitionsVisitor import DefinitionsVisitor

    """
    class VisitorImpl(DefinitionsVisitor):

        def defaultResult(self):
            return list()

        def aggregateResult(self, aggregate, nextResult):
            aggregate.append(nextResult)
            return aggregate

        def visitTerminal(self, node):
            return node.symbol.text

        def visitOptionalArgument(self, ctx):
            value = self.visit(ctx.value)
            result = OptionalArgument(ctx.identifier.text if ctx.identifier else None, value)
            return result

        def visitOptionalArgumentList(self, ctx):
            result = [self.visit(argument) for argument in ctx.arguments]
            return result

        def visitRequiredArgument(self, ctx):
            result = [self.visit(value) for value in ctx.values]
            return result

        def visitRequiredArgumentList(self, ctx):
            result = [self.visit(argument) for argument in ctx.arguments]
            return result

        def visitCommand(self, ctx):

            required_args = self.visit(ctx.required_arguments) if ctx.required_arguments else []
            optional_args = self.visit(ctx.optional_arguments) if ctx.optional_arguments else []

            # required_args = [arg.text if isinstance(arg, Token) else arg for arg in required_args]
            # optional_args = [arg.text if isinstance(arg, Token) else arg for arg in optional_args]

            cmd = Command(identifier=ctx.identifier.text,
                          required_arguments=required_args,
                          optional_arguments=optional_args)
            return cmd

        def visitScope(self, ctx):
            content = self.visitChildren(ctx)
            return Scope(content=content)

        def visitContent(self, ctx):
            result = self.visitChildren(ctx)
            result = result[0]
            return result

        def visitDefinition(self, ctx):
            result = self.visitChildren(ctx)
            result = result[0]
            return result

        def visitParse(self, ctx):
            result = self.visitChildren(ctx)[:-1]
            return result

        def __init__(self):
            super().__init__()
        """

    class VisitorImpl(DefinitionsVisitor):

        def defaultResult(self):
            return list()

        def aggregateResult(self, aggregate, nextResult):
            aggregate.append(nextResult)
            return aggregate

        def visitTerminal(self, node):
            return node.symbol.text

        def visitOptionalArgumentList(self, ctx):
            result = self.visit(ctx.arguments) if not isinstance(ctx.arguments, Token) else ctx.arguments.text
            return result

        def visitRequiredArgument(self, ctx):
            result = self.visit(ctx.argument) if not isinstance(ctx.argument, Token) else ctx.argument.text
            return result

        def visitRequiredArgumentList(self, ctx):
            result = [self.visit(argument) for argument in ctx.arguments]
            return result

        def visitCommand(self, ctx):

            required_args = self.visit(ctx.required_arguments) if ctx.required_arguments else []
            optional_args = self.visit(ctx.optional_arguments) if ctx.optional_arguments else []

            cmd = Command(identifier=ctx.identifier.text,
                          required_arguments=required_args,
                          optional_arguments=optional_args)
            return cmd

        def visitScope(self, ctx):
            content = self.visitChildren(ctx)
            return Scope(content=content)

        def visitContent(self, ctx):
            result = self.visitChildren(ctx)
            result = result[0]
            return result

        def visitDefinition(self, ctx):
            result = self.visitChildren(ctx)
            result = result[0]
            return result

        def visitParse(self, ctx):
            result = self.visitChildren(ctx)[:-1]
            return result

        def __init__(self):
            super().__init__()

    def __init__(self):

        super().__init__(
            LexerClass=DefinitionsParser.DefinitionTokens,
            ParserClass=DefinitionsParser.Definitions,
            VisitorClass=DefinitionsParser.VisitorImpl
        )


def main():

    import sys

    from antlr4 import ParserATNSimulator

    ParserATNSimulator.debug = True

    parser = DefinitionsParser()
    result = parser.parse_file(sys.argv[1])

    pass


if __name__ == '__main__':
    main()
