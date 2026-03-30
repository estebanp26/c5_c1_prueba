import valid
import register


def register_student():
    students = []
    active = "A"
    while active == "A":
        print("\n--- WELCOME TO SYSTEM REGISTER SCHOOL EL BARRIO ---")
        print("1. Add student | 2. Show students | 3. Search student | 4. Update info")
        print("5. Delete info | 6. Save CSV | 7. Load CSV | 8. Exit")

        select = input("Select an option (1-8): ")

        try:
            if select == "1":
                n = input("Name: ").lower()
                id = float(input("ID: "))
                a = int(input("Age: "))
                g = int(input("Grade: "))
                s = input("Status (A/I): ")
                if s != "I":
                    print("This Student is active.")
                else:
                    "A" == active
                    print("This student is inactive")
                valid.add_student(students, n, id, a, g, s)

            elif select == "2":

                valid.show_student(students)

            elif select == "3":
                n = input("Name of student: ")
                res = valid.find_student(students, n)
                print(res if res else "Student not found.")

            elif select == "4":
                n = input("Name: ")
                id = input("ID: ")
                a = input("New Age: ")
                g = input("New Grade: ")
                s("Status: ")
                valid.update_information(students, n, float(id) if id else None, int(
                    a) if a else None, int(g) if g else None)

            elif select == "5":
                n = input("Name to delete: ")
                valid.delete_student(students, n, id, a, g, )

            elif select == "6":

                register.save_csv(students, "register.csv")

            elif select == "7":
                data = register.load_csv("register.csv")
                if data:
                    students = register
                    print("Data loaded.")

            elif select == "8":
                break
        except Exception as e:
            print(f"Error: {e}")


# Only runs in the main.
if __name__ == "__main__":
    register_student()
