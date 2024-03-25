from PySide2.QtCore import QObject, Signal

from assembler.commands.stop import STOP
from assembler.commands.add import ADD
from assembler.commands.sub import SUB
from assembler.commands.mul import MUL
from assembler.commands.div import DIV
from assembler.commands.and_ import AND
from assembler.commands.or_ import OR
from assembler.commands.xor import XOR
from assembler.commands.shl import SHL
from assembler.commands.shr import SHR
from assembler.commands.slt import SLT
from assembler.commands.sle import SLE
from assembler.commands.seq import SEQ
#from assembler.commands.load import LOAD
#from assembler.commands.store import STORE
from assembler.commands.jump import JUMP
from assembler.commands.braz import BRAZ
from assembler.commands.branz import BRANZ
from assembler.commands.scall import SCALL



class CompilerSoftware(QObject) :
    
    registers_value_updated = Signal(list)
    pc_updated              = Signal(int)
    
    def __init__(self) -> None:
        super().__init__()
        self._set_instruction()
    
    def _set_instruction(self):
        ''' Set instruction map between commands and command's instance '''
        self.instruction_dictionary = {
            "STOP":STOP(),
            "ADD" : ADD(),
            "SUB" : SUB(),
            "MUL" : MUL(),
            "DIV" : DIV(),
            "AND" : AND(),
            "OR"  : OR(),
            "XOR" : XOR(),
            "SHL" : SHL(),
            "SHR" : SHR(),
            "SLT" : SLT(),
            "SLE" : SLE(),
            "SEQ" : SEQ(),
            #"LOAD": LOAD(),
            #"STORE":STORE(),
            "JUMP" : JUMP(),
            "BRAZ":  BRAZ(),
            "BRANZ": BRANZ(),
            "SCALL" : SCALL()
        }
        
        
        self.opcode_map = {
            0 : "STOP",
            1 : "ADD",
            2 : "SUB",
            3 : "MUL",
            4 : "DIV",
            5 : "AND",
            6 : "OR" ,
            7 : "XOR",
            8 : "SHL",
            9 : "SHR",
            10: "SLT",
            11: "SLE",
            12: "SEQ",
            #13: "LOAD",
            #14: "STORE",
            15: "JUMP",
            16: "BRAZ",
            17: "BRANZ",
            18: "SCALL"
        }
