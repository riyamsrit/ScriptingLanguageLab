from functools import reduce
mylist=[1,2,3,4,5,6]
print("Original List",mylist)

new_list=[x*3 for x in mylist]
print("New List",new_list)

or_sum=reduce(lambda x,y:x+y,mylist)
print("Original Sum",or_sum)

new_sum=reduce(lambda x,y:x+y,new_list)
print("New sum",new_sum)