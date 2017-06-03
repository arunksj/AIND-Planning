from aimacode.planning import Action
from aimacode.utils import expr
from aimacode.search import Node
import unittest
from lp_utils import decode_state
from my_air_cargo_problems import (
    air_cargo_p1, air_cargo_p2, air_cargo_p3,
)
from my_planning_graph import (
    PlanningGraph, PgNode_a, PgNode_s, mutexify
)

if __name__ == '__main__':
    problem1 = air_cargo_p1()

    print(problem1.actions_list)

    print(problem1.initial)

    pg = PlanningGraph(problem1, problem1.initial)
