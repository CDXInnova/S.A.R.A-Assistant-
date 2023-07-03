import JarvisAI
import re
import pprint
import random

obj = JarvisAI.JarvisAssistant()

# Cambiar el modelo de voz a una mujer joven en español
obj.voice_change('es', 'f', 2)

def t2s(text):
    obj.text2speech(text)


# Función para buscar información en Wikipedia
def search_wikipedia(topic):
    response = obj.tell_me(topic)
    return response


# Función para buscar información en Google
def search_google(query):
    response = f"Lo siento, no puedo buscar en Google en este momento. Pero puedo proporcionarte información sobre {query} desde otras fuentes."
    return response


# Función para manejar las preguntas relacionadas con emprendedores y startups
def handle_entrepreneurship_questions(query):
    # Aquí puedes implementar la lógica para responder preguntas específicas sobre emprendedores y startups
    response = f"Aquí encontrarás información relevante para emprendedores y startups sobre {query}."
    return response


# Función para saludar al usuario y pedir su nombre
def greet_and_get_name():
    obj.text2speech("¡Hola! Soy tu asistente virtual. ¿Cómo puedo ayudarte hoy?")
    name = obj.mic_input()
    obj.text2speech(f"Mucho gusto, {name}. ¿En qué puedo ayudarte?")
    return name


# Obtener el nombre del usuario al inicio del programa
user_name = greet_and_get_name()

while True:
    res = obj.mic_input()

    if re.search('hello|hi', res):
        obj.text2speech(f"Hola, {user_name} ¿En qué puedo ayudarte?")

    if re.search('wikipedia', res):
        match = re.search('wikipedia (.+)', res)
        if match:
            topic = match.group(1)
            response = search_wikipedia(topic)
            obj.text2speech(response)
        else:
            obj.text2speech("Lo siento, no pude entender el tema que estás buscando en Wikipedia.")

    if re.search('google', res):
        match = re.search('google (.+)', res)
        if match:
            query = match.group(1)
            response = search_google(query)
            obj.text2speech(response)
        else:
            obj.text2speech("Lo siento, no pude entender la consulta que estás buscando en Google.")

    if re.search('entrepreneurship|startups', res):
        match = re.search('(?:tell me about|search for) (.+)', res)
        if match:
            query = match.group(1)
            response = handle_entrepreneurship_questions(query)
            obj.text2speech(response)
        else:
            obj.text2speech("Lo siento, no pude entender la consulta relacionada con emprendedores y startups.")

    if re.search('exit|bye', res):
        obj.text2speech(f"Adiós, {user_name}. ¡Que tengas un excelente día!")
        break
