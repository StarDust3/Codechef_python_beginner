##EXAMPLE FOR REDUCE FUNCTION##
#The reduce() function in Python takes in a function and a list as argument. The function is called with a lambda function and a list and a new reduced result is returned. This performs a repetitive operation over the pairs of the list.#
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x,y: x+y),li)
print(sum)

##EXAMPLE FOR MAP FUNTION##
#The map() function in Python takes in a function and a list as argument. The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items returned by that function for each item.#
lis = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2, lis))
print(final_list)

##EXAMPLE FOR FILTER FUNCTION##
#The filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True. #
fin_list = list(filter(lambda x: (x%2 !=0), lis))
print(fin_list)





