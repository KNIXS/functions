def Add(a,b): #fuction definition with parameters
    print(f"{a} + {b} = {a+b}")

#Add(200, 300) #calling function with arguments
#Add(1200, 300) #calling function with arguments
numList1 = [120, 230, 45, 20]
numList2 = [23.90, 45.90, 34.90, 89]
for i in range(0, len(numList1)):
    #print(numList1[i], numList2[i])
    Add(numList1[i], numList2[i])