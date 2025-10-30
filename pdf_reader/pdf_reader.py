# ------------------------------------------
# PDF READER
# ------------------------------------------
# This program reads the text from a PDF file
# and speaks it aloud using the pyttsx3 text-to-speech engine.
# ------------------------------------------

import PyPDF2
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Set voice and speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice (if available)
engine.setProperty('rate', 150)

# Ask user for the PDF file name
filename = input("ENTER PDF FILE NAME (WITH .pdf EXTENSION): ")

# Open the PDF file in read-binary mode
with open(filename, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    print(f"\nTOTAL PAGES: {total_pages}\n")

    # Loop through all pages
    for i in range(total_pages):
        page = reader.pages[i]
        text = page.extract_text()

        if text:
            print(f"--- PAGE {i + 1} ---\n{text}\n")
            engine.say(text)  # Convert text to speech
            engine.runAndWait()
        else:
            print(f"[Warning] Page {i + 1} has no readable text.")
