print("1.Program to print four values dec, oct, hex, bin")
print("2.Program to find the largest string among two strings")
print("3.Program to calculate the number of possible binary strings")
n=int(input("Enter your choise : "))

if n==1:
     a=int(input("Enter your number : "))
     print("Decimal : ",a, " Hex : ",hex(a)," Octal : ",oct(a), "Binary : ",bin(a))

if n==2:
    b=input("Enter first string : ")
    c=input("Enter the second string : ")

    if len(b)>len(c):
        print("The first string is larger than the second string")

    if len(b)<len(c):
        print("The second string is larger than the first string")
    if len(b)==len(c):
        print("Both strings are equal")


if n==3:
    d = int(input("Enter your number : "))
    print(bin(d))
    res = 2 ** (len(bin(d)) - 2)

    print("The number of possible bitstrings is : ", res)




