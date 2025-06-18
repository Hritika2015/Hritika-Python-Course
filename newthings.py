import array as arr
array_num = arr.array('i', [5, 5, 5, 5, 5, 5, 5])
print("Nummber of occurences of the number 5 said in the array: "+str(array_num.count(5)))
array_num.reverse()
print("Reverse order of items:")
print(str(array_num))
