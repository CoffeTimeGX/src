from .command import Command


class OR(Command):
    MSB = 0
    LSB = 1

    command = 6

    position_code = 31, 27
    position_operand1 = 26, 22
    position_x = 21, 21
    position_if_number = 20, 5
    position_if_register = 9, 5
    position_result = 4, 0

    instruction = 0

    def __init__(self):
        # super().__init__()
        pass

    def set_bin_instruction(self, elements: tuple) -> int:
        '''
        Build the instruction from elements (tuple).
        '''
        # set operand
        # print(elements)
        operand_1 = int(elements[1][1:])
        result = int(elements[3][1:])

        # build instruction
        instruction = 0
        instruction = self.build_instruction(instruction, self.command, self.position_code[self.LSB])
        instruction = self.build_instruction(instruction, operand_1, self.position_operand1[self.LSB])

        # operand 2 can be a register or a signer 16 bits interger
        if self._is_register2(elements):
            operand_2 = int(elements[2][1:])
            instruction = self.build_instruction(instruction, 0, self.position_x[self.LSB])
            instruction = self.build_instruction(instruction, operand_2, self.position_if_register[self.LSB])

        else:
            operand_2 = int(elements[2][0:])
            instruction = self.build_instruction(instruction, 1, self.position_x[self.LSB])
            instruction = self.build_instruction(instruction, operand_2, self.position_if_number[self.LSB])

        instruction = self.build_instruction(instruction, result, self.position_result[self.LSB])
        return instruction

    def decode_bin_instruction(self, instruction: int, registers: list) -> list:
        ''' Return the new registers list from instruction '''

        alpha_register = self.extract_sub_instruction(instruction, self.position_operand1[self.MSB],
                                                      self.position_operand1[self.LSB])
        gamma_register = self.extract_sub_instruction(instruction, self.position_result[self.MSB],
                                                      self.position_result[self.LSB])
        state_bit = self.extract_sub_instruction(instruction, self.position_x[self.MSB], self.position_x[self.LSB])
        operand_1 = registers[alpha_register]

        if not state_bit:
            beta_register = self.extract_sub_instruction(instruction, self.position_if_register[self.MSB],
                                                         self.position_if_register[self.LSB])
            operand_2 = registers[beta_register]
        else:
            operand_2 = self.extract_sub_instruction(instruction, self.position_if_number[self.MSB],
                                                     self.position_if_number[self.LSB])

        registers[gamma_register] = operand_1 | operand_2
        return registers

    def _is_register2(self, elements):
        ''' Return True if operand 2 are a register, else False  '''
        return elements[2][0] == 'R'
