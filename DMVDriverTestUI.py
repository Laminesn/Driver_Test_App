from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ChoiceImageQuestion import ChoiceImageQuestion
from ChoiceQuestion import ChoiceQuestion


class DMVDriverTestUI(QWidget):
    def __init__(self, questions) -> None:
        super().__init__()
        self.questions = questions
        self.current_question_index = 0
        self.num_correct = 0

        self.setGeometry(500, 200, 800, 575)
        self.setWindowTitle("DMV Driver's Test")

        # to use pyqt create a window, insert a layout inside based on needs
        # within layout add elements based on needs and display elements
        # for specialized cases make a layout of layouts(nested) and add elements
        # after populating each layout append to master layout for final result

        # Grid LAYOUT format (ELement to Add, x, y, xspan, yspan)
        master_layout = QVBoxLayout(self)

        # Layout for Image (if needed ONLY)
        if type(self.questions[0]).__name__ is not ChoiceQuestion:
          self.pixmap = QPixmap(self.questions[0].get_image())  # create image element by passing filename
          self.pixmap = self.pixmap.scaled(800, 400, Qt.KeepAspectRatio, Qt.FastTransformation)
          self.image_label = QLabel()
          self.image_label.setPixmap(self.pixmap)  # set picture to label
          master_layout.addWidget(self.image_label, alignment=Qt.AlignTop)

        # Layout for Question + RadioButton + Comments
        layout2 = QVBoxLayout()
        self.question_label = QLabel(wordWrap=True)   # create label with question
        self.question_label.setText(self.questions[0].get_question())
        self.question_label.setStyleSheet("font-weight: bold; font-size:18px")   # Make label bolded
        layout2.addWidget(self.question_label)   # add to layout as widget

        choices = self.questions[0].get_choices()   # get answer choices, choices is a list
        self.answer_group = QButtonGroup(self)   # make group of answer buttons
        self.answer_group.setExclusive(False)

        for i, choice in enumerate(choices):   # create radio button with answers
            radio_button = QRadioButton(choice)
            radio_button.setStyleSheet("font-size:13px")
            radio_button.clicked.connect(self.on_item_clicked)
            layout2.addWidget(radio_button)   # add to layout
            self.answer_group.addButton(radio_button, i)

        self.comments_label = QLabel(wordWrap=True)   # create label with comments
        # self.comments_label.resize(800, 400)
        layout2.addWidget(self.comments_label)   # add to layout as widget
        layout2.addStretch(1)
        master_layout.addLayout(layout2)

        # Layout for Status bar + Next button + Quit button
        layout3 = QHBoxLayout()

        # create Label with question number and correct number
        self.question_number_label = QLabel(f"Question {self.current_question_index + 1} of {len(self.questions)}")
        self.correct_number_label = QLabel("Correct: 0/40")
        
        # add to layout
        layout3.addWidget(self.question_number_label)
        layout3.addWidget(self.correct_number_label)

        # create next button and link to next function below to display next question
        next_button = QPushButton("Next Question")
        next_button.setGeometry(0, 0, 800, 0)
        next_button.clicked.connect(self.next_click)
        layout3.addWidget(next_button)

        # create quit button and link to quit function to quit quiz
        quit_button = QPushButton("Quit Quiz")
        quit_button.setGeometry(0, 0, 800, 0)
        quit_button.clicked.connect(self.quit_click)
        layout3.addWidget(quit_button)

        master_layout.addLayout(layout3)
        self.setLayout(master_layout)   # set the shown layout in your window to the completed master layout

    def on_item_clicked(self):

      selected_answer_index = self.answer_group.checkedId()

      # Make the other answers unselectable
      for i in range(4):
        if i is not selected_answer_index:
          self.answer_group.button(i).setCheckable(False)
      
      # Update the comments label based on the selected answer
      selected_answer = self.questions[self.current_question_index].get_choices()[selected_answer_index]
      self.comments_label.setText(f"{self.questions[self.current_question_index].get_comments()}")

      self.check_answer()
      return


    def next_click(self):
        # Check if an answer is selected before moving to the next question
        if self.answer_group.checkedButton() is None:
            QMessageBox.warning(self, "Warning", "Please select an answer before moving to the next question.")
            return

        # Record the answer (you might want to save it somewhere if needed)
        selected_answer_index = self.answer_group.checkedId()
        selected_answer = self.questions[self.current_question_index].get_choices()[selected_answer_index]
        # print(f"User Answer to Question {self.current_question_index + 1}: {selected_answer}")

        # Move to the next question
        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.update() # Update the image, question, and answer choices
        else:
            # If no more questions, show a message or handle the end of the quiz

            num = str(self.num_correct)
            end = "Thank you for completing the quiz. You got " + num + " questions out of 40 correct"
            QMessageBox.information(self, "Quiz Completed", end)
            self.quit_click()


    # update the display to show next question
    def update(self) -> None:

      if type(self.questions[self.current_question_index]) is not ChoiceQuestion:
        self.pixmap = QPixmap(self.questions[self.current_question_index].get_image())
        self.pixmap = self.pixmap.scaled(800, 400, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.image_label.setPixmap(self.pixmap)
      else:
        self.pixmap = QPixmap()
        self.image_label.setPixmap(self.pixmap)

      self.question_label.setText(self.questions[self.current_question_index].get_question())
      choices = self.questions[self.current_question_index].get_choices()
      for i, choice in enumerate(choices):
        self.answer_group.button(i).setChecked(False)
        self.answer_group.button(i).setText(choice)
        self.answer_group.button(i).setCheckable(True)

      # Update the question number label
      self.question_number_label.setText(f"Question {self.current_question_index + 1} of {len(self.questions)}")
      self.comments_label.setText(f" ")
      self.correct_number_label.setText(f"Correct: {self.num_correct}/40")
      return

    def quit_click(self):
        # self.results()
        self.close()


    def check_answer(self):
        try:
            # Check which radio button is selected
            selected_answer = None
            for radio_button in self.answer_group.buttons():
                if radio_button.isChecked():
                    selected_answer = radio_button.text()

            # Check if an answer is selected
            if selected_answer is not None:
                # Check the correctness of the answer
                selected_answer_index = self.answer_group.checkedId()
                if self.questions[self.current_question_index].check_answer(selected_answer) is True:
                  self.num_correct += 1
            else:
                QMessageBox.warning(self, "Warning", "Please select an answer before checking.")
        except Exception as e:
            print(f"Error in check_answer: {e}")

    def results(self):
        # Display quiz results (you might want to implement this)
        self.correct_number_label.setText(f"Correct: {self.num_correct}")  # Replace 1 with the actual number of correct answers