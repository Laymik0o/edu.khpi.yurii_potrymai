class Student:
    # _labs_passed = 0
    # _labs_points = 0
    # _task_points = 0
    _labs = {}
    _individual_task = []

    _points = 0
    _course = {}

    def __init__(self, name, course_info):
        self._name = name
        self._course = course_info
        for i in range(course_info["labs_amount"] + 1):
            self._labs[i] = [0, 0]

    def lab_work(self, lab_number, attempt_number, points):
        if (0 <= points <= self._course.get("lab_work_points") and
                lab_number in self._labs and
                attempt_number >= 1):
            self._labs[lab_number] = [points, attempt_number]
        else:
            print("One of given parameters is invalid")

    def individual_task(self, attempt_number, points):
        if (0 <= points <= self._course["individual_task_points"] and
                attempt_number >= 1):
            self._individual_task = [points, attempt_number]
        else:
            print("One of given parameters is invalid")

    def course_result(self):
        self.calculate_all_ponits()
        max_course_points = (self._course["individual_task_points"] +
                             self._course["lab_work_points"] *
                             self._course["labs_amount"])
        is_auto_exam = self._points >= self._course["points_percentage_for_exam"] * max_course_points
        return self._points, is_auto_exam

    def calculate_all_ponits(self):
        self._points += self._individual_task[0]
        for lab in self._labs:
            self._points += self._labs[lab][0]


def start():
    name = "Ivan Popov"
    course_info = {
        "individual_task_points": 100,
        "lab_work_points": 100,
        "labs_amount": 5,
        "points_percentage_for_exam": 0.8
    }
    student = Student(name, course_info)
    student.individual_task(2, 95)
    student.lab_work(1, 1, 100)
    student.lab_work(2, 1, 91)
    student.lab_work(3, 2, 88)
    student.lab_work(4, 1, 99)
    student.lab_work(5, 4, 75)
    student.lab_work(5, 5, 83)
    student.lab_work(6, 1, 100)

    print("Course results:")
    result = student.course_result()
    print("Student's points: ", result[0])
    print("Can student pass exam exterally? ", result[1])


if __name__ == "__main__":
    start()
