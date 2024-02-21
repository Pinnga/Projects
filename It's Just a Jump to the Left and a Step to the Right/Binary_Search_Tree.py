class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.


    #Performance Analysis: __init__(self,value):
    #Performance: O(1)
    #This function does not perform any operations that depend on the size of the tree
    #Thus, the performance is constant. 

    def __init__(self, value):
      self.value = value
      self.Lchild = None
      self.Rchild = None
      self.size = 1
      # TODO complete Node initialization
    

    #Performance Analysis: Update_size(self):
    #Performance: O(1)
    #This function just updates the size attribute of a node and performs a constant number of 
    #updates regardless of the size of the tree.

    def Update_size(self):
      max = 0
      if self.Lchild != None:
        max = self.Lchild.size
      if self.Rchild != None and max < self.Rchild.size:
        max = self.Rchild.size
      self.size = max + 1


  #Performance Analysis: __init__(self):
  #Performance: O(1)
  #Performs in constant time regardless the size of the tree.
  def __init__(self):
    self.__root = None
    # TODO complete initialization




  #Performance Analysis: insert_element(self,value)
  #Performance: O(logn)
  #The performance of this function is O(logn) because when inserting a value,
  #Because the tree is already sorted, the time complexity decreases each time the 
  #recursion happens.
  def insert_element(self, value):
    self.__root = self.__recursive_IE(value,self.__root)

    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    pass # TODO replace pass with your implementation



  #Performance Analysis:__recursive_IE(self,value,node)
  #Performance: O(logn)
  #The performance of this function is O(logn) because when inserting a value,
  #Because the tree is already sorted, the time complexity decreases each time the 
  #recursion happens.

  def __recursive_IE(self, value, node):
    if node == None:
      New_tree = Binary_Search_Tree.__BST_Node(value)
      return New_tree
    elif node.value == value:
      raise ValueError("Value already exists")
    if node.value < value:
      node.Rchild = self.__recursive_IE(value, node.Rchild)
    if node.value > value:
      node.Lchild = self.__recursive_IE(value, node.Lchild)
    node.Update_size()
    return self.__balance(node)



  #Performance Analysis: remove_element(self,value)
  #Performance: O(logn)
  #The performance of this function is O(logn) because when trying to remove a value,
  #the function traverses through the tree in log time. The time decreases each time the recursion happens
  def remove_element(self, value):
    self.__root = self.__recursive_RE(value, self.__root)

    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    pass # TODO replace pass with your implementation



  #Performance Analysis: __recursive_RE(self,value,node)
  #Performance: O(logn)
  #The performance of this function is O(logn) because when trying to remove a value,
  #the function traverses through the tree in log time. The time decreases each time the recursion happens
  def __recursive_RE(self, value, node):
    if node == None:
      raise ValueError("Value not found")
    if value < node.value:
      node.Lchild = self.__recursive_RE(value, node.Lchild)
    elif value > node.value:
      node.Rchild = self.__recursive_RE(value, node.Rchild)
    else:
      if node.Lchild == None and node.Rchild == None:
        node = None
      elif node.Lchild == None:
        node = node.Rchild
      elif node.Rchild == None:
        node = node.Lchild
      else:
        x = self.__get_min(node.Rchild)
        node.value = x.value
        node.Rchild = self.__recursive_RE(x.value, node.Rchild)
    if node != None:
      node.Update_size()
    return self.__balance(node)



  #Performance Analysis: __get_min(self,node)
  #Performance: O(logn)
  #this function has an log performance because as the function traverses through the tree,
  #the number of steps are constantly being halfed after each recusion. Thus the time complexity
  #is O(logn)
  def __get_min(self, node):
    if node.Lchild == None:
      return node
    else:
      return self.__get_min(node.Lchild)
    


  #in order functions

  #Performance Analysis: __recursive_in_order(self,node,lst)
  #Performance: O(n)
  #The performance for this function is linear because the function must visit every node in the
  #binary tree. Thus the performance is affected by the size/length of the tree.
  def __recursive_in_order(self,node,lst):
    if node:
      lst = self.__recursive_in_order(node.Lchild,lst)
      lst.append(str(node.value))
      lst = self.__recursive_in_order(node.Rchild,lst)
    return lst
  


  #Performance Analysis: in_order
  #Performance:O(n)
  #This method calls the recursive_in_order function. Thus, the time complexity is the same.
  def in_order(self):
    if self.__root == None:
      return '[ ]'
    else:
      j = []
      self.__recursive_in_order(self.__root,j)
      j = '[ ' + ', '.join(j) + ' ]'
      return j

    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.

    

  #pre order functions

  #Performance Analysis: __recursive_Pre_order(self,node,lst)
  #Performance:O(n)
  #The performance for this function is linear because the function must visit every node in the
  #binary tree. Thus the performance is affected by the size/length of the tree.
  def __recursive_Pre_Order(self,node,lst):
    if node:
      lst.append(str(node.value))
      lst = self.__recursive_Pre_Order(node.Lchild,lst)
      lst = self.__recursive_Pre_Order(node.Rchild,lst)
    return lst



  #Performance Analysis: pre_order(self)
  #Performance:O(n)
  #This function calls the recursive method: __recursive_Pre_order. Thus, the time
  #complexity is the same as the recursive one.
  def pre_order(self):
    if self.__root == None:
      return '[ ]'
    else:
      j = []
      self.__recursive_Pre_Order(self.__root,j)
      j = '[ ' + ', '.join(j) + ' ]'
      return j

    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.



  #post order functions

  #Performance Analysis: _recursive_post_order(self,node,lst)
  #Performance: O(n)
  #The performance for this function is linear because the function must visit every node in the
  #binary tree. Thus the performance is affected by the size/length of the tree.
  def __recursive_Post_Order(self,node,lst):
    if node:
      lst = self.__recursive_Post_Order(node.Lchild,lst)
      lst = self.__recursive_Post_Order(node.Rchild,lst)
      lst.append(str(node.value))
    return lst
  


  #Performance Analysis: post_order(self)
  #Performance:O(n)
  #The performance for this function is also O(n) because it calls the function __recursive_post_order
  def post_order(self):
    if self.__root == None:
      return '[ ]'
    else:
      j = []
      self.__recursive_Post_Order(self.__root,j)
      j = '[ ' + ', '.join(j) + ' ]'
      return j

    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.

  

  #to_list functions
  
  #Performance Analysis: to_list(self)
  #Performance: O(n)
  #This function calls the function: __recursive_to_list(self,node,list). Thus, the performance
  #is the same as the called function.
  def to_list(self):
    # Construct and return a Python list/array containing the in-order
    # traversal of the tree. Your solution must be recursive. This will
    # involve the introduction of additional private methods to support
    # the recursion control variable.
    pass # TODO replace pass with your implementation
    lst = []
    return self.__recursive_to_list(self.__root,lst)



  #Performance Analysis: __recursive_to_list(self,node,lst)
  #Performance: O(n)
  #The performance of this function is linear because the function has it so it traverses through every single node
  #Thus, the time complexity/performance is dependent on the size/length of the tree.
  def __recursive_to_list(self,node,lst):
    if node:
      lst = self.__recursive_to_list(node.Lchild,lst)
      lst.append((node.value))
      lst = self.__recursive_to_list(node.Rchild,lst)
    return lst
  


  #Performance Analysis: get_height(self)
  #Performance: O(1)
  #This function returns the height of the tree. The time complexity is O(1) because the function
  #returns a stored value which does not get affected by the size of the tree/how many nodes the tree has.
  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    pass # TODO replace pass with your implementation
    if self.__root == None:
      return 0
    return self.__root.size



  #BALACNING STARTS HERE!!!!!!!!!

  #Performance Analysis:__balance(self,node)
  #Performance: O(1)
  #All functions used in balance have a performance of O(1). Thus, the time complexity of running this code
  #is constant
  def __balance(self, node):
        if node is None:
            return None
        
        if self.__charge(node) > 1:
            if self.__charge(node.Rchild) < 0:
                node.Rchild = self.__rotate_right(node.Rchild)
            node = self.__rotate_left(node)
  
        elif self.__charge(node) < -1:
            if self.__charge(node.Lchild) > 0:
                node.Lchild = self.__rotate_left(node.Lchild)
            node = self.__rotate_right(node)

        node.size = 1 + max(self.__height(node.Lchild), self.__height(node.Rchild))
        return node



  #Performance Analysis: __height(self,node)
  #Performance: O(1)
  #This function just accesses the size attribute of the entire program. Thus the function only
  #requires a single operation to return the height of the node, resulting in constant time. 
  def __height(self, node):
        if node is None:
            return 0
        return node.size
  


  #Performance Analysis: __charge(self,node)
  #Performance: O(1)
  #The charge function performas at a constant performance because it runs with disregard to the size of the tree.
  #The function just calculates the difference in height between the right child and the left child.
  def __charge(self, node):
        return self.__height(node.Rchild) - self.__height(node.Lchild)
  


  #Performance Analysis: __rotate_left(self,node)
  #Performance:O(1)
  #The rotate_left function has a time complexity of O(1). This is because the program is not really affected by the number of values in the trees.
  #Thus, performs in a constant number of operations on each node. 
  def __rotate_left(self, node):
        floater_point = node.Rchild
        node.Rchild = floater_point.Lchild
        floater_point.Lchild = node
        node.size = 1 + max(self.__height(node.Lchild), self.__height(node.Rchild))
        floater_point.size = 1 + max(self.__height(floater_point.Lchild), self.__height(floater_point.Rchild))
        return floater_point
  


  #Performance Analysis: __rotate_right(self,node)
  #Performance: O(1)
  #The rotate_right function has a time complexity of O(1). This is because the program is not really affected by the number of values in the trees.
  #Thus, performs in a constant number of operations on each node. 
  def __rotate_right(self, node):
        floater_point = node.Lchild
        node.Lchild = floater_point.Rchild
        floater_point.Rchild = node
        node.size = 1 + max(self.__height(node.Lchild), self.__height(node.Rchild))
        floater_point.size = 1 + max(self.__height(floater_point.Lchild), self.__height(floater_point.Rchild))
        return floater_point
    

  #Performance Analysis: __str__(self)
  #Performance: O(n)
  #this function has a performance of linear time. The function returns a string implementation
  #of the tree. The runtime is affected by the number of nodes in the tree. Thus, the time complexity is linear.
  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass 

