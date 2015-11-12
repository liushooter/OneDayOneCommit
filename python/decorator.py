def log_func(log):
    def wrap(func):
        def func_wrapper(*args, **kwargs):
            log.debug("%s:" % func)
            for i, arg in enumerate(args):
                log.debug("\targs-%d: %s" % (i + 1, arg))
            for k, v in enumerate(kwargs):
                log.debug("\tdict args: %s: %s" % (k, v))
            return func(*args, **kwargs)
        return func_wrapper
    return wrap

# http://imtx.me/archives/1706.html
# http://stackoverflow.com/a/16661932/1240067 ruby decorator

############################

def hello(fn):
    def wrapper():
        print "hello, %s" % fn.__name__
        fn()
        print "goodby, %s" % fn.__name__
    return wrapper

@hello
def foo():
    print "i am foo"

foo()

# http://coolshell.cn/articles/11265.html