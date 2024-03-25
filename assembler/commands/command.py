from abc import ABC,abstractmethod
import re

class Command():
    MSB = 0
    LSB = 1
    
    
    def set_bin_instruction(self,elements:tuple):
        ''' 
        Build the instruction from elements (tuple).
        '''
        pass
    
    def build_instruction(self,instruction_in_build:int,data:int,position:int) -> int:
        instruction_in_build += data << position
        return instruction_in_build
    
    def extract_sub_instruction(self,instruction:int,msb:int,lsb:int) -> int :
        mask = (2**(msb-lsb+1)-1) << lsb
        return (instruction & mask) >> lsb
    
    def decode_bin_instruction(self,instruction:int,registers:list) -> list :
        ''' Return the new registers list from instruction '''
        pass
    
    def _is_register2(self,elements):
        ''' Return True if operand 2 are a register, else False  '''
        return elements[2][0] == 'R'
    
    def _is_a_register(self, element:type):
        ''' Return True if element is a register, else False  '''
        pattern = r'^R([0-9]|[1-2][0-9]|3[0-1])$'
        return re.match(pattern, element)