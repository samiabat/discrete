#RSA ALGORITHM IMPLEMENTATION BY PYTHON
#Group members
#Samuel abatneh UGR/7229/12
#Sefineh Tesfa UGR/2844/12
#Jebessa Dejene UGR/0459/12
#Abel mekonen UGR/7784/12
#Genzeb alemu UGR/9822/12
#Hiwot derese UGR/2790/12
#date 29/09/2021

def gcd(a, b): #function decleared and defined. This function apply euler theorem to find and return gcd of numbers
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(a, (a % b))


prime_1 = int(input("prime one: "))
prime_2 = int(input("prime two: "))
message1 = int(input("enter the message 1: "))

n = prime_1 * prime_2
theta = (prime_1 - 1) * (prime_2 - 1)
e = 0
liste = []
for k in range(2, theta):
    if gcd(k, theta) == 1:
        liste.append(k)

print("your possible value of e is the following choose one:", liste)

e = int(input("please enter the value of e  :"))
d = 0

for k in range(2, n):
    if (k * e - 1) % theta == 0:
        d = k
        break

print("menu:")
print("y: to Encrypt ")
print("N: to Decrypt")
command = input("")
command = command.lower()

if command == "y":
    encryrptMessage1 = (message1** e % n)
    st = str(encryrptMessage1)
    print("the encrypted message is " + st)

elif command == "n":
    message_1 = (message1** d % n)
    mess = str(message_1)
    print("decrypted message: " + mess)

c = input("to exit press key: 'c'  ")
while c == 1:
    break
