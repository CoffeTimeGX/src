from compiler_soft import CompilerSoftware
import re

class Assembler(CompilerSoftware) :
    
    """ Attributs """
    
    address     = 0 # index of the current instruction
    aliaser     = {} # Dictionnaire de label
    
    """ Constructor """
    
    def __init__(self,input_filename:str,output_filename:str):
        """
        Class constructor.
        
        Args:
            input_filename (str)  : pathname of a ASM code.
            output_filename (str) : filename of the binary file returned
            
        Example:
            assembleur = Assembleur(input_filename='unit_test/basic_operations.txt',output_filename='bin_file.txt')
        """
        super().__init__()
        self.input_file = open(input_filename,'r')      # input file
        self.output_file = open(output_filename,'w')    # output file
    
    """ Public functions """
    
    def encode(self):
        ''' 
        Encode instructions in a binary file from an assembler file.
        use set_bin_instruction(element:tuple) of a command.
        '''
        
        for line in self.input_file :
            
            elements = self._analyze_line(line)
            if elements == []:
                continue
            current_command = self.instruction_dictionary[elements[0]]
            bin_instruction = current_command.set_bin_instruction(elements)
            
            hex_string = f"0x{self.address:08x} 0x{bin_instruction:08x}"
            print(hex_string)
            print(elements)
            
            self.output_file.write(hex_string)
            self.output_file.write('\n')
            
            self.address += 1
            
        self.input_file.close()
        self.output_file.close()
            
    
    """ Private functions """
    
    def _analyze_line(self,line:str)->list:
        ''' Return a list of elements from a assembleur txt line '''
        # Remove commentary (; or #)
        new_line = re.sub(r'[#;].*$', '', line) 
        
        # Trouver tous les éléments de l'instruction (y compris les opcodes, registres et valeurs)
        elements = re.findall(r'[rR]?\w+', new_line)
        
        # Exclure les étiquettes (labels) si la ligne commence par une étiquette
        if ':' in line:
            elements = elements[1:]
        # Convertir les opcodes en majuscules
        elements = [element.upper() if element.isalpha() else element for element in elements]
        return elements
    
    
    

    
if __name__ == "__main__" :
    
    pathname = "test_file.txt"
    assembleur = Assembler(pathname,"hey")
    assembleur.encode()
    
    