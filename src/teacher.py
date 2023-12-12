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
            board_pref = row['Board Pref 0-none,     1-white,    2-chalk']
            time_pref = row['Time Pref  0-none      1-morn     2-aft          3-eve']
            days_pref = row['Days of Week         0-no pref   1-MWF      2-TR']

            # Extract course preferences
            course_prefs = {str(i): row[str(i)] for i in range(1, 30)}  # Adjust range based on the number of courses

            teacher = Teacher(id, min_sections, max_sections, board_pref, time_pref, days_pref, course_prefs)
            teachers.append(teacher)

        return teachers

    def get_preference_score(self, schedule):
        # Initialize the score
        preference_score = 0

        # Check each course-section assignment in the schedule
        for course_section in schedule.course_sections:
            assigned_teacher_id, assigned_time, assigned_day = course_section.get_details()

            # Check if the course-section is assigned to this teacher
            if assigned_teacher_id == self.id:
                # Get the preference score for the course-section
                course_pref_score = self.course_prefs.get(course_section.catalog_number,
                                                          0)  # default to 0 if no preference

                # Add the preference score to the total preference score
                # Assuming that a score of 0 is the best (most preferred) and higher scores are worse
                preference_score += course_pref_score

        # Additional preference checks for board, time, and day can be added

        return preference_score
