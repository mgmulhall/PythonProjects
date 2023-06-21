import unittest
from pydoc import *
from deque import Make_deque

#Unit Tests for Make_deque
class TestMakeDeque(unittest.TestCase):
    list=[]
    def test_Make_deque(self):
        #Create Add A and B to list1 using Make_deque
        list1=Make_deque.Add(self,'A','1')
        list1=Make_deque.Add(self,'B','2')
        list1=Make_deque.Add(self,'C','1')
        
        #Initalize list2 with 'A' and 'B'
        list2 = ['C','A','B']
        
        #Run unit test
        self.assertEqual(list1, list2)

if __name__ == '__main__':
    unittest.main()