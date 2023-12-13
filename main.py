import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from tela import Ui_MainWindow
from operator import neg

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.zeroButton.clicked.connect(lambda: pressionado("0"))
        self.ui.umButton.clicked.connect(lambda: pressionado("1"))
        self.ui.doisButton.clicked.connect(lambda: pressionado("2"))
        self.ui.tresButton.clicked.connect(lambda: pressionado("3"))
        self.ui.quatroButton.clicked.connect(lambda: pressionado("4"))
        self.ui.cincoButton.clicked.connect(lambda: pressionado("5"))
        self.ui.seisButton.clicked.connect(lambda: pressionado("6"))
        self.ui.seteButton.clicked.connect(lambda: pressionado("7"))
        self.ui.oitoButton.clicked.connect(lambda: pressionado("8"))
        self.ui.noveButton.clicked.connect(lambda: pressionado("9"))
        self.ui.dotButton.clicked.connect(lambda: pressionado("."))
        self.ui.plusButton.clicked.connect(lambda: pressionado("+"))
        self.ui.minusButton.clicked.connect(lambda: pressionado("-"))
        self.ui.divisionButton.clicked.connect(lambda: pressionado("/"))
        self.ui.multiplicationButton.clicked.connect(lambda: pressionado("*"))
        self.ui.percentageButton.clicked.connect(lambda: pressionado("%"))
        self.ui.plusMinusButton.clicked.connect(lambda: pressionado("+-"))
        self.ui.equalButton.clicked.connect(lambda: resultado())
        self.ui.clearButton.clicked.connect(lambda: clearOutput())
        self.ui.backspaceButton.clicked.connect(lambda: backspace())

        def resultado():
            saida = self.ui.outputLabel.text()

            try:
                resposta = eval(saida) if not '%' in saida else float(saida[:-1]) / 100
                self.ui.outputLabel.setText(f"{resposta:.2f}")

            except:
                self.ui.outputLabel.setText("ERRO")


        def backspace():
            saida = self.ui.outputLabel.text()
            self.ui.outputLabel.setText(saida[:-1])
            if not len(saida[:-1]):
                clearOutput()

        def clearOutput(number="0"):
            self.ui.outputLabel.setText(str(number))

        self.operacoes = ['+', '-', '*', '/', '.','%']

        def pressionado(tecla):
            saida = self.ui.outputLabel.text()

            if 'ERRO' in saida:
                clearOutput(tecla)

            else:   
                if saida == "0":
                    saida = ""
                if tecla in self.operacoes and saida[-1] in self.operacoes:
                    saida = saida[:-1]
                    
                elif tecla == '+-':
                    saida = neg(float(saida))
                    
                    self.ui.outputLabel.setText(str(saida))
                    return
                
                saida += tecla
                self.ui.outputLabel.setText(saida)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())