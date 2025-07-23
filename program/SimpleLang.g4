grammar SimpleLang;

prog: stat+ ;

stat: expr NEWLINE ;

expr: expr '**' expr                               # Power 
    | expr op=('*'|'/') expr                       # MulDiv
    | expr op=('+'|'-') expr                       # AddSub
    | expr op=('=='|'<'|'>'|'<='|'>='|'!=') expr   # Comparison
    | INT                                          # Int
    | FLOAT                                        # Float
    | STRING                                       # String
    | BOOL                                         # Bool
    | CHAR                                         # Char
    | '(' expr ')'                                 # Parens
    ;

INT: [0-9]+ ;
FLOAT: [0-9]+'.'[0-9]* ;
STRING: '"' .*? '"' ;
BOOL: 'true' | 'false' ;
CHAR: '\'' . '\'' ;
NEWLINE: '\r'? '\n' ;
WS: [ \t]+ -> skip ;