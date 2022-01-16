class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(Node):
    def __init__(self):
        self.head = None

    def insert(self,data):
        tmp = Node(data)
        if self.head == None:
            self.head = tmp
            return
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = tmp

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    /* Actual Code Below */        
    
    def remove_duplicates(self):

        s = self.head
        d = dict()
        prev = None
        while s :
            if s.data in d.keys():
                prev.next = s.next
                s = None
            else:
                d[s.data] = 1
                prev = s

            s = prev.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(3)
    ll.insert(5)
    ll.insert(7)
    ll.insert(9)
    ll.insert(11)
    ll.insert(1)
    ll.insert(3)
    ll.insert(5)
    ll.insert(7)
    ll.insert(9)

    ll1 = LinkedList()
    ll1.insert(2)
    ll1.insert(4)
    ll1.insert(6)
    ll1.insert(8)
    ll1.insert(10)
    ll1.insert(12)

    print("==========LL===========")
    ll.print_list()
    print("==========LL1===========")
    ll1.print_list()
    print("==========Bef===========")

    #print("==========LL1===========")
    ll.remove_duplicates()
    print("==========After Duplicate Removing===========")
    ll.print_list()
