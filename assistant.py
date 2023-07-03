# Las librerias deben importarse desde la consola o desde línea de comando ejecutando pip install  # noqa: E501
import speech_recognition as sr
import openai
from pygame import mixer
import pyttsx3
import os
import time as ti
import random


openai.api_key = "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"


# Definimos la función que transforma la voz captada en el mic a texto
def transformar_audio_a_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("Ya puedes hablar!")
        audio = r.listen(origen)
        try:
            pedido = r.recognize_google(audio, language="es-PE")
            print("You: " + pedido)
            return pedido
        except sr.UnknownValueError:
            print("Ups, no entendi!")
            return "Sigo esperando"
        except sr.RequestError:
            print("Ups, no hay servicio!")
            return "Sigo esperando"
        except:
            print("Ups, algo salio mal!")
            return "Sigo esperando"


# Definimos la función que va a transformar el texto (mensaje) en audio
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    # Bajar velocidad de reproducción, por defecto es 200
    engine.setProperty('rate', 150)

    # Obtener lista de voces disponibles
    voices = engine.getProperty('voices')
    # Recorrer las voces para encontrar la voz en español de Perú
    for voice in voices:
        if "spanish" in voice.languages and "peru" in voice.id:
            engine.setProperty('voice', voice.id)  # Configurar la voz en español de Perú
            break

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


def main():
    conversation = ""

    hablar("Hola! Soy SARA tu asesora empresarial virtual. Estoy aquí para ayudarte en todo lo relacionado con tu negocio. ¿En qué puedo asistirte?")

    while True:
        question = transformar_audio_a_texto().lower()

        conversation += "\nYou: " + question + "\nSARA:"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=conversation,
            temperature=0.5,
            max_tokens=100,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["\n", " You:", " SARA:"]
        )
        answer = response.choices[0].text.strip()
        conversation += answer
        print("SARA: " + answer + "\n")
        hablar(answer)


main()
