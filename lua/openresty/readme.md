# OpenResty

https://openresty.org/en/installation.html

https://openresty.org/en/linux-packages.html

https://luarocks.org/

https://moonbingbing.gitbooks.io/openresty-best-practices

## luarocks

```
luarocks install luasocket
luarocks install luasql-sqlite3
luarocks install lua-resty-http
sudo luarocks install lua-resty-template 2.0
sudo luarocks remove lua-resty-template

luarocks list
```

## OpenResty cli

```
PATH=/usr/local/openresty/nginx/sbin:$PATH
export PATH

nginx -p `pwd`/ -c conf/nginx.conf # run

sudo kill -HUP `cat logs/nginx.pid` # 重启

openresty -s quit -p `pwd` -c conf/nginx.conf # quit

openresty -s reload -p `pwd` -c conf/nginx.conf # reload
```