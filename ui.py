import sys
from PySide2.QtWidgets import QMainWindow,QLabel,QPushButton,QLineEdit,QHBoxLayout,QVBoxLayout,QApplication,QFrame
from PySide2.QtCore import QObject, Signal

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self._set_registers_widgets()
        self._set_menu_widgets()
        
        self.main_layout = QVBoxLayout()
        self.main_frame = QFrame()
        self.main_frame.setLayout(self.main_layout)
        
        self.main_layout.addWidget(self.registers_frame)
        self.main_layout.addWidget(self.menu_frame)
        
        self.setCentralWidget(self.main_frame)
        
    
    def _set_registers_widgets(self):
        """ Set widget """
        self.label_register_list = []
        self.lineedit_register_list = []
        self.layout_register_list = []
        self.registers_layout_left = QVBoxLayout()
        self.registers_layout_center_left = QVBoxLayout()
        self.registers_layout_center_right = QVBoxLayout()
        self.registers_layout_right = QVBoxLayout()
        
        for i in range(32):
            self.label_register_list.append(QLabel(f"R{i}"))
            self.lineedit_register_list.append(QLineEdit(f""))
            self.layout_register_list.append(QHBoxLayout())
            
            self.layout_register_list[i].addWidget(self.label_register_list[i])
            self.layout_register_list[i].addWidget(self.lineedit_register_list[i])
            
        for j in range(8):
            self.registers_layout_left.addLayout(self.layout_register_list[j])
            self.registers_layout_center_left.addLayout(self.layout_register_list[j+8])
            self.registers_layout_center_right.addLayout(self.layout_register_list[j+16])
            self.registers_layout_right.addLayout(self.layout_register_list[j+24])
            
            
        self.registers_layout = QHBoxLayout()
        self.registers_layout.addLayout(self.registers_layout_left)
        self.registers_layout.addLayout(self.registers_layout_center_left)
        self.registers_layout.addLayout(self.registers_layout_center_right)
        self.registers_layout.addLayout(self.registers_layout_right)
        self.registers_frame = QFrame()
        self.registers_frame.setLayout(self.registers_layout)
        
        
    def _set_menu_widgets(self):
        self.next_button = QPushButton("Étape suivante")
        self.stop_button = QPushButton("STOP")
        self.start_button = QPushButton("START")
        
        self.menu_layout = QHBoxLayout()
        self.menu_layout.addWidget(self.next_button)
        self.menu_layout.addWidget(self.stop_button)
        self.menu_layout.addWidget(self.start_button)
        self.menu_frame = QFrame()
        self.menu_frame.setLayout(self.menu_layout)
            
       
    def _set_signal(self):
        self.next_instruction_signal = Signal(list)
        
        
             
if __name__ == "__main__" : 
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
  
    print('done')