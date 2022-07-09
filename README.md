# RBE550-Motion-planning

### Assignment 1: Turtles
TBF

### Assignment 2: Flatland

Planning algorithms - Breadth first search, Depth first search, Dijkstra’s, and
A* have been implemented on a grid world environment of configurable obstacle
density.

#### Breadth First Search:
![Breadth First Search](/hw1/media/bfs.gif)

#### Depth First Search:
![Depth First Search](/hw1/media/dfs.gif)

#### Dijkstra's (diagonal steps allowed):
![Dijkstra's](/hw1/media/dijkstras.gif)

#### A*:
![A*](/hw1/media/a-star.gif)

### Steps to run the code

1. Add to your .bashrc

   `export PYTHONPATH=/home/<user>/RBE550-Motion-planning/`


2. Create virtual env. and source it

   `python3.9-venv -m venv venv`

   `source venv/bin/activate`


2. Install requirements:

   `pip install -r requirements.txt`


4. Run path_planner.py

   `python hw1/path_planner.py`
