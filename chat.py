import openai
from gtts import gTTS
import pygame
import os

openai.api_key = "AIzaSyDsC-YuBt1xI9Wi4KBGJx4yL7BB6N68qfA"

def reconhecer_voz(caminho_audio):
    with open(caminho_audio, "rb") as audio_file:
        transcricao = openai.Audio.transcribe("whisper-1", audio_file)
    return transcricao["text"]

def gerar_resposta_chatgpt(texto_entrada):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": texto_entrada}]
    )
    return response.choices[0].message.content

def sintetizar_voz(texto_resposta):
    tts = gTTS(text=texto_resposta, lang='pt')
    tts.save("resposta.mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("resposta.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
