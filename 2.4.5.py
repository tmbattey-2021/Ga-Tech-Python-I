amount = 67

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write a program that will print out the coins needed to
#arrive at the amount shown above. Assume that we always want
#the maximum number of large coins: for example, for 67 cents,
#we want 2 quarters, 1 dime, 1 nickel, and 2 pennies instead
#of 6 dimes and 7 pennies.
#
#If you are unfamiliar with American currency: a quarter is
#worth 25 cents; a dime is worth 10 cents; a nickel is worth
#5 cents; a penny is worth 1 cent.
#
#To make things easier, we've gone ahead and supplied your
#print statements. All you need to do is create four variables:
#quarters, dimes, nickels, and pennies.
#
#HINT: Change the value of amount as you go to reflect what
#coins you've already found.


#Add your code here!



#If your code above is correct, the following lines will
#initially print (for amount = 67):
#Quarters: 2
#Dimes: 1
#Nickels: 1
#Pennies: 2
quarters = amount // 25
tot_quarters = amount - (quarters * 25) 
dimes = tot_quarters // 10
tot_dimes = tot_quarters - (dimes * 10)
nickels = tot_dimes // 5
pennies = tot_dimes - (nickels * 5)

print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
