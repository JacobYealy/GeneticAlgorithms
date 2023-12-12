from GeneticAlgorithms.src import schedule


class Teacher:
    def __init__(self, id, min_sections, max_sections, board_pref, time_pref, days_pref, course_prefs):
        self.id = id
        self.min_sections = min_sections
        self.max_sections = max_sections
        self.board_pref = board_pref
        self.time_pref = time_pref
        self.days_pref = days_pref
        # course_prefs is a list or dictionary mapping course catalog numbers to preference scores
        self.course_prefs = course_prefs

    def create_teachers_from_dataframe(df):
        teachers = []
        for index, row in df.iterrows():
            id = row['Teacher ID']
            min_sections = row['Min Sections']
            max_sections = row['Max Sections']
            board_pref = row['Board Pref 0-none, 1-white, 2-chalk']
            time_pref = row['Time Pref  0-none 1-morn 2-aft 3-eve']
            days_pref = row['Days of Week 0-no pref 1-MWF 2-TR']

            # Extract course preferences
            course_prefs = {str(i): row[str(i)] for i in range(1, 30)}  # Adjust range based on the number of courses

            teacher = Teacher(id, min_sections, max_sections, board_pref, time_pref, days_pref, course_prefs)
            teachers.append(teacher)

        return teachers

    def get_preference_score(self, course_section):
        # Initialize the score
        preference_score = 0

        # Check each course-section assignment in the schedule
        for course_section in schedule.course_sections:
            assigned_teacher_id, assigned_board_type, assigned_time, assigned_days = course_section.get_details()

            # Check if the course-section is assigned to this teacher
            if assigned_teacher_id == self.id:
                # Get the preference score for the course-section
                course_pref_score = self.course_prefs.get(course_section.catalog_number,
                                                          0)  # default to 0 if no preference
                preference_score += course_pref_score  # Lower score is better

                # Add board preference score (assuming 0 for match, otherwise 1)
                if assigned_board_type != self.board_pref and self.board_pref != 0:
                    preference_score += 1  # Penalize mismatch

                # Add time preference score (assuming 0 for match, otherwise 1)
                if assigned_time != self.time_pref and self.time_pref != 0:
                    preference_score += 1  # Penalize mismatch

                # Add day preference score (assuming 0 for match, otherwise 1)
                if assigned_days != self.days_pref and self.days_pref != 0:
                    preference_score += 1  # Penalize mismatch

        return preference_score
