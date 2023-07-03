
# S.A.R.A. - Asistente Virtual Empresarial

S.A.R.A. (Sistema de Asesoramiento y Resolución de Consultas Empresariales) es un asistente virtual basado en inteligencia artificial creado por CDX INNOVA. Proporciona asesoramiento y respuestas a consultas relacionadas con negocios y emprendimiento.

**¡Importante! S.A.R.A. se encuentra en etapa BETA y está en proceso de aprendizaje local.**

## Características principales
- Capacidad de reconocimiento de voz para transformar la entrada de audio en texto.
- Interacción con el modelo de lenguaje GPT-3.5 para proporcionar respuestas a consultas empresariales.
- Integración con una base de datos MySQL para almacenar preguntas y respuestas.

## Requisitos previos
- Python 3.7 o superior
- Paquetes Python: speech_recognition, openai, gtts, pygame, pyttsx3, mysql-connector-python

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/sara-asistente-virtual.git
   ```

2. Instala los paquetes Python necesarios:

   ```bash
   pip install -r requirements.txt
   ```

3. Configura la conexión a la base de datos MySQL:

   - Asegúrate de tener XAMPP o un servidor MySQL instalado y en funcionamiento.
   - Crea una base de datos llamada `bitacora`.
   - Ejecuta el script SQL proporcionado en `database.sql` para crear la tabla `consultoria`.
   - Actualiza las credenciales y la configuración de conexión en el archivo `database.py`.

## Uso

1. Ejecuta el archivo principal `main.py`:

   ```bash
   python main.py
   ```

2. Sigue las instrucciones de S.A.R.A. para realizar consultas empresariales.
3. Habla claramente tu pregunta y espera la respuesta.

## Contribuciones

Actualmente, no se aceptan contribuciones externas para el proyecto. Sin embargo, puedes utilizar este código como referencia o inspiración para tus propios proyectos.

## Aviso de licencia

CDX INNOVA mantiene todos los derechos de autor y propiedad intelectual de este proyecto. No se otorga ninguna licencia para editar o distribuir independientemente este código sin el permiso explícito de CDX INNOVA.

---

¡Gracias por utilizar S.A.R.A.! Esperamos que encuentres útil este asistente virtual en tu experiencia empresarial. Si tienes alguna pregunta o consulta, no dudes en contactarnos.

© 2023 CDX INNOVA. Todos los derechos reservados.
```