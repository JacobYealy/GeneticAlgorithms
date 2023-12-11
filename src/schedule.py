import numpy as np


class Schedule:
    def __init__(self, teachers, course_sections, classrooms, time_modules):
        # Assuming teachers is a list of Teacher objects, each with their own course_prefs attribute
        self.teachers = teachers
        self.course_sections = course_sections  # This should be a list of CourseSection objects
        self.classrooms = classrooms
        self.time_modules = time_modules
        # The schedule_matrix dimensions should align with the problem's constraints and preferences
        # For simplicity, this example assumes a 2D matrix with teachers and course sections only
        self.schedule_matrix = np.zeros((len(teachers), len(course_sections)))

    def evaluate_fitness(self):
        # Evaluate the fitness of the schedule, including preference scores
        total_differences = 0
        total_preference_scores = 0

        for t_index, teacher in enumerate(self.teachers):
            assigned_sections = np.sum(self.schedule_matrix[t_index, :])
            ideal_number = len(self.course_sections) / len(self.teachers)
            differences = assigned_sections - ideal_number
            total_differences += np.abs(differences)

            # Collect preference scores for assigned sections
            for c_index, course_section in enumerate(self.course_sections):
                if self.schedule_matrix[t_index, c_index] == 1:  # Assuming 1 represents an assigned section
                    # Here you would calculate the preference score based on the teacher's preferences
                    total_preference_scores += teacher.get_preference_score(course_section)

        # Fitness evaluation accounts for both the balance of sections and teacher preferences
        # Here we are minimizing the sum of differences and preference scores, hence the inverse
        fitness = 1 / (total_differences + total_preference_scores)
        return fitness
