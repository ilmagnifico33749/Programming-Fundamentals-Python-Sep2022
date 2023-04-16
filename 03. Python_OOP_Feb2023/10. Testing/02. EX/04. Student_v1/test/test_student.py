import unittest
from project.student import Student

class Test_Student(unittest.TestCase):
    def setUp(self) -> None:
        self.student_name = "Michael"
        self.student_courses = {"German": [], "Spanish": [], "French": []}
        self.student = Student(self.student_name, self.student_courses)

    def test_init_keeping_default_values(self):
        test_student = Student(self.student_name)
        result = [test_student.name, test_student.courses]
        expected_result = ["Michael", {}]
        self.assertEqual(result, expected_result)

    def test_init_not_keeping_default_values(self):
        test_student = Student(self.student_name, self.student_courses)
        result = [test_student.name, test_student.courses]
        expected_result = ["Michael", {"German": [], "Spanish": [], "French": []}]
        self.assertEqual(result, expected_result)

    def test_enroll_already_enrolled(self):
        return_result = self.student.enroll("German", ["test_note_one"], "test note_two")
        expected_return_result = "Course already added. Notes have been updated."
        notes_update_result = self.student.courses["German"]
        notes_update_expected_result = ["test_note_one"]
        self.assertEqual(return_result, expected_return_result)
        self.assertEqual(notes_update_result, notes_update_expected_result)

    def test_enroll_not_enrolled_yet_with_notes(self):
        return_result_one = self.student.enroll("Chinese", ["test_note_one"], "Y")
        expected_return_result_one = "Course and course notes have been added."
        return_result_two = self.student.enroll("Japanese", ["test_note_one"], "")
        expected_return_result_two = "Course and course notes have been added."
        self.assertEqual(return_result_one, expected_return_result_one)
        self.assertEqual(return_result_two, expected_return_result_two)
        self.assertEqual(self.student.courses["Chinese"], ["test_note_one"])

    def test_enroll_not_enrolled_yet_no_notes(self):
        return_result = self.student.enroll("Chinese", ["test_note_one"], "test note_two")
        expected_return_result = "Course has been added."
        self.assertEqual(return_result, expected_return_result)
        self.assertEqual(self.student.courses["Chinese"], [])

    def test_add_notes_not_enrolled_to_course(self):
        with self.assertRaises(Exception) as excp_msg:
            self.student.add_notes("Chinese", "test_note_three")
        self.assertEqual("Cannot add notes. Course not found.", str(excp_msg.exception))

    def test_add_notes_enrolled_to_course(self):
        result_return = self.student.add_notes("German", "Nicht")
        expected_return = "Notes have been updated"
        notes_in_course = self.student.courses["German"]
        expected_notes_in_course = ["Nicht"]
        self.assertEqual(result_return, expected_return)
        self.assertEqual(notes_in_course, expected_notes_in_course)


    def test_leaving_course_not_enrolled_to(self):
        with self.assertRaises(Exception) as excp_msg:
            self.student.leave_course("Chinese")
        self.assertEqual("Cannot remove course. Course not found.", str(excp_msg.exception))

    def test_leaving_course_enrolled_to(self):
        result_return = self.student.leave_course("German")
        expected_result_return = "Course has been removed"
        result_new_course_after_deletion = self.student.courses
        expected_result_new_course_after_deletion = {"Spanish": [], "French": []}
        self.assertEqual(result_return, expected_result_return)
        self.assertEqual(result_new_course_after_deletion, expected_result_new_course_after_deletion)


if __name__ == "__main__":
    unittest.main()

