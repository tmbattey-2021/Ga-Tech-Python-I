Before we move on, let's cover something that might make your life a little easier later on.

Imagine you wanted to print three integers at once, along with some labeling. For example...

print("The first value is", first_val, ", the second value is", second_val, ", the third value is", third_val)
That line is a little confusing to read, isn't it? There are commas and spaces being used inside and outside of strings, variable names being used along side similar-looking labeling strings... it's just messy to read.

The same line could be rewritten like this:

print("The first value is {0}, the second value is {1}, the third value is {2}".format(first_val, second_val, third_val))
Just like the first line, Python will automatically convert these values to strings if necessary. Even better, this approach works outside a print statement -- we could also do this and never have to convert any integers to strings:

my_string = "The first value is {0}, the second value is {1}, the third value is {2}".format(first_val, second_val, third_val)
We'll talk more later about what's actually going on there, but this syntax might help you. When you add that .format at the end with a list of variables or values, it automatically matches them by order to the numbers given inside brackets in the string, like {0} and {2}. first_val is used where {0} is found, second_val is used where {1} is found, and third_val is used where {2} is found (because Python starts counting at 0).

Try to use that on the following problem!

mystery_value_1 = 6
mystery_value_2 = 3

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Print a sentence describing the values you get when you add,
#subtract, multiply, and divide the numbers above. The
#sentence should look like this:
#
#The sum is 9, the difference is 3, the product is 18, and the
#quotient is 2.0.
#
#Make sure to include all commas, spaces, and periods exactly
#as shown -- the only thing that should change based on the
#values of the variables is the numbers.


#Add your code here!
