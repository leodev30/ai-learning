class Action:
    def __init__(self, i, j, XorO):
        self.i = i
        self.j = j
        self.XorO = XorO

class State:
    def __init__(self):
        self.state = ['***', '***', '***']

    def print(self):
        print('------')
        for s in self.state:
            print(s)

    def get_player(self):
        x_count = self.get_count('X')
        o_count = self.get_count('O')
        if x_count == o_count: return 'MAX'
        else: return 'MIN'

    def get_count(self, XorO):
        count = 0
        for s in self.state:
            for c in s:
                if c == XorO: 
                    count += 1
        return count

    def isTerminalState(self):
        if self.state[0] == 'XXX' or self.state[0] == 'OOO' or self.state[1] == 'XXX' or self.state[1] == 'OOO' or self.state[2] == 'XXX' or self.state[2] == 'OOO':
            return True
        if self.column(0) == 'X' or self.column(0) == 'O' or self.column(1) == 'X' or self.column(1) == 'O' or self.column(2) == 'X' or self.column(2) == 'O':
            return True
        if self.main_diag() == 'X' or self.main_diag() == 'O' or self.other_diag() == 'X' or self.other_diag() == 'O':
            return True
        if self.get_count('*') == 0:
            return True
        return False

    def getTerminalStateValue(self):
        if self.state[0] == 'XXX' or self.state[1] == 'XXX' or self.state[2] == 'XXX':
            return 1
        if self.state[0] == 'OOO' or self.state[1] == 'OOO' or self.state[2] == 'OOO':
            return -1
        if self.column(0) == 'X' or self.column(1) == 'X' or self.column(2) == 'X':
            return 1
        if self.column(0) == 'O'  or self.column(1) == 'O'  or self.column(2) == 'O':
            return -1
        if self.main_diag() == 'X' or self.other_diag() == 'X':
            return 1
        if self.main_diag() == 'O' or self.other_diag() == 'O':
            return -1
        if self.get_count('*') == 0:
            return 0
        raise Exception('not implemented')

    def column(self, i):
        if self.state[0][i] != '*' and self.state[0][i] == self.state[1][i] and self.state[0][i] == self.state[2][i]:
            return self.state[0][i]
        else:
            return '*'

    def main_diag(self):
        if self.state[0][0] != '*' and self.state[0][0] == self.state[1][1] and self.state[0][0] == self.state[2][2]:
            return self.state[0][0]
        else:
            return '*'

    def other_diag(self):
        if self.state[0][2] != '*' and self.state[0][2] == self.state[1][1] and self.state[0][2] == self.state[2][0]:
            return self.state[0][2]
        else:
            return '*'

    def get_value(self): # minimax
        if self.isTerminalState():
            return self.getTerminalStateValue(), None

        player = self.get_player()
        if player == 'MAX':
            v, action = self.get_max_value()
        else: # MIN
            v, action = self.get_min_value()

        # self.print()
        # print("player", player, "value", v)

        return v, action

    def get_max_value(self):
        v, max_action = float('-inf'), None
        for successor, action in self.get_successors('X'):
            new_value, _ = successor.get_value()
            if new_value > v:
                v, max_action = new_value, action
        # print("MAX", v)
        return v, max_action

    def get_min_value(self):
        v, min_action = float('inf'), None
        for successor, action in self.get_successors('O'):
            new_value, _ = successor.get_value()
            if new_value < v:
                v, min_action = new_value, action
        # print("MIN", v)
        # [s.print() for s in self.get_successors('O')]
        return v, min_action

    def get_successors(self, XorO):
        result = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == '*':
                    result.append(self.get_successor(i, j, XorO))
        return result

    def get_successor(self, i, j, XorO):
        successor = State()
        for k in range(3):
            if k != i: 
                successor.state[k] = self.state[k]
            else:
                successor.state[k] = self.state[k][:j] + XorO + self.state[k][j+1:]
        return successor, Action(i, j, XorO)
    
def main():
    print("TIC TAC TOE")
    state = State()
    
    state.state = ['***', '***', '***']
    state.print()
    print(state.get_player())
    # print(state.getTerminalStateValue())
    # state.get_successor(2, 2, 'O').print()
    value, action = state.get_value()
    print( value, action.i, action.j, action.XorO )
if __name__ == "__main__":
    main()