#Have this program read an 'out.py' file made by the student's python file
#Use unit  testing to Assert that the string imported from the txt is equal to what we want (the values we want to match must be supplied at runtime)

import unittest
import out

class TestStudentSubmissions(unittest.TestCase):
  
  def __init__(self):
    # We will need to include a variable predicting the wanted output type within each assignment; for example: output_type = int
    self.type = out.output_type
    
  def setUp(self):
  
  def test_integer(self):
    
  def tearDown(self):
    

unittest.main()
