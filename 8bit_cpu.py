import time
class Computer8bit:
    def __init__(self):
        self.mem = [  # ПЗУ 16 Байт
            0b01000000,  # Ячейка 0 IN записать
            0b00000000,  # Ячейка 1 в регистр 0
            0b11100000,  # Ячейка 2 MUL умножить
            0b00000000,  # Ячейка 3 регистр 0
            0b00000000,  # Ячейка 4 на регистр 0
            0b10000000,  # Ячейка 5 PRM вывести
            0b00000000,  # Ячейка 6 регистр 0
            0b11111111,  # Ячейка 7 HALT
            0b00000000,  # Ячейка 8
            0b00000000,  # Ячейка 9
            0b00000000,  # Ячейка 10
            0b00000000,  # Ячейка 11
            0b00000000,  # Ячейка 12
            0b00000000,  # Ячейка 13
            0b00000000,  # Ячейка 14
            0b00000000,  # Ячейка 15
        ]
        self.reg = [  # Регистры 4 Байта
            0b00000000,  # Регистр 00
            0b00000000,  # Регистр 01
            0b00000000,  # Регистр 10
            0b00000000   # Регистр 11
        ]
        self.pc = 0  # Program Counter (указывает на текущую команду)

    def run(self):
        while self.pc < len(self.mem):
            command = self.mem[self.pc]

            if  command == 0b10000000:  # PRM (Вывести содержимое регистра: PRM reg_addr)
                reg = self.mem[self.pc + 1]
                print(f"0b{self.reg[reg]:08b}")
                self.pc += 2

            if command == 0b01000000:  # IN (Ввести значение в регистр)
                reg = self.mem[self.pc + 1]
                self.reg[reg] = int(input(), 2) & 0b11111111
                self.pc += 2

            elif command == 0b11000000:  #LD (Загрузить из памяти в регистр: LD reg_addr mem_addr)
                reg_addr = self.mem[self.pc + 1]
                mem_addr = self.mem[self.pc + 2]
                self.reg[reg_addr] = self.mem[mem_addr] & 0b11111111
                self.pc += 3

            elif command == 0b00100000:  #ST (Загрузить из регистра в память: ST reg_addr mem_addr)
                reg_addr = self.mem[self.pc + 1]
                mem_addr = self.mem[self.pc + 2]
                self.mem[mem_addr] = self.reg[reg_addr] & 0b11111111
                self.pc += 3

            elif command == 0b10100000:  # ADD (Cложение: ADD reg_addr1 reg_addr2)
                reg_1 = self.mem[self.pc + 1]
                reg_2 = self.mem[self.pc + 2]
                self.reg[reg_1] = (self.reg[reg_1] + self.reg[reg_2]) & 0b11111111
                self.pc += 3

            elif command == 0b01100000:  # SUB (Вычитание: SUB reg_addr1 reg_addr2)
                reg_1 = self.mem[self.pc + 1]
                reg_2 = self.mem[self.pc + 2]
                self.reg[reg_1] = (self.reg[reg_1] - self.reg[reg_2]) & 0b11111111
                self.pc += 3

            elif command == 0b11100000:  # MUL (Умножение: MUL reg_addr1 reg_addr2)
                reg_1 = self.mem[self.pc + 1]
                reg_2 = self.mem[self.pc + 2]
                self.reg[reg_1] = (self.reg[reg_1] * self.reg[reg_2]) & 0b11111111
                self.pc += 3

            elif command == 0b00010000:  # DIV (Деление: DIV reg_addr1 reg_addr2)
                reg_1 = self.mem[self.pc + 1]
                reg_2 = self.mem[self.pc + 2]
                self.reg[reg_1] = (self.reg[reg_1] // self.reg[reg_2]) & 0b11111111
                self.pc += 3

            elif command == 0b10010000:  # DEC (Декремент: DEC reg_addr)
                reg_addr = self.mem[self.pc + 1]
                self.reg[reg_addr] = (self.reg[reg_addr] - 1) & 0b11111111
                self.pc += 2

            elif command == 0b01010000:  # INC (Инкремент: INC reg_addr)
                reg_addr = self.mem[self.pc + 1]
                self.reg[reg_addr] = (self.reg[reg_addr] + 1) & 0b11111111
                self.pc += 2

            elif command == 0b11010000:  # JMP (Переход: JMP addr)
                addr = self.mem[self.pc + 1]
                self.pc = addr

            elif command == 0b11111111:  # HALT (Остановка)
                print("Программа выполнена!")
                break
            time.sleep(0.2)

PC = Computer8bit()
PC.run()