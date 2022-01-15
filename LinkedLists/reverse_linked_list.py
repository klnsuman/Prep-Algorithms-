class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(Node):
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode = Node(data)
        if self.head==None:
            self.head = newNode
            return

        curNode = self.head
        while curNode.next:
            curNode = curNode.next

        curNode.next = newNode

    def print_list(self):
        curNode = self.head
        while curNode:

            print(curNode.data)
            curNode = curNode.next


    def rev_list(self):
        cur = self.head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.print_list()
    print("===============")
    ll.rev_list()
    print("==After Reversal =====")
    ll.print_list()

