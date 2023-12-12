from genetic_algorithm import GeneticAlgorithm
from teacher import Teacher
from schedule import Schedule
import pandas as pd

def load_teachers_from_excel(file_path):
        # Probably want to change this out with teacher functions
    df = pd.read_excel(file_path)
    teachers = []
    for index, row in df.iterrows():
        teachers.append(Teacher(
            id=row['Teacher ID'],
            min_sections=row['Min Sections'],
            max_sections=row['Max Sections'],
            board_pref=row['Board Pref'],
            time_pref=row['Time Pref'],
            days_pref=row['Days of Week'],
            section_prefs={i: row[i] for i in range(1, 30)}
        ))
    return teachers

def main():
    teachers = load_teachers_from_excel('../data/Simulated Data.xlsx')


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
