TARGETS = Grammar.interp Grammar.tokens GrammarLexer.interp GrammarLexer.py GrammarLexer.tokens GrammarListener.py GrammarParser.py

ALL: $(TARGETS)

$(TARGETS) &: Grammar.g4
	antlr4 -Dlanguage=Python3 Grammar.g4

clean:
	rm $(TARGETS)
