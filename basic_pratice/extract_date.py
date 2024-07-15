'''Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014'''


exam_st_date = (11, 12, 2014)


# The placeholders %i are used to format the integers.
# The placeholders %d are used to format the integers.
# The placeholders %s are used to format the strings.

print("The examination will start from : %i / %i / %i " %exam_st_date)
