class node:
    def __init__(self,data,link = None):
        self.data = data # element
        self.link = link # memory location

class linkedlist:
    def __init__(self,head=None):
        self.head = head
        
    def append(self,data):
        new_node = node(data,self.head) # data - 10 , None - link
        self.head = new_node

    def display(self):
        itr = self.head
        while itr:
            print(itr.data,end=" ")   
            itr = itr.link 
if __name__ == "__main__":
    obj = linkedlist()
    obj.append(10)
    obj.append(20)
    obj.display()
