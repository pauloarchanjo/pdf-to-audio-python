import pyttsx3
import PyPDF2
import tempfile
import time

def wait_for_conversion(engine):
    while engine.isBusy():
        time.sleep(0.1)

with open('your_pdf_file.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)

    text = ''
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()

clean_text = ' '.join(text.strip().split())

print(clean_text)

speaker = pyttsx3.init()

with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write(clean_text)

speaker.save_to_file(temp_file.name, 'your_audio_file.mp3')

wait_for_conversion(speaker)

speaker.runAndWait()

temp_file.close()

speaker.stop()
