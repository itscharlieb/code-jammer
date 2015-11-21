import unittest
import data_manager

class TestLukemia(unittest.TestCase):

    def test_load_raw_data(self):
        csv_data_file = 'data.csv'
        raw_data = data_manager.load_raw_data(csv_data_file)
        self.assertEqual(len(raw_data), 167)
        self.assertEqual(len(raw_data[0]), 269)

    def test_as_cleaned(self):
        csv_data_file = 'data.csv'
        raw_data = data_manager.load_raw_data(csv_data_file)
        ids, ftrs = data_manager.as_cleaned(raw_data)
        self.assertEqual(len(ids), 166)
        self.assertEqual(len(ftrs), 166)
        self.assertEqual(len(ftrs[0]), 268)

    def test_as_arrays(self):
        csv_data_file = 'data.csv'
        raw_data = data_manager.load_raw_data(csv_data_file)
        ids, ftrs = data_manager.as_cleaned(raw_data)
        ids, ftrs, rm_tps, rm_tms, dl = data_manager.as_arrays(ids, ftrs)


if __name__ == "__main__":
    unittest.main()