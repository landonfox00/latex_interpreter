# Generated from .\Grammar.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16K\n\16\r\16")
        buf.write("\16\16L\3\17\3\17\3\20\3\20\3\21\5\21T\n\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25\3\2\6\5\2\62;C\\c|\3\2#\u0080")
        buf.write("\7\2$(<<??]_\u0080\u0080\b\2##)\61=>@B`b}\177\2]\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\3)\3\2\2\2\5\60\3\2\2\2\7\63\3\2\2\2")
        buf.write("\t\65\3\2\2\2\13\67\3\2\2\2\r9\3\2\2\2\17;\3\2\2\2\21")
        buf.write(">\3\2\2\2\23A\3\2\2\2\25C\3\2\2\2\27E\3\2\2\2\31G\3\2")
        buf.write("\2\2\33J\3\2\2\2\35N\3\2\2\2\37P\3\2\2\2!S\3\2\2\2#U\3")
        buf.write("\2\2\2%W\3\2\2\2\'Y\3\2\2\2)*\7k\2\2*+\7o\2\2+,\7r\2\2")
        buf.write(",-\7q\2\2-.\7t\2\2./\7v\2\2/\4\3\2\2\2\60\61\7c\2\2\61")
        buf.write("\62\7u\2\2\62\6\3\2\2\2\63\64\7]\2\2\64\b\3\2\2\2\65\66")
        buf.write("\7_\2\2\66\n\3\2\2\2\678\7<\2\28\f\3\2\2\29:\7.\2\2:\16")
        buf.write("\3\2\2\2;<\7&\2\2<=\7&\2\2=\20\3\2\2\2>?\7$\2\2?@\7$\2")
        buf.write("\2@\22\3\2\2\2AB\7&\2\2B\24\3\2\2\2CD\7^\2\2D\26\3\2\2")
        buf.write("\2EF\7?\2\2F\30\3\2\2\2GH\7\'\2\2H\32\3\2\2\2IK\t\2\2")
        buf.write("\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\34\3\2\2\2")
        buf.write("NO\t\3\2\2O\36\3\2\2\2PQ\t\4\2\2Q \3\2\2\2RT\t\5\2\2S")
        buf.write("R\3\2\2\2T\"\3\2\2\2UV\7\13\2\2V$\3\2\2\2WX\7\f\2\2X&")
        buf.write("\3\2\2\2YZ\7\"\2\2Z[\3\2\2\2[\\\b\24\2\2\\(\3\2\2\2\5")
        buf.write("\2LS\3\b\2\2")
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
    T__11 = 12
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
            "'$'", "'\\'", "'='", "'%'", "'\t'", "'\n'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "TERM", "CHARACTER", "OPERATOR", "NON_OPERATOR", "TAB", "NEWLINE", 
            "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "TERM", "CHARACTER", 
                  "OPERATOR", "NON_OPERATOR", "TAB", "NEWLINE", "WHITESPACE" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


