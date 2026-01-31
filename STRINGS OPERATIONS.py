#arthemetic operator
c = "HELLO" + " "+ "WORLD" #adding string using concatination
print(c)
print("*" * 99999)

a = "hello" != "world" #not equal to
print(a)
b = "mumbai" > "pune" #greater than , measure lexiographically
print(b)
c1 = "goa" < "kolkata" #smaller than
print(c1)
c2 = "kol">"Kol" #due to small letters come later
print(c2)

#logical operator
a1 = "Hello" and "World"  #it will print world because it is on true place
print(a1)
a2 = "World" and "Hello"
print(a2)
a3 = "Hello" or "World"
print(a3)
a4 = "World" or "Hello"
print(a4)

#for loop

a5 = "hello world"
for i in a5:
    print(i)

a6 = "hello world"
for i in a6[2:7]: #slicing
    print(i)

a7= "hello world" #slicing with given index
for i in a7[2:7:2]:
    print(i)

a8 = "hello world"
print('H' in a8)

a9 = "hello world"
print('H' not in a9)