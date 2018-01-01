from PyQt4.QtGui import *
import sys



class Calculator:
    def __init__(self):
        app = QApplication(sys.argv)
        widget = QWidget()
        widget.resize(600,300)
        self.input1 = QLineEdit("", widget)
        self.input1.move(100,40)
        self.input2 = QLineEdit("", widget)
        self.input2.move(100,80)
        clckadd = QPushButton("ADD", widget)
        clckadd.move(400,20)
        clcksub = QPushButton("SUBTRACT", widget)
        clcksub.move(400,70)
        clckmul = QPushButton("MULTIPLY", widget)
        clckmul.move(400,140)
        clckdiv = QPushButton("DIVIDE", widget)
        clckdiv.move(400,210)
        self.label = QLabel("", widget)
        self.label.move(100,150)
        self.label.setFixedWidth(200)
        widget.show()
        clckadd.clicked.connect(self.addition)
        clcksub.clicked.connect(self.subtraction)
        clckmul.clicked.connect(self.multiplication)
        clckdiv.clicked.connect(self.division)
        sys.exit(app.exec_())

    def addition(self):
        var1 = str(self.input1.text())
        var2 = str(self.input2.text())
        if self.check(var1,var2):
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.label.setText("Addition is: "+str(num1+num2))

    def subtraction(self):
        var1 = str(self.input1.text())
        var2 = str(self.input2.text()) 
        if self.check(var1,var2):
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.label.setText("Subtraction is: "+str(num1-num2))

    def multiplication(self):
        var1 = str(self.input1.text())
        var2 = str(self.input2.text())
        if self.check(var1,var2):
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.label.setText("Multiplication is: "+str(num1*num2))

    def division(self):
        var1 = str(self.input1.text())
        var2 = str(self.input2.text())
        if self.check(var1,var2):
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.label.setText("Division is: "+str(num1/num2))
   
    def check(self,var1,var2):
        if not (var1.isdigit() and var2.isdigit()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            self.label.setText(" ")
            msg.setText("This works only for integer values")
            ret = msg.exec_()
            return False
        return True


c=Calculator()
