'''Basic level'''

# Q1 Ek tuple (10, 20, 30, 40, 50) banao aur 3rd element print karo.
a = (10,20,30,40,50)
print(a[2])

# Q2 Tuple (1, 2, 3, 4, 5) ka length nikaalo.
a1 = (1,2,3,4,5)
print(len(a1))

# Q3 Tuple ("apple", "banana", "mango") me "banana" hai ya nahi check karo.
A  = ("apple", "banana", "mango")
if "banana" in A:
    print(True)
else:
    print(False)

# Q4 Tuple (10, 20, 30, 40, 50) ka last element print karo.
a2 = (10, 20, 30, 40, 50)
print(a2[-1])

# Q5 Tuple (1, 2, 3) aur (4, 5, 6) ko join karke naya tuple banao.
A1 = (1,2,3)
A2 = (4,5,6)
A3 = A1 + A2
print(A3)

