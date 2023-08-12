from tkinter import *

from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window= Tk()
        self.window.title("QuizzJizz")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)

        self.score_label = Label(text = "Score: 0", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row = 0, column=1)

        self.canvas = Canvas(width=300, height=250, bg = "white")
        self.question_text = self.canvas.create_text(150, 125,text = "Some Question Text", fill = THEME_COLOR, font = ("Arial", 17, "italic"), width = 280)
        self.canvas.grid(row = 1, column =0, columnspan=2, pady = 50)
        trueimage = PhotoImage(file=r'C:\udemy projects\quizzler\images\true.png')
        falseimage = PhotoImage(file=r'C:\udemy projects\quizzler\images\false.png')
        self.true_button = Button(image = trueimage, highlightthickness=0, command=self.yes)
        self.false_button = Button(image = falseimage, highlightthickness=0, command = self.no)
        
        self.true_button.grid(row=2, column=1)
        self.false_button.grid(row=2, column=0)

        self.get_next_q()

        self.window.mainloop()


    def get_next_q(self):
        self.canvas.config(bg= "white")

        if self.quiz.still_has_questions():
            next_q = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_q)
            self.score_label.config(text = f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text ="End of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def yes(self):
        self.give_feedback(self.quiz.check_answer("true"))



    def no(self):
        self.give_feedback(self.quiz.check_answer("false"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_q)
