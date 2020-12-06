class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    #traversal
    def __iter__(self):
        if not self.head:
            return None
        node = self.head
        while node is not None:
            yield node
            node = node.next

    #insertion
    #beginning O(1)
    def add_first(self, node):
        # new_node = Node(data=data)
        node.next = self.head
        self.head = node

    #end O(N)
    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        # for cur_node in self:
        #     pass
        cur_node.next = node

    #middle O(n)
    def add_after(self, target_node_data, node):
        if not self.head:
            raise Exception("List is empty")
        for cur_node in self:
            if cur_node.data == target_node_data:
                node.next = cur_node.next
                cur_node.next = node
                return
        raise Exception(f"Target data {target_node_data} not found in linked list")

    ##DELETION
    def delete_node(self, target_node_data):
        if not self.head:
            raise Exception(f"List is empty")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        raise Exception("Couldn't find given data in the list")

ll = LinkedList(nodes=[1,2,3,4,5,6])
ll.add_first(Node(data="first"))
ll.add_last(Node(data="last"))
ll.add_after(3, Node(data="mid"))
ll.delete_node(3)

print(ll)

for node in ll:
    print(node)