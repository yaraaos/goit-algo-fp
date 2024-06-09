class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Створення списку: 1 -> 2 -> 3 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Реверсування списку
new_head = reverse_list(head)

# Виведення реверсованого списку: 3 -> 2 -> 1 -> None
current = new_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")