from ventana_principal import *
from grapher import Grapher
import re
import os
import pattern_utils
import datetime
import main as mn


def parseTxt(text):
  """Parse a given txt file"""
  text = text.split()
  result_companies = []
  for word in text:
    if re.search(",$", word):
      result_companies.append(word[:-1])
    else:
      result_companies.append(word)
  return result_companies 


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
    self.setupUi(self)
    self.current_grapher = None
    self.historic_grapher = None
    self.companies = None
    self.isRunning = False
    self.checkboxes = [self.head_and_shoulders, self.ascending_triangle, self.descending_triangle, 
                                                            self.inv_head_and_shoulders, self.double_bottom, self.double_top]
    self.historicpatternsbtn.clicked.connect(self.PreRunProgram)
    self.currentpatternsbtn.clicked.connect(self.PreRunProgram)
    self.openfilebtn.clicked.connect(self.openTxt)

  def PreRunProgram(self):
    if self.isRunning:
      print('Already running')
      return
    if self.companies == None:
      print('Select companies')
      return
    if self.windowsize.text() == '' or int(self.windowsize.text()) < 80:
      print('select a valid windowsize')
      return
    if not isinstance(self.initialdate.date().toPyDate(), datetime.date) and not isinstance(self.enddate.date().toPyDate(), datetime.date):
      raise Exception('Enter a valid year format %dddd')
    selected_types_set = set()
    for checkbox in self.checkboxes:
      if checkbox.isChecked():
        selected_types_set.add(checkbox.objectName())
    self.runProgram(self.sender(), selected_types_set)

  def runProgram(self, button, selected_types):
    self.isRunning = True
    if button is None or not isinstance(button, QtWidgets.QPushButton):
        return  # Safety check
    windowsize = int(self.windowsize.text())
    patterns_dictionary = pattern_utils.loadPatterns(15, selected_types)
    historic_results = []
    current_results = []
    for company in self.companies:
      if button == self.historicpatternsbtn:
        historic_results = historic_results + mn.trainHistoricDatabase(company, patterns_dictionary, self.initialdate.date().toPyDate(), self.enddate.date().toPyDate(), windowsize)
      elif button == self.currentpatternsbtn:
        current_results = current_results + mn.findCurrentPatterns(company, patterns_dictionary, windowsize)
    self.isRunning = False
    if button == self.currentpatternsbtn:
      self.show_current_patterns(current_results)
    else:
      tendency_results = pattern_utils.calculateTendencyProbability(historic_results, selected_types)
      self.show_historic_patterns(historic_results, tendency_results)

  def show_historic_patterns(self, historic_results, tendency_results):
    self.historic_grapher = Grapher()
    self.historic_grapher.add_tendency_info(tendency_results)
    self.historic_grapher.plot_patterns(historic_results)
    self.historic_grapher.show()
  
  def show_current_patterns(self, current_results):
    self.current_grapher = Grapher()
    self.current_grapher.plot_patterns(current_results)
    self.current_grapher.show()
  
  def openTxt(self):
    options = QtWidgets.QFileDialog.Options()
    fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt)", options=options)
    if fileName:
      with open(fileName, 'r') as file:
        input_text = file.read()
        self.selectedfile.setText('Selected File: ' + os.path.basename(fileName))
        self.companies = parseTxt(input_text)



if __name__ == "__main__":
  app = QtWidgets.QApplication([])
  window = MainWindow()
  window.show()
  app.exec_()



    #self.Dialog = QtWidgets.QDialog()
    #self.ui = Ui_Dialog()
    #self.ui.setupUi(self.Dialog)
    #self.Dialog.show()
  

'''
        #add a label in the center and show the companies
        self.companiesLabel = QtWidgets.QLabel(self.centralwidget)    
            # Set the text of the label
        companies_text = ', '.join(self.companies)
        self.companiesLabel.setText(f"Companies: {companies_text}")
        # Position the label (you can adjust the geometry as needed)
        self.companiesLabel.setGeometry(QtCore.QRect(400, 420, 481, 30))  # Example position
        # Show the label
        self.companiesLabel.show()
'''