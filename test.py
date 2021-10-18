#Have this program read an 'out.txt' file made by the student's python file
#Use unit  testing to Assert that the string imported from the txt is equal to what we want (the values we want to match must be supplied at runtime)

import unittest

class TestStudentSubmissions(unittest.TestCase):
  
  def __init__(self):
    # I think I'll need the solution or ideal function in a file or something to import here, not sure though
    self.control = open(answer_key.txt)
  
  def setUp(self):
    # Gonna need some info on where exactly this out.txt is coming from, I'm assuming I'm gonna need to access it through os
    self.student = open(out.txt)
  
  def test_student_files(self):
    # So are we actually trying to run some functions inside of here and see if they come up with the same results? Or just if the files match?
    self.assertEqual(self.student, self.control)
    
  def tearDown(self):
    self.fi.dispose()
    

unittest.main()
