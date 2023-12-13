import numpy as np
from schedule import Schedule
from utils import timing

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, num_generations, teachers, course_sections, classrooms, time_modules):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.num_generations = num_generations
        self.teachers = teachers
        self.course_sections = course_sections
        self.classrooms = classrooms
        self.time_modules = time_modules
        self.population = [Schedule(teachers, course_sections, classrooms, time_modules) for _ in range(population_size)]

    @timing
    def run_evolution(self):
        for generation in range(self.num_generations):
            fitness_scores = [schedule.evaluate_fitness() for schedule in self.population]
            parents = self.select_parents(fitness_scores)
            children = self.crossover(parents)
            self.mutate(children)
            self.population = children

    def select_parents(self, fitness_scores):
        # Selection logic to choose parents for the next generation
        parents = []
        for _ in range(len(self.population)):
            competitors = np.random.choice(self.population, 4)
            best = min(competitors, key=lambda x: x.evaluate_fitness())
            parents.append(best)
        return parents

    def crossover(self, parents):
        # Crossover logic to create children from parents
        children = []
        for _ in range(0, len(parents), 2):
            parent1, parent2 = parents[_], parents[_+1]
            child = self.create_child(parent1, parent2)
            children.append(child)
        return children

    def create_child(self, parent1, parent2):
        # One-point crossover
        crossover_point = np.random.randint(0, len(parent1.course_sections))
        child_schedule_matrix = np.zeros_like(parent1.schedule_matrix)

        child_schedule_matrix[:crossover_point, :] = parent1.schedule_matrix[:crossover_point, :]
        child_schedule_matrix[crossover_point:, :] = parent2.schedule_matrix[crossover_point:, :]

        child = Schedule(parent1.teachers, parent1.course_sections, parent1.classrooms, parent1.time_modules)
        child.schedule_matrix = child_schedule_matrix
        return child

    def mutate_schedule(self, schedule):
        num_mutations = np.random.randint(1, len(schedule.course_sections))
        for _ in range(num_mutations):
            teacher_idx = np.random.randint(0, len(schedule.teachers))
            section_idx = np.random.randint(0, len(schedule.course_sections))
            # Mutate logic (?)
            schedule.schedule_matrix[teacher_idx, section_idx] = 1 - schedule.schedule_matrix[teacher_idx, section_idx]

