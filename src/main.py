from genetic_algorithm import GeneticAlgorithm
from teacher import Teacher
from schedule import Schedule
import pandas as pd


def load_course_sections_from_excel(file_path, sheet_name):
    """
    Load course sections from an Excel sheet.

    Args:
    file_path (str): The path to the Excel file.
    sheet_name (str): The name of the sheet to read course section data from.

    Returns:
    list: A list of dictionaries, each representing a course section.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    course_sections = []
    for _, row in df.iterrows():
        course_section = {
            'id': row.get('Course Section ID (CRN)', None),
            'name': row.get('Course Name', None),
            'section': row.get('Section', None),
            'units': row.get('Units', None)
        }
        course_sections.append(course_section)
    return course_sections


test_course_sections = load_course_sections_from_excel('../data/CPP Real World Data.xlsx', 'All Spring Course Sections (I)')
print(test_course_sections[:5])  # Display first 5 course sections for testing purposes



def load_classrooms_from_excel(file_path, sheet_name):
    """
    Load classroom data from an Excel sheet.

    Args:
    file_path (str): The path to the Excel file.
    sheet_name (str): The name of the sheet to read classroom data from.

    Returns:
    list: A list of dictionaries, each representing a classroom.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    classrooms = []
    for _, row in df.iterrows():
        classroom = {
            'room_number': row.get('Room Number', None),
            'board_type': row.get('Chalkboard or Whiteboard', None)
        }
        classrooms.append(classroom)
    return classrooms

# For testing the function that loads classrooms
test_classrooms = load_classrooms_from_excel('../data/CPP Real World Data.xlsx', 'All Classrooms (J)')
print("Test classrooms:", test_classrooms[:5])  # Display first 5 classrooms for testing purposes


def load_time_modules_from_excel(file_path, sheet_name):
    """
    Load time module data from an Excel sheet.

    Args:
    file_path (str): The path to the Excel file.
    sheet_name (str): The name of the sheet to read time module data from.

    Returns:
    list: A list of dictionaries, each representing a time module.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    time_modules = []
    for _, row in df.iterrows():
        time_module = {
            'time_slot_id': row.get('Time Slot ID', None),
            'description': row.get('Description', None)
        }
        time_modules.append(time_module)
    return time_modules


# For testing the function that loads time modules
test_time_modules = load_time_modules_from_excel('../data/CPP Real World Data.xlsx', 'All Times (K)')
print("Times:", test_time_modules[:5])  # Display first 5 time modules for testing purposes


def load_teachers_from_excel(file_path):
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

# For testing the function that loads time modules
test_teacher_modules = load_teachers_from_excel('../data/CPP Real World Data.xlsx')
print("Teachers:", test_teacher_modules[:5])  # Display first 5 time modules for testing purposes

def main():
    # Load teachers
    teachers = load_teachers_from_excel('../data/Simulated Data.xlsx')

    # Load course sections from the Excel file
    course_sections = load_course_sections_from_excel('../data/CPP Real World Data.xlsx',
                                                      'All Spring Course Sections (I)')

    # Load classrooms from the Excel file
    classrooms = load_classrooms_from_excel('../data/CPP Real World Data.xlsx', 'All Classrooms (J)')

    # Load time modules from the Excel file
    time_modules = load_time_modules_from_excel('../data/CPP Real World Data.xlsx', 'All Times (K)')

    # Initialize the GeneticAlgorithm with the loaded data
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

    # Run the evolutionary algorithm
    ga.run_evolution()


if __name__ == "__main__":
    main()