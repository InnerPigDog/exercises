CHILDREN = ("Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny",
            "Harriet", "Ileana", "Joseph", "Kincaid", "Larry")

PLANTS = {"V": "Violets", "R": "Radishes", "G": "Grass", "C": "Clover"}


class Garden:
    def __init__(self, diagram: str, students: list[str] = CHILDREN):
        students = sorted(students)
        # Not all children have necessarily a plant. To avoid index errors only children with plants are considered.
        n_students = (len(diagram) - 1)//4
        self.student_plants = {}
        lines = diagram.split("\n")

        for i in range(n_students):
            self.student_plants.update(
                {students[i]: [PLANTS[lines[j][k]] for j in range(len(lines)) for k in (2 * i, 2 * i + 1)]})

        # self.child_plants = {students[i]: {PLANTS[diagram[2 * i]],
        #                                    PLANTS[diagram[2 * i + 1]],
        #                                    PLANTS[diagram[2 * i + 2 * n_children + 1]],
        #                                    PLANTS[diagram[2 * i + 2 * n_children + 2]]} for i in range(n_children)}

    def plants(self, student: str) -> list[str]:
        return self.student_plants[student]
