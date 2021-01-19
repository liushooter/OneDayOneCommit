local path = "/usr/local/lib/lua/5.3/socket/core.so"
local f = package.loadlib(path, "luaopen_socket")

local fun = assert(package.loadlib(path, "luaopen_socket"))
fun()  -- 真正打开库