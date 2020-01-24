def bubbleSort(mylist):
    for passnum in range(len(mylist)-1,0,-1):
        for i in range(passnum):
            if mylist[i]>mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp

mylist = [16,8,20,10,9,15]
bubbleSort(mylist)
print(mylist) 
print("what is the next number in the sequence?")
