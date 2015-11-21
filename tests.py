import unittest
import lukemia

class TestLukemia(unittest.TestCase):

    def test_load_raw_data(self):
        csv_data_file = 'data.csv'
        raw_data = lukemia.load_raw_data(csv_data_file)
        self.assertEqual(len(raw_data), 167)
        self.assertEqual(len(raw_data[0]), 269)

    def test_as_cleaned(self):
        csv_data_file = 'data.csv'
        raw_data = lukemia.load_raw_data(csv_data_file)
        cleaned = lukemia.as_cleaned(raw_data)
        self.assertEqual(len(cleaned), 166) #one less than previous for removing csv labels


if __name__ == "__main__":
    unittest.main()