#! /usr/bin/env python3
a = [1, 3, 4, 5, 8]
a.append(23) #adding element at last position of list.
a.insert(0,23) #inserting at first position of list.
a.insert(2,21) #inserting at second position of list.

print("list : ", a)

del a[-1] #delete last element.
a.remove(3) #delete element from list.
print("deletion opeartion on list : ", a)

a.append(11)
k= a.count(11)
print("k : ", k)

b = [34, 56, 221, 3]
a.append(b) # append list at end of list a.
print(a)

a.extend(b)
print(a)

a.remove(b)
a.reverse()
print("reverse : ",a)

a.sort()
print(a)

