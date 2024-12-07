import pandas as pd
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QLineEdit, QWidget
import matplotlib.pyplot as plt

def f(x):
    return fvar1*pow((x+fvar4), fvar2)+fvar3

def get_f():
    try:
        global fvar1, fvar2, fvar3, fvar4
        fvar1 = float(input_prompt1.text())
        fvar2 = float(input_prompt2.text())
        fvar3 = float(input_prompt3.text())
        fvar4 = float(input_prompt4.text())
        df["y"] = df["x"].apply(f)
        df.plot(x= "x", y="y", kind="scatter", grid=True)
        plt.show()
    except:
        print("error: bad input, try again")

lst = []
counter = -1000
while counter <= 1000:
    lst.append(counter)
    counter += 0.01
df = pd.DataFrame({"x": lst})
app = QApplication([])
w = QWidget()
input_prompt1 = QLineEdit()
input_prompt1.setPlaceholderText("Συντελεστής του χ: ")
input_prompt2 = QLineEdit()
input_prompt2.setPlaceholderText("Εκθέτης του χ: ")
input_prompt3 = QLineEdit()
input_prompt3.setPlaceholderText("Κατακόρυφη μετατόπιση: ")
input_prompt4 = QLineEdit()
input_prompt4.setPlaceholderText("Οριζόντια μετατόπιση: ")
pb1 = QPushButton("enter")
lv1 = QVBoxLayout()
lv1.addWidget(input_prompt1)
lv1.addWidget(input_prompt2)
lv1.addWidget(input_prompt3)
lv1.addWidget(input_prompt4)
lv1.addWidget(pb1)
w.setLayout(lv1)
w.resize(500, 500)
w.show()
pb1.clicked.connect(get_f)
app.exec()