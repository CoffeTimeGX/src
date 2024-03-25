from .command import Command

class JUMP(Command):

    command = 15

    position_code = 31,27
    position_reg = 4,0
    position_val = 25,5
    imm = 26,26
    
    instruction = 0

    def __init__(self):
        super().__init__()

    def set_bin_instruction(self, elements: tuple) -> int:
        '''
        Build the instruction from elements (tuple).
        '''
        
        instruction = self.build_instruction(self.instruction, self.command, self.position_code[self.LSB])
        if self._is_a_register(elements[1]):
            new_pc = int(elements[1][1:])
            # print(f"new pc : {new_pc}")
            instruction = self.build_instruction(instruction, new_pc, self.position_reg[self.LSB])
            instruction = self.build_instruction(instruction, 0, self.imm[self.LSB])
        else :
            instruction = self.build_instruction(instruction, int(elements[1]), self.position_val[self.LSB])
            instruction = self.build_instruction(instruction, 1, self.imm[self.LSB])
            
        return instruction

    def decode_bin_instruction(self, instruction: int, registers: list) -> list:
        ''' Return the new registers list from instruction '''
        pass
        
    def extract_pc(self,instruction:int,registers: list):
        imm = self.extract_sub_instruction(instruction,self.imm[self.MSB],self.imm[self.LSB])
        if imm :
            pc = self.extract_sub_instruction(instruction,self.position_val[self.MSB],self.position_val[self.LSB])
        else : 
            reg = self.extract_sub_instruction(instruction,self.position_reg[self.MSB],self.position_reg[self.LSB])
            pc = registers[reg]
        # print(f"PC : {pc}")
        return pc        
        




