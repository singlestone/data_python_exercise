"""parquet/teacher related tests
"""
import unittest
import fastparquet
from solution.solution import ClassTeacherIndex


class ExploratoryParquetTestCase(unittest.TestCase):
    """collaborator/exploratory tests
    """

    # yeah, see solution readme - I fled this path for just columnar filtering
    # def test_read_chunks(self):
    #     pf = fastparquet.ParquetFile('teachers.parquet')
    #     records = 0
    #     row_groups = 0
    #     for row_group in pf.iter_row_groups():
    #         print("here is a rowgroup", row_group.shape, ":\n", row_group)
    #         records = records + 1
    #         row_groups = row_groups + 1
    #     self.assertEqual(1, row_groups)

    def test_index_teachers_classes(self):
        """figure out how to work with parquet
        """
        teacher_file = fastparquet.ParquetFile('teachers.parquet')
        indexed = teacher_file.to_pandas(columns=['fname', 'lname'], index='cid')
        record = indexed.loc['08-2046381'] # this class id is taught by
        self.assertEqual('Jessa', record.fname)
        self.assertEqual('Gibbs', record.lname)

    def test_show_teachers_file(self):
        """read/display teacher data
        """
        print(self)
        teacher_file = fastparquet.ParquetFile('teachers.parquet')
        for chunk in iter(teacher_file.iter_row_groups()):
            print("teachers - ", chunk.shape, ":\n", chunk.head)


class ClassTeacherIndexTestCase(unittest.TestCase):
    """Unit tests for the parquet code
    """
    def test_index_teachers_classes(self):
        """verify we can match `cid` to a teacher
        """
        index = ClassTeacherIndex()
        teacher = index['08-2046381'] # this class id is taught by
        self.assertEqual(('Jessa', 'Gibbs'), teacher)
