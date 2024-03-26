# import necessary modules
import xml.etree.ElementTree as ET
from ChoiceImageQuestion import ChoiceImageQuestion
from ChoiceQuestion import ChoiceQuestion

# class for question structure
class XMLParser:

  # constructor (filepath)
  def __init__(self, filepath) -> None:
    self.filepath = filepath
    self.questions = list()
    
  
  # parse through xml file and return a list of question objects
  def parse(self) -> list():

    # Parse the XML file
    tree = ET.parse(self.filepath)
    root = tree.getroot()

    # Iterate through each 'question' element in the XML
    for question in root.findall('question'):
      # Extract the text of the question
      question_text = question.find('questionText').text.strip()
      
      # Extract the 'questionImage' element, if it exists
      question_image_element = question.find('questionImage')
      image_path = question_image_element.get('path').strip() if question_image_element is not None else None
      
      # Print the question text
      # print('Question:', question_text)
      
      # Print the image path if it exists
      if image_path is not None:
        # print('Image Path:', image_path)

        image_question = ChoiceImageQuestion()   # create image question object
        image_question.set_text(question_text)   # add question 
        image_question.set_image(image_path)     # add image path
      
        # Accessing answers
        for answer in question.findall('answer'):
            # Extract information about each answer
            is_correct = answer.get('correct', 'false')  # default to 'false' if 'correct' attribute is not present
            answer_text = answer.text.strip()

            image_question.add_choice(answer_text, is_correct)   #add current answer
            # print(f'\tAnswer (Correct: {is_correct}): {answer_text}')

        # Accessing answer comments
        answer_comments_element = question.find('answerComments')
        answer_comments = answer_comments_element.text.strip() if answer_comments_element is not None else None

        if answer_comments is not None:
            image_question.set_answer_comments(answer_comments)
            
        # print('Answer Comments:', answer_comments)

        # Add a newline for better readability between questions
        # print('\n')

        # append to list of questions
        self.questions.append(image_question)

      # if question does not have an image   
      else:

        choice_question = ChoiceQuestion()   # create choice question object
        choice_question.set_text(question_text)   # add question 
      
        # Accessing answers
        for answer in question.findall('answer'):
            # Extract information about each answer
            is_correct = answer.get('correct', 'false')  # default to 'false' if 'correct' attribute is not present
            answer_text = answer.text.strip()

            choice_question.add_choice(answer_text, is_correct)   #add current answer
            # print(f'\tAnswer (Correct: {is_correct}): {answer_text}')

        # Accessing answer comments
        answer_comments_element = question.find('answerComments')
        answer_comments = answer_comments_element.text.strip() if answer_comments_element is not None else None

        if answer_comments is not None:
            choice_question.set_answer_comments(answer_comments)
            
        # print('Answer Comments:', answer_comments)

        # Add a newline for better readability between questions
        # print('\n')

        # append to list of questions
        self.questions.append(choice_question)


    return self.questions

    # checks the users answers with the correct answers
    # and displays the results
  def check_user_answers(self) -> None:
      correct_count = 0

      for index, question in enumerate(self.questions):
          user_answer = self.user_answers.get(index)
          correct_answer = question.get_answer()

          if user_answer is not None and question.check_answer(user_answer):
              correct_count += 1

      print(f"Number of Correct Answers: {correct_count} out of {len(self.questions)}")

  
  # printing output
  # (always check ImageQuestion first since it is the subclass of ChoiceQuestion)
  def printing(self) -> None:
     for question in self.questions:
        
        #check the type of object to decide how to print data
        if isinstance(question, ChoiceImageQuestion):
          print('Question: ', question.get_question())
          print('Image: ', question.get_image())
          for answer in question.get_choices():
             print("Answer: " + answer)

          print("CORRECT ANSWER ==== " + question.get_answer())
          print("Comments: "+ question.get_comments())
          print('\n')
        
        elif isinstance(question, ChoiceQuestion):
          print('Question: ', question.get_question())
          for answer in question.get_choices():
             print("Answer: " + answer)

          print("CORRECT ANSWER ==== " + question.get_answer())
          print("Comments: "+ question.get_comments())
          print('\n')

           
