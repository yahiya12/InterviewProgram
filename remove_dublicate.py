final_list=[1,2,3,1,4,5,4]
print(final_list)
arr=[]
for i in final_list:
    if i not in arr:
        arr.append(i)
print(arr)


