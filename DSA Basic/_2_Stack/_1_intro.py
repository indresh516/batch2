class array:
    def __init__(self,fix_size):
        self.fix_size=fix_size
        self.length=0
        self.data=[]

    def add(self, element):
        if self.length<self.fix_size:
            self.data.append(element)
            