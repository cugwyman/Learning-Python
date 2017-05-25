list = [int(x) for x in raw_input().split(' ')]
list1 = []#You can't use "list1 = list2 = list3 = []" here!!!
list2 = []
list3 = []
list_sorted = []
num_list1 = num_list2 = num_list3 = 0
'''for x in list:
    if (list.index(x)+1) % 3 != 0 and (list.index(x)+1) % 2 == 0:
        list1.append(x)
    elif (list.index(x)+1) % 3 == 0:
        list2.append(x)
    else:
        list3.append(x)'''
for x in range(len(list)):
    if (x+1) % 3 != 0 and (x+1) % 2 == 0:
        list1.append(list[x])
    elif (x+1) % 3 == 0:
        list2.append(list[x])
    else:
        list3.append(list[x])
list1 = sorted(list1)
list2 = sorted(list2, reverse = True)
'''for x in list:
    if (list.index(x)+1) % 3 != 0 and (list.index(x)+1) % 2 == 0:
        list_sorted.append(list1[num_list1])
        num_list1 = num_list1 + 1
    elif (list.index(x)+1) % 3 == 0:
        list_sorted.append(list2[num_list2])
        num_list2 = num_list2 + 1
    else:
        list_sorted.append(list3[num_list3])
        num_list3 = num_list3 + 1'''
for x in range(len(list)):
    if (x+1) % 3 != 0 and (x+1) % 2 == 0:
        list_sorted.append(list1[num_list1])
        num_list1 = num_list1 + 1
    elif (x+1) % 3 == 0:
        list_sorted.append(list2[num_list2])
        num_list2 = num_list2 + 1
    else:
        list_sorted.append(list3[num_list3])
        num_list3 = num_list3 + 1
print ' '.join(str(x) for x in list_sorted)
