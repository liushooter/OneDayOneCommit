zero = -> p { -> x { x }   }
one = -> p { ->x {p[x] } }
two =  -> p { ->x{ p[p[x]] } }
three =  -> p { ->x{ p[p[p[x]]] } }

def to_integer(proc)
  proc[->n {n+1}][0]
end

_true  = -> x { -> y{ x } }
_false = -> x { -> y{ y } }

def to_boolean(proc)
  proc[true][false]
end

def _if(proc, x, y)
  proc[x][y]
end

_if = -> b { b }

pair = -> x { -> y { -> f{ f[x][y]} } }
left = -> p { p[->x{-> y{x}}] }
right = -> p { p[->x{-> y{y}}] }

increment = -> n { -> p { -> x { p[n[p][x]] } } }

def slide(pair)
  [pair.last, pair.last+1]
end
