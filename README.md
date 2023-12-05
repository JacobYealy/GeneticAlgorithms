# Genetic Algorithms

## Instructions (Delete later)

We will work with some of the model described in the attached thesis. I have (tried) to summarize the data
into usable digital form in 2 spreadsheets. One contains the simulated data that was used for most of the 
models and experiments described in the paper. The other contains the real world data gathered for the 
Math & Stats department at Cal Poly Pomona. 

The goal of this project is to actually implement
and run a Genetic Algorithm and compare our results to the published results from the paper.


## Functions

### Objective Function
Model 5's objective function is designed to maximize teacher satisfaction with their assigned course-sections.

### Teacher satisfaction Matrix
It's a matrix where each row represents a teacher and each column represents a course-section. 
The satisfaction is rated on a scale of 0 to 5, with 0 being the most desired outcome and 5 the least.

### Constraints
The model utilizes the same decision variables as the Basic Teacher Model and 
employs constraints from the Basic Teacher Model (2.10 - 2.14 and 2.17 - 2.19) and the 
Teacher Preference Model (2.20 - 2.28). However, constraints (2.29 and 2.30) are not considered in this model, 
as preferences are now accounted for in the objective function on a course-section-by-course-section basis, 
rather than just pure versus applied preferences.

### Minimization of objective function
The objective is to minimize the overall dissatisfaction.