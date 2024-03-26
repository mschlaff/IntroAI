
# valueIterationAgents.py͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# -----------------------͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# Licensing Information:  You are free to use or extend these projects for͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# educational purposes provided that (1) you do not distribute or publish͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# solutions, (2) you retain this notice, and (3) you provide clear͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# The core projects and autograders were primarily created by John DeNero͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# Student side autograding was added by Brad Miller, Nick Hay, and͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# Pieter Abbeel (pabbeel@cs.berkeley.edu).͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁


# valueIterationAgents.py͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# -----------------------͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# Licensing Information:  You are free to use or extend these projects for͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# educational purposes provided that (1) you do not distribute or publish͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# solutions, (2) you retain this notice, and (3) you provide clear͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# The core projects and autograders were primarily created by John DeNero͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# Student side autograding was added by Brad Miller, Nick Hay, and͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# Pieter Abbeel (pabbeel@cs.berkeley.edu).͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

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
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
        "*** YOUR CODE HERE ***"

        for i in range(self.iterations):
            newVal = self.values.copy()
            for state in self.mdp.getStates():
                if not self.mdp.isTerminal(state):

                    # find qVal and choose max
                    qVal = [self.computeQValueFromValues(state, action) for action in self.mdp.getPossibleActions(state)]
                    newVal[state] = max(qVal)

            # update vals in next loop
            self.values = newVal


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        "*** YOUR CODE HERE ***"
        """

        if self.mdp.isTerminal(state):
            return 0.0

        qVal = 0.0
        for next, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            reward = self.mdp.getReward(state, action, next)
            qVal += prob * (reward + self.discount * self.values[next])

        return qVal

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        "*** YOUR CODE HERE ***"
        """
        possible_actions = self.mdp.getPossibleActions(state)
        if not possible_actions:
            return None

        best_action = possible_actions[0]
        best_q_value = self.computeQValueFromValues(state, best_action)

        # find qVal for all actions
        for action in possible_actions[1:]:
            q_value = self.computeQValueFromValues(state, action)
            if q_value > best_q_value:
                best_q_value = q_value
                best_action = action

        # choose max qVal action
        return best_action

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
