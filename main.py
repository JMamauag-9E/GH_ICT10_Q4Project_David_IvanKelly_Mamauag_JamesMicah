from pyscript import document, display

class classmate:
    def __init__(self, name, section, fav_subject):
        self.name = name
        self.section = section
        self.fav_subject = fav_subject

    def introduce(self):
        return (
            f"Hi! my name is {self.name}. "
            f"My section is {self.section}, "
            f"and my favorite subject is {self.fav_subject}."
        )

classmates = [
classmate("James",  "Emerald", "Philosophy"),
classmate("Kyla",   "Emerald", "English"),
classmate("Annika", "Emerald", "English"),
classmate("Joseph", "Emerald", "Values Education"),
classmate("Aurelia",  "Emerald", "English"),
]

def show_list(event):
    output_div = document.getElementById("output")
    
    if output_div.innerHTML != "":
        output_div.innerHTML = ""

    else:
        for mate in classmates:
            display(mate.introduce(), target="output")

def add_classmate(event):
    name = document.getElementById("Name").value.strip()
    section = document.getElementById("Section").value.strip()
    fav_subject = document.getElementById("FavSubject").value.strip()

    if not name or not section or not fav_subject:
        display(
            "Fill in all lines before adding someone.",
            target="output",
        )
        return

    classmate_new = classmate(name, section, fav_subject)
    classmates.append(classmate_new)
    display(f"Added: {classmate_new.introduce()}", target="output")

    document.getElementById("Name").value = ""
    document.getElementById("Section").value = ""
    document.getElementById("FavSubject").value = ""