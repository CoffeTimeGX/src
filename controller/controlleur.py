import threading


class Controller :
    
    ''' Attributs '''
    
    
    
    ''' Constructor '''
    
    def __init__(self,simulator,ui) -> None:
        self.simulator = simulator
        self.ui = ui
        self.set_signals()
    
    
    ''' Public functions '''
    
    def set_signals(self):
        self.ui.next_button.clicked.connect(self.simulator.decode_next_line)
        self.simulator.registers_value_updated.connect(self.ui.update_ui_registers)
        self.simulator.pc_updated.connect(self.ui.update_ui_pc)
        
        self.ui.start_button.clicked.connect(self._thread_run_function)
    # def update_registers_ui(self):
    
    def _thread_run_function(self):
        self.ui.start_button.setEnabled(False)
        self.ui.next_button.setEnabled(False)
        data_sender_thread = threading.Thread(target=self.simulator.run)
        data_sender_thread.start()
        
    
    
    ''' Private functions '''