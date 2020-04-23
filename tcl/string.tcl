#!/usr/bin/tclsh

set str "Have a nice day!"; # Have a nice day!
string length $str; #字符串的长度，包括了空格，共16
string index $str 8; # 返回索引号码为8的字符，即 i
string range $str 3 end; #返回从索引号为3开始到结尾的内容，为e a nice day!