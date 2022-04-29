assignment_num = 1
day = "Friday"
month = "September"
date = 13
time = "5PM"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#At the beginning of each week, we try to post an announcement
#outlining everything you need to do during the week. Let's
#see if we could parameterize that.
#
#The variables above -- assignment_num, day, month, date, and
#time -- give various values about when an assignment is due.
#Using these values you should print a sentence like this:
#
# You should submit Assignment 1 by Friday, September 13 at 5PM.
#
#The general form would be:
# You should submit Assignment [assignment_num] by [day], [month] [date] at [time].
#
#Make sure the punctuation and spaces are all exactly as written.
#There should be spaces before and after the assignment number,
#a comma and space after the day of the week, and a period
#after the time.


#Add your code here!


str_num = str(assignment_num)
str_date = str(date)
print("You should submit Assignment " + str_num + " by " + day + ", " + month + " " + str_date + " at " + time + ".")
      


