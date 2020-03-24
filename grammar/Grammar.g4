grammar Grammar;


/*
 * Parser Rules
 */

program					: statement* ;

statement				: ( import_ | block | print_ | definition | comment )? NEWLINE ;

import_					: 'import' TERM ( 'as' TERM )? ;

// TODO: import block bodies
block					: header NEWLINE ;

header					: ( TERM | multiline_description ) ( '[' parameters ']' )? ':' ;

parameters				: ( definition | description ) ( ',' parameters )? ;

print_					: multiline_description | ( '$$' | '""' ) multiline_expression ;

multiline_description	: description | '$' expression '$' | multiline_description ( NEWLINE TAB+ )? multiline_description ;

description				: ( TERM | NON_OPERATOR | '\\' OPERATOR ) description? ;

multiline_expression	: expression ( NEWLINE TAB+ expression )? ;

expression				: ( TERM | CHARACTER ) expression? ;

definition				: TERM '=' ( block | print_ ) ;

comment					: '%' CHARACTER* ;


/*
 * Lexer Rules
 */

TERM					: [a-zA-Z0-9]+ ;

CHARACTER				: [\u0021-\u007e] ;

OPERATOR				: '$' | '"' | '%' | '&' | '#' | '~' | '[' | ']' | ':' | '=' | '\\' ;

NON_OPERATOR			: '\u0021' | [\u0027-\u002f] | '\u003b' | '\u003c' | [\u003e-\u0040] | [\u005e-\u0060] | [\u007b-\u007d] ;

TAB						: '\t' ;

NEWLINE					: '\n' ;

WHITESPACE				: ' ' -> skip ;
