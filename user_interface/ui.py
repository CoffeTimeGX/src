import sys
from PySide2.QtWidgets import QMainWindow,QLabel,QPushButton,QLineEdit,QHBoxLayout,QVBoxLayout,QApplication,QFrame,QSpacerItem,QSizePolicy
from PySide2.QtCore import QObject, Signal, Slot


class MainWindow(QMainWindow):
    
    lineedit_register_list = []
    
    def __init__(self):
        super().__init__()
        self._set_registers_widgets()
        self._set_menu_widgets()
        self._set_header_widget()
        
        self.main_layout = QVBoxLayout()
        self.main_frame = QFrame()
        self.main_frame.setLayout(self.main_layout)
        
        self.main_layout.addWidget(self.header_frame)
        self.main_layout.addWidget(self.registers_frame)
        self.main_layout.addWidget(self.menu_frame)
        
        self.setCentralWidget(self.main_frame)
    
    @Slot(list)
    def update_ui_registers(self,registers:list) -> None:
        ''' Update all registers line edit '''
        
        for reg in range(32):
            reg_value = str(registers[reg])
            self.lineedit_register_list[reg].setText(reg_value)
        
    @Slot(int)
    def update_ui_pc(self,pc:int) -> None :
        self.pc_line_edit.setText(str(pc))

        
    
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
        self.pc_line_edit = QLineEdit("0")
        self.pc_label = QLabel("PC :")
        
        pc_layout = QHBoxLayout()
        pc_layout.addWidget(self.pc_label)
        pc_layout.addWidget(self.pc_line_edit)
        
        next_layout = QVBoxLayout()
        next_layout.addWidget(self.next_button)
        next_layout.addLayout(pc_layout)
        
        menu_layout = QHBoxLayout()
        menu_layout.addLayout(next_layout)
        menu_layout.addWidget(self.stop_button)
        menu_layout.addWidget(self.start_button)
        menu_layout.addItem(QSpacerItem(QSizePolicy.Expanding, QSizePolicy.Expanding))
        
        
        # menu_layout = QVBoxLayout()
        # menu_layout.addLayout(next_layout)
        # menu_layout.addLayout(button_layout)
        
        self.menu_frame = QFrame()
        self.menu_frame.setLayout(menu_layout)
            
    def _set_header_widget(self):
        
        self.header_frame = QFrame(self)
        self.header_frame.setFrameShadow(QFrame.Raised)

        # Création des labels
        titre_label = QLabel("Nom de l'Application")
        titre_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        sous_titre1_label = QLabel("Arnaud Bleunven")
        sous_titre1_label.setStyleSheet("font-size: 18px;")

        sous_titre2_label = QLabel("Hamza Talha Naciri")
        sous_titre2_label.setStyleSheet("font-size: 18px;")

        # Création du layout pour le QFrame
        header_layout = QVBoxLayout()
        header_layout.addWidget(titre_label)
        header_layout.addWidget(sous_titre1_label)
        header_layout.addWidget(sous_titre2_label)
        self.header_frame.setLayout(header_layout)

if __name__ == "__main__" : 
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
  
    print('done')