import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)
           
        names = ['cls', 'Bck',  '' ,  'Close',
                 '7'  ,   '8',  '9',  '/'    ,
                 '4'  ,   '5',  '6',  '*'    ,
                 '1'  ,   '2',  '3',  '-'    ,
                 '0'  ,   '.',  '=',  '+'    ]

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Calculator")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())