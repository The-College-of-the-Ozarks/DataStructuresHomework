#Have this program read an 'out.py' file made by the student's python file
#Use unit  testing to Assert that the string imported from the txt is equal to what we want (the values we want to match must be supplied at runtime)

import unittest
import out

class TestStudentSubmissions(unittest.TestCase):
  # I am using func() as a filler name for any functioon in out.py
  
  def test_multiply_two_integers(self):
    for i in range(20):
      with self.subTest(i=i):
        a = random.randint(-10, 10)
        b = random.randint(-10,10)
        self.assertEqual(out.func(a, b), a * b)
    

unittest.main()
