word_list = ['hello','world','my','name','is','Anna']
letter = "o"
newString=[]
def findChar(arr):
    for i in arr: 
        if letter in str(i):
            newString.append(i)
    print "NewString : ", newString

findChar(word_list)

