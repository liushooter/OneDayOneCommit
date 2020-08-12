local http = require('resty.http')
local json = require("cjson")
local template = require("resty.template")

local httpc = http.new()
local url="https://httpbin.org/get"
local res, err = httpc:request_uri(url, {
    keepalive_timeout = 2000 -- 毫秒
})

if not res or res.status ~= 200 then
    ngx.log(ngx.ERR, "request error#", err)
    ngx.say("error")
    return
end

ngx.log(ngx.INFO, "request status#", res.status)
-- ngx.header.content_type="application/json;charset=utf8"
local json = json.decode(res.body)

local ip = json.origin
local userAgent = json.headers['User-Agent']

template.render("index.html", {
  ip = ip,
  userAgent = userAgent
})

