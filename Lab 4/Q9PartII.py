m1 = input("Enter a message: ")
m2 = ""
m3 = []

for ch in m1: 
    m2 += ch
    m3.append(m2)

for message in m3[::-1]: 
    print (message)