#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' task: Visitor
    Visitor walks on Path only
    - when Visitor meet Brachiosaurus, Trex, or Parasaurolophus, they turn into Path
'''

__description__ = 'Visitor walks on Path and transforms dinosaurs into Path'
__author__ = 'Andres Mock'

import sys
import copy
sys.path.append('../')

from cells.Cells import *
from tasks.Task import Task

class RangerProtects(Task):
    ''' simulates ranger behavior '''
    def do_task(self, cell=None):
        ''' do the task > manipulate cells '''
        if cell is None:  # if not cell clicked by mouse
            cell = self.get_random_cell(Ranger)  # want a Visitor only to ..
        if isinstance(cell, Ranger):  # it's a Visitor
            neighbor = self.get_neighbor_cell_direction(cell, ["up", "left", "right","down"])  # get a random neighbor
            if isinstance(neighbor, (Brachiosaurus, Trex, Parasaurolophus)):  # meet a dinosaur
                neighbor = neighbor.mutate_to(Path)  # transform into Path
                self.update(neighbor)
            elif isinstance(neighbor, Path):
                previous_state = neighbor.get_state()  # save previous state
                cell.swap(neighbor)
                neighbor.set_state(previous_state)  # restore previous state
                self.update(cell)
                self.update(neighbor)
