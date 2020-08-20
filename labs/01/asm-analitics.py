import sys
            
class asm_analitics:
    
    def __init__(self,log_file='log'):
        
        log = open(log_file,'r')
        self.lines = log.readlines()

        self.instructions = {}
        self.functions = {}
        
        self.get_info()
        
    def get_info(self):

        for line in self.lines:
            if line[0].isnumeric():
                direction = line[:16]
                function = line[17:].replace(":\n","")
                self.functions[function[1:-1]] = direction
            if line[:4] == "    ":
                if len(line[32:].split()) == 0: 
                    continue
                instruction = line[32:].split()[0]
                if instruction not in self.instructions.keys():
                    self.instructions[instruction] = 1
                else:
                    self.instructions[instruction] += 1
                    
    def print_data(self):

        print('Hi, this is the output of the analysis:')
        print('\tYou have %d kind of instructions in this object file:' % len(self.instructions))
        for instruction in self.instructions:
            print('\t\t{0:<10s} : Executed {1:3d} times'.format(instruction, self.instructions[instruction]))
        print('\tYou have %d functions' % len(self.functions))
        for function in self.functions:
            print('\t\t{0:<21s} : Located at {1:<16s} addr'.format(function, self.functions[function]))

if __name__ == "__main__":
    
    try:
        if len(sys.argv)>1:
            asm = asm_analitics(sys.argv[1])
            asm.print_data()
        else:
            asm = asm_analitics()
            asm.print_data()
    except FileNotFoundError as err:
        print("Please, enter a valid file name.")