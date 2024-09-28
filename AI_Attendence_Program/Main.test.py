import unittest
import os

class TestAttendance(unittest.TestCase):
    def setUp(self):
        self.attendance_file = 'Attendence.csv'
        if os.path.exists(self.attendance_file):
            os.remove(self.attendance_file)

    def test_duplicate_attendance(self):
        from Main import attendance

        # Simulate attendance for the same person twice
        attendance('John Doe')
        attendance('John Doe')

        with open(self.attendance_file, 'r') as f:
            attendance_records = f.readlines()

        # Check if there is only one record for the person
        self.assertEqual(len(attendance_records), 2)
        self.assertEqual(attendance_records[0].strip(), 'John Doe,')
        self.assertEqual(attendance_records[1].strip(), 'John Doe,')

if __name__ == '__main__':
    unittest.main()