"""csv handling collaboration and unit tests
"""
import unittest
import pandas
from solution.solution import StudentDataProcessor

# collaborator/exploratory tests

class ExploratoryCsvTestCase(unittest.TestCase):
    """explore and validate pandas csv support
    """
    def test_read_chunks(self):
        """explore and validate pandas and incremental csv read
        """
        chunks = 0
        records = 0
        for chunk in pandas.read_csv("students.csv", sep='_', chunksize=10):
            print("here is a chunk", chunk.shape, ":\n", chunk)
            chunks = chunks + 1
            records = records + len(chunk)
        self.assertEqual(100, chunks)
        self.assertEqual(1000, records)

    def test_head_students_file(self):
        """tool for reading/viewing students data
        """
        print(self)
        students = pandas.read_csv("students.csv", sep='_')
        print("students - ", students.shape, ":\n", students.head)

class StudentDataProcessorTestCase(unittest.TestCase):
    """tests of my functionality for csv/student stuff
    """

    def __init__(self, *args, **kwargs):
        """satisfy linting by containing records set call
        """
        super().__init__(*args, **kwargs)
        self.records = 0

    def test_processes_all(self):
        """make sure we hit all 1000 records in the sample set
        """
        processor = StudentDataProcessor()
        def counter(record):
            if record is not None:
                self.records = self.records + 1
        processor.process(counter)
        self.assertEqual(1000, self.records)

    def test_extracts_3fields(self):
        """make sure the data returned by the record generator has the desired structure
        """
        processor = StudentDataProcessor()
        gen = processor.record_gen()
        i = iter(gen)
        record = next(i)
        self.assertEqual(3, len(record))
