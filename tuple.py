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

'''Intermediate level'''
# Q6 Tuple (10, 20, 30, 40, 50) ke first 3 elements slicing se print karo.
b1 = (10, 20, 30, 40, 50)
print(b1[0:3])

# Q7 Tuple (1, 2, 3, 2, 4, 2) me 2 kitni baar aata hai count karo.
b2 = (1, 2, 3, 2, 4, 2)
count = 0        #built in method [print(b2.count(2))]
for i in b2:
    if i == 2:
        count += 1
print(count)
    
# Q8 Tuple (10, 20, 30, 40, 50) me 30 ka index find karo.
b3  = (10, 20, 30, 40, 50)
index_count = -1          #print(b3.index(30))
for i in b3:
    index_count += 1
    if i  == 30:
        print(index_count)
        break

# Q9 User se 5 numbers input lekar tuple banao.
tup = []
for i in range(5):
    a = input("enter elements of tuples:- ")
    tup.append(a)
b4  = tuple(tup)
print(b4)

# Q10 Tuple ke saare elements ka sum nikaalo:
b5 = (5, 10, 15, 20)
sum = 0 
for i in b5:
    sum += i
print(sum)
