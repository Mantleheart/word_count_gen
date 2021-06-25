from PySide2.QtWidgets import QFileDialog, QProgressDialog, QWidget, QMessageBox, QApplication, QGridLayout, QPushButton, QTextEdit, QGroupBox
from PySide2 import QtCore, QtGui
import docu_analyzer
import sys
import csv



class app(QWidget):
    def __init__ (self):
        super(app, self).__init__()
 
        self.title = "Document Analyzer"
        self.left = 10
        self.top = 10
        self.width = 100
        self.height = 300
        self.make_ui()

        


    def open_dir(self, target):
        fileName = QFileDialog()
        filenames = list()
        if fileName.exec_():
            fileNames = fileName.selectedFiles()
            target.setText(fileNames[0])

    def make_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.create_layout()

        self.go = QPushButton("Analyze")
        self.go.clicked.connect(lambda: self.begin_task())
        self.output = QTextEdit()
        self.output.setText("Output (Nothing yet)")
        
        window_layout = QGridLayout()
        window_layout.setAlignment(QtCore.Qt.AlignTop)
        window_layout.addWidget(self.box0,1,1,1,1)
        window_layout.addWidget(self.go,2,1,1,1)
        window_layout.addWidget(self.output,3,1,1,1)
        
        self.setLayout(window_layout)
        
        self.show()


    def create_layout(self):
        self.box0 = QGroupBox("Options")
        self.current_file = QTextEdit()
        self.current_file.setText("None selected")

        self.current_file.setFixedSize(200,30)
        self.current_file.layout()
        layout = QGridLayout()
        self.box0.setLayout(layout)
        
        self.file_finder = QPushButton("Select File")
        self.file_finder.setToolTip("Click here to select the file you would like to analyze.")
        self.file_finder.clicked.connect(lambda: self.open_dir(self.current_file))
        layout.addWidget(self.current_file, 0, 0,1, 1)
        layout.addWidget(self.file_finder, 1, 0, 1, 1)

        
        
    def begin_task(self):
        print("Beginning Analysis...")
        self.output.setText(docu_analyzer.analyze(self.current_file.toPlainText()))
        

App = QApplication(sys.argv)
ex = app()
sys.exit(App.exec_())

