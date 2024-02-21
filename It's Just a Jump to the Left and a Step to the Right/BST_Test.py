import unittest
from Binary_Search_Tree import *
from fractions import *



class BSTTester(unittest.TestCase):

    def setUp(self):
        self.__binary = Binary_Search_Tree()



    def test_empty_tree_str(self):
        self.assertEqual('[ ]',str(self.__binary))

    def test_empty_tree_len(self):
        self.assertEqual(0,(self.__binary.get_height()))

    def test_empty_tree_In_order_traversal_str(self):
        self.assertEqual('[ ]',self.__binary.in_order())
    
    def test_empty_tree_pre_order_traversal_str(self):
        self.assertEqual('[ ]',self.__binary.pre_order())
    
    def test_empty_tree_post_order_traversal_str(self):
        self.assertEqual('[ ]',self.__binary.post_order())



    def test_insert_val_height(self):
        self.__binary.insert_element(50)
        self.assertEqual(1,self.__binary.get_height())

    def test_insert_val_str(self):
        self.__binary.insert_element(50)
        self.assertEqual('[ 50 ]',str(self.__binary))
    
    def test_insert_val_in_order_str(self):
        self.__binary.insert_element(50)
        self.assertEqual('[ 50 ]',self.__binary.in_order())
    
    def test_insert_val_pre_order_str(self):
        self.__binary.insert_element(50)
        self.assertEqual('[ 50 ]',self.__binary.pre_order())
    
    def test_insert_val_post_order_str(self):
        self.__binary.insert_element(50)
        self.assertEqual('[ 50 ]',self.__binary.post_order())



    def test_insert_val_remove_val_height(self):
        self.__binary.insert_element(50)
        self.__binary.remove_element(50)
        self.assertEqual(0,self.__binary.get_height())
    
    def test_insert_val_remove_val_str(self):
        self.__binary.insert_element(50)
        self.__binary.remove_element(50)
        self.assertEqual('[ ]',str(self.__binary))
    
    def test_insert_val_remove_val_in_order_str(self):
        self.__binary.insert_element(50)
        self.__binary.remove_element(50)
        self.assertEqual('[ ]',self.__binary.in_order())
    
    def test_insert_val_remove_val_pre_order_str(self):
        self.__binary.insert_element(50)
        self.__binary.remove_element(50)
        self.assertEqual('[ ]',self.__binary.pre_order())
    
    def test_insert_val_remove_val_post_order_str(self):
        self.__binary.insert_element(50)
        self.__binary.remove_element(50)
        self.assertEqual('[ ]',self.__binary.post_order())

    

    def test_insert_val_x2_height(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(40)
        self.assertEqual(2,self.__binary.get_height())
    
    def test_insert_val_x2_str(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(40)
        self.assertEqual('[ 40, 50 ]',str(self.__binary))

    def test_insert_val_x2_in_order_str(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(40)
        self.assertEqual('[ 40, 50 ]',self.__binary.in_order())
    
    def test_insert_val_x2_pre_order_str(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(40)
        self.assertEqual('[ 50, 40 ]',self.__binary.pre_order())

    def test_insert_val_x2_post_order_str(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(40)
        self.assertEqual('[ 40, 50 ]',self.__binary.post_order())
    


    def test_insert_val_x2_remove_val_height(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.remove_element(50)
        self.assertEqual(1,self.__binary.get_height())
    
    def test_insert_val_x2_remove_val_str(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.remove_element(50)
        self.assertEqual('[ 70 ]',str(self.__binary))
    
    def test_insert_val_x2_remove_val_in_order_str(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.remove_element(50)
        self.assertEqual('[ 70 ]',self.__binary.in_order())

    def test_insert_val_x2_remove_val_pre_order_str(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.remove_element(50)
        self.assertEqual('[ 70 ]',self.__binary.pre_order())

    def test_insert_val_x2_remove_val_post_order_str(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.remove_element(50)
        self.assertEqual('[ 70 ]',self.__binary.post_order())                   
    

    #70-50-30 order case: 1
    def test_insert_val_x3_height_1(self):
        self.__binary.insert_element(70)
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.assertEqual(2,self.__binary.get_height())
    
    def test_insert_val_x3_str_1(self):
        self.__binary.insert_element(70)
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.assertEqual('[ 30, 50, 70 ]', str(self.__binary))

    def test_insert_val_x3_in_order_str_1(self):
        self.__binary.insert_element(70)
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.assertEqual('[ 30, 50, 70 ]', self.__binary.in_order())
    
    def test_insert_val_x3_pre_order_str_1(self):
        self.__binary.insert_element(70)
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.assertEqual('[ 50, 30, 70 ]', self.__binary.pre_order())
    
    def test_insert_val_x3_post_order_str_1(self):
        self.__binary.insert_element(70)
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.assertEqual('[ 30, 70, 50 ]', self.__binary.post_order())
    



    #30-50-70 order case: 2
    def test_insert_val_x3_height_2(self):
        self.__binary.insert_element(30)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.assertEqual(2,self.__binary.get_height())
    
    def test_insert_val_x3_str_2(self):
        self.__binary.insert_element(30)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.assertEqual('[ 30, 50, 70 ]', str(self.__binary))

    def test_insert_val_x3_in_order_str_2(self):
        self.__binary.insert_element(30)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.assertEqual('[ 30, 50, 70 ]', self.__binary.in_order())
    
    def test_insert_val_x3_pre_order_str_2(self):
        self.__binary.insert_element(30)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.assertEqual('[ 50, 30, 70 ]', self.__binary.pre_order())
    
    def test_insert_val_x3_post_order_str_2(self):
        self.__binary.insert_element(30)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.assertEqual('[ 30, 70, 50 ]', self.__binary.post_order())



    #50-30-70 order case: 3
    def test_insert_val_x3_height_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.assertEqual(2,self.__binary.get_height())
    
    def test_insert_val_x3_str_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.assertEqual('[ 30, 50, 70 ]', str(self.__binary))

    def test_insert_val_x3_in_order_str_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.assertEqual('[ 30, 50, 70 ]', self.__binary.in_order())
    
    def test_insert_val_x3_pre_order_str_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.assertEqual('[ 50, 30, 70 ]', self.__binary.pre_order())
    
    def test_insert_val_x3_post_order_str_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.assertEqual('[ 30, 70, 50 ]', self.__binary.post_order())



    #70-30-50 order case: 4
    def test_insert_val_x3_height_4(self):
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(50)
        self.assertEqual(2,self.__binary.get_height())
    
    def test_insert_val_x3_str_4(self):
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(50)
        self.assertEqual('[ 30, 50, 70 ]', str(self.__binary))

    def test_insert_val_x3_in_order_str_4(self):
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(50)
        self.assertEqual('[ 30, 50, 70 ]', self.__binary.in_order())
    
    def test_insert_val_x3_pre_order_str_4(self):
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(50)
        self.assertEqual('[ 50, 30, 70 ]', self.__binary.pre_order())
    
    def test_insert_val_x3_post_order_str_4(self):
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(50)
        self.assertEqual('[ 30, 70, 50 ]', self.__binary.post_order())



    #30-70-50 order case: 5
    def test_insert_val_x3_height_5(self):
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(50)
        self.assertEqual(2,self.__binary.get_height())
    
    def test_insert_val_x3_str_5(self):
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(50)
        self.assertEqual('[ 30, 50, 70 ]', str(self.__binary))

    def test_insert_val_x3_in_order_str_5(self):
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(50)
        self.assertEqual('[ 30, 50, 70 ]', self.__binary.in_order())
    
    def test_insert_val_x3_pre_order_str_5(self):
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(50)
        self.assertEqual('[ 50, 30, 70 ]', self.__binary.pre_order())
    
    def test_insert_val_x3_post_order_str_5(self):
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(50)
        self.assertEqual('[ 30, 70, 50 ]', self.__binary.post_order())
    


    #50-30-70-20-10 order case:1
    def test_insert_val_x5_height_1(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(10)
        self.assertEqual(3,self.__binary.get_height())
    
    def test_insert_val_x5_str_1(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(10)
        self.assertEqual('[ 10, 20, 30, 50, 70 ]',str(self.__binary))
    
    def test_insert_val_x5_in_order_1(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(10)
        self.assertEqual('[ 10, 20, 30, 50, 70 ]',self.__binary.in_order())
    
    def test_insert_val_x5_pre_order_1(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(10)
        self.assertEqual('[ 50, 20, 10, 30, 70 ]',self.__binary.pre_order())
    
    def test_insert_val_x5_post_order_1(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(10)
        self.assertEqual('[ 10, 30, 20, 70, 50 ]',self.__binary.post_order())



    #50-30-70-80-90 order case:2
    def test_insert_val_x5_height_2(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(80)
        self.__binary.insert_element(90)
        self.assertEqual(3,self.__binary.get_height())
    
    def test_insert_val_x5_str_2(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(80)
        self.__binary.insert_element(90)
        self.assertEqual('[ 30, 50, 70, 80, 90 ]',str(self.__binary))
    
    def test_insert_val_x5_in_order_2(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(80)
        self.__binary.insert_element(90)
        self.assertEqual('[ 30, 50, 70, 80, 90 ]',self.__binary.in_order())
    
    def test_insert_val_x5_pre_order_2(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(80)
        self.__binary.insert_element(90)
        self.assertEqual('[ 50, 30, 80, 70, 90 ]',self.__binary.pre_order())
    
    def test_insert_val_x5_post_order_2(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(80)
        self.__binary.insert_element(90)
        self.assertEqual('[ 30, 70, 90, 80, 50 ]',self.__binary.post_order())
    


    #50-30-70-10-20 order case:3
    def test_insert_val_x5_height_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(10)
        self.__binary.insert_element(20)
        self.assertEqual(3,self.__binary.get_height())
    
    def test_insert_val_x5_str_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(10)
        self.__binary.insert_element(20)
        self.assertEqual('[ 10, 20, 30, 50, 70 ]',str(self.__binary))
    
    def test_insert_val_x5_in_order_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(10)
        self.__binary.insert_element(20)
        self.assertEqual('[ 10, 20, 30, 50, 70 ]',self.__binary.in_order())
    
    def test_insert_val_x5_pre_order_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(10)
        self.__binary.insert_element(20)
        self.assertEqual('[ 50, 20, 10, 30, 70 ]',self.__binary.pre_order())
    
    def test_insert_val_x5_post_order_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(10)
        self.__binary.insert_element(20)
        self.assertEqual('[ 10, 30, 20, 70, 50 ]',self.__binary.post_order())



    #50-30-70-90-80 order case:4
    def test_insert_val_x5_height_4(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(90)
        self.__binary.insert_element(80)
        self.assertEqual(3,self.__binary.get_height())
    
    def test_insert_val_x5_str_4(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(90)
        self.__binary.insert_element(80)
        self.assertEqual('[ 30, 50, 70, 80, 90 ]',str(self.__binary))
    
    def test_insert_val_x5_in_order_4(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(90)
        self.__binary.insert_element(80)
        self.assertEqual('[ 30, 50, 70, 80, 90 ]',self.__binary.in_order())
    
    def test_insert_val_x5_pre_order_4(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(90)
        self.__binary.insert_element(80)
        self.assertEqual('[ 50, 30, 80, 70, 90 ]',self.__binary.pre_order())
    
    def test_insert_val_x5_post_order_4(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(90)
        self.__binary.insert_element(80)
        self.assertEqual('[ 30, 70, 90, 80, 50 ]',self.__binary.post_order())
    


    #50-30-70-20-40-10 order case: 1
    def test_insert_val_x6_height_1(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(40)
        self.__binary.insert_element(10)
        self.assertEqual(3,self.__binary.get_height())
    
    def test_insert_val_x6_str_1(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(40)
        self.__binary.insert_element(10)
        self.assertEqual('[ 10, 20, 30, 40, 50, 70 ]',str(self.__binary))

    def test_insert_val_x6_in_order_str_1(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(40)
        self.__binary.insert_element(10)
        self.assertEqual('[ 10, 20, 30, 40, 50, 70 ]',self.__binary.in_order())
    
    def test_insert_val_x6_pre_order_str_1(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(40)
        self.__binary.insert_element(10)
        self.assertEqual('[ 30, 20, 10, 50, 40, 70 ]',self.__binary.pre_order())

    def test_insert_val_x6_post_order_str_1(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(40)
        self.__binary.insert_element(10)
        self.assertEqual('[ 10, 20, 40, 70, 50, 30 ]',self.__binary.post_order())



    #50-30-70-60-80-90 order case: 2
    def test_insert_val_x6_height_2(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(60)
        self.__binary.insert_element(80)
        self.__binary.insert_element(90)
        self.assertEqual(3,self.__binary.get_height())
    
    def test_insert_val_x6_str_2(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(60)
        self.__binary.insert_element(80)
        self.__binary.insert_element(90)
        self.assertEqual('[ 30, 50, 60, 70, 80, 90 ]',str(self.__binary))

    def test_insert_val_x6_in_order_str_2(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(60)
        self.__binary.insert_element(80)
        self.__binary.insert_element(90)
        self.assertEqual('[ 30, 50, 60, 70, 80, 90 ]',self.__binary.in_order())
    
    def test_insert_val_x6_pre_order_str_2(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(60)
        self.__binary.insert_element(80)
        self.__binary.insert_element(90)
        self.assertEqual('[ 70, 50, 30, 60, 80, 90 ]',self.__binary.pre_order())

    def test_insert_val_x6_post_order_str_2(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(60)
        self.__binary.insert_element(80)
        self.__binary.insert_element(90)
        self.assertEqual('[ 30, 60, 50, 90, 80, 70 ]',self.__binary.post_order())
    


    #50-30-70-20-40-35 order case: 3
    def test_insert_val_x6_height_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(40)
        self.__binary.insert_element(35)
        self.assertEqual(3,self.__binary.get_height())
    
    def test_insert_val_x6_str_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(40)
        self.__binary.insert_element(35)
        self.assertEqual('[ 20, 30, 35, 40, 50, 70 ]',str(self.__binary))

    def test_insert_val_x6_in_order_str_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(40)
        self.__binary.insert_element(35)
        self.assertEqual('[ 20, 30, 35, 40, 50, 70 ]',self.__binary.in_order())
    
    def test_insert_val_x6_pre_order_str_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(40)
        self.__binary.insert_element(35)
        self.assertEqual('[ 40, 30, 20, 35, 50, 70 ]',self.__binary.pre_order())

    def test_insert_val_x6_post_order_str_3(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(20)
        self.__binary.insert_element(40)
        self.__binary.insert_element(35)
        self.assertEqual('[ 20, 35, 30, 70, 50, 40 ]',self.__binary.post_order())



    #50-30-70-60-70-65 order case: 4
    def test_insert_val_x6_height_4(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(60)
        self.__binary.insert_element(80)
        self.__binary.insert_element(65)
        self.assertEqual(3,self.__binary.get_height())
    
    def test_insert_val_x6_str_4(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(60)
        self.__binary.insert_element(80)
        self.__binary.insert_element(65)
        self.assertEqual('[ 30, 50, 60, 65, 70, 80 ]',str(self.__binary))

    def test_insert_val_x6_in_order_str_4(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(60)
        self.__binary.insert_element(80)
        self.__binary.insert_element(65)
        self.assertEqual('[ 30, 50, 60, 65, 70, 80 ]',self.__binary.in_order())
    
    def test_insert_val_x6_pre_order_str_4(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(60)
        self.__binary.insert_element(80)
        self.__binary.insert_element(65)
        self.assertEqual('[ 60, 50, 30, 70, 65, 80 ]',self.__binary.pre_order())

    def test_insert_val_x6_post_order_str_4(self):
        self.__binary.insert_element(50)
        self.__binary.insert_element(30)
        self.__binary.insert_element(70)
        self.__binary.insert_element(60)
        self.__binary.insert_element(80)
        self.__binary.insert_element(65)
        self.assertEqual('[ 30, 50, 65, 80, 70, 60 ]',self.__binary.post_order())
    



    def test_insert_val_x6_remove_val_height(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(80)
        self.assertEqual(3,self.__binary.get_height())
    
    def test_insert_val_x6_remove_val_str(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(80)
        self.assertEqual('[ 30, 50, 60, 65, 70 ]',str(self.__binary))

    def test_insert_val_x6_remove_val_in_order_str(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(80)
        self.assertEqual('[ 30, 50, 60, 65, 70 ]',self.__binary.in_order())
    
    def test_insert_val_x6_remove_val_pre_order_str(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(80)
        self.assertEqual('[ 60, 50, 30, 70, 65 ]',self.__binary.pre_order())

    def test_insert_val_x6_remove_val_post_order_str(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(80)
        self.assertEqual('[ 30, 50, 65, 70, 60 ]',self.__binary.post_order())
    


    #case: 1
    def test_insert_val_x6_remove_val_x3_height_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(80)
        self.__binary.remove_element(50)
        self.__binary.remove_element(30)
        self.assertEqual(2,self.__binary.get_height())
    
    def test_insert_val_x6_remove_val_x3_str_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(80)
        self.__binary.remove_element(50)
        self.__binary.remove_element(30)
        self.assertEqual('[ 60, 65, 70 ]',str(self.__binary))
    
    def test_insert_val_x6_remove_val_x3_in_order_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(80)
        self.__binary.remove_element(50)
        self.__binary.remove_element(30)
        self.assertEqual('[ 60, 65, 70 ]',self.__binary.in_order())
    
    def test_insert_val_x6_remove_val_x3_pre_order_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(80)
        self.__binary.remove_element(50)
        self.__binary.remove_element(30)
        self.assertEqual('[ 65, 60, 70 ]',self.__binary.pre_order())
    
    def test_insert_val_x6_remove_val_x3_post_order_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(80)
        self.__binary.remove_element(50)
        self.__binary.remove_element(30)
        self.assertEqual('[ 60, 70, 65 ]',self.__binary.post_order())
    


    #case: 2
    def test_insert_val_x6_remove_val_x3_height_2(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(30)
        self.__binary.remove_element(70)
        self.__binary.remove_element(80)
        self.assertEqual(2,self.__binary.get_height())
    
    def test_insert_val_x6_remove_val_x3_str_2(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(30)
        self.__binary.remove_element(70)
        self.__binary.remove_element(80)
        self.assertEqual('[ 50, 55, 60 ]',str(self.__binary))
    
    def test_insert_val_x6_remove_val_x3_in_order_2(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(30)
        self.__binary.remove_element(70)
        self.__binary.remove_element(80)
        self.assertEqual('[ 50, 55, 60 ]',self.__binary.in_order())
    
    def test_insert_val_x6_remove_val_x3_pre_order_2(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(30)
        self.__binary.remove_element(70)
        self.__binary.remove_element(80)
        self.assertEqual('[ 55, 50, 60 ]',self.__binary.pre_order())
    
    def test_insert_val_x6_remove_val_x3_post_order_2(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(30)
        self.__binary.remove_element(70)
        self.__binary.remove_element(80)
        self.assertEqual('[ 50, 60, 55 ]',self.__binary.post_order())
    


    #case: 3
    def test_insert_val_x6_remove_val_x3_height_3(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(65)
        self.__binary.remove_element(50)
        self.__binary.remove_element(30)
        self.assertEqual(2,self.__binary.get_height())
    
    def test_insert_val_x6_remove_val_x3_str_3(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(65)
        self.__binary.remove_element(50)
        self.__binary.remove_element(30)
        self.assertEqual('[ 60, 70, 80 ]',str(self.__binary))
    
    def test_insert_val_x6_remove_val_x3_in_order_3(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(65)
        self.__binary.remove_element(50)
        self.__binary.remove_element(30)
        self.assertEqual('[ 60, 70, 80 ]',self.__binary.in_order())
    
    def test_insert_val_x6_remove_val_x3_pre_order_3(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(65)
        self.__binary.remove_element(50)
        self.__binary.remove_element(30)
        self.assertEqual('[ 70, 60, 80 ]',self.__binary.pre_order())
    
    def test_insert_val_x6_remove_val_x3_post_order_3(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(65)
        self.__binary.insert_element(80)
        self.__binary.remove_element(65)
        self.__binary.remove_element(50)
        self.__binary.remove_element(30)
        self.assertEqual('[ 60, 80, 70 ]',self.__binary.post_order())


    
    #case: 4
    def test_insert_val_x6_remove_val_x3_height_4(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(55)
        self.__binary.remove_element(70)
        self.__binary.remove_element(80)
        self.assertEqual(2,self.__binary.get_height())
    
    def test_insert_val_x6_remove_val_x3_str_4(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(55)
        self.__binary.remove_element(70)
        self.__binary.remove_element(80)
        self.assertEqual('[ 30, 50, 60 ]',str(self.__binary))
    
    def test_insert_val_x6_remove_val_x3_in_order_4(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(55)
        self.__binary.remove_element(70)
        self.__binary.remove_element(80)
        self.assertEqual('[ 30, 50, 60 ]',self.__binary.in_order())
    
    def test_insert_val_x6_remove_val_x3_pre_order_4(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(55)
        self.__binary.remove_element(70)
        self.__binary.remove_element(80)
        self.assertEqual('[ 50, 30, 60 ]',self.__binary.pre_order())
    
    def test_insert_val_x6_remove_val_x3_post_order_4(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(55)
        self.__binary.remove_element(70)
        self.__binary.remove_element(80)
        self.assertEqual('[ 30, 60, 50 ]',self.__binary.post_order())
    


    #case: 1
    def test_insert_val_x6_remove_val_x1_height_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(60)
        self.assertEqual(3,self.__binary.get_height())
    
    def test_insert_val_x6_remove_val_x1_str_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(60)
        self.assertEqual('[ 30, 50, 55, 70, 80 ]',str(self.__binary))
    
    def test_insert_val_x6_remove_val_x1_in_order_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(60)
        self.assertEqual('[ 30, 50, 55, 70, 80 ]',self.__binary.in_order())
    
    def test_insert_val_x6_remove_val_x1_pre_order_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(60)
        self.assertEqual('[ 70, 50, 30, 55, 80 ]',self.__binary.pre_order())
    
    def test_insert_val_x6_remove_val_x1_post_order_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(60)
        self.assertEqual('[ 30, 55, 50, 80, 70 ]',self.__binary.post_order())
    


    #case: 1
    def test_insert_val_x6_remove_val_x2_height_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(60)
        self.__binary.remove_element(70)
        self.assertEqual(3,self.__binary.get_height())
    
    def test_insert_val_x6_remove_val_x2_str_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(60)
        self.__binary.remove_element(70)
        self.assertEqual('[ 30, 50, 55, 80 ]',str(self.__binary))
    
    def test_insert_val_x6_remove_val_x2_in_order_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(60)
        self.__binary.remove_element(70)
        self.assertEqual('[ 30, 50, 55, 80 ]',self.__binary.in_order())
    
    def test_insert_val_x6_remove_val_x2_pre_order_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(60)
        self.__binary.remove_element(70)
        self.assertEqual('[ 50, 30, 80, 55 ]',self.__binary.pre_order())
    
    def test_insert_val_x6_remove_val_x2_post_order_1(self):
        self.__binary.insert_element(60)
        self.__binary.insert_element(50)
        self.__binary.insert_element(70)
        self.__binary.insert_element(30)
        self.__binary.insert_element(55)
        self.__binary.insert_element(80)
        self.__binary.remove_element(60)
        self.__binary.remove_element(70)
        self.assertEqual('[ 30, 55, 80, 50 ]',self.__binary.post_order())
    



















































if __name__ == '__main__':
    unittest.main()