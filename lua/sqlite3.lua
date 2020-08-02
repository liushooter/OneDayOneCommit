sqlite3 = require "luasql.sqlite3"
local env  = sqlite3.sqlite3()
local conn = env:connect('./topSites.db')
print(env, conn)
print()

status,errorString = conn:execute([[select * from keywords limit 1]])
print(status, errorString)
print(string.rep("-",100))

cursor,errorString = conn:execute([[select * from top_sites order by url_rank asc]])
row = cursor:fetch ({}, "a")

while row do
   print(string.format("Id: %s, title: %s, url: %s, rank: %s", row.id, row.title, row.url, row.url_rank))
   row = cursor:fetch (row, "a")
end

-- https://www.kaifaxueyuan.com/server/lua/lua-database-access-sqlite.html