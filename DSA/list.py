#ListList
# create, append, insert, remove, pop, slice, reverse, sort, sort with key, len, count, index, extend, clear, copy, check membership, list comprehension, merge two lists




#-------------------------------------------- create List ----------------------------------------------------------------------- 
empty_List = []
print(empty_List)

conversion_to_list = list()
print(conversion_to_list)

filled_list = [1,2,3,4,5]
print(filled_list)

list_from_touples_list = list((1,2,3,4))
print(list_from_touples_list)

list_of_letters_in_string = list("abcd")
print(list_of_letters_in_string)

repeated_value_list = [0] * 5
print(repeated_value_list)

list_comprehention = [x ** 2 for x in range(5)]
print(list_comprehention)


#----------------------------------------------- append -------------------------------------------------------


dummy_list = [1,3,5,8,2,4,10,9]

dummy_list.append(7)
print(dummy_list)

dummy_list.insert(1,11)
print(dummy_list)

dummy_list.extend(filled_list)
print(dummy_list)

dummy_list += list_comprehention
print(dummy_list)

dummy = dummy_list + list_comprehention
print(dummy)

#-------------------------------------- insert ------------------------------------------------------

list_for_insert = [1,2,3,4,5,6,7,8,9,10]

list_for_insert.insert(0,11)
print(list_for_insert)

list_for_insert.insert(5,100)
print(list_for_insert)

list_for_insert.insert(len(list_for_insert),500)
print(list_for_insert)

i = 10
list_for_insert.insert(i,250)
print(list_for_insert)




#------------------------------------- remove --------------------------------------------------------

list_for_remove = [1,2,3,4,5,6,7,8,9,10]
print(list_for_remove)

list_for_remove.remove(1)
print(list_for_remove)

list_for_remove.pop(1)
print(list_for_remove)

del list_for_remove[5:]
print(list_for_remove)






























