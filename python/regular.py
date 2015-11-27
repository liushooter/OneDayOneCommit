import re


def num_to_currency(num, digits = 0):
    print("origin num = "+str(num))

    # '{:0,.2f}'.format(520235.14159)  => 520,235.14

    if num is None:
        num = 0

    format_str = "{:0,.%sf}" % (digits)
    regular = r'0{1,%s}$' % (digits) #'0{1,8}$'

    result = format_str.format(num)

    if result.find(".") > 0:
        print re.sub(regular, '0', result)
    else:
        print result
    print result
    print "--------------------------"


print("^"*100)


num_to_currency(10, digits = 8)
num_to_currency(1000, digits = 8)
num_to_currency(12345, digits = 8)
num_to_currency(12345678, digits = 8)
num_to_currency(12345678.123456789, digits = 8)
num_to_currency(12345678.12345678, digits = 8)
num_to_currency(12345678.10000000, digits = 8)
num_to_currency(12345678.12345600, digits = 8)
num_to_currency(12345678.12345670, digits = 8)



# import re
# val =“18612345678"

# re.sub(r'(.{4})(.{4})$', '****\g<2>', val)
# re.sub(r'(.{,4})(.{,4})$', '****\g<2>', val)

# re.sub(r'^(.{3}).*(.{4})$', '\g<1>****\g<2>', val)
# re.sub(r'0*$', '0', result)



# n.to_s.gsub!(/(\d)(?=(\d\d\d)+(?!\d))/, "\\1,”)
