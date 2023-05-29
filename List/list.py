# List in python

# List is a collection of items. It is mutable and ordered.

a = [10, 20, 30, 40, 50]
print(a)

# Accessing list items
print(a[0])
print(a[1])

# Using for loop
for i in a:
    print(i)

# Using while loop
i = 0
while i < len(a):
    print(a[i])
    i += 1

# List slicing
print(a[0:3]) # 0, 1, 2
print(a[1:4]) # 1, 2, 3
print(a[2:]) # 2, 3, 4
print(a[:3]) # 0, 1, 2
print(a[:]) # 0, 1, 2, 3, 4

# List methods
# append() - add item at the end of the list
a.append(60)
print(a)

# insert() - add item at the specified index
a.insert(3, 35)
print(a)

# remove() - remove item from the list
a.remove(35)
print(a)

# pop() - remove item from the specified index
a.pop(3)
print(a)

# clear() - remove all items from the list
a.clear()
print(a)

# del - delete the list completely
del a
print(a) # NameError: name 'a' is not defined

# copy() - copy the list
a = [10, 20, 30, 40, 50]
b = a.copy()
print(b)

# count() - count the number of items in the list
print(a.count(10))

# index() - return the index of the specified item
print(a.index(30))

# sort() - sort the list
a.sort()
print(a)

# reverse() - reverse the list
a.reverse()
print(a)

# extend() - add items from another list to the current list
a.extend([60, 70, 80])
print(a)

# len() - return the length of the list
print(len(a))

# min() - return the minimum value from the list
print(min(a))

# max() - return the maximum value from the list
print(max(a))

# sum() - return the sum of all items in the list
print(sum(a))

# all() - return True if all items in the list are True
print(all(a))

# any() - return True if any item in the list is True
print(any(a))


