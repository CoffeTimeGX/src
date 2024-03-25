from .command import Command


class SCALL(Command):

    command = 18

    position_code = 31, 27
    postion_system_call = 26,0

    instruction = 0

    def __init__(self):
        # super().__init__()
        pass

    def set_bin_instruction(self, elements: tuple) -> int:
        '''
        Build the instruction from elements (tuple).
        '''
        system_call = int(elements[1])
        print(f"system_call : {system_call}")
        instruction = self.build_instruction(self.instruction, self.command, self.position_code[self.LSB])
        instruction = self.build_instruction(instruction, system_call, self.postion_system_call[self.LSB])
       
        return instruction

    def decode_bin_instruction(self, instruction: int, registers: list) -> list:
        ''' Return the new registers list from instruction '''



    def _is_register2(self, elements):
        ''' Return True if operand 2 are a register, else False  '''
        return elements[2][0] == 'R'
