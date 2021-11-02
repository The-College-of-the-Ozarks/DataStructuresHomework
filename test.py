#Have this program read an 'out.py' file made by the student's python file
#Use unit  testing to Assert that the string imported from the txt is equal to what we want (the values we want to match must be supplied at runtime)

import unittest
import random
import out

class TestStudentSubmissions(unittest.TestCase):
  # I am using func() as a filler name for any functioon in out.py
  
  def test_multiply_two_integers(self):
    for i in range(20):
      with self.subTest(i=i):
        a = random.randint(-10,10)
        b = random.randint(-10,10)
        self.assertEqual(out.func(a, b), a * b)
        
  def test_multiply_integers_with_args(self):
    for i in range(5):
      with self.subTest(i=i):
        a = random.randint(-10,10)
        self.assertEqual(out.func(a), a)
    for j in range(5):
      with self.subTest(j=j):
        a = random.randint(-10,10)
        b = random.randint(-10,10)
        self.assertEqual(out.func(a, b), a * b)
    for k in range(5):
      with self.subTest(k=k):
        a = random.randint(-10,10)
        b = random.randint(-10,10)
        c = random.randint(-10,10)
        d = random.randint(-10,10)
        e = random.randint(-10,10)
        self.assertEqual(out.func(a, b, c, d, e), a * b * c * d * e)

    def test_sort_numbers_in_list(self):
      for i in range(10):
        unsorted_list = []
        n = random.randint(1, 30)
        for j in range(n):
          unsorted_list.append(random.randint(-50, 50))
        self.assertEqual(out.func(unsorted_list), sorted(unsorted_list))
     
    

unittest.main()
