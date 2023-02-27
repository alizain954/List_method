a = [1 , 2 , 3, 4, 5, 6, 7]

print(a)
print(id(a)) # id of list which is save in the memeory
print(type(a)) #  tell the type of the variable a
print(len(a)) # ive the length of the list
# access the list with the index
print(a[1]) # give the value which is on the index 1
# index is start from 0

# Negative indexing is start from the -1
print(a[-1])

#sciling the list give two value there the different method of sciling
print(a[2:5]) # start from index and end in the index 5 but the index 5 is not include
print(a[2:]) # start from 2 index and stop at the end of the list
print(a[:6]) # start from 0 index and stop at the 6 index of the list
# negative Sciling
print(a[-4:-1]) # returns the items from (-4) index to, but NOT including (-1):

#now we chage the value from the list

a[1] = "Ali Zain"
print(a)

a[1:3] = ["imran khan", "prime mister"]
print(a)

#now we change the value with insert property

a.insert(2, "sir Arif")
print(a)

# Add the value with append and insert
# with append method
a.append("pakistan")
print(a)
#with the insert value
a.insert(7, "cricket")
print(a)
# with the extend value
b = ["hockey", "badmatin", "swiming"]
a.extend(b)
print(a)

# Remove the data from the list
a.remove(5)
print(a)
# with the pop method
a.pop()
print(a)

# we can use the Del method and also clear method

# Loop on the list
for i in a:
    print(i)

# list comprishion
c = []
for x in a:
    c.append(x)
print(c)

d = ['ali', 'zain', 'he' , 'she' , 'then', 'pakistan']
newlist = [x for x in d if "a" in x]
print(newlist)

# sorted the list
d.sort()
print(d)
#Sort the list descending:
d.sort(reverse=True)
print(d)

# copy th list
e = a.copy()
print(e)
f = list(d)
print(f)

#join the list

a1 = ["a", "b", "c"]
a2 = [1, 2, 3]
a3 = a1 + a2
print(a3)

b1 = ["a", "b" , "c"]
b2 = [1, 2, 3]
for x in a1:
  b1.append(x)
print(b1)

c1 = ["a", "b" , "c"]
c2 = [1, 2, 3]
c1.extend(c2)
print(c1)

# there are lot method of list
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
