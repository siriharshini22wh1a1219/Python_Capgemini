import logging
logging.basicConfig(
    filename="exam.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Exam:

    pass_marks = 40

    def __init__(self, student_name, total_questions):
        self.student_name = student_name
        self.total_questions = total_questions
        self.correct_answers = 0
        self.is_started = False
        self.is_submitted = False
        self.score = 0

    def start_exam(self):
        if self.is_started==False:
            self.is_started = True
            logging.info("Exam started by %s",self.student_name)

    def submit_exam(self, correct_answers):
        if self.is_started and not self.is_submitted:
            self.correct_answers = correct_answers
            self.is_submitted = True
            logging.info("Exam submitted by %s",self.student_name)
            self.calculate_score()

    def calculate_score(self):
        self.score = (self.correct_answers / self.total_questions) * 100
        logging.info("Score is %d", self.score)

        if self.score >= Exam.pass_marks:
            logging.info("Result: PASS")
        else:
            logging.info("Result: FAIL")

    @classmethod
    def update_pass_marks(cls, new_marks):
        cls.pass_marks = new_marks
        logging.info("Pass marks updated to %d", cls.pass_marks)

e1 = Exam("Harshini", 50)

e1.start_exam()
e1.submit_exam(35)

Exam.update_pass_marks(50)

e2 = Exam("Siri", 50)
e2.start_exam()
e2.submit_exam(20)
