class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self,data):
        self.data = data
    
    def setNext(self,newNext):
        self.next = newNext

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

#overriding string to print linked list
    def __str__(self):
        node_str = ""
        current_node = self.head
        while current_node:
            if current_node.getNext():
                node_str = node_str + str(current_node.getData()) + ", "
            else:
                node_str = node_str + str(current_node.getData())

            current_node = current_node.getNext()

        return node_str

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count


    def search(self,item):
        current = self.head
        while current or current.getData() != item:
            current = current.getNext()
        return current

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

#ll = UnorderedList()
#ll.add(20)
#ll.add(30)
#ll.add(40)
#print(ll)
