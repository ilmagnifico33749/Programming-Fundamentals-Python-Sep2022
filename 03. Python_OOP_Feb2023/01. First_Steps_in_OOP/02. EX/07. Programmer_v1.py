
class Programmer:
    def __init__(self, name, language, skills):
        self.name = str(name)
        self.language = str(language)
        self.skills = int(skills)

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += int(skills_earned)
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        previous_language = self.language
        if new_language != previous_language and self.skills >= skills_needed:
            self.language = new_language
            return f"{self.name} switched from {previous_language} to {new_language}"

        elif new_language == previous_language and self.skills >= skills_needed:
            return f"{self.name} already knows {new_language}"

        elif new_language != previous_language and self.skills < skills_needed:
            return f"{self.name} needs {skills_needed - self.skills} more skills"



# ############################################################
# Test_Code_1:
programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
# -----------------------------------------------------------
# Output_1:
# John does not know Python
# John already knows Java
# John needs 50 more skills
# John watched Java: zero to hero
# John switched from Java to Python
# John watched Python Masterclass
# ############################################################
