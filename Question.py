# class for question structure
class Question:

  # constructor
  def __init__(self) -> None:
    self.question_text = ""
    self.answer = ""


  # set question
  def set_text(self, question:str) -> None:
    self.question_text = question


  # set correct answer
  def set_answer(self, correct:str) -> None:
    self.answer = correct


  # check correct answer from user selected
  def check_answer(self, selected:str) -> bool:
    if self.answer == selected:
      return True
    else:
      return False


  # get question
  def get_question(self) -> str:
    return self.question_text


  # get answer
  def get_answer(self) -> str:
    return self.answer


  # display for the Questions (POPULATE!!!!!!!!!)
  def display(self) -> None:
    return
