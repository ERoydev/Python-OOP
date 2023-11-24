import unittest
from student.project.student import Student


class StudentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Emil", {'Python': ['Basic', 'Algorithms']})

    def test_initialization_if_correct(self):
        test = Student("John")
        self.assertEqual("Emil", self.student.name)
        self.assertEqual({'Python': ['Basic', 'Algorithms']}, self.student.courses)
        self.assertEqual({}, test.courses)

    def test_enroll_if_course_name_in_courses_and_add_notes_inside(self):
        result = self.student.enroll('Python', ['Fundamentals', 'OOP'])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'Python': ['Basic', 'Algorithms', 'Fundamentals', 'OOP']}, self.student.courses)
        self.assertEqual({'Python': ['Basic', 'Algorithms', 'Fundamentals', 'OOP']}, self.student.courses)

    def test_enroll_if_course_notes_is_Y_or_empty_space(self):
        result = self.student.enroll('JS', ['Basic'], 'Y')
        result2 = self.student.enroll("PHP", ['Fundamental'])
        result3 = self.student.enroll("C#", ['Fundamental'], 'hey')

        self.assertEqual('Course and course notes have been added.', result2)
        self.assertNotEqual('Course and course notes have been added.', result3)
        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual({'Python': ['Basic', 'Algorithms'], 'JS': ['Basic'], 'PHP': ['Fundamental'], 'C#': []}, self.student.courses)

    def test_enroll_if_course_is_created(self):
        result = self.student.enroll("C#", ['Fundamental'], 'hey')
        self.assertEqual("Course has been added.", result)
        self.assertEqual({'Python': ['Basic', 'Algorithms'], 'C#': []}, self.student.courses)

    def test_add_notes_if_course_exists_and_notes_are_updated(self):
        self.assertEqual({'Python': ['Basic', 'Algorithms']}, self.student.courses)
        result = self.student.add_notes("Python", "solve testing")
        self.assertEqual({'Python': ['Basic', 'Algorithms', 'solve testing']}, self.student.courses)

        self.assertEqual("Notes have been updated", result)

    def test_add_notes_course_not_found_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('JS', "update CSS")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_course_exists_and_is_removed_functionality(self):
        self.assertEqual({'Python': ['Basic', 'Algorithms']}, self.student.courses)
        result = self.student.leave_course('Python')
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_if_course_dont_exist_and_cannot_be_removed_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('JavaScript')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()