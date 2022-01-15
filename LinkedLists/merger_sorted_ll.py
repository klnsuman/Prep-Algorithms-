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

  

    def merge_sorted_lst(self,ll1):

        p = self.head
        q = ll1.head

        s = None

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q

        if not q:
            s.next = p

        self.head = new_head
        return self.head


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(3)
    ll.insert(5)
    ll.insert(7)
    ll.insert(9)
    ll.insert(11)

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

    #ll.merge_ll(ll,ll1)
    #s.print_list()
    ll.merge_sorted_lst(ll1)
    print("==========After Merge===========")
    ll.print_list()

    ll_1 = LinkedList()
    ll_1.insert(1)
    ll_1.insert(3)
    ll_1.insert(4)
    ll_1.insert(5)


    ll_2 = LinkedList()

    ll_2.insert(2)

    ll_1.merge_sorted_lst(ll_2)
    print("==========After 2nd Merge===========")
    ll_1.print_list()
