from collections import deque

class queue:
    def __init__(self):
        self.data = deque()

    def add(self,element):
        self.data.append(element)

    def pop(self):
        self.data.popleft()

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def delete(self):
        del self.data

        
        
        
queue_obj = queue()

#for i in range(2):
#    client={}
#    client['TokenNo']=input("Enter the token No : ")
#    client['Name']=input("Enter the Name : ")
#    client['Dtype']=input("Enter the Dtype : ")
#    queue_obj.add(client)

queue_obj.add(20)
queue_obj.add(30)
print(queue_obj.data)
queue_obj.pop()
#queue_obj.pop()
#queue_obj.pop()
print(type(queue_obj.data))
#print(queue_obj.is_empty())


# print(queue_obj.data)

# print(queue_obj.is_empty())

# print(queue_obj.size())


#size = int(input("Enter the size : "))
#for i in range(size):
#    element = int(input("Enter the element : "))
#    queue_obj.add(element)

#print(queue_obj.data)