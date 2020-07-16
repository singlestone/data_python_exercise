"""entry point for processing the data sets
"""
from solution.solution import StudentDataProcessor
from solution.solution import student_teacher_lookup_output

def main():
    """required entry point function
    """
    processor = StudentDataProcessor()

    print("These are the Student Registrations:")
    for student_report in processor.record_gen(visitor=student_teacher_lookup_output):
        print(student_report)

if __name__ == "__main__":
    main()
