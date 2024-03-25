""" main """
import sys
from PySide2.QtWidgets import QApplication

from assembler.assembler import Assembler
from simulator.simulator import Simulator
from user_interface.ui import MainWindow
from controller.controlleur import Controller
from terminal import terminal as tr
from ui_input import GUI_path, getpath

in_pathname = None
if len(sys.argv) != 1:  # S'il y a un seul argument, ça veut dire que l'on a appelé l'exécutable, donc pas besoin de gérer les arguments du terminal
    in_pathname, out_pathname = tr()
else: # On appelle donc l'interface utilisateur de récupération des chemins de répertoire
    out_pathname = GUI_path()+"/bin_file.txt"
    in_pathname  = getpath()


# Assembleur
assembler = Assembler(input_filename=in_pathname,output_filename=out_pathname)
assembler.encode()

# UI
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()

# Simulateur
simulator = Simulator(input_filename="bin_file.txt")
# simulator.decode_text()

controller = Controller(simulator,main_window)
controller.simulator.load_memory("init_registers.txt")


sys.exit(app.exec_())