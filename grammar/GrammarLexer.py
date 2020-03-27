# Generated from Grammar.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\7\rK\n\r\f\r\16\r")
        buf.write("N\13\r\3\r\3\r\3\16\6\16S\n\16\r\16\16\16T\3\17\3\17\3")
        buf.write("\20\3\20\3\21\5\21\\\n\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write("\3\2\6\5\2\62;C\\c|\3\2#\u0080\7\2$(<<??]_\u0080\u0080")
        buf.write("\b\2##)\61=>@B`b}\177\2g\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2")
        buf.write("\5\60\3\2\2\2\7\63\3\2\2\2\t\65\3\2\2\2\13\67\3\2\2\2")
        buf.write("\r9\3\2\2\2\17;\3\2\2\2\21>\3\2\2\2\23A\3\2\2\2\25C\3")
        buf.write("\2\2\2\27E\3\2\2\2\31G\3\2\2\2\33R\3\2\2\2\35V\3\2\2\2")
        buf.write("\37X\3\2\2\2![\3\2\2\2#]\3\2\2\2%_\3\2\2\2\'a\3\2\2\2")
        buf.write(")*\7k\2\2*+\7o\2\2+,\7r\2\2,-\7q\2\2-.\7t\2\2./\7v\2\2")
        buf.write("/\4\3\2\2\2\60\61\7c\2\2\61\62\7u\2\2\62\6\3\2\2\2\63")
        buf.write("\64\7]\2\2\64\b\3\2\2\2\65\66\7_\2\2\66\n\3\2\2\2\678")
        buf.write("\7<\2\28\f\3\2\2\29:\7.\2\2:\16\3\2\2\2;<\7&\2\2<=\7&")
        buf.write("\2\2=\20\3\2\2\2>?\7$\2\2?@\7$\2\2@\22\3\2\2\2AB\7&\2")
        buf.write("\2B\24\3\2\2\2CD\7^\2\2D\26\3\2\2\2EF\7?\2\2F\30\3\2\2")
        buf.write("\2GL\7\'\2\2HK\7\"\2\2IK\5\35\17\2JH\3\2\2\2JI\3\2\2\2")
        buf.write("KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MO\3\2\2\2NL\3\2\2\2OP\b")
        buf.write("\r\2\2P\32\3\2\2\2QS\t\2\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2")
        buf.write("\2\2TU\3\2\2\2U\34\3\2\2\2VW\t\3\2\2W\36\3\2\2\2XY\t\4")
        buf.write("\2\2Y \3\2\2\2Z\\\t\5\2\2[Z\3\2\2\2\\\"\3\2\2\2]^\7\13")
        buf.write("\2\2^$\3\2\2\2_`\7\f\2\2`&\3\2\2\2ab\7\"\2\2bc\3\2\2\2")
        buf.write("cd\b\24\2\2d(\3\2\2\2\7\2JLT[\3\b\2\2")
        return buf.getvalue()


class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    Comment = 12
    TERM = 13
    CHARACTER = 14
    OPERATOR = 15
    NON_OPERATOR = 16
    TAB = 17
    NEWLINE = 18
    WHITESPACE = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'as'", "'['", "']'", "':'", "','", "'$$'", "'\"\"'", 
            "'$'", "'\\'", "'='", "'\t'", "'\n'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "Comment", "TERM", "CHARACTER", "OPERATOR", "NON_OPERATOR", 
            "TAB", "NEWLINE", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "Comment", "TERM", "CHARACTER", 
                  "OPERATOR", "NON_OPERATOR", "TAB", "NEWLINE", "WHITESPACE" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


