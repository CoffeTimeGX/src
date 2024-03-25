from .command import Command


class BRANZ(Command): #saute à l'adresse position_addr si position_register != 0
    command = 17

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
        new_pc = int(elements[2])
        register_to_check =  int(elements[1][1:])
        # print(f"new pc : {new_pc}")
        instruction = self.build_instruction(instruction,register_to_check, self.position_register[self.LSB])
        instruction = self.build_instruction(instruction, new_pc, self.position_addr[self.LSB])


        return instruction

    def decode_bin_instruction(self, instruction: int, registers: list) -> list:
        ''' Return the new registers list from instruction '''
        pass

    def extract_pc(self, instruction: int, registers: list):
        position_register = self.extract_sub_instruction(instruction, self.position_register[self.MSB], self.positiposition_registern_operand[self.LSB])
        if position_register:
            reg = self.extract_sub_instruction(instruction, self.position_addr[self.MSB], self.position_addr[self.LSB])
            pc = registers[reg]

        # print(f"PC : {pc}")
        return pc





