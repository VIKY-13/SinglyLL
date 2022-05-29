class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head = None
    def AddBegin(self,data):
        newnode=node(data)
        newnode.ref=self.head
        self.head=newnode
    def AddEnd(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = newnode
    def AddAfter(self,data,x):
        n=self.head
        while n is not None:
            if n.data == x:
                break
            else:
                n = n.ref
            if n is None:
                print("Not found")
            else:
                newnode = node(data)
                newnode.ref = n.ref
                n.ref = newnode
    def AddBefore(self,data,x):
        if self.head is None:
            print("empty")
        if self.head.data==x:
            newnode=node(data)
            newnode.ref=self.head
            self.head=newnode
            return
        n=self.head
        while n is not None:
            if n.ref.data==x:
                break
            else:
                n=n.ref
        if n.ref is None:
            print("not founnd")
        else:
            newnode=node(data)
            newnode.ref=n.ref
            n.ref=newnode

    def printLL (self):
        if self.head == None:
            print("inked list is empty!")
        else:
            n = self.head
            while n!=None:
                print(n.data ,"-->",end=' ')
                n=n.ref
    def InsertIfEmpty(self,data):
        if self.head is None:
            newnode = node(data)
            self.head = newnode
        else:
            print("its not empty")
    def DeleteBegin(self):
        if self.head is None:
            print("empty")
        else:
            self.head=self.head.ref
    def DeleteEnd(self):
        if self.head is None:
            print("empty")
        elif self.head.ref is None:
            self.head=None
        else:
            n = self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def DeleteNode(self,x):
        if self.head is None:
            print("emptty")
            return
        if x==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("not found")
        else:
            n.ref=n.ref.ref
ll=LinkedList()
ll.AddBegin(10)
ll.AddEnd(100)
ll.AddAfter(300,100)
ll.AddEnd(200)
ll.AddBegin(11)
ll.AddBefore(3,11)
ll.DeleteEnd()
ll.DeleteBegin()
ll.DeleteBegin()
ll.DeleteNode(100)
ll.printLL()