from app import frequency_analysis_generator
import unittest
import time
from threading import Thread


def without_yield():
    with open('file.txt', mode='r', encoding='utf-8') as file:
        for line in file:
            return line


class TestWordFrequencyAnalysisTool(unittest.TestCase):

    def test_response_time(self):
        t2_time_start = time.time()

        t2 = Thread(target=without_yield)
        t2.start()
        t2.join()

        t2_time_end = time.time() - t2_time_start

        t1_time_start = time.time()

        t1 = Thread(target=frequency_analysis_generator)
        t1.start()
        t1.join()
        
        t1_time_end = time.time() - t1_time_start

        
        self.assertTrue(t2_time_end > t1_time_end)

if __name__ == '__main__':
    unittest.main()