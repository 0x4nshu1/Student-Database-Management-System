import json


class DatabaseOperations:
    def __init__(self, file_path="students_database.json"):
        self.file_path = file_path
        self.students = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, "rt") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.file_path, "wt") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, rollno, name, age, gender):
        if rollno in self.students:
            print("Student already exists.")
        else:
            self.students[rollno] = {"name": name, "age": age, "gender": gender}
            print("New Student Added Successfully")
            self.save_data()

    def delete_student(self, rollno):
        if rollno not in self.students:
            print("No such student found.")
        else:
            del self.students[rollno]
            print("Deletion Successful")
            self.save_data()

    def display_all(self):
        if not self.students:
            print("No Students Found!")
        else:
            print("\nRoll No.\tName\tAge\tGender")
            for key in sorted(self.students.keys()):
                student = self.students[key]
                print(f"{key}\t\t{student['name']}\t{student['age']}\t{student['gender']}")

    def search_by_rollno(self, rollno):
        student = self.students.get(rollno)
        if student is None:
            print("No Such Record Found!")
        else:
            print(f"\nRoll No.: {rollno}\nName   : {student['name']}")
            print(f"Age    : {student['age']}\nGender : {student['gender']}")


# Main Program
print("Welcome to Student's Database\n")
db_value = DatabaseOperations()

while True:
    try:
        choice = int(
            input("Enter 0 for adding a student, 1 for searching a student, 2 for deleting a student, or 3 to exit: "))

        if choice == 0:
            db_value.add_student(
                int(input("Enter your ROLL No: ")),
                input("Enter the student's name: "),
                int(input("Enter the student's age: ")),
                input("Enter the student's gender: ")
            )
        elif choice == 1:
            rollno = int(input("Enter the ROLL No to search: "))
            db_value.search_by_rollno(rollno)
        elif choice == 2:
            rollno = int(input("Enter the ROLL No to delete: "))
            db_value.delete_student(rollno)
        elif choice == 3:
            db_value.save_data()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")
