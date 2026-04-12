# A linked list is a chain of nodes. Each node holds data + a pointer to the next node.
# Unlike a list/array, nodes are NOT stored in contiguous memory — they are linked via pointers.
#
# Structure:
#   [data | next] -> [data | next] -> [data | next] -> None
#   head                                               tail


# ── Node ──────────────────────────────────────────────────────────────────────

class Node:
    # A single box in the chain
    def __init__(self, data):
        self.data = data   # the value stored in this node
        self.next = None   # pointer to the next node (None = no next node yet)


# ── LinkedList ────────────────────────────────────────────────────────────────

class LinkedList:
    def __init__(self):
        self.head = None   # empty list — no first node yet

    # ── append ────────────────────────────────────────────────────────────────
    def append(self, data):
        # Add a new node at the END of the list
        new_node = Node(data)

        if self.head is None:          # list is empty → new node becomes head
            self.head = new_node
            return

        current = self.head            # start from the beginning
        while current.next:            # walk until the last node (next is None)
            current = current.next
        current.next = new_node        # attach new node after the last node

    # ── prepend ───────────────────────────────────────────────────────────────
    def prepend(self, data):
        # Add a new node at the BEGINNING — O(1), no traversal needed
        new_node = Node(data)
        new_node.next = self.head      # new node points to the old head
        self.head = new_node           # new node is now the head

    # ── delete ────────────────────────────────────────────────────────────────
    def delete(self, data):
        # Remove the FIRST node that contains this data
        if self.head is None:          # nothing to delete
            return

        if self.head.data == data:     # target is the head itself
            self.head = self.head.next # move head forward (old head is dropped)
            return

        current = self.head
        while current.next:                        # walk until second-to-last
            if current.next.data == data:          # next node is the target
                current.next = current.next.next   # skip over the target node
                return
            current = current.next

    # ── search ────────────────────────────────────────────────────────────────
    def search(self, data):
        # Return True if data exists in the list, else False
        current = self.head
        while current:                 # walk every node
            if current.data == data:
                return True
            current = current.next
        return False

    # ── reverse ───────────────────────────────────────────────────────────────
    def reverse(self):
        # Flip all the next pointers so the list walks in the opposite direction
        prev = None
        current = self.head
        while current:
            next_node = current.next   # save the next node before we overwrite it
            current.next = prev        # flip: point current node BACK to previous
            prev = current             # move prev one step forward
            current = next_node        # move current one step forward
        self.head = prev               # prev is now the new head (old tail)

    # ── display ───────────────────────────────────────────────────────────────
    def display(self):
        # Print the list as:  1 -> 2 -> 3 -> None
        current = self.head
        parts = []
        while current:
            parts.append(str(current.data))
            current = current.next
        print(" -> ".join(parts) + " -> None")


# ── Quick demo ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()          # 1 -> 2 -> 3 -> None

    ll.prepend(0)
    ll.display()          # 0 -> 1 -> 2 -> 3 -> None

    ll.delete(2)
    ll.display()          # 0 -> 1 -> 3 -> None

    print(ll.search(3))   # True
    print(ll.search(9))   # False

    ll.reverse()
    ll.display()          # 3 -> 1 -> 0 -> None
