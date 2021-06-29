# Implementation of linked list
# ("1- INSERT ELEMENT AT BEGINNING")
# ("2- INSERT ELEMENT AT END")
# ("3- INSERT ELEMENT AT A PARTICULAR POSITION")
# ("4- INSERT ELEMENT AT CENTER")
# ("5- BULK INSERTION OF ELEMENT")
# ("6- DELETE ELEMENT FROM BEGINNING")
# ("7- DELETE ELEMENT FROM END")
# ("8- DELETE ELEMENT FROM A PARTICULAR POSITION")
# ("9- DELETE ELEMENT FROM CENTER")
# ("10- DELETE ALL ELEMENTS")
# ("11- SEARCH AN ELEMENT")
# ("12- TRAVERSAL IN LIST")
# ("13- COUNT NUMBER OF NODES IN LIST")

class LinkedList:
    head = None

    class Node:
        data = None
        next = None

    # ("1- INSERT ELEMENT AT BEGINNING")
    def insert_begin(self,value):
        node = self.Node()
        node.data = value
        node.next = None
        if (self.head == None):
            self.head = node
        else:
            node.next = self.head
            self.head = node

    # ("2- INSERT ELEMENT AT END")
    def insert_end(self,value):
        node=self.Node()
        node.data=value
        node.next=None
        if (self.head==None):
            self.head=node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node

    # ("3- INSERT ELEMENT AT A PARTICULAR POSITION")
    def insert_pos(self,value,position):
        node = self.Node()
        node.data = value
        node.next = None
        if self.head==None:
            self.head=node
        else:
            count = 0
            temp = self.head
            while temp != None:
                count = count + 1
                temp = temp.next
            n = count+1
            if position<=n:
                if position==1:
                    self.insert_begin(value)
                elif position==count+1:
                    self.insert_end(value)
                else:
                    temp = self.head
                    for i in range(0, position - 2):
                        temp = temp.next
                    temp1 = temp.next
                    temp.next = node
                    node.next = temp1
            else:
                print("Invalid position entered")

    # ("4- INSERT ELEMENT AT CENTER")
    def insert_mid(self,value):
        node = self.Node()
        node.data = value
        node.next = None
        if self.head == None:
            self.head = node
        else:
            count = 0
            temp = self.head
            while temp.next != None:
                count = count + 1
                temp = temp.next
            n = int(count / 2)
            temp = self.head
            for i in range(0, n - 1):
                temp = temp.next
            temp1 = temp.next
            temp.next = node
            node.next = temp1

    # ("5- BULK INSERTION OF ELEMENT")
    def bulk_insertion(self):
        arr = [1, 2, 3, 4]
        for i in range(len(arr)):
            node = self.Node()
            node.data = arr[i]
            node.next = None
            if self.head == None:
                self.head = node
            else:
                temp = self.head
                while (temp.next != None):
                    temp = temp.next
                temp.next = node

    # ("6- DELETE ELEMENT FROM BEGINNING")
    def delete_begin(self):
        if self.head == None:
            print("List is empty")
        else:
            self.head = self.head.next

    # ("7- DELETE ELEMENT FROM END")
    def delete_end(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None

    # ("8- DELETE ELEMENT FROM A PARTICULAR POSITION")
    def delete_pos(self,position):
        if self.head==None:
            print("List is empty")
        else:
            count = 0
            temp = self.head
            while temp != None:
                count = count + 1
                temp = temp.next
            if position<=count:
                if position==1:
                    self.delete_begin()
                elif position==count:
                    self.delete_end()
                else:
                    temp = self.head
                    for i in range(0, position - 2):
                        temp = temp.next
                    temp1 = temp.next
                    temp.next = temp1.next
            else:
                print("Invalid position entered")

    # ("9- DELETE ELEMENT FROM CENTER")
    def delete_center(self):
        if self.head == None:
            print("List is empty")
        else:
            count = 0
            temp = self.head
            while temp.next != None:
                count = count + 1
                temp = temp.next
            n = int(count / 2)
            temp = self.head
            for i in range(0, n - 1):
                temp = temp.next
            temp1 = temp.next
            temp.next = temp1.next

    # ("10- DELETE ALL ELEMENTS")
    def delete_all(self):
        if self.head == None:
            print("List is empty")
        else:
            self.head = None

    # ("11- SEARCH AN ELEMENT")
    def search_element(self, value):
        if self.head==None:
            print("List is empty")
        else:
            flag=0
            temp=self.head
            while temp!=None:
                if temp.data==value:
                    print("Element Found")
                    flag=1
                temp=temp.next
            if flag==0:
                print("Element not found")

    # ("12- TRAVERSAL IN LIST")
    def traversal(self):
        if (self.head == None):
            print("List is empty")
        else:
            temp = self.head
            while (temp!=None):
                print(temp.data, end=' ')
                temp = temp.next

    # ("13- COUNT NUMBER OF NODES IN LIST")
    def node_count(self):
        count = 0
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp != None:
                count = count + 1
                temp = temp.next
            print("Number of nodes :", count)

    # This function helps in execution of the other functions (that perform various Linkedlist operations)
    def perform(self):
        print("1- INSERT ELEMENT AT BEGINNING")
        print("2- INSERT ELEMENT AT END")
        print("3- INSERT ELEMENT AT A PARTICULAR POSITION")
        print("4- INSERT ELEMENT AT CENTER")
        print("5- BULK INSERTION OF ELEMENT")
        print("6- DELETE ELEMENT FROM BEGINNING")
        print("7- DELETE ELEMENT FROM END")
        print("8- DELETE ELEMENT FROM A PARTICULAR POSITION")
        print("9- DELETE ELEMENT FROM CENTER")
        print("10- DELETE ALL ELEMENTS")
        print("11- SEARCH AN ELEMENT")
        print("12- TRAVERSAL IN LIST")
        print("13- COUNT NUMBER OF NODES IN LIST")
        print("14- EXIT")
        flag=1
        while(flag):
            ch = int(input("Enter the choice of operation : "))
            if ch == 1:
                val=int(input("Enter the element to insert : "))
                self.insert_begin(val)
                flag = 1
            elif ch == 2:
                val = int(input("Enter the element to insert : "))
                self.insert_end(val)
                flag = 1
            elif ch == 3:
                val = int(input("Enter the element to insert : "))
                position = int(input("Enter the position to insert element : "))
                self.insert_pos(val,position)
                flag = 1
            elif ch == 4:
                val = int(input("Enter the element to insert : "))
                self.insert_mid(val)
                flag = 1
            elif ch==5:
                self.bulk_insertion()
            elif ch == 6:
                self.delete_begin()
                flag = 1
            elif ch == 7:
                self.delete_end()
                flag = 1
            elif ch == 8:
                position=int(input("Enter the position to delete element : "))
                self.delete_pos(position)
                flag = 1
            elif ch == 9:
                self.delete_center()
                flag = 1
            elif ch == 10:
                self.delete_all()
                flag = 1
            elif ch == 11:
                val = int(input("Enter the value of element to search : "))
                self.search_element(val)
                flag = 1
            elif ch == 12:
                print("The list is : ",end="")
                self.traversal()
                print()
                flag = 1
            elif ch == 13:
                print("Total number of nodes in list : ",end="")
                self.node_count()
                print()
                flag = 1
            elif ch == 13:
                print("Quiting as per your wish !")
                exit()
            else:
                print("Wrong choice of operation")
                flag=1

# Creating class object
obj = LinkedList()
obj.perform()