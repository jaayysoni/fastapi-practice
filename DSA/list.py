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

print("create List ends here")
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

print("append ends here")
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

print("insert ends here")


#------------------------------------- remove --------------------------------------------------------

list_for_remove = [1,2,3,4,5,6,7,8,9,10]
print(list_for_remove)

list_for_remove.remove(1)
print(list_for_remove)

list_for_remove.pop(1)
print(list_for_remove)

del list_for_remove[5:]
print(list_for_remove)

print("Remove till here")
#------------------------------------- pop ------------------------------------------------------------

list_for_pop = [1,2,3,4,5,6,7,8,9]

removed = list_for_pop.pop()
print(removed)
print(list_for_pop)

list_for_pop.pop(5)
print(list_for_pop)

list_for_pop.pop(-2)
print(list_for_pop)

list_for_pop.pop(0)
print(list_for_pop)

print("pop ends here")

#------------------------------------ Slice ------------------------------------------------------------

list_to_slice = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
copy = list_to_slice[:]
print(copy)

first_three = list_to_slice[:3]
print(first_three[:3])

print(list_to_slice[5:])

print(list_to_slice[3:7])

print(list_to_slice[::2])

print(list_to_slice[::-1])

print(list_to_slice[-3:])

print(list_to_slice[5:10:3])

print("slice ends here")

#------------------------------------------- reverse --------------------------------------------------

list_to_reverse = [10,9,8,7,6,5,4,3,2,1]

# reverse() mutates the list in place
list_to_reverse.reverse()
print(list_to_reverse)

# slicing with [::-1] returns a new reversed list, original unchanged
reversed_copy = list_to_reverse[::-1]
print(reversed_copy)

print("reverse ends here")

#------------------------------------------- sort -----------------------------------------------------

list_to_sort = [5, 2, 9, 1, 7, 3, 8, 4, 6]

# sort() mutates in place, ascending by default
list_to_sort.sort()
print(list_to_sort)

# reverse=True sorts descending in place
list_to_sort.sort(reverse=True)
print(list_to_sort)

# sorted() returns a new list, original stays unchanged
original = [5, 2, 9, 1, 7, 3, 8, 4, 6]
new_sorted = sorted(original)
print(original)
print(new_sorted)

print("sort ends here")

#------------------------------------------- sort with key --------------------------------------------

# sort by absolute value using abs as key
mixed = [-10, 3, -1, 7, -5, 2]
mixed.sort(key=abs)
print(mixed)

# sort strings by their length
words = ["banana", "fig", "apple", "kiwi", "date"]
words.sort(key=len)
print(words)

# sort strings by length descending
words.sort(key=len, reverse=True)
print(words)

# sort list of dicts by a specific field using lambda
students = [
    {"name": "Jay", "marks": 88},
    {"name": "Aman", "marks": 72},
    {"name": "Priya", "marks": 95},
]
students.sort(key=lambda s: s["marks"])
print(students)

# sorted() with key returns a new list, original unchanged
top_students = sorted(students, key=lambda s: s["marks"], reverse=True)
print(top_students)

print("sort with key ends here")

#------------------------------------------- len ------------------------------------------------------

nums = [10, 20, 30, 40, 50]

# len() returns total number of elements
print(len(nums))

# useful to get last index
print(nums[len(nums) - 1])

# len on nested list counts outer elements only
nested = [[1, 2], [3, 4], [5, 6]]
print(len(nested))

print("len ends here")

#------------------------------------------- count ----------------------------------------------------

count_list = [1, 2, 3, 2, 4, 2, 5, 1]

# count() returns how many times a value appears
print(count_list.count(2))

# count a value that appears once
print(count_list.count(1))

# count a value not in list returns 0
print(count_list.count(99))

print("count ends here")

#------------------------------------------- index ----------------------------------------------------

index_list = [10, 20, 30, 40, 50, 30]

# index() returns position of first occurrence
print(index_list.index(30))

# search within a specific range index(value, start, end)
print(index_list.index(30, 3))

# index of first element
print(index_list.index(10))

print("index ends here")

#------------------------------------------- extend ---------------------------------------------------

base = [1, 2, 3]
extra = [4, 5, 6]

# extend() adds all elements of another iterable to the list in place
base.extend(extra)
print(base)

# extend with a tuple
base.extend((7, 8, 9))
print(base)

# extend with a string adds each character
chars = ['a', 'b']
chars.extend("cd")
print(chars)

print("extend ends here")

#------------------------------------------- clear ----------------------------------------------------

list_to_clear = [1, 2, 3, 4, 5]
print(list_to_clear)

# clear() removes all elements, list still exists as empty
list_to_clear.clear()
print(list_to_clear)

print("clear ends here")

#------------------------------------------- copy -----------------------------------------------------

original_list = [1, 2, 3, 4, 5]

# copy() creates a shallow copy, changes to copy won't affect original
shallow_copy = original_list.copy()
shallow_copy.append(99)
print(original_list)
print(shallow_copy)

# slice copy does the same thing
slice_copy = original_list[:]
slice_copy.append(100)
print(original_list)
print(slice_copy)

print("copy ends here")

#------------------------------------------- check membership -----------------------------------------

membership_list = [1, 2, 3, 4, 5]

# in operator returns True if element exists
print(3 in membership_list)

# not in returns True if element does not exist
print(10 not in membership_list)

# use in inside an if condition
if 4 in membership_list:
    print("4 is present")

print("check membership ends here")

#------------------------------------------- list comprehension ---------------------------------------

# basic comprehension: squares of 0 to 4
squares = [x ** 2 for x in range(5)]
print(squares)

# comprehension with condition: even numbers only
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# transform strings to uppercase
names = ["jay", "aman", "priya"]
upper_names = [name.upper() for name in names]
print(upper_names)

# nested comprehension: flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)

print("list comprehension ends here")

#------------------------------------------- merge two lists ------------------------------------------

list_a = [1, 2, 3]
list_b = [4, 5, 6]

# using + operator creates a new merged list
merged = list_a + list_b
print(merged)

# using extend() merges in place into list_a
list_a.extend(list_b)
print(list_a)

# using unpacking to merge multiple lists
list_c = [7, 8, 9]
merged_all = [*list_a, *list_b, *list_c]
print(merged_all)

print("merge two lists ends here")