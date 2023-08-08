import sys
from src.automata import Automata 

automata_returns = {
    Automata.FINAL_STATE: "Accepted!",
    Automata.NON_FINAL_STATE: "Rejected! Input didn't end in final state!",
    Automata.REJ_NO_TRANSITION: "Rejected! Undefined transition!",
    Automata.REJ_INVALID_SYMBOL: "Rejected! Input is not on the alphabet!"
}

def main():
    automata = Automata()

    states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12']
    
    transitions = [
        {'usuário': 'q1', 'senha': None, 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': None, 'confirmar': None, 'dinheiro': None, 'troco': None, 'numCartão': None, 'senhaCorreta': None, 'senhaErrada': None},
        {'usuário': None, 'senha': 'q2', 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': None, 'confirmar': None, 'dinheiro': None, 'troco': None, 'numCartão': None, 'senhaCorreta': None, 'senhaErrada': None},
        {'usuário': None, 'senha': None, 'barbie': 'q3', 'megatubarão': 'q3', 'oppenheimer': 'q3', 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': None, 'confirmar': None, 'dinheiro': None, 'troco': None, 'numCartão': None, 'senhaCorreta': None, 'senhaErrada': None},
        {'usuário': None, 'senha': None, 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': 'q2', '17h': 'q4', '19h': 'q4', '21h': 'q4', 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': None, 'confirmar': None, 'dinheiro': None, 'troco': None, 'numCartão': None, 'senhaCorreta': None, 'senhaErrada': None},
        {'usuário': None, 'senha': None, 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': 'q5', 'pipocaDoce': 'q5', 'refrigerante': 'q5', 'chocolate': 'q5', 'água': 'q5', 'bala': 'q5', 'voltar': None, 'confirmar': None, 'dinheiro': None, 'troco': None, 'numCartão': None, 'senhaCorreta': None, 'senhaErrada': None},
        {'usuário': None, 'senha': None, 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': 'q4', 'confirmar': 'q6', 'dinheiro': None, 'troco': None, 'numCartão': None, 'senhaCorreta': None, 'senhaErrada': None},
        {'usuário': None, 'senha': None, 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': None, 'confirmar': None, 'dinheiro': 'q7', 'troco': None, 'numCartão': None, 'senhaCorreta': None, 'senhaErrada': None},
        {'usuário': None, 'senha': None, 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': None, 'confirmar': None, 'dinheiro': None, 'troco': 'q12', 'numCartão': None, 'senhaCorreta': None, 'senhaErrada': None},
        {'usuário': None, 'senha': None, 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': None, 'confirmar': None, 'dinheiro': None, 'troco': None, 'numCartão': 'q8', 'senhaCorreta': None, 'senhaErrada': None},
        {'usuário': None, 'senha': None, 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': None, 'confirmar': None, 'dinheiro': None, 'troco': None, 'numCartão': None, 'senhaCorreta': 'q12', 'senhaErrada': 'q9'},
        {'usuário': None, 'senha': None, 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': None, 'confirmar': None, 'dinheiro': None, 'troco': None, 'numCartão': None, 'senhaCorreta': 'q12', 'senhaErrada': 'q10'},
        {'usuário': None, 'senha': None, 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': None, 'confirmar': None, 'dinheiro': None, 'troco': None, 'numCartão': None, 'senhaCorreta': 'q12', 'senhaErrada': 'q11'},
        {'usuário': None, 'senha': None, 'barbie': None, 'megatubarão': None, 'oppenheimer': None, 'outroIngresso': None, '17h': None, '19h': None, '21h': None, 'pipocaSalgada': None, 'pipocaDoce': None, 'refrigerante': None, 'chocolate': None, 'água': None, 'bala': None, 'voltar': None, 'confirmar': None, 'dinheiro': None, 'troco': None, 'numCartão': None, 'senhaCorreta': 'q12', 'senhaErrada': None},
    ]

    initial = 'q0'
    finals = ['q12']

    # creates automaton based on the given data
    automata.create(states, transitions, initial, finals)

    while True:
        print('-'*30)
        mode = input("Read input from terminal (1) or file `test.txt` (2): ")

        # accepts an empty word only if the initial state is also a final state
        if (initial in finals):
            flag = Automata.FINAL_STATE
        else:
            flag = Automata.NON_FINAL_STATE

        # placeholder
        text = '0'

        automata.reset_inital_state()

        # mode 1 : terminal 
        if mode == "1":
            
            while text != "" and flag not in [Automata.REJ_NO_TRANSITION, Automata.REJ_INVALID_SYMBOL]:
                text = input()

                # ends when it reads an emtpy line
                if text == "":
                    break

                flag = automata.run_step(text)

            print(automata_returns[flag])

    # essa parte não tá funcionando mas daqui a pouco resolvo 

        """ elif mode == "2":
            # Modo 2 => Leitura do Arquivo
            lines = []

            try:
                with open('test.txt') as f:
                    lines = f.read().splitlines()

                for line in lines:
                    if line == "" or flag in [Automata.REJ_NO_TRANSITION, Automata.REJ_INVALID_SYMBOL]:
                        break

                    flag = automata.run_step(line)

                print(automata_returns[flag])
            except FileNotFoundError:
                print("Error! File `test.txt` not found!")
        else:
            break """

if __name__ == "__main__":
    main()






