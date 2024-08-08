import pyttsx3
from pydub import AudioSegment
import os
import re
import random
from text_generator import generator

voice_id=[]
comand=int(input("how many voices do your computer have:"))
if comand == 2:
    voice_id=[0,1]
elif comand == 4:
    voice_id=[0,1,2,3,4]
else :
    voice_id=[0]  

def text_filter(sentences):
    separated_sentences = []
    
    for item in sentences:
        split_sentences = [sentence.strip() + punctuation for sentence, punctuation in re.findall(r'\d+\.\s([^.!?]+)([.!?]*)', item)]
    
        for sentence in split_sentences:
            separated_sentences.append(sentence)  
    return separated_sentences 

def text_to_speech(text, temp_file):  
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voiceid=random.choice(voice_id)
    engine.setProperty('voice', voices[voiceid].id)
    engine.setProperty('rate', 140)
    
    engine.save_to_file(text, temp_file)
    engine.runAndWait()
    
def save_audio(temp_file, output_folder, output_filename):
    audio = AudioSegment.from_wav(temp_file)
    output_path = os.path.join(output_folder, output_filename)
    audio.export(output_path, format="wav")
    os.remove(temp_file)
    return output_path

def get_unique_filename(output_folder, base_name, extension="wav"):
    counter = 1
    output_filename = f"{base_name}.{extension}"
    output_path = os.path.join(output_folder, output_filename)
    
    while os.path.exists(output_path):
        output_filename = f"{base_name}_{counter}.{extension}"
        output_path = os.path.join(output_folder, output_filename)
        counter += 1
        
    return output_filename

if __name__ == "__main__":
    sentences = generator()
    sentences = text_filter(sentences)  
    output_folder = "gemini/dataset"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for idx, text in enumerate(sentences):
        temp_file = "temp.wav"
        text_to_speech(text, temp_file)
        base_name = f"output_{idx+1}"
        unique_filename = get_unique_filename(output_folder, base_name)
        saved_path = save_audio(temp_file, output_folder, unique_filename)
        print(f"Saved audio for sentence {idx+1} as {saved_path}")

