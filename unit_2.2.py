is_weekend = True
is_holiday = False
is_rainy = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a program that will determine what kind of plans you
#could make based on what kind of day it is and what the
#weather is like.
#
#You have three variables to use in these decisions:
#
# - is_weekend, whether it's a weekend day
# - is_holiday, whether it's a holiday
# - is_rainy, whether it's going to be raining
#
#Your four options are:
#
# - Beach, if it's both a holiday and a weekend as long as
#   it's _not_ raining. If it's raining, the beach is not
#   an option.
# - Lake, if it's a weekend and not raining. It doesn't
#   matter if it's a holiday or not.
# - Park, if it's not raining. It doesn't matter whether
#   it's a weekend or holiday.
# - Home, if it's raining, or if it's neither a weekend
#   nor a holiday.
#
#In other words: the Beach is an option on holiday weekends
#when the weather is good. The Lake is an option on regular
#weekends when the weather is good. The Park is an option
#any time the weather is good. Home is an option if it's
#raining, or if it's not a weekday that isn't a holiday.

#
#Print your results like this, based on whether each is
#an option according to the logic above:
#
# - Beach: False
# - Lake: True
# - Park: True
# - Home: False


#Add your code here!

print("Beach:", is_weekend and is_holiday and not(is_rainy))
print("Lake:", is_weekend and not(is_rainy))
print("Park:", not(is_rainy))
print("Home:", is_rainy or not(is_weekend or is_holiday))