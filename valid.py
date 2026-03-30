def add_student(students, n, id, a, g, s):
    register = {"name": n, "id": id, "age": a, "grade": g, "status": s}
    students.append(register)
    print("Student added successfully.")


def show_student(students):
    if not students:
        print("This student doesn' exist.")
    else:
        for r in students:
            print(
                f"Name: {r['name']} | ID: {r['id']} | Age: {r['age']}| Grade: {r['grade']} | Status: {r['status']}")


def find_student(students, n):
    for r in students:
        if r['name'].lower() == n.lower():
            return r
    return None


def update_information(students, n, id,  a, g ):
    r = find_student(students, n,)
    if r:
        if id is not None:
            r['id'] = id
        if a is not None:
            r['age'] = a
        if g is not None:
            r['grade'] = g

        print("Student updated.")
    else:
        print("Student not found.")


def delete_student(students, n ):
    r = find_student(students, n )
    if r:
        students.remove(r)
        print("Student deleted.")
    else:
        print("Student not found.")
