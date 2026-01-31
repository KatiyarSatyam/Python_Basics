#1.Numerical literal
a = 0b1010 #Binary literals
b = 100 #Decimal literals
c= 0o310 #Octal literals
d = 0x12c #Hexadecimal literals

#float literals
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3

#complex literal
x = 3.14j

print(a,b,c,d)
print(float_1, float_2, float_3)
print(x, x.imag, x.real)

#2.String literals
string = 'HELLO'
strings = ("Helloooo")
char = "C"
multiline_str = """THIS IS A MULTILINE STRING IN WHICH WE CAN GET INPUT AS A PARAGRAPH"""
unicode = u"\U0001f600"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)

#3.Boolean literal

a = True + 4
b = False + 20
print("a:", a)
print("b:", b)

#Special literal
a = None
print(a)
