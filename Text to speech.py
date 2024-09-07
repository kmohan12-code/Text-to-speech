import tkinter as tk
from tkinter import LabelFrame, Label, Entry, Button
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak_text():
    """Function to convert text to speech."""
    text = text_entry.get()  # Get the text from the entry widget
    if text:  # Check if the text is not empty
        engine.say(text)  # Queue the text to be spoken
        engine.runAndWait()  # Wait for the speech to finish

# Create the main window
root = tk.Tk()
root.title("Text to Speech")
root.geometry("500x500")  # Set the window size
root.resizable(False, False)  # Disable window resizing

# Create a LabelFrame to hold the widgets
obj = LabelFrame(root, text="Text to Speech", font=20, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

# Create a label for the text entry
lbl = Label(obj, text="Text", font=30)
lbl.pack(side=tk.LEFT, padx=5)

# Create an entry widget for user input
text_entry = Entry(obj, font=30, width=25, bd=5)
text_entry.pack(side=tk.LEFT, padx=5)

# Create a button to trigger the speech
speak_button = Button(obj, text="Speak", font=20, bg="black", fg="white", command=speak_text)
speak_button.pack(side=tk.LEFT, padx=5)

# Start the main loop
root.mainloop()
