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
