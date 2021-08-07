largest_num=13
print("Before:",largest_num)
for the_num in (8,56,2,65,3,78,14):
    if the_num > largest_num:
         largest_num = the_num
    print(largest_num,the_num)
print("After:",largest_num)
