from link_list import *

def removeDuplicate(ll):
    if ll.head == None:
        return
    hashing = []
    current = ll.head
    seen = set([current.getData()])
    while current.getNext():
        if current.getNext().getData() in seen:
            current.setNext(current.getNext().getNext())
        else:
            seen.add(current.getNext().getData())
            current = current.getNext()

    return ll

def removeDuplicateNoSpace(ll):
    if ll.head == None:
        return
    current = ll.head
    while current:
        runner = current
        while runner.getNext():
            if runner.getNext().getData() == current.getData():
                runner.setNext(runner.getNext().getNext())
            else:
                runner = runner.getNext()
        current = current.getNext()
    return ll.head

ll = UnorderedList()
ll.add(2)
ll.add(1)
ll.add(3)
ll.add(1)
ll.add(4)
ll.add(2)
print(ll)
removeDuplicate(ll)
print(ll)
ll.add(4)
ll.add(3)
ll.add(5)
ll.add(6)
ll.add(7)
print(ll)
removeDuplicateNoSpace(ll)
print(ll)
