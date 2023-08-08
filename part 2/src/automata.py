from src.state import State

class Automata:
    # O autômato está num estado final
    FINAL_STATE = 0
    # O autômato está num estado não-final
    NON_FINAL_STATE = 1
    # O autômato REJEITA pois não há transição válida
    REJ_NO_TRANSITION  = 2
    # O autômato REJEITA pois não reconhece esse símbolo
    REJ_INVALID_SYMBOL = 3

    def __init__(self):
        self.all_states = []
        self.cur_state = None

    def create(self, states, transistions, initial, finals):
        num = len(states)

        name = ''
        cur_transistions = {}
        is_inital = False
        is_final = False

        for i in range(0, num):
            name = states[i]
            cur_transistions = transistions[i]
            is_inital = name == initial
            is_final = name in finals

            state = State(name, cur_transistions, is_inital, is_final)

            self.all_states.append(state)

        self.cur_state = self.return_initial_state()

        # self.mount()

    # Descrição de todos os estados -- não utlizado
    def mount(self):
        for state in self.all_states:
            print(state.name)
            print(state.transistions)
            print(state.is_initial)
            print(state.is_final)
            print("\n")

    def reset_inital_state(self):
        self.cur_state = self.return_initial_state()

    def return_initial_state(self):
        for state in self.all_states:
            if state.is_initial:
                return state

    def return_state_by_name(self, name):
        for state in self.all_states:
            if state.name == name:
                return state

    # Tenta colocar o autômato no próximo estado,
    # dado o estado atual (self) e o símbolo lido (text)
    def run_step(self, text):
        if text not in self.cur_state.transistions:
            return Automata.REJ_INVALID_SYMBOL

        next_state_name = self.cur_state.transistions[text]
        self.cur_state = self.return_state_by_name(next_state_name)

        if self.cur_state == None:
            return Automata.REJ_NO_TRANSITION

        if not self.cur_state.is_final:
            return Automata.NON_FINAL_STATE

        return Automata.FINAL_STATE
