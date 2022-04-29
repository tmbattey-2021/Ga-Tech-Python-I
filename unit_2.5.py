donuts = 119

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#A donut shop sells donuts in four sizes: packs of 60 donuts,
#packs of 12 donuts, packs of 3 donuts, and individual donuts.
#
#To divide donuts into packs, they start by making as many of
#the largest pack as they can. Then, they make as many of the
#next largest pack, then the next pack, then finally they sell
#the remaining donuts individually. For example, if they baked
#119 donuts, then they would divide those donuts into one
#pack of 60, four packs of 12, three packs of 3, and 2
#individual donuts.
#
#Based on the variable donuts above, calculate how many of
#each size they will make. Print the results according to
#this template:
#
#Packs of 60: 1
#Packs of 12: 4
#Packs of 3: 3
#Packs of 1: 2


#Add your code here!

p60 = donuts // 60
#print(p60)
p12 = (donuts - (p60 * 60)) // 12
#print(p12)
p3 = (donuts - (p60 * 60) - (p12 * 12)) // 3
#print(p3)
pfinal = (donuts - (p60 * 60) - (p12 * 12)) % 3
#print(pfinal)

print("Packs of 60:", p60)
print("Packs of 12:", p12)
print("Packs of 3:", p3)
print("Packs of 1:", pfinal)