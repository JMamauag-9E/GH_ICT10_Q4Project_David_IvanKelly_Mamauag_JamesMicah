import logging
import warnings

# Suppress matplotlib font cache warnings
logging.getLogger('matplotlib').setLevel(logging.ERROR)
warnings.filterwarnings("ignore", message=".*font cache.*")

from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

# Global data storage
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
absences = [0, 0, 0, 0, 0]

def displaying_output(e):
    document.getElementById("output").innerHTML = ""
    day = document.getElementById('input1').value
    
    try:
        num = int(document.getElementById('input2').value)
    except ValueError:
        num = 0

    index = days.index(day)
    absences[index] = num

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(days, absences, marker='o', linestyle='-', color='#1e3c72')

    ax.set_title("Attendance Tracker")
    ax.set_xlabel("Days")
    ax.set_ylabel("Number of Absences")
    ax.grid(True)

    # Use display on the figure itself
    display(fig, target="output")