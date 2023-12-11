from genetic_algorithm import GeneticAlgorithm
from teacher import Teacher
from schedule import Schedule

def main():
    # Initialize teachers with example data
    teachers = [
        Teacher(id=1, min_sections=2, max_sections=4, board_pref=1, time_pref=1, days_pref=2, section_prefs=[...]),  # Replace with actual preferences
        # Add more Teacher instances
    ]

    # Initialize other parameters with example data
    course_sections = [...]  # Replace with actual course section identifiers
    classrooms = [...]  # Replace with actual classroom identifiers
    time_modules = [...]  # Replace with actual time module identifiers

    ga = GeneticAlgorithm(
        population_size=100,
        mutation_rate=0.01,
        crossover_rate=0.7,
        num_generations=50,
        teachers=teachers,
        course_sections=course_sections,
        classrooms=classrooms,
        time_modules=time_modules
    )

    ga.run_evolution()

if __name__ == "__main__":
    main()
