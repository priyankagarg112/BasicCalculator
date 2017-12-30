from PyQt4.QtGui import *
import sys



class Calculator:
    def __init__(self):
        print "Inside init"
        app = QApplication(sys.argv)
        widget = QWidget()
        widget.resize(600,300)
        self.input1 = QLineEdit("", widget)
        self.input1.move(100,40)
        self.input2 = QLineEdit("", widget)
        self.input2.move(100,80)
        clckadd = QPushButton("ADD", widget)
        clckadd.move(400,20)
        self.clcksub = QPushButton("SUBTRACT", widget)
        self.clcksub.move(400,70)
        self.clckmul = QPushButton("MULTIPLY", widget)
        self.clckmul.move(400,140)
        self.clckdiv = QPushButton("DIVIDE", widget)
        self.clckdiv.move(400,210)
        self.label = QLabel("", widget)
        self.label.move(100,150)
        self.label.setFixedWidth(200)
        widget.show()
        clckadd.clicked.connect(self.addition)
        sys.exit(app.exec_())

    def addition(self):
        num1 = int(self.input1.text())
        num2 = int(self.input2.text())
        self.label.setText("Addition is: "+str(num1+num2))

    def subtraction(self):
        num1 = int(self.input1.text())
        num2 = int(self.input2.text())
        self.label.setText("Subtraction is: "+str(num1-num2))

    def multiplication(self):
        num1 = int(self.input1.text())
        num2 = int(self.input2.text())
        self.label.setText("Multiplication is: "+str(num1*num2))

    def division():
        num1 = int(self.input1.text())
        num2 = int(self.input2.text())
        self.label.setText("Division is: "+str(num1/num2))


c=Calculator()
