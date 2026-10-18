"""que : find unique even numbers from a given list
l1 = [22,43,21,45,45,43,2,3,4,5,6,7,2,3,4,5,6,7]"""

l1 = [22, 43, 21, 45, 45, 43, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7]

l1 = [22,43,21,45,45,43,2,3,4,5,6,7,2,3,4,5,6,7] 
results =[]
for i in l1:
    if i % 2 == 0:
        results.append(i)
#         print(results)
# print(results)
final_results = tuple(set(results))
print(final_results)
print(type(final_results))
      
