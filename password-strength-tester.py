import math

# The User-inputted password
password = input(f'What is the your Password? \n>')

# R = Pool of Unique Characters
def getR(user_password):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`"

    has_lower = any(char in lower for char in user_password)
    has_upper = any(char in upper for char in user_password)
    has_digits = any(char in digits for char in user_password)
    has_symbols = any(char in symbols for char in user_password)

    R = 0
    if has_lower:
        R += 26
    if has_upper:
        R += 26
    if has_digits:
        R += 10
    if has_symbols:
        R += 32
    
    return R

R = getR(password)

# L = Number of Characters in your Password
def getL(user_password):
    return len(password)

L = getL(password)

# E = Bits of Entropy
def getE(R,L):
    E = math.log2(pow(R,L))
    return E

E = getE(R,L)

# Password Stregnth according to scale

def getStrength(E):
    Strength = ""
    if E < 30:
        Strength = "Very Weak"
    elif E > 30 and E < 50:
        Strength = "Weak"
    elif E > 50 and E < 60:
        Strength = "Decent"
    elif E > 60 and E < 80: 
        Strength = "Strong"
    elif E > 80:
        Strength = "Very Strong"
    else: 
        Strength = "Undetermined"
    return Strength

strength = getStrength(E)

# Print Statements
print(f'This is the password: {password}')
print(f'This is the value of L: {L}')
print(f'This is the value of R: {R}')
print(f'This is the value of E: {E}')
print(f'Strength = {strength}')
