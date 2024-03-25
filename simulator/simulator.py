from simulator.opcode import Opcode
from compiler_soft import CompilerSoftware
from assembler.commands.jump import JUMP
from assembler.commands.stop import STOP
import time



class Simulator(CompilerSoftware) :
    
    """ Attributs """
    
    general_counter:int = 0
    local_counter:int = 0
    start_time:int = 0
    pc:int = 0
    registers:list = []
    is_running:bool = True
    
    """ Class constructor """
    
    def __init__(self,input_filename:str) -> None:
        """ 
        Class constructor.
        
        Args:
            input_filename (str) : the pathname of a binary file with instructions.
            
        Example:
            simulator = Simulator("bin_file.txt")
        """
        super().__init__()
        self._init_register()
        
        with open(input_filename,'r') as file:
            self.input_file = file.readlines()
        
    
    """ Public functions """
    
    def load_memory(self,pathname:str) -> None:
        """
        Load values of registers from a txt file.
        
        Args:
            pathname (str): exemple : init_registers.txt
            
        Example:
            simulator.load_memory(pathname='init_registers.txt')
        """
        i = 0
        with open(pathname,"r") as f:
            for ligne in f :
                self.registers[i] = int(ligne)
                i += 1     
        self.registers_value_updated.emit(self.registers)
        
    
    def run(self) -> None:
        """
        Run the program until STOP instruction.
        """
        self.start_time = time.time()
        
        while(self.is_running):
            self.decode_next_line()

    
    def decode_next_line(self) -> list :
        """ 
        Decode the next instruction.
        Send the signal 'registers_value_updated' with list of new registers.
        Send the signal 'pc_updated' with new pc value.

        Return the new register value.
        
        Example : 
            simulator.decode_next_line()
            >>> [0,0,1,0,64,...]
        """
        
        index_instruction = self.pc
        self.pc += 1
        
        # Line = 0x12345678 0x12345678 : index instruction + instruction
        line = self.input_file[index_instruction]
        index_instruction = int(line[2:10],16)
        instruction = int(line[13:-1],16)
        
        # Opcode always on 20 first bits (between digit 27 and 31)
        opcode = instruction >> 27
        current_command = self.instruction_dictionary[self.opcode_map[opcode]]

        if (isinstance(current_command,JUMP)) : # Current command is a JUMP ?
            self.pc = current_command.extract_pc(instruction,self.registers) # Request new PC
        elif (isinstance(current_command,STOP)) : # Current command is a STOP ?
            self.is_running = False
            return self.registers
        else : # Operations
            # Send registers list and return the registers list updated
            self.registers = current_command.decode_bin_instruction(instruction,self.registers)
            
        self.set_register(addr=0,value=0) # Reg 0 is always 0
        
        self.local_counter += 1
        # if self.local_counter == 100000 :
        #     self.local_counter = 0
        #     # Update UI with registers and pc value
        #     self.registers_value_updated.emit(self.registers)
        #     self.pc_updated.emit(self.pc)
            
        self.current_time = time.time() - self.start_time
        
        if self.current_time > 1: # seconde
            print("Nombre d'appels par seconde :", self.local_counter)
            self.local_counter = 0
            self.start_time = time.time()
            
            
        return self.registers
        
        
            
    def set_register(self,addr:int,value:int) -> None:
        """
        Args:
            addr (int): the address of the register to modify
            value (int): the new value of the register
        """
        self.registers[addr] = value
    
    """ Private functions """
        
    def _init_register(self) -> None:
        """ 
        Initialization of registers.
        There are 32 registers, initial value is 0.
        """
        for i in range(32):
            self.registers.append(0)
            
    def _count(self):
        pass
        