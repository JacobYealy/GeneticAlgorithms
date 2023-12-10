# Genetic Algorithms: Teacher Preference Model

## Goal
The goal of Model 3 is to minimize the difference 
in the number of course-sections assigned to each teacher, ideally balancing their workloads.

## Process
Define Decision Variables:

xijkt: A binary variable that indicates whether course-section i is assigned to classroom j at time module k with teacher t.
Qt: A real number that measures the difference between the number of course-sections taught by teacher t and the ideal number they should teach.

Objective Function:
The objective is to minimize Qt across all teachers t, ensuring an even distribution of course-sections among teachers.

Constraints:
Use the same constraints from previous models (2.10) - (2.14) and (2.17) - (2.30), except those specific to Model 2.
Additional constraints for Qt (2.31) and (2.32) ensure that Qt bounds the absolute value of the difference between the actual number of course-sections a teacher teaches and the ideal number.

Implementation:
Create a data structure or class to represent the schedule and include methods for initializing and evaluating the fitness based on the objective function.
Implement the genetic algorithm operators such as selection, crossover, and mutation to work with the scheduling representation.
Ensure the algorithm respects the defined constraints during the initialization and evolution of the population.
Define a function or method to calculate Qt for each teacher based on the current schedule representation and include it in the fitness evaluation.

Initialization:
Initialize the population with feasible schedules respecting the constraints and ensuring a diverse representation of potential solutions.

Evolution Loop:
Within the genetic algorithm's main loop, select the best-fitting schedules as parents for producing offspring.
Apply crossover and mutation operators to generate a new population of schedules.
Evaluate the new population and select the next generation of schedules based on their fitness scores.

Result Analysis:
After the algorithm converges or reaches a stopping condition, analyze the best schedules to ensure they meet the objective and constraints.
Possibly implement additional analysis to compare the genetic algorithm's results with heuristic or other non-optimal methods mentioned in the thesis.

Code Organization:
Update model.py to include the classes and methods for the genetic algorithm and the schedule representation.
Use utils.py for any additional helper functions needed during the implementation.

### Requirements
Make sure to run "pip install -r requirements.txt"

### Branching
Make a branch for each component you work on
