import csv

def save_csv(students, path):
    if not students:
        print("This student doesn't exist.")
        return
    try:
        with open(path, 'w', newline='') as f:
            writer = csv.DictWriter(
                f, fieldnames=["name", "id", "age", "grade", "status"])
            writer.writeheader()
            writer.writerows(students)
        print(f"Student saved in: {path}")
    except Exception as e:
        print(f"Error saving file: {e}")


def load_csv(path):
    loaded_students = []
    try:
        with open(path, 'r',) as f:
            reader = csv.DictReader(f)
            for row in reader:
                    n = row['name']
                    id = float(row['id'])
                    a = int(row['age'])
                    g = row['grade']
                    s = row['status']
                    loaded_students.append(
                            {"name": n, "id": id, "age": a, "grade": g, "status": s})
        return loaded_students
    except FileNotFoundError:
        return []
