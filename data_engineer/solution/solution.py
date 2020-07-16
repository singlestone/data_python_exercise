"""Data Engineer Exercise Solution"""
import pandas
import fastparquet

# scratch
# generators to provide csv/parquet records one at a time?

# if using arrow... (ew - huge complicated dependency with native code bindings
# - not doing it for this)
# use `open_csv()` from arrow to read csv incrementally
# use `read_row_group()` from arrow to read parquet incrementally

# use pandas to chunk read csv https://pythonspeed.com/articles/chunking-pandas/

# use fastparquet to chunk read parquet with less dependencies
# https://fastparquet.readthedocs.io/en/latest/details.html#iteration


class StudentDataProcessor:
    """StudentDataProcessor

    encapsulates the incremental CSV parsing and dataset traversal, using a
    generator function for iterating over it and the visitor pattern to run
    arbitrary code against it."""

    def __init__(self):
        self.raw_gen = pandas.read_csv("students.csv", sep='_', chunksize=10,
                                       usecols=('fname', 'lname', 'cid'))

    def record_gen(self, visitor=lambda x: x):
        """record_gen is a generator of student record tuples, for now limited to first/last/cid"""
        for chunk in iter(self.raw_gen):
            for record in chunk.values:
                yield visitor(record)

    def process(self, visitor):
        """
        process runs a function against all records
        """
        for chunk in iter(self.raw_gen):
            for record in chunk.values:
                visitor(record)


class ClassTeacherIndex(dict):
    """ClassTeacherIndex manages the class:teacher lookups.
    It omits columns to save memory, but serves to extract an associative set."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parquet_file = fastparquet.ParquetFile('teachers.parquet')
        self.index = parquet_file.to_pandas(columns=['fname', 'lname'], index='cid')

    def __getitem__(self, cid):
        teacher = self.index.loc[cid]
        return (teacher.fname, teacher.lname)


def student_teacher_lookup_output(student_tuple, index=ClassTeacherIndex()):
    """This function looks up and adds the teacher information for student/class entries"""
    class_id = student_tuple[2]
    teacher_tuple = index[class_id]
    output = 'Student, {}, is taught by {}, in class with id {}.'
    return output.format(' '.join(student_tuple[0:2]), ' '.join(teacher_tuple), class_id)
