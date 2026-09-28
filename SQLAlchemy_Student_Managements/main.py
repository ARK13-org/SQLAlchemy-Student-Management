from database import Database, Field, Master, Student, ClassRoom


def main():
    db = Database()

    # Create database tables
    db.create_tables()

    with db.get_session() as session:

        # -------------------------
        # Create a field
        # -------------------------

        math = Field(name="Math")

        # -------------------------
        # Create a student
        # -------------------------

        student = Student(
            name="Alireza",
            last_name="Koupaei",
            field=math,
        )

        # -------------------------
        # Create a master
        # -------------------------

        master = Master(
            name="Fargol",
            last_name="Zarabian",
        )

        # -------------------------
        # Create a classroom
        # -------------------------

        classroom = ClassRoom(
            name="C1",
            field=math,
            master=master,
        )

        # -------------------------
        # Add student to classroom
        # -------------------------

        classroom.students.append(student)

        session.add(classroom)
        session.commit()

        # -------------------------
        # Display results
        # -------------------------

        print("Field:")
        print(math)

        print("\nMaster:")
        print(master)

        print("\nStudent:")
        print(student)

        print("\nClassroom:")
        print(classroom)

        print("\nClassroom students:")
        for student in classroom.students:
            print(student)


if __name__ == "__main__":
    main()