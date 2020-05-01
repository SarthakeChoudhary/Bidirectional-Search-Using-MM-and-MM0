# Implementation of Bi-directional Search using MM, MM0 in Pac-Man Domain

We have implemented a Bi-diretional Serach using MM and MM0 algorithm for a Pac-Man Domain which is guaranteed to meet in the middle. We are also provinding a comparative analysis of this algorithm with that of A* search. The algorithm is tested for different range of complexity(obstacles encountered by the Pac-Man) namely for 0%,30% and 50% respectively.


The pseudocode is inspired from the paper “Bidirectional Search That Is Guaranteed to Meet in the Middle”, Robert C. Holte, Ariel Felner, Guni Sharon, Nathan R. Sturtevant, AAAI 2016.


# What you will need to run this:

Python 2 

# How to run:
Navigate to the search folder of Bidirectional_Search and enter the following commands:
The code can be tested for different maze size namely: tiny, medium and big

## To check the results for 0% complexity:

* To run A*, python pacman.py -l tinyMaze0 -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
* To run MM0, python pacman.py -l tinyMaze0 -z .5 -p SearchAgent -a fn=bdmm0,heuristic=manhattanHeuristic
* To run MM, python pacman.py -l tinyMaze0 -z .5 -p SearchAgent -a fn=bdmm,heuristic=manhattanHeuristic

* To check the complexity for medium and big maze, replace tinyMaze0 by mediumMaze0 or bigMaze0

## To check the results for 30% complexity:

* To run A*, python pacman.py -l mediumMaze30 -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
* To run MM0, python pacman.py -l mediumMaze30 -z .5 -p SearchAgent -a fn=bdmm0,heuristic=manhattanHeuristic
* To run MM, python pacman.py -l mediumMaze30 -z .5 -p SearchAgent -a fn=bdmm,heuristic=manhattanHeuristic

* To check the complexity for tiny and big maze, replace mediumMaze30 by tinyMaze30 or bigMaze30

## To check the results for 50% complexity:

* To run A*, python pacman.py -l bigMaze50 -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
* To run MM0, python pacman.py -l bigMaze50 -z .5 -p SearchAgent -a fn=bdmm0,heuristic=manhattanHeuristic
* To run MM, python pacman.py -l bigMaze50 -z .5 -p SearchAgent -a fn=bdmm,heuristic=manhattanHeuristic

* To check the complexity for medium and tiny maze, replace bigMaze50 by mediumMaze50 or tinyMaze50

# Team Members:
* Sarthake Choudhary
* Ashish Verma
* Ibrahim Hasan
* Anusha Vaidya

   
