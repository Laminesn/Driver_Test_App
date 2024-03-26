# Author: Lamine Deen
# Project: Driver License Test + GUI

from DMVDriverTestUI import DMVDriverTestUI
from XMLParser import XMLParser
from PyQt5.QtWidgets import QApplication
import sys


def main ():
  # Create a QApplication object, which manages the GUI application's control flow
  app = QApplication(sys.argv)

  # xml filepath
  xml_filepath = "florida_drivers_test.xml"
  # Create an instance of the XMLParser class and return a list of question objects
  parser = XMLParser(xml_filepath)
  questions = parser.parse()
  # parser.printing()      # remove when done
  # Create instance of DMVDriver class and show UI to user
  driver_UI = DMVDriverTestUI(questions)
  driver_UI.show()
  # Start the application's event loop and exit when the window is closed
  sys.exit(app.exec_())


main()
