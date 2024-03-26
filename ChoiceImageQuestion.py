# import necessary modules
from ChoiceQuestion import ChoiceQuestion

# list of answers + question comments
class ChoiceImageQuestion(ChoiceQuestion):

  # constructor
  def __init__(self) -> None:
    super().__init__();       # temporary object from superclass (ChoiceQuestion)
    self.image_path = ""


  # set image from filepath + add to label element return it
  def set_image(self, filepath:str) -> None:
    self.image_path = filepath

  # @OVERRIDE ---------------------------------------$
  # add answer choices and if correct answer save seperately
  def add_choice(self, choice: str, correct: bool) -> None:
    super().add_choice(choice, correct)      # use method from superclass


  # @OVERRIDE ---------------------------------------$
  # set question comments
  def set_answer_comments(self, comments:str) -> None:
    super().set_answer_comments(comments)    # use method from superclass


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


  # @OVERRIDE ---------------------------------------$
  # get answer choices
  def get_choices(self) -> list():
    return self.choices                        # use method from superclass


  # @OVERRIDE ---------------------------------------$
  # get answer comments
  def get_comments(self) -> str:
    return super().get_comments()              # use method from superclass


  # get image filename
  def get_image(self) -> str:
    return self.image_path


  # display for the Choice Questions (POPULATE!!!!!!!!!)
  def display(self) -> None:
    return
