from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 478)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn1 = QtWidgets.QPushButton(Form)
        self.btn1.setObjectName("btn1")
        self.horizontalLayout.addWidget(self.btn1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setObjectName("t2")
        self.horizontalLayout_2.addWidget(self.t2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.t3 = QtWidgets.QLineEdit(Form)
        self.t3.setObjectName("t3")
        self.horizontalLayout_3.addWidget(self.t3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.btn2 = QtWidgets.QPushButton(Form)
        self.btn2.setObjectName("btn2")
        self.horizontalLayout_3.addWidget(self.btn2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.t4 = QtWidgets.QLineEdit(Form)
        self.t4.setObjectName("t4")
        self.horizontalLayout_4.addWidget(self.t4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.btn1.clicked.connect(self.findbook)
        self.btn2.clicked.connect(self.total)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Book Title"))
        self.btn1.setText(_translate("Form", "Find Book"))
        self.label_2.setText(_translate("Form", "Price Rs."))
        self.label_3.setText(_translate("Form", "Quantity"))
        self.btn2.setText(_translate("Form", "Total"))
        self.label_4.setText(_translate("Form", "Total Amount Rs."))

    def findbook(self):
        mybook=sqlite3.connect('bookstores.db')
        mycursor=mybook.cursor()
        title=self.t1.text()
        sql="SELECT * FROM book WHERE Title='"+title+"';"
        x=mycursor.execute(sql)

        if x!=None:
            mycursor.execute("SELECT Price FROM book WHERE Title='"+title+"'")
            y=mycursor.fetchone()
            
            price=(y[0])
            self.t2.setText(str(price))
        else:
            output = 'Book Not Found' 
            self.t2.setText(output)

    def total(self):
        mybook=sqlite3.connect('bookstores.db')
        mycursor=mybook.cursor()        
        qnty=int(self.t3.text())
        title=self.t1.text()
        mycursor.execute("SELECT Price FROM book WHERE Title='"+title+"'")
        y=mycursor.fetchone()
            
        price=(y[0])        
        self.t4.setText(str(price*qnty))
        
                
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

