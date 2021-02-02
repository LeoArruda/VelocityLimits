import unittest
import json
from input_output.load import load_files

class IOLoad_Test(unittest.TestCase):
    """
    load_file tests to evaluate the success of the entire solution
    once compared to the provided output.txt file. 
    """
    def test_LoadAndCompareResultsCase(self):
        input_file = "./data/input.txt"
        load_files(input_file)
        with open("./data/output.txt") as test_file:
            expected_result = test_file.readlines()
        
        with open("./data/result.txt") as result_file:
            result = result_file.readlines()

        for i in range(len(expected_result)):
            result_value = json.loads(result[i])
            expected_value = json.loads(expected_result[i])
            self.assertEqual(expected_value["id"], result_value["id"])
            self.assertEqual(expected_value["accepted"], result_value["accepted"])
            self.assertEqual(expected_value["customer_id"], result_value["customer_id"])

