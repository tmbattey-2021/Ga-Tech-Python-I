num_a = 1
num_b = 2
num_c = 3
num_d = 4
num_e = 5
num_z = 3

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#It's been said that the most confusing WiFi password you can
#have is: 2444666668888888, because you can read it as: one 2,
#three 4s, five 6s, seven 8s. Whisper the 's' and the listener
#will think it's just 12345678.
#
#Write a program that will generate a bad password according to
#a similar formula. Specifically, the variables above -- num_a,
#num_b, num_c, num_d, and num_e -- give you 5 integers. Your
#password should be: num_a num_b times, num_b num_c times,
#num_c num_d times, num_d num_e times, and num_e num_a times, in
#that order. Then, the entire password should repeat num_z times.
#
#So, for the initial values of num_a through num_e, this would
#be:
#
# 112223333444445112223333444445112223333444445
#
#That is, 1 two times, 2 three times, 3 four times, 4 five times,
#and 5 one time, all then repeated 3 times.
#
#You may assume all numbers will be between 0 and 9. Note, though,
#that if a number is 0, that means the preceding number will
#not actually appear. Moreover, if num_z is 0, the result string
#should be empty.


#Add your code below!


print((str(num_a) * num_b + str(num_b) * num_c + str(num_c) * num_d + str(num_d) * num_e + str(num_e) * num_a) * num_z)