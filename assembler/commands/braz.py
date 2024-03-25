from .command import Command


class BRAZ(Command):
    command = 16

    position_code = 31, 27
    position_register = 26, 22
    position_addr = 21, 0

    instruction = 0

    def __init__(self):
        super().__init__()

    def set_bin_instruction(self, elements: tuple) -> int:
        '''
        Build the instruction from elements (tuple).
        '''

        instruction = self.build_instruction(self.instruction, self.command, self.position_code[self.LSB])
        register_to_check =  int(elements[1][1:])
        new_pc = int(elements[2])
        # print(f"new pc : {new_pc}")
        instruction = self.build_instruction(instruction,register_to_check, self.position_register[self.LSB])
        instruction = self.build_instruction(instruction, new_pc, self.position_addr[self.LSB])


        return instruction

    def decode_bin_instruction(self, instruction: int, registers: list) -> list:
        ''' Return the new registers list from instruction '''
        pass

    def extract_pc(self, instruction: int, registers: list):
        position_register = self.extract_sub_instruction(instruction, self.position_register[self.MSB], self.position_register[self.LSB])
        if position_register:
            reg = self.extract_sub_instruction(instruction, self.position_addr[self.MSB], self.position_addr[self.LSB])
            pc = registers[reg]

        # print(f"PC : {pc}")
        return pc





