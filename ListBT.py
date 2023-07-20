#!/usr/bin/env python
# coding: utf-8

# In[2]:


def finds(input_list):
    if len(input_list) < 2:
        raise ValueError("List must contain at least two elements.")

    largest = max(input_list[0], input_list[1])
    second_largest = min(input_list[0], input_list[1])

    for num in input_list[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

    return largest, second_largest

# Khởi tạo list chứa các số cho trước
my_list = [15, 27, 10, 8, 35, 50, 40]

# Tìm hai số lớn nhất trong list
largest_num, second_largest_num = finds(my_list)

print("Hai số lớn nhất trong list là:", largest_num, "và", second_largest_num)

