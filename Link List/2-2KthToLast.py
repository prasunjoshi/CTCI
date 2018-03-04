from link_list import *

def kthToLastRecursive(root,k,index):
    if root:
        if index >=k:
            print(root.getData())
        index += 1
        kthToLast(root.getNext(),k,index)
    else:
        return

def kthToLastIterative(ll,k):
    current = runner = ll.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.getNext()
    while runner:
        current = current.getNext()
        runner = runner.getNext()
    return current

ll = UnorderedList()
ll.add(10)
ll.add(20)
ll.add(15)
ll.add(25)
ll.add(30)
ll.add(11)
ll.add(43)
ll.head = kthToLastIterative(ll,4)
print(ll)
