
import unittest
import madlib2repo

class Test_madlib(unittest.TestCase):

    def test_madlib2repo_TheLittleBlank_save_madlib_should_add_to_filled_list(self):
        # Arrange
        self.a = 'a' 
        self.b = 'b'
        self.c = 'c'
        self.d = 'd'
        self.e = 'e'
        self.f = 'f'
        self.g = 'g'
        self.h = 'h'
        self.i = 'i'
        self.j = 'j'

        # Act
        madlib2repo.TheLittleBlank.save_madlib(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j)
        actual = len(madlib2repo.filled)
        expected = 1

        # Assert
        self.assertEqual(actual,expected)
    
    def test_madlib2repo_TheNBlanks_init_should_have_9_arguments(self):
        # Arrange
        self.a = 'a' 
        self.b = 'b'
        self.c = 'c'
        self.d = 'd'
        self.e = 'e'
        self.f = 'f'
        self.g = 'g'
        self.h = 'h'
        self.i = 'i'

        # Act
        actual = madlib2repo.TheNBlanks(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i)

        # Assert
        self.assertIsInstance(actual, madlib2repo.TheNBlanks)
    
    def test_madlib2repo_ARecipe_init_should_have_13_arguements(self):
        # Arrange
        self.a = 'a'
        self.b = 'b'
        self.c = 'c'
        self.d = 'd' 
        self.e = 'e'
        self.f = 'f'
        self.g = 'g'
        self.h = 'h'
        self.i = 'i'
        self.j = 'j'
        self.k = 'k'
        self.l = 'l' 
        self.m = 'm'

        # Act
        actual = madlib2repo.ARecipe(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m)

        # Assert
        self.assertIsInstance(actual, madlib2repo.ARecipe)
