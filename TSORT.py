lst = []
n = int(input("Enter number of elements : ")) 

for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele)
lst.sort()
#print(lst)

for x in range(len(lst)): 
    print(lst[x])

