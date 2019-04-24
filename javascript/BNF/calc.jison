/* lexical grammar */
%lex
%%

\s+                   /* skip whitespace */
[0-9]+("."[0-9]+)?    return 'NUMBER'
<<EOF>>               return 'EOF'
.                     return 'INVALID'
"+"                   return "PLUS"

/lex

%start expressions

%% /* language grammar */

expressions
  : NUMBER EOF
    {
      console.log($1);
      return $1;
    }
  ;

statement:
  NUMBER PLUS NUMBER
  {$$ = $1 + $3}
  |
  NUMBER
  {$$ = $1}
  ;