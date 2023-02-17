def find_value(arr,val):
    loc=0
    for i in arr:
        if i==val:
            return f"Value found in {loc} Index"
        loc+=1
    return "Value not found"

a=[1,2,3,4,5,6]
print(a)
print(find_value(a,11))

