# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_imagenes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1172, 827)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1148, 768))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Exit"))
   
    def add(self):
        '''
        #sc = MplCanvas(self, width=5, height=4, dpi=100)
        #sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
       
        for i in range(1,10):
            #object = QtWidgets.QLabel("TextLabel")
            #self.verticalLayout_5.addWidget(object)
            sc = MplCanvas(self, width=5, height=4, dpi=100)
            sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
            self.verticalLayout_5.addWidget(sc)
        '''
        total_height = 0
        for i in range(1, 10):
            sc = MplCanvas(self, width=5, height=4, dpi=100)
            sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        
        # Establece el tamaño mínimo de cada gráfica para evitar que se reduzca
            sc.setMinimumSize(500, 400)  # Ajusta estos valores según tus necesidades

        # Añade la gráfica al layout
            self.verticalLayout_5.addWidget(sc)

        # Actualiza la altura total del contenedor
            total_height += 400  # Asegúrate de que este valor coincida con el tamaño mínimo de la gráfica
    # Establece el tamaño mínimo del contenedor de las gráficas
        self.scrollAreaWidgetContents_4.setMinimumSize(QtCore.QSize(500, total_height))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.add()

    Form.show()
    sys.exit(app.exec_())



