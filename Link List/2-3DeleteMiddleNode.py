from link_list import *

def deleteMiddleNode(node):
    node.setData(node.getNext().getData())
    node.setNext(node.getNext().getNext())

ll = UnorderedList()
ll.add(10)
ll.add(20)
ll.add(15)
ll.add(90)
ll.add(11)
print(ll)
deleteMiddleNode(ll.head.getNext().getNext().getNext())
print(ll)
