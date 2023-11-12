import tkinter as tk
from googletrans import Translator
import pyperclip

translated_text_for_copy = ""  # Define the variable here

def translate_text():
    global translated_text_for_copy  # Declare it as a global variable
    input_text = input_text_entry.get()
    target_language = target_language_entry.get()

    translator = Translator()
    translated_text = translator.translate(input_text, dest=target_language)

    translated_text_label.config(text="Translated text: " + translated_text.text)
    translated_text_for_copy = translated_text.text  # Store the translated text for copying

def copy_translated_text():
    copy_to_clipboard(translated_text_for_copy)
    copy_status_label.config(text="Text copied to clipboard")

def copy_to_clipboard(text):
    pyperclip.copy(text)

# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Create input and target language entry fields
input_text_label = tk.Label(root, text="Enter text to translate:")
input_text_label.pack()
input_text_entry = tk.Entry(root, width=40)
input_text_entry.pack()

target_language_label = tk.Label(root, text="Enter the target language (e.g., 'fr' for French):")
target_language_label.pack()
target_language_entry = tk.Entry(root, width=10)
target_language_entry.pack()

# Create a Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Create a Copy to Clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_translated_text)
copy_button.pack()

# Display translated text
translated_text_label = tk.Label(root, text="")
translated_text_label.pack()

# Display copy status
copy_status_label = tk.Label(root, text="")
copy_status_label.pack()

# Run the GUI
root.mainloop()
