# search.py͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# ---------͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# Licensing Information:  You are free to use or extend these projects for͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁ 
# educational purposes provided that (1) you do not distribute or publish͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁ 
# solutions, (2) you retain this notice, and (3) you provide clear͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁ 
# attribution to UC Berkeley, including a link to͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁ 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# The core projects and autograders were primarily created by John DeNero͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁ 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
# Student side autograding was added by Brad Miller, Nick Hay, and͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁ 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    ## use a stack to make sure pacman picks the deepest node from the search tree
    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    visited = set()

    ## do while there are still moves left available
    while not stack.isEmpty():
        currState, actions = stack.pop()

        ## if pacman finds the goal, return actions it took
        if problem.isGoalState(currState):
            return actions

        ## if state not visited yet and not goal
        if currState not in visited:
            ## add to visited
            visited.add(currState)

            ## get next moves
            successors = problem.getSuccessors(currState)

            ## if there are options to move more push them to the stack
            for nextState, action, _ in successors:
                newActions = actions + [action]
                stack.push((nextState, newActions))

    ## if pacman cant find the goal return empty list
    return []

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"

    ## use a queue to make sure pacman picks the shallowest node from the search tree
    queue = util.Queue()
    queue.push((problem.getStartState(), []))
    visited = set()

    ## do while there are still moves left available
    while not queue.isEmpty():
        currState, actions = queue.pop()

        ## if pacman finds the goal, return actions it took
        if problem.isGoalState(currState):
            return actions

        ## if state not visited yet and not goal
        if currState not in visited:
            ## add to visited
            visited.add(currState)

            ## get next moves
            successors = problem.getSuccessors(currState)

            ## if there are options to move more push them to the queue
            for nextState, action, _ in successors:
                newActions = actions + [action]
                queue.push((nextState, newActions))

    ## if pacman cant find the goal return empty list
    return []


def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"

    ## use a priority queue to make sure pacman picks the cheapest cost node from the search tree
    prio = util.PriorityQueue()
    prio.push((problem.getStartState(), [], 0), 0)
    visited = set()

    ## do while there are still moves left available
    while not prio.isEmpty():
        currState, actions, currCost = prio.pop()

        ## if pacman finds the goal, return actions it took
        if problem.isGoalState(currState):
            return actions

        ## if state not visited yet and not goal
        if currState not in visited:
            ## add to visited
            visited.add(currState)

            ## get next moves
            successors = problem.getSuccessors(currState)

            ## if there are options to move more push them to the queue
            for nextState, action, nextCost in successors:
                newActions = actions + [action]
                newCost = currCost + nextCost
                prio.push((nextState, newActions, newCost), newCost)

    ## if pacman cant find the goal return empty list
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"

    ## use a priority queue to make sure pacman picks the cheapest cost node from the search tree
    prio = util.PriorityQueue()
    prio.push((problem.getStartState(), [], 0), 0)
    visited = set()

    ## do while there are still moves left available
    while not prio.isEmpty():
        currState, actions, currCost = prio.pop()

        ## if pacman finds the goal, return actions it took
        if problem.isGoalState(currState):
            return actions

        ## if state not visited yet and not goal
        if currState not in visited:
            ## add to visited
            visited.add(currState)

            ## get next moves
            successors = problem.getSuccessors(currState)

            ## if there are options to move more push them to the queue
            for nextState, action, nextCost in successors:
                newActions = actions + [action]
                newCost = currCost + nextCost
                priority = newCost + heuristic(nextState, problem)
                prio.push((nextState, newActions, newCost), priority)

    ## if pacman cant find the goal return empty list
    return []

# Abbreviations͏󠄂͏️͏󠄌͏󠄎͏︈͏︂͏︁
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
