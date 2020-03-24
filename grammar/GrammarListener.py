# Generated from .\Grammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#import_.
    def enterImport_(self, ctx:GrammarParser.Import_Context):
        pass

    # Exit a parse tree produced by GrammarParser#import_.
    def exitImport_(self, ctx:GrammarParser.Import_Context):
        pass


    # Enter a parse tree produced by GrammarParser#block.
    def enterBlock(self, ctx:GrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by GrammarParser#block.
    def exitBlock(self, ctx:GrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by GrammarParser#header.
    def enterHeader(self, ctx:GrammarParser.HeaderContext):
        pass

    # Exit a parse tree produced by GrammarParser#header.
    def exitHeader(self, ctx:GrammarParser.HeaderContext):
        pass


    # Enter a parse tree produced by GrammarParser#parameters.
    def enterParameters(self, ctx:GrammarParser.ParametersContext):
        pass

    # Exit a parse tree produced by GrammarParser#parameters.
    def exitParameters(self, ctx:GrammarParser.ParametersContext):
        pass


    # Enter a parse tree produced by GrammarParser#print_.
    def enterPrint_(self, ctx:GrammarParser.Print_Context):
        pass

    # Exit a parse tree produced by GrammarParser#print_.
    def exitPrint_(self, ctx:GrammarParser.Print_Context):
        pass


    # Enter a parse tree produced by GrammarParser#multiline_description.
    def enterMultiline_description(self, ctx:GrammarParser.Multiline_descriptionContext):
        pass

    # Exit a parse tree produced by GrammarParser#multiline_description.
    def exitMultiline_description(self, ctx:GrammarParser.Multiline_descriptionContext):
        pass


    # Enter a parse tree produced by GrammarParser#description.
    def enterDescription(self, ctx:GrammarParser.DescriptionContext):
        pass

    # Exit a parse tree produced by GrammarParser#description.
    def exitDescription(self, ctx:GrammarParser.DescriptionContext):
        pass


    # Enter a parse tree produced by GrammarParser#multiline_expression.
    def enterMultiline_expression(self, ctx:GrammarParser.Multiline_expressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#multiline_expression.
    def exitMultiline_expression(self, ctx:GrammarParser.Multiline_expressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#definition.
    def enterDefinition(self, ctx:GrammarParser.DefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#definition.
    def exitDefinition(self, ctx:GrammarParser.DefinitionContext):
        pass


    # Enter a parse tree produced by GrammarParser#comment.
    def enterComment(self, ctx:GrammarParser.CommentContext):
        pass

    # Exit a parse tree produced by GrammarParser#comment.
    def exitComment(self, ctx:GrammarParser.CommentContext):
        pass


