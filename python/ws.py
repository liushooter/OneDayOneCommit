def application(env, start_response):
  start_response('200 OK', [('Content-Type','text/html')])
  return "Hello World"

# uwsgi --http :8001 --wsgi-file ws.py