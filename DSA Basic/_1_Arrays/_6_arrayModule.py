import array as arr
#lst=[1.1,2.2,3.3,4.4]
# you can only add homogenous datatype
#data = arr.array('d',lst)
#print(data)

data = arr.array('i',[-1,7,1,2,4])
print(data)

data.append(7)
print(data)

data.pop()
print(data)

data.extend([5,2,1,4])
print(data)
