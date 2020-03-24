from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarListener import GrammarListener
from GrammarParser import GrammarParser
import sys

class GrammarPrintListener(GrammarListener):
    def enterImport_(self, ctx):
        if ctx.TERM(1):
            print('----importing {0} as {1}'.format(ctx.TERM(0), ctx.TERM(1)))
        else:
            print('----importing {0}'.format(ctx.TERM(0)))

    def enterComment(self, ctx):
        print('----skipping comment')


def main():
    lexer = GrammarLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.program()
    printer = GrammarPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()
