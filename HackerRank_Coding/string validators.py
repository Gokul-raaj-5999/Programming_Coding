if __name__ == '__main__':
    s = input()
    alphanumeric='False'
    alphabetical='False'
    digits='False'
    lowercase='False'
    uppercase='False'
    if(s.isalnum()):
        alphanumeric='True'
    for i in s:
        if(i.isalpha()):
            alphabetical='True'
        if(i.isdigit()):
            digits='True'
        if(i.islower()):
            lowercase='True'
        if(i.isupper()):
            uppercase='True'
    if(alphabetical=='True' and digits=='True'):
        alphanumeric='True'
    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)

###############################################################################
"""
INPUT:
qA2

OUTPUT:
True
True
True
True
True
"""
