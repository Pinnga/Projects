class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.value = val
            self.nextvalue = None
            self.prevvalue = None

            #Performance Analysis: __init__()
            #This function's performance is constant time: O(1)
            #This is because the function does not contain/require any loops or iterations.


    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__head = None
        self.__tail = None
        self.__size = 0

        #Performance Analysis: __init__()
        #This function's performance is constant time: O(1)
        #This is because the function does not contain/require any loops or iterations.

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size
    
        #Performance Analysis: __len__()
        #This function's performance is constant time: O(1)
        #This is because the function does not contain/require any loops or iterations.
        

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        newest = Linked_List.__Node(val)
        newest.nextvalue = None
        
        if self.__head is None:
            self.__head = newest
            self.__tail = newest
            self.__size = 1
        else:
            cur = self.__tail
            self.__tail.nextvalue = newest
            self.__tail = newest
            newest.prevvalue = cur
            self.__size = self.__size + 1

        #Performance Analysis: append_element
        #This function's performance is constant time: O(1)
        #In our case we have doubly linked lists, thus, the code does not have to iterate through the list, performing at a constant time. 
        

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
    
        if index >= self.__size or index < 0:
            raise IndexError
        new = Linked_List.__Node(val)
        if index == 0:
            new.nextvalue = self.__head
            self.__head.prevvalue = new
            self.__head = new  
        else:
            cur = self.__head
            for i in range(0,index-1):
                cur = cur.nextvalue
            new.nextvalue = cur.nextvalue
            new.prevvalue = cur
            cur.nextvalue = new
            if new.nextvalue != None:
                new.nextvalue.prevvalue = new   
        self.__size = self.__size + 1
    
        #Performance Analysis: insert_element_at()
        #This function's performance is linear time: O(n)
        #The worst case scenario is when one adds an element to the end of the list. This is because it iterates through the entire list until it reaches the last node. Thus, the function's performance is linear time. 




    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if index < 0 or index >= self.__size:
            raise IndexError
        if index == 0:
            r = self.__head
            self.__head = self.__head.nextvalue
            if self.__head != None:
                self.__head.prevvalue = None
        else:
            cur = self.__head
            for i in range(0,index-1):
                cur = cur.nextvalue
            if cur != None and cur.nextvalue != None:
                r = cur.nextvalue
                cur.nextvalue = r.nextvalue
                if r.nextvalue != None:
                    r.nextvalue.prevvalue = cur
        self.__size = self.__size -1
        return r.value
    
        #Performance Analysis: remove_element_at()
        #This function's performance is linear time: O(n)
        #The worst case scenario is when one adds an element to the end of the list. This is because it iterates through the entire list until it reaches the last node. Thus, the function's performance is linear time.


    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index < 0 or index >= self.__size:
            raise IndexError
        cur = self.__head
        for i in range(index):
            cur = cur.nextvalue
        return cur.value
    
        #Performance Analysis: get_element_at()
        #This function's performance is linear time: O(n)
        #The worst case scenario is when one adds an element to the end of the list. This is because it iterates through the entire list until it reaches the last node. Thus, the function's performance is linear time.

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__head is None:
            return
        self.__tail.nextvalue = self.__head
        self.__head.prevvalue = self.__tail
        self.__head = self.__head.nextvalue
        self.__head.prevvalue = None
        self.__tail = self.__tail.nextvalue
        self.__tail.nextvalue = None
        
        #Performance Analysis: rotate_left()
        #This function's performance is constant time: O(1)
        #This is because the function does not contain/require any loops or iterations.


        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation

        if self.__size == 0:
            return '[ ]'
        
        cur = self.__head
        result = '[ '
        while cur != None:
            result = result + str(cur.value) + ', '
            cur = cur.nextvalue
    
        return result[0:-2] + ' ]'
        #Performance Analysis: __str__()
        #This function's performance is linear time: O(n)
        #This is because the function has a loop and it depends on the length of the linked list. 


    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__cur = self.__head
        return self
    
        #Performance Analysis: __iter__()
        #This function's performance is constant time: O(1)
        #This is because the function does not contain/require any loops or iterations and the performance does not depend on the length of the linked list. 
        

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.__cur is None:
            raise StopIteration
        result = self.__cur.value
        self.__cur = self.__cur.nextvalue
        return result
    
        #Performance Analysis: __next__()
        #This function's performance is constant time: O(1)
        #This is because the function does not contain/require any loops or iterations and the performance does not depend on the length of the linked list. 

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        if self.__size == 0:
            return Linked_List()
        rev = Linked_List()
        cur = self.__tail
        while cur:
            rev.append_element(cur.value)
            cur = cur.prevvalue
        return rev

        #Performance Analysis: __reversed__()
        #This function's performance is Linear time: O(n)
        #This is because this function contains a loop and the performance depends on the length of the linked list. 


if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    

    test = Linked_List()

    test.append_element(1)
    print(test)
    print(test.__len__())
    test.append_element(2)
    print(test)
    print(test.__len__())
    #This test case tests if the append_element function and the len function
    #are working properly. The append function successfully adds an element at
    #the new tail position and the len/size increases by 1.

    test.append_element(1)
    print(test.__len__())
    print(test)
    test.insert_element_at(2,0)
    print(test.__len__())
    print(test)
    test.insert_element_at(3,5)
    #This test case tests if the insert_element function works properly.
    #The insert_elemnt function is seems to successfully change the length
    #and correctly modify's the list's structure. Also, when putting an index value
    #that is bigger than the size of the linked list, the program successfully raises
    #an IndexError.

    print(test) #------>in empty list scenario.
    print(test.__len__())
    test.append_element(1)
    print(test)
    print(test.__len__())
    #When appending a value in an empty list, the append function raises
    #the index by 1 and successfully modify's the list's structure.
    

    test.append_element(1)
    print(test)
    print(test.__len__())
    test.remove_element_at(0)
    print(test)
    print(test.__len__())
    test.append_element(1)
    print(test)
    print(test.__len__())
    test.remove_element_at(5)
    #This test case tests if the remove_element function works properly.
    #The function seems to be working correctly. When removing values from the linked list,
    #the index decreases by a size of one and it correctly modifys the list's structure. Also,
    #when putting an index value that is outside of the size of the linked list, the program suc-
    #cessfully raises an IndexError

    print(test) #------>in empty list scenario
    test.remove_element_at(0)
    #When removing a value in an empty list, the function raises an IndexError.
    #this function works properly because there are no values to remove in the list.


    test.append_element(1)
    test.append_element(2)
    test.append_element(3)
    print(test)
    print(test.__len__())
    #This test case tests if the len function is working properly.
    #The len function seems to be working properly. When 3 values were appended to the list,
    #the len function successfully reported 3, which is the number of values stored in the list.

    print(test)#------> in empty list scenario
    print(test.__len__())
    #This test cases tests the len function on an empty list.
    #len works properly with empty lists, for it reports that the size is 0 for an empty list. 

    test.append_element('Data')
    test.append_element('Structures')
    test.append_element('Rocks!')
    print(test)
    #This test case tests if the string representation of the linked lists are correct.
    #The str function seems to be working properly. The function reports with the correct
    #structure of the values, and the order of the values are correct.

    test.append_element(1)
    test.append_element(2)
    test.append_element(3)
    test.append_element(4)
    test.append_element(5)
    for val in test:
        print(val)
    #This test case tests if a for loop visits every value in the list.
    #This test was successfull because the print function printed out the contents of the list
    #with the correct order.

    test.append_element(1)
    test.append_element(2)
    test.append_element(3)
    test.append_element(4)
    test.append_element(5)
    print(test)
    for val in reversed(test):
        print(val)
    #This test case tests if a for loop visits every value in the list that is reversed.
    #this test case was successfull because the print function printed out the contents of the list
    #reversed in the correct order.


    print(test)#------> in empty list scenario
    print(test.__reversed__())
    #This test case tests if reversed works properly for an empty list.
    #the reversed function seems to be working properly because it returns the same
    #empty list. 

    test.append_element(1)
    test.append_element(2)
    test.append_element(3)
    print(test)
    test.rotate_left()
    print(test)
    #This test case tests if the rotate_left fucntion works properly
    #This rotate_left function seems to be working correctly because it reported a linked list
    #with all the values shifting to the left.

    print(test)#------> in empty list scenario
    test.rotate_left()
    print(test)
    #This test case tests if the rotate_left function works properly in an empty list scenario
    #it seems to be working properly because it is returning the same empty list.
    
