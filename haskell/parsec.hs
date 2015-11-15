import Text.ParserCombinators.Parsec hiding (spaces)
import System.Environment

symbol :: Parser Char
symbol = oneOf "!#$%&|*+-/:<=>?@^_~" -- 定义一个能够识别出Scheme中允许的符号的解析器

-- http://www.jianshu.com/p/77cc5a67765d
