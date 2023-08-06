# -*- coding: utf-8 -*-

from antlr4 import *

__all__ = ['Visitor', 'GenericParser']


class Visitor(object):

    def __init__(self, *args, LexerClass=None, ImplErrorClass=None, **kwargs):
        super(Visitor).__init__()

        if ImplErrorClass is None:
            ImplErrorClass = RuntimeError

        self.LexerClass = LexerClass
        self.ImplErrorClass = ImplErrorClass

        if len(args) != 0:
            raise self.ImplErrorClass('Unexpected visitor arguments.')

        if len(kwargs) != 0:
            raise self.ImplErrorClass('Unexpected visitor keyword arguments.')

    def defaultResult(self):
        return []

    def aggregateResult(self, aggregate, nextResult):
        aggregate.append(nextResult)
        return aggregate

    def visitImpl(self, ctx):
        return self.defaultResult()

    def visitChildrenImpl(self, ctx):
        return self.defaultResult()


class GenericParser(object):

    def __init__(self, *, LexerClass, ParserClass, VisitorClass, errorStrategy=None):

        if errorStrategy is None:
            errorStrategy = BailErrorStrategy()

        self.LexerClass = LexerClass
        self.ParserClass = ParserClass
        self.VisitorClass = VisitorClass
        self.errorStrategy = errorStrategy

    def parse_string(self, string):
        input_stream = InputStream(string)
        return self.parse_input_stream(input_stream)

    def parse_file(self, file_path):
        input_stream = FileStream(fileName=file_path, encoding='utf-8')
        return self.parse_input_stream(input_stream)

    def parse_input_stream(self, input_stream):

        lexer = self.LexerClass(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = self.ParserClass(input=token_stream)
        parser._errHandler = self.errorStrategy
        tree = parser.parse()

        visitor = self.VisitorClass()
        return visitor.visit(tree)
