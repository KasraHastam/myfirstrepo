list = [3,1,4,1,5]
list.append(9)
list.extend([2,6])
list.remove(1)
list.pop(2)
list[1]=100
list.sort()
print('tamrin 1: ',list)

list2 = [10,20,30,40,50,60,70]
extract = list2[1:5]
print('tamrin 2: ',extract)
even_index = list2[0::2]
print(even_index)
reversed_list2 = list2[::-1]
print(reversed_list2)
last_three = list2[-3:]
print(last_three)

import copy

originial = [[1,2],[3,4]]
