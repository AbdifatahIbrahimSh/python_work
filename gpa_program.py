"""Develops a program that takes the points of courses and returns the actual gpa of that semester
   Developer: Abdifatah
   Date: 01 November, 2022
   Time: 2:30pm
"""
class GPA:
    """Creates a class fro gpa"""

    def __init__(self, course_names_and_grades):
        """Initializes the object with course points"""
        self.course_names_and_grades = course_names_and_grades;
        self.honors = []

    def grade_in_letter(self, marks):
        """Changes the marks into letter"""
        if marks >= 0 and marks <= 100:
            if marks > 94: return 'A+'
            elif marks > 89: return 'A'
            elif marks > 84: return 'A-'
            elif marks > 79: return 'B+'
            elif marks > 74: return 'B'
            elif marks > 69: return 'B-'
            elif marks > 64: return 'C+'
            elif marks > 59: return 'C'
            elif marks > 54: return 'C-'
            elif marks > 49: return 'D'
            else: return 'F'
        else:
            return None

    def quality_point_equivalent(self, marks):
        """Changes the marks in a quality point average"""
        if marks >= 0 and marks <= 100:
            if marks > 94: return 4.00
            elif marks > 89: return 4.00
            elif marks > 84: return 3.67
            elif marks > 79: return 3.33
            elif marks > 74: return 3.00
            elif marks > 69: return 2.67
            elif marks > 64: return 2.33
            elif marks > 59: return 2.00
            elif marks > 54: return 1.67
            elif marks > 49: return 1.00
            else: return 0.00
        else:
            return None

    def honor(self, qpe):
        """Finds the honor of the course"""
        return 3 * qpe;
    
    def total_of_qpes(self, gpe):
        """Finds the sum of the quality point equavalents"""
        sum = 0
        for index in range(0, len(gpe)):
            sum += gpe[index]
        return sum;

    def gpa(self):
        
        return self.total_of_qpes() / (len(self.course_names_and_grades) * 3);

    def get_full_gpa(self):
        """Calculates gpa and prints them into the user"""
        draft_of_gpa = ''
        draft_of_gpa += f"{'CourseName':45s} {'Credit':10s} {'Points':10s} {'Letter':10s} {'GPE':10s} {'Honor':10s}\n"
        draft_of_gpa += f"{'':-<45s} {'':-<10s} {'':-<10s} {'':-<10s} {'':-<10s} {'':-<10s}\n"
        for course_name, grade in self.course_names_and_grades.items():
            letter = self.grade_in_letter(grade)
            gpe = self.quality_point_equivalent(grade)
            honor = self.honor(gpe)
            self.honors.append(honor)
            draft_of_gpa += f"{course_name:45s} {3:<10} {grade:<10d} {letter:10s} {gpe:<10.2f} {honor:<10.2f}\n"

        return draft_of_gpa


    def print_gpa(self):
        """Returns a string format of the gpa"""
        final_draft = ''
        final_draft += self.get_full_gpa().rstrip()
        sum = self.total_of_qpes(self.honors)
        gpa = sum / (len(self.course_names_and_grades) * 3)
        final_draft += f"\n{(len(self.course_names_and_grades) * 3):47d} {sum:47.2f}"
        final_draft += f"\n{'GPA':>83s} {gpa:10.2f}"
        return final_draft;

    def write_to_file(self, file_name):
        """Prints the trasncript into a txt file"""
        filename = f"{file_name}.txt"
        with open(filename, 'w') as f:
            f.write(self.print_gpa()) 


