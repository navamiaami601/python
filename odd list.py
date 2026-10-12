list=[1,3,5,7,2]
print(f"original list:{list}")
list2={x for x in list if x%2 !=0}
print(f"list of odd numbers:{list2}")
