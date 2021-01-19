print(type("Hi"))      --> string
print(type(10.4*3))             --> number
print(type(print))              --> function
print(type(type))               --> function
print(type(true))               --> boolean
print(type(nil))                --> nil
print(type(type(X)))            --> string

----------
print(type(X)==nil)
print(type(X)=='nil')

if false or nil then
  print("至少有一个是 true")
else
  print("false 和 nil 都为 false")
end

if 0 then
  print("数字 0 是 true")
else
  print("数字 0 是 false")
end

----------

print(type(2))
print(type(2.2))
print(type(0.2))
print(type(2e+1))
print(type(0.2e-1))
print(type(7.8263692594256e-06))
----------

print(2^5)
print("2" + 6)
print("2" + "6")
print("2 + 6")
print("-2e2" * "6")

----------

print("a" .. 'b')
print(157 .. 428)
---------

name = "shooter"
print('len: '.. #name)
----------

-- test.lua 文件脚本
a = 5               -- 全局变量
local b = 5         -- 局部变量

function joke()
    c = 5           -- 全局变量
    local d = 6     -- 局部变量
end

joke()
print(c,d)          --> 5 nil

do
    local a = 6     -- 局部变量
    b = 6           -- 对局部变量重新赋值
    print(a,b);     --> 6 6
end

print(a,b)      --> 5 6

----------
print("error" + 1)
