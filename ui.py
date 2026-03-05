from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz :QuizBrain ):
        self.quiz = quiz
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzes")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas = Canvas(width=350,height=300,bg="white",)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.ques_t = self.canvas.create_text(175,150,text="some ramdom text",fill="Black",font=("Arial",20,"italic"),width=280)
        true_button = PhotoImage(file="./images/true.png")
        false_button = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_button,highlightthickness=0,border=0,command=self.get_correct_ans)
        self.true_button.grid(column=1,row=2,pady=15)

        self.false_button = Button(image=false_button,highlightthickness=0,border=0,command=self.wrong_ans)
        self.false_button.grid(column=0,row=2,pady=15)

        self.score_text = Label(text=f"score:{self.score}", font=("Arial", 20, "italic"), bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0, pady=10)

        self.next_question_interface()
        self.window.mainloop()

    def next_question_interface(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.ques_t, text= q_text)

        else:
            self.canvas.itemconfigure(self.ques_t,text="You've Reached the end of the Quiz ")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def get_correct_ans(self):
        self.feedback(self.quiz.check_answer("True"))



    def wrong_ans(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self,is_right):
        if is_right:
            self.score += 1
            self.score_text.config(text=f"score:{self.score}")
            self.canvas.config(bg="#90EE90")
            self.window.after(1000, self.next_question_interface)

        else:
            self.canvas.config(bg="#DC143C")
            self.window.after(1000, self.next_question_interface)





