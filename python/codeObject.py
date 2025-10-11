import dis

def f(a, b=1, /, *args, **kwargs):
  year = 2025
  pass

dis.dis(f)

code = f.__code__

print(code.co_name)
print(code.co_filename)
print(code.co_lines)

print(code.co_flags)
print(code.co_stacksize)

print(code.co_argcount)
print(code.co_posonlyargcount)
print(code.co_kwonlyargcount)

print(code.co_nlocals)
print(code.co_varnames)
print(code.co_names)

print(code.co_cellvars)
print(code.co_freevars)
print(code.co_consts)
