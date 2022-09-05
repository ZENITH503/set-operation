# in order to make an empty set
myset = set()
print(type(myset))
myset.add(4)
myset.add(5)
myset.add(3)
print(myset)
#incase if we add 2 times 4 in the set then also it would show only one 4 in the set because it takes only one value and not the repetative
myset.add((1,2,3,4,5,6,7,8,9)) #this function could print and add a sequence of objects as a set
print(myset)# here we can add a set into a set but not a list or tupple or dictionary into a set
#set items cannot be changed, are unindexed
print(len(myset))#prints the length of the set
myset.remove(5)#removes the element from the set
print(myset)
#this function removes any element from the set and returns it to the user
print(myset.pop()) 
print(myset.pop()) 
#the function clears the set
#print(myset.clear())
print(myset.union({1,2,3,4,10}))
print(myset.intersection({1,2,3,4,5,11,23}))