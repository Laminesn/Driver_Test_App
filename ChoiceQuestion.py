# import necessary modules
from Question import Question

# list of answers + question comments
class ChoiceQuestion(Question):

  # constructor
  def __init__(self) -> None:
    super().__init__()       # temporary object from superclass (Question)
    self.choices = list()
    self.comments = ""


  # add answer choices and if correct answer save seperately
  def add_choice(self, choice: str, correct: bool) -> None:
    self.choices.append(choice)

    if correct == "true":               # if correct save answer in superclass attribute
      super().set_answer(choice)


  # set question comments
  def set_answer_comments(self, comments:str) -> None:
    self.comments = comments


  # @OVERRIDE ---------------------------------------$
  # set question 
  def set_text(self, question:str) -> None:
    super().set_text(question)                # use method from superclass
  

  # @OVERRIDE ---------------------------------------$
  # get question
  def get_question(self) -> str:
    return super().get_question()             # use method from superclass


  # @OVERRIDE ---------------------------------------$
  # get answer
  def get_answer(self) -> str:
    return super().get_answer()                # use method from superclass


  # @OVERRIDE ---------------------------------------$
  # check correct answer from user selected
  def check_answer(self, selected:str) -> bool:
    return super().check_answer(selected)      # use method from superclass


  # get answer choices
  def get_choices(self) -> list():
    return self.choices


  # get answer comments
  def get_comments(self) -> str:
    return self.comments


  # display for the Choice Questions (POPULATE!!!!!!!!!)
  def display(self) -> None:
    return

