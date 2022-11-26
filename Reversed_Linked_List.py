class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        temp = self.head
        while temp:
            if temp.next is None:
                temp.next = Node(data, None)
                return
            temp = temp.next

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def print_list(self):
        ls = ''
        temp = self.head
        while temp:
            ls += str(temp.data) + " "
            temp = temp.next
        #print(ls)
        return  ls
    def get_length(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 0
        while temp:
            count +=1
            temp = temp.next
        return count


    def reverse_list(self):
        if self.head is None:
            return
        temp = self.head
        newlist = LinkedList()
        v = ''
        while temp:
            if temp.data % 2 == 0:
                newlist.insert_at_start(temp.data)
            else:
                v += newlist.print_list() + str(temp.data)+" "
                newlist = LinkedList()
            temp = temp.next
        print(v+newlist.print_list())




if __name__ == '__main__':
    ll = LinkedList()
    N = int(input())
    lists = list(map(int, input().split()))[:N]
    ll.insert_values(lists)
    ll.reverse_list()