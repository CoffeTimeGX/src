from .command import Command

class STOP(Command):

    command = 0
    instruction = command
    
    def __init__(self) :
        # super().__init__()
        pass
    
    def set_bin_instruction(self,elements:tuple) -> int:
        ''' 
        Build the instruction from elements (tuple).
        '''
        pass
        
    def decode_bin_instruction(self,instruction:int,registers:list) -> list :
        ''' Return the new registers list from instruction '''
        # TODO 
        
        
