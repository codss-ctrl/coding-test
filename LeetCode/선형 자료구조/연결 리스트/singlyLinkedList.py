# Create Nodes
# Create Linked List
# Add nodes to linked list
# print linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insert(self, newNode):
        # head => John => None
        if self.head is None:
            self.head = newNode

        else:
            # head=>John=>Ben=>None || John -> Matthew
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertHead(self, newNode):
        # data = Matthew, next => None
        # head -> Matthew -> John -> Ben

        temporaryNode = self.head  # John
        self.head = newNode  # Matthew
        self.head.next = temporaryNode
        del temporaryNode

    def insertAt(self, newNode, position):
        # head -> John -> Ben -> None || newNode => Matthew || position => 1
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head  # John, Ben
        currentPosition = 0  # 0, 1

        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return

        while True:
            if currentPosition == position:
                prevNode.next = newNode
                newNode.next = currentNode
                break
            prevNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def deleteHead(self):
        if self.isListEmpty() is False:
            prevNode = self.head
            self.head = self.head.next
            prevNode.next = None
        else:
            print("Linked list is empty. Delete failed")

    def deleteAt(self, position):
        # head -> John -> Ben -> Matthew -> None || position => 1
        if position < 0 or position >= self.listLength():
            print("Invalid Position")
            return
        if self.isListEmpty() is False:
            if position == 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0

            while True:
                if currentPosition == position:
                    prevNode.next = currentNode.next
                    currentNode.next = None
                    break
                prevNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

    def deleteEnd(self):
        # head -> John -> Ben -> Matthew -> None
        lastNode = self.head
        while lastNode.next is not None:
            prevNode = lastNode
            lastNode = lastNode.next
        prevNode.next = None

    def printList(self):
        # head=>John->Ben->Matthew
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


# Node => data, next
# firstNode.data => John, firstNode.next => None
firstNode = Node("John")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Matthew")
linkedList.insertAt(thirdNode, 2)
linkedList.deleteAt(1)
linkedList.printList()
