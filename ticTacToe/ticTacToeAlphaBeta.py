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
        [print(s) for s in self.state]

    def get_player(self):
        x_count = self.get_count('X')
        o_count = self.get_count('O')
        return 'MAX' if x_count == o_count else 'MIN'

    def get_count(self, XorO):
        count = sum([s.count(XorO) for s in self.state], 0)
        return count

    def isTerminalState(self):
        if self.row(0) == 'X' or self.row(0) == 'O' or self.row(1) == 'X' or self.row(1) == 'O' or self.row(2) == 'X' or self.row(2) == 'O':
            return True
        if self.column(0) == 'X' or self.column(0) == 'O' or self.column(1) == 'X' or self.column(1) == 'O' or self.column(2) == 'X' or self.column(2) == 'O':
            return True
        if self.main_diag() == 'X' or self.main_diag() == 'O' or self.other_diag() == 'X' or self.other_diag() == 'O':
            return True
        if self.get_count('*') == 0:
            return True
        return False

    def getTerminalStateValue(self):
        if self.row(0) == 'X' or self.row(1) == 'X' or self.row(2) == 'X':
            return 1
        if self.row(0) == 'O' or self.row(1) == 'O' or self.row(2) == 'O':
            return -1
        if self.column(0) == 'X' or self.column(1) == 'X' or self.column(2) == 'X':
            return 1
        if self.column(0) == 'O' or self.column(1) == 'O' or self.column(2) == 'O':
            return -1
        if self.main_diag() == 'X' or self.other_diag() == 'X':
            return 1
        if self.main_diag() == 'O' or self.other_diag() == 'O':
            return -1
        if self.get_count('*') == 0:
            return 0
        raise Exception('not implemented')

    @staticmethod
    def check3(a, b, c):
        return a if a != '*' and a == b and a == c else '*'

    def row(self, i):
        return self.check3(self.state[i][0], self.state[i][1], self.state[i][2])

    def column(self, i):
        return self.check3(self.state[0][i], self.state[1][i], self.state[2][i])

    def main_diag(self):
        return self.check3(self.state[0][0], self.state[1][1], self.state[2][2])

    def other_diag(self):
        return self.check3(self.state[0][2], self.state[1][1], self.state[2][0])

    def get_value(self, alpha, beta):  # minimax
        if self.isTerminalState():
            return self.getTerminalStateValue(), None

        player = self.get_player()
        v, action = self.get_max_value(
            alpha, beta) if player == 'MAX' else self.get_min_value(alpha, beta)

        return v, action

    def get_max_value(self, alpha, beta):
        v, max_action = float('-inf'), None
        for successor, action in self.get_successors('X'):
            new_value, _ = successor.get_value(alpha, beta)
            if new_value > v:
                v, max_action = new_value, action
            if v >= beta:
                return v, max_action
            alpha = max(alpha, v)

        return v, max_action

    def get_min_value(self, alpha, beta):
        v, min_action = float('inf'), None
        for successor, action in self.get_successors('O'):
            new_value, _ = successor.get_value(alpha, beta)
            if new_value < v:
                v, min_action = new_value, action
            if v <= alpha:
                return v, min_action
            beta = min(beta, v)

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
                successor.state[k] = self.state[k][:j] + \
                    XorO + self.state[k][j+1:]
        return successor, Action(i, j, XorO)


def main():
    print("TIC TAC TOE")
    state = State()

    state.state = ['***', '***', '***']
    state.print()
    answer = input("Do you want to go first (y/n) ? ")
    human = 'MAX' if answer.lower() == 'y' else 'MIN'
    turn = 'MAX'
    while not state.isTerminalState():
        if human == turn:
            answer = input("Enter your play (1 1, 1 2 ..., 3 3) ? ")
            i, j = [int(x) for x in answer.split(' ')[:2]]
            i, j = i-1, j-1
            state, _ = state.get_successor(
                i, j, 'X' if human == 'MAX' else 'O')

        else:  # machine turn
            value, action = state.get_value(float('-inf'), float('inf'))
            print('I (machine) will play at', action.i, action.j)
            state, _ = state.get_successor(
                action.i, action.j, 'O' if human == 'MAX' else 'X')

        turn = 'MIN' if turn == 'MAX' else 'MAX'
        state.print()

    value = state.getTerminalStateValue()
    winner = 'MAX' if value == 1 else 'MIN' if value == -1 else 'DRAW'
    if human == winner:
        print('You win !!!')
    else:
        print('You loss !!!' if winner != 'DRAW' else 'Draw !!!')


if __name__ == "__main__":
    main()