# 0 / 10 점
def myfunction(msg) :
    a = 0
    b = 10
    msg = msg
    def myfunction_inner() :
        return msg
    return myfunction_inner

msg = "Hello, World"
aaa = myfunction(msg)
print(aaa())

# 8.75 / 10 점
def myfunction(msg) :
    """This function is a pylint testing function."""
    # a = 0
    # b = 10
    msg_local = msg
    def myfunction_inner() :
        return msg_local
    return myfunction_inner
MSG = "Hello, World"
aaa = myfunction(MSG)
print(aaa())
