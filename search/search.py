# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import numpy as np
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    visited=[]
    print(problem.getStartState())
    stack = util.Stack()
    path = []
    cost = 0
    if stack.isEmpty() == True:
        stack.push((problem.getStartState(),path,cost))

    while (not stack.isEmpty()):
        temp = stack.pop()
        print(temp)
        if problem.isGoalState(temp[0]):
            print(temp[2])
            return temp[1]

        if (temp[0] not in visited):           #if current position not in visited nodes, add it to the visited list
            visited.append(temp[0])

        successors = problem.getSuccessors(temp[0])
        # print(successors)
        for i in successors:
            if i[0] not in visited:         #pushing all successors in stack that are yet to be explored
                stack.push((i[0], temp[1] + [i[1]], temp[2]+i[2]))


    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited=[]          # visited nodes
    queue = util.Queue()
    path = []
    cost = 0
    if queue.isEmpty() == True:
        queue.push((problem.getStartState(),path,cost))

    while not queue.isEmpty():
        temp = queue.pop()
        # print(temp)
        if problem.isGoalState(temp[0]):
            # print('hello',temp[2])
            return temp[1]

        if (temp[0] not in visited):    #if current position not in visited nodes, add it to the visited list
            visited.append(temp[0])

            successors = problem.getSuccessors(temp[0])
            for i in successors:
                # print(i)
                if i[0] not in visited:  #pushing all successors in queue that are yet to be explored
                    queue.push((i[0], temp[1] + [i[1]], temp[2]+i[2]))


    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = []
    pqueue = util.PriorityQueue()
    path = []
    cost = 0
    if pqueue.isEmpty() == True:
        pqueue.push((problem.getStartState(),path,cost),cost)

    while (not pqueue.isEmpty()):
        temp = pqueue.pop()

        if problem.isGoalState(temp[0]):
            print(temp[2])
            return temp[1]

        if (temp[0] not in visited):        #if current position not in visited nodes, add it to the visited list
            visited.append(temp[0])

            successors = problem.getSuccessors(temp[0])
            for i in successors:
                if i[0] not in visited:     #pushing all successors in priority queue that are yet to be explored
                    pqueue.push((i[0], temp[1] + [i[1]], temp[2]+i[2]), temp[2]+i[2])

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    visited = []
    pqueue = util.PriorityQueue()
    path = []
    cost = 0
    if pqueue.isEmpty() == True:
        pqueue.push((problem.getStartState(),path,cost),cost)

    while (not pqueue.isEmpty()):
        temp = pqueue.pop()
        # print(temp)
        if problem.isGoalState(temp[0]):
            # print(temp[2])
            return temp[1]

        if (temp[0] not in visited):        #if current position not in visited nodes, add it to the visited list
            visited.append(temp[0])

            successors = problem.getSuccessors(temp[0])
            # print(successors)
            for i in successors:
                if i[0] not in visited:         #pushing all successors in priority queue that are yet to be explored
                    pqueue.push((i[0], temp[1] + [i[1]], temp[2]+i[2]), temp[2]+i[2] + heuristic(i[0],problem))


def MM0(problem):
    def PathReverse(p):
        """
        Given a action list, return the reversed version of it.
        """
        path = []
        for x in p:
            if x == 'North':
                z = 'South'
                path.append(z)
            if x == 'South':
                z = 'North'
                path.append(z)
            if x == 'West':
                z = 'East'
                path.append(z)
            if x == 'East':
                z = 'West'
                path.append(z)
        return path[::-1]

    gF = 0
    epsilon = 1
    gB = 0
    OpenF = util.PriorityQueue()
    OpenB = util.PriorityQueue()
    OpenF.push((problem.getStartState(), [], 0), 2 * gF)
    OpenB.push((problem.goal, [], 0), 2 * gB)

    ClosedF = {}
    ClosedB = {}
    gF_dic = {}
    gB_dic = {}
    gF_dic[problem.getStartState()] = gF
    gB_dic[problem.goal] = gB
    U = float('inf')

    while (not OpenF.isEmpty()) and (not OpenB.isEmpty()):

        CurrentPopF = OpenF.pop()
        CurrentPopB = OpenB.pop()
        StateF = CurrentPopF[0]
        StateB = CurrentPopB[0]
        gF = CurrentPopF[2]
        gB = CurrentPopB[2]
        pathF = CurrentPopF[1]
        pathB = CurrentPopB[1]

        C = min(gF, gB)

        if StateF == StateB:
            print('reached goal1')
            return pathF + PathReverse(pathB)
        if StateF in ClosedB:
            pathB = ClosedB[StateF]
            print(ClosedB, ClosedF, StateF)
            print('reached goal2')
            return pathF + PathReverse(pathB)
        if StateB in ClosedF:
            pathF = ClosedF[StateB]
            print('reached goal3')
            return pathF + PathReverse(pathB)

        if (C == gF):
            OpenB.push(CurrentPopB,2 * gB)
            ClosedF[CurrentPopF[0]] = pathF
            SuccessorsF = problem.getSuccessors(StateF)
            for i in SuccessorsF:
                if OpenF.isthere(i[0]) or i[0] in ClosedF:
                    if gF_dic[i[0]] < gF + i[2]:
                        continue
                    if OpenF.isthere(i[0]):
                        OpenF.remove_by_value(i[0])
                    elif i[0] in ClosedF:
                        del ClosedF[i[0]]
                gF_dic[i[0]] = gF + i[2]
                OpenF.push((i[0], pathF + [i[1]], gF + i[2]),2*(gF + i[2]))

        else:
            OpenF.push(CurrentPopF, 2 * gF)
            ClosedB[CurrentPopB[0]] = pathB
            SuccessorsB = problem.getSuccessors(StateB)
            for i in SuccessorsB:
                if OpenB.isthere(i[0]) or i[0] in ClosedB:
                    if gB_dic[i[0]] < gB + i[2]:
                        continue
                    if OpenB.isthere(i[0]):
                        OpenB.remove_by_value(i[0])
                    elif i[0] in ClosedB:
                        del ClosedB[i[0]]
                gB_dic[i[0]] = gB + i[2]
                OpenB.push((i[0], pathB + [i[1]], gB + i[2]), 2*(gB + i[2]))

    return[]


def MM(problem,heuristic=nullHeuristic):
    def PathReverse(p):
        """
        Given a action list, return the reversed version of it.
        """
        path = []
        for x in p:
            if x == 'North':
                z = 'South'
                path.append(z)
            if x == 'South':
                z = 'North'
                path.append(z)
            if x == 'West':
                z = 'East'
                path.append(z)
            if x == 'East':
                z = 'West'
                path.append(z)
        return path[::-1]

    gF = 0
    epsilon = 1
    gB = 0
    OpenF = util.PriorityQueue()
    OpenB = util.PriorityQueue()
    hf = heuristic(problem.getStartState(),problem)
    hb = heuristic(problem.goal, problem)
    OpenF.push((problem.getStartState(), [], 0), max(hf,2 * gF))
    OpenB.push((problem.goal, [], 0), max(hb,2 * gB))

    ClosedF = {}
    ClosedB = {}
    gF_dic = {}
    gB_dic = {}
    gF_dic[problem.getStartState()] = gF
    gB_dic[problem.goal] = gB
    U = float('inf')

    while (not OpenF.isEmpty()) and (not OpenB.isEmpty()):

        CurrentPopF = OpenF.pop()
        CurrentPopB = OpenB.pop()
        StateF = CurrentPopF[0]
        StateB = CurrentPopB[0]
        gF = CurrentPopF[2]
        gB = CurrentPopB[2]
        pathF = CurrentPopF[1]
        pathB = CurrentPopB[1]

        C = min(gF, gB)

        if StateF == StateB:
            print('reached goal1')
            return pathF + PathReverse(pathB)
        if StateF in ClosedB:
            pathB = ClosedB[StateF]
            print(ClosedB, ClosedF, StateF)
            print('reached goal2')
            return pathF + PathReverse(pathB)
        if StateB in ClosedF:
            pathF = ClosedF[StateB]
            print('reached goal3')
            return pathF + PathReverse(pathB)

        if (C == gF):
            OpenB.push(CurrentPopB, gB)
            ClosedF[CurrentPopF[0]] = pathF
            SuccessorsF = problem.getSuccessors(StateF)
            for i in SuccessorsF:
                h_f = heuristic(i[0],problem)
                if OpenF.isthere(i[0]) or i[0] in ClosedF:
                    if gF_dic[i[0]] < gF + i[2]:
                        continue
                    if OpenF.isthere(i[0]):
                        OpenF.remove_by_value(i[0])
                    elif i[0] in ClosedF:
                        del ClosedF[i[0]]
                gF_dic[i[0]] = gF + i[2]
                ff = h_f + gF + i[2]
                OpenF.push((i[0], pathF + [i[1]], max(ff,2*(gF + i[2]))),max(ff,2*(gF + i[2])))

                # if OpenB.isthere(i[0]):
                #     U = min(U, gF_dic[i[0]] + gB_dic[1[0]])
        else:
            OpenF.push(CurrentPopF, gF)
            ClosedB[CurrentPopB[0]] = pathB
            SuccessorsB = problem.getSuccessors(StateB)
            for i in SuccessorsB:
                h_b = heuristic(i[0],problem)
                if OpenB.isthere(i[0]) or i[0] in ClosedB:
                    if gB_dic[i[0]] < gB + i[2]:
                        continue
                    if OpenB.isthere(i[0]):
                        OpenB.remove_by_value(i[0])
                    elif i[0] in ClosedB:
                        del ClosedB[i[0]]
                gB_dic[i[0]] = gB + i[2]
                fb = h_b + gB + i[2]
                OpenB.push((i[0], pathB + [i[1]], max(fb,2*(gB + i[2]))), max(fb,2*(gB + i[2])))

                # if OpenF.isthere(i[0]):
                #     U = min(U, gF_dic[i[0]] + gB_dic[1[0]])
    return[]

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
mm0 = MM0
mm = MM