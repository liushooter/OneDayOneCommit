tbl = {"apple", "pear", "orange", "grape"}

print('tbl len '..#tbl)
for key, val in pairs(tbl) do
    print("Key", key)
end

for k, v in pairs(tbl) do
  print(k .. " - " .. v)
end

print()
tbl[1] = nil -- index从1开始
for k, v in pairs(tbl) do
  print(k .. " - " .. v)
end

----------

a = 10
repeat
   print("a的值为:", a)
   a = a + 1
until( a > 15 )

----------
print()
while( a < 20 )
do
   print("a 的值为:", a)
   a=a+1
   if( a > 15)
   then
      break
   end
end

----------
print()

for i=1, 5 do
    if i <= 2 then
        print(i, "yes continue")
        goto continue
    end
    print(i, " no continue")
    ::continue::
    print([[end]])
end
----------
----------
-- while( true )
-- do
--    print("循环将永远执行下去")
-- end