import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QWidget, QPlainTextEdit, QGroupBox, QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView
from Codigo import Codigo

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        QMainWindow.setWindowFlags(self,Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Simulador")
        self.setWindowIcon(QIcon("Imagenes/venadocolaBlanca.png"))
        self.resize(800,580)
        
        self.fondoMainWindow()
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.codigo = Codigo("Codigo.txt")
        self.grupoDeComponentes()
        self.separadores()
        self.ptEjecutar.clicked.connect(self.prueba)

    def prueba(self):
        fileW = open("Codigo.txt","w")
        fileW.write(self.cuadroDeTexto.toPlainText())
        fileW.close()
        self.codigo = Codigo("Codigo.txt ")
        self.codigo.exec_data(self.codigo.registro["lineaData"])
        print(self.codigo.ram)
        

    def fondoMainWindow(self):
        fondo = QLabel(self)
        fondo.setGeometry(QRect(-30,0,860,580))
        imagen = QPixmap("Imagenes/fondoMain1.png") 
        fondo.setPixmap(imagen)
        fondo.setScaledContents(True)

    def grupoDeComponentes(self):
        self.grupoDeComponentes = QGroupBox(self.centralwidget)
        self.grupoDeComponentes.setGeometry(QRect(0,0,800,580))
        self.plainText(self.grupoDeComponentes)
        self.tablas(self.grupoDeComponentes)
        self.botones(self.grupoDeComponentes)

    
    def plainText(self, espacio):
        self.cuadroDeTexto = QPlainTextEdit(espacio)
        self.cuadroDeTexto.setGeometry(QRect(200,10,400,380))
        self.cuadroDeTexto.setPlainText("""

        """)
        self.resultado = QPlainTextEdit(espacio)
        self.resultado.setGeometry(QRect(10,440,780,125))
        self.resultado.setReadOnly(True)
        self.resultado.setPlainText("""QtARMSim version 0.4.16
(c) 2014-19 Sergio Barrachina Mir
Developed at the Jaume I University, Castellón, Spain.

Connected to ARMSim (ARMSim version info follows).
V 1.4
(c) 2014 Germán Fabregat
ATC - UJI

C:/Users/jean6/OneDrive/Escritorio/UNAH/Clases_IP_2020/Arquitectura/SegundoParcial/cap5/borrar.s assembled. 
Assembly errors:
Símbolo «bytekhk» no definido.
                                    """)
    def tablas(self, espacio):
        self.tablaRegistros = QTableWidget(espacio)
        self.tablaRegistros.setGeometry(QRect(10,10,145,380))
        self.tablaRegistros.setColumnCount(1)
        self.tablaRegistros.setRowCount(16)   
        nombreFilas=[]
        for x in range(0,16):
            nombreFilas.append("r%s"%x)
            self.tablaRegistros.setItem(x,0,QTableWidgetItem("0x00000000"))
        self.tablaRegistros.setVerticalHeaderLabels(nombreFilas)
        nombreColumna = ["Registros"]
        self.tablaRegistros.setHorizontalHeaderLabels(nombreColumna)
        self.tablaRegistros.setAlternatingRowColors(True)
        self.tablaRegistros.setSelectionMode(QAbstractItemView.SingleSelection)#Seleccionar una celda a la vez

        self.tablaMemoria = QTableWidget(espacio)
        self.tablaMemoria.setGeometry(QRect(635,10,145,380))
        self.tablaMemoria.verticalHeader().setVisible(False)
        self.tablaMemoria.setColumnCount(1)
        self.tablaMemoria.setRowCount(40)
        fila=0
        for key in self.codigo.ram:
            self.tablaMemoria.setItem(fila,0,QTableWidgetItem(key))
            fila+=1
        self.tablaMemoria.setAlternatingRowColors(True)
        nombreColumna = ["Memoria RAM"]
        self.tablaMemoria.setHorizontalHeaderLabels(nombreColumna)
        self.tablaMemoria.setColumnWidth(0,140)
        self.tablaMemoria.setSelectionMode(QAbstractItemView.SingleSelection)#Seleccionar una celda a la vez

    
    def botones(self, espacio):
        self.ptNuevo = QPushButton(espacio)
        self.ptNuevo.setText("Nuevo")
        self.ptNuevo.setGeometry(QRect(200,400,200,35))
        self.ptNuevo.setIcon(QIcon("Imagenes/signs.png"))

        self.ptEjecutar = QPushButton(espacio)
        self.ptEjecutar.setText("Ejecutar")
        self.ptEjecutar.setGeometry(QRect(405,400,195,35))
        self.ptEjecutar.setIcon(QIcon("Imagenes/computer.png"))

    def separadores(self):
        line=QFrame(self)                          
        line.setGeometry(QRect(165,20,20,350))     
        line.setFrameShape(QFrame.VLine)           
        line.setFrameShadow(QFrame.Raised)         
        #line.setLineWidth(2)                     

        line2=QFrame(self)                          
        line2.setGeometry(QRect(610,20,20,350))     
        line2.setFrameShape(QFrame.VLine)          
        line2.setFrameShadow(QFrame.Raised)         

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()

