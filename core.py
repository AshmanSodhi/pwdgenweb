import random
def low(length , type):
    length = length
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "0123456789!@#$%^&*()"
    password = ""

    if type == 1:
        for i in range(0,length):
            password = password + random.choice(lower)
        return password
    elif type == 2:
        for i in range(0,length):
            password = password + random.choice(upper)
        return password
    elif type == 3:
        a=''
        b=''
        c= ''
        for i in range(0,int(length/2)):
            a = a + random.choice(upper)
        for i in range(0,int(length/2)):
            b = b + random.choice(digits)
        c = c + a + b
        cl = list(c)
        random.shuffle(cl)
        password = password.join(cl)
        return ''.join(cl)
        
