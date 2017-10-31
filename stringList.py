words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
print words.replace('day','month',)
print words

posday = words.find('day')
print posday 
#str.replace(old, new[, max])
print words.replace("day", "month", 1)
print posday 
#will replace day with month upto 2 occurance
print words.replace("day", "month", 2)
print posday 

x = [2,54,-2,7,12,98]
print "Max value element : ", max(x)
print "Max value element : ", min(x)
'''
First and Last
Print the first and last values in a list like this 
one: x = ["hello",2,54,-2,7,12,98,"world"].
Now create a new list containing only the first and last values in the original list. 
Your code should work for any list.
'''
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]

y = [19,2,54,-2,7,12,98,32,10,-3,6]
y.sort()
print y

#len gives length of a an array
z= len(y)
print z
#s
print y[0:5]
#  print firsthalf
newArray = [y[0:5]]
print newArray
secondArray = y[6:10]
print secondArray
# newArray.append(secondArray) 
newArray = newArray + secondArray
print "result"
print newArray 

 The starting index and ending index should be separated by the ":"character.
x = [99,4,2,5,-3]
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];

first_list = x[:len(x)/2] # optional first parameter of slice defaults to zero
second_list = x[len(x)/2:] # optional second parameter of slice defaults to the list's length
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list

