from tkinter import *
import os


# METHOD
# -------------------------------------------------------------
def submit():
    """
    take entry from text_area and put save it in a file named
    'Short_notes.txt' in the same folder,
    after saving it deletes the entry and wait for next entry.
    :return: None
    """
    x = text.get("1.0", END)
    if x.isspace() or x == "":
        pass
    else:
        with open(rf"{os.path.abspath('Short_notes.txt')}",
                  'a+',
                  encoding="utf8") as fp:
            fp.write(str(x) + "\n")
        text.delete("1.0", END)


# END METHOD
# -------------------------------------------------------------


# WINDOWS
# --------------------------------------------------
def open_notes():
    """
    creates a new window to show saved notes.
    delete button to delete the notes
    :return: None
    """

    # METHOD
    # -------------------------------------------------------------
    def delete():
        """
        remove everything stored in the file 'Short_notes.txt',
        exit from the notes window.
        :return: None
        """
        try:
            # instead of os.remove() i preferred :
            with open(rf"{os.path.abspath('Short_notes.txt')}",
                      'w+',
                      encoding="utf8") as f:
                f.write("")

            notes_window.destroy()
        except FileNotFoundError:
            pass

    # END METHOD
    # -------------------------------------------------------------

    notes_window = Toplevel()
    notes_window.title("Notes")
    notes_window.resizable(False, False)  # non-resizable

    text_1 = Text(notes_window,
                  font=("Ink free", 17, "bold"),
                  bg="light grey",
                  fg="dark Red",
                  height=8,
                  width=20,
                  padx=10,
                  pady=10,
                  )
    text_1.pack()

    delete_button = Button(notes_window,
                           font=("Arial", 10, "bold italic"),
                           width=36,
                           bd=5,
                           relief=RAISED,
                           text="delete",
                           command=delete,
                           bg="pink")
    delete_button.pack(side=BOTTOM)

    # taking text from the file to show in notes_window
    try:
        with open(rf"{os.path.abspath('Short_notes.txt')}",
                  'r+',
                  encoding="utf8") as fp:
            x = fp.read()

        if x == "" or x.isspace():
            text_1.insert("1.0", "No notes found!!")
            text_1.config(state="disabled")
        else:
            text_1.insert("1.0", x)
            text_1.config(state="disabled")

    except FileNotFoundError:
        text_1.insert("1.0", "No notes found!!")
        text_1.config(state="disabled")

    notes_window.mainloop()


# MAIN WINDOW
# ====================================================
"""
main window contains
1) text_area     : where we type notes.
2) submit_button : to save the notes.
3) open_button   : to show the notes.
"""
window = Tk()
window.config(background="light yellow")
window.resizable(False, False)  # non-resizable
window.title("Short Notes")

text = Text(window,
            font=("Ink free", 20, "bold"),
            bg="light yellow",
            fg="dark Red",
            height=8,
            width=20,
            padx=10,
            pady=10,
            )

text.pack()

submit_button = Button(window,
                       font=("Arial", 10, "bold italic"),
                       width=20,
                       bd=5,
                       relief=RAISED,
                       text="Save note",
                       command=submit,
                       bg="pink")
submit_button.pack(side=LEFT)
open_button = Button(window,
                     font=("Arial", 10, "bold italic"),
                     width=20,
                     bd=5,
                     relief=RAISED,
                     text="Show notes",
                     command=open_notes,
                     bg="pink")
open_button.pack(side=RIGHT)
window.mainloop()

# END MAIN WINDOW
# ====================================================
# END WINDOWS
# --------------------------------------------------
