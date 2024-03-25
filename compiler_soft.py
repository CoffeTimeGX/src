from PySide2.QtCore import QObject, Signal


from assembler.commands.add import ADD
from assembler.commands.sub import SUB
from assembler.commands.mul import MUL
from assembler.commands.div import DIV
from assembler.commands.and_ import AND
from assembler.commands.or_ import OR
from assembler.commands.xor import XOR
from assembler.commands.shl import SHL
from assembler.commands.shr import SHR
from assembler.commands.scall import SCALL
from assembler.commands.jump import JUMP
from assembler.commands.braz import BRAZ
from assembler.commands.branz import BRANZ



class CompilerSoftware(QObject) :
    
    registers_value_updated = Signal(list)
    pc_updated              = Signal(int)
    
    def __init__(self) -> None:
        super().__init__()
        self._set_instruction()
    
    def _set_instruction(self):
        ''' Set instruction map between commands and command's instance '''
        self.instruction_dictionary = {
            "ADD" : ADD(),
            "SUB" : SUB(),
            "MUL" : MUL(),
            "DIV" : DIV(),
            "AND" : AND(),
            "OR"  : OR(),
            "XOR" : XOR(),
            "SHL" : SHL(),
            "SHR" : SHR(),
            "JUMP" : JUMP(),
            "BRAZ":  BRAZ(),
            "BRANZ": BRANZ(),
            "SCALL" : SCALL()
        }
        
        
        self.opcode_map = {
            1 : "ADD",
            2 : "SUB",
            3 : "MUL",
            4 : "DIV",
            5 : "AND",
            6 : "OR" ,
            7 : "XOR",
            8 : "SHL",
            9 : "SHR",
            14 : "JUMP",
            16 : "BRAZ",
            17 : "BRANZ",
            18 : "SCALL"
        }
