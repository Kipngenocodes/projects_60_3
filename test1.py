import unittest
import script

class TestMain(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = script.Guess_game(answer, guess) 
        self.assertTrue(result)
    def test_input_incorrect(self):
        result = script.Guess_game(5, 0) 
        self.assertFalse(result)
    def test_input_out_of_range(self):
        result = script.Guess_game(5, 11) 
        self.assertFalse(result)
    def test_input_of_string(self):
        result = script.Guess_game(5, "11") 
        self.assertFalse(result)
    

if __name__ == "__main__":
    unittest.main()