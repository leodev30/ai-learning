# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*
        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.
          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        self.oldValues = self.values.copy()
        states = mdp.getStates()
        for i in range(iterations):
            for state in states:
                actions = mdp.getPossibleActions(state)
                if not mdp.isTerminal(state):
                    actionValue = -float('inf')
                    for action in actions:
                        qValue = self.computeQValueFromValues(state, action)
                        actionValue = max(actionValue, qValue)
                    self.values[state] = actionValue
            self.oldValues = self.values.copy()

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__)
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        # trả về giá trị Q của cặp (state, action) được cung cấp bởi hàm giá trị được cho bởi self.values.
        qValue = 0
        for nextState, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            # tính qvalue 
            qValue += prob * (self.discount * self.oldValues[nextState] + self.mdp.getReward(state, action, nextState))
        return qValue

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.
          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        # tính toán hành động tốt nhất theo hàm giá trị được cung cấp bởi self.values.
        actions, maxValue, decision = self.mdp.getPossibleActions(state), -float('inf'), None
        for action in actions:
            # tính giá trị qValue hành động tại từng (state, action)
            actionValue = self.computeQValueFromValues(state, action)
            # nếu mà giá trị action lớn hơn giá trị gán max thì cập nhật lại max và đưa ra decision chính là action tại state đó
            if actionValue > maxValue:
                maxValue = actionValue
                decision = action
        return decision

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)