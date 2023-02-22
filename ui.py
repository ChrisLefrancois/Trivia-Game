from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.score = 0
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label()
        self.score_label.config(text=f"Score: {self.score}", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Amazon required blah blah",
            fill="black",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        self.right_image = PhotoImage(file="./images/true.png")
        self.wrong_image = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=self.right_image, highlightbackground=THEME_COLOR, command=self.right_answer)
        self.false_button = Button(image=self.wrong_image, highlightbackground=THEME_COLOR, command=self.wrong_answer)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reach the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def right_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



