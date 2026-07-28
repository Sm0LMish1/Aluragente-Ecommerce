# 🛍️ Asistente Virtual para Lumina Boutique (E-Commerce)

## Descripción del Proyecto
Asistente inteligente virtual de atención al cliente impulsado por Inteligencia Artificial. Este proyecto fue diseñado para **Lumina Boutique**, una pequeña tienda online de ropa y accesorios. 

El agente actúa como un representante de servicio al cliente disponible 24/7. Su mayor fortaleza es la confiabilidad: está programado bajo un estricto control para **no alucinar ni inventar información**. El asistente responde amablemente a las dudas de los usuarios basándose *únicamente* en las políticas y documentos oficiales de la tienda. Si no sabe la respuesta, deriva al cliente con el soporte humano.

---------------------------------------------------------------------------------------------
## Arquitectura del Sistema
El sistema utiliza un enfoque directo y eficiente conocido como **Prompt Stuffing** (Inyección de Contexto):
1. **Base de Datos:** Toda la documentación oficial de la tienda (políticas, envíos, FAQs) se centraliza y lee desde un archivo CSV.
2. **Orquestación:** Los datos estructurados se inyectan directamente en las instrucciones del sistema (`System Instructions`) del modelo de IA, confinando su comportamiento a las reglas del negocio.
3. **Interacción:** El usuario se comunica a través de una interfaz web. El agente procesa la pregunta, busca en su contexto inyectado y devuelve una respuesta precisa en tiempo real manteniendo la memoria de la conversación.

---------------------------------------------------------------------------------------------
## 🛠️ Tecnologías y Herramientas 🛠️
*   **Lenguaje:** Python 3.13+
*   **Inteligencia Artificial:** Modelo `gemini-3.1-flash-lite` mediante el SDK oficial de Google (`google-genai`).
*   **Procesamiento de Datos:** Pandas.
*   **Frontend (Interfaz Web):** Streamlit.
*   **Despliegue (Deploy):** Streamlit Community Cloud conectado a GitHub.

---------------------------------------------------------------------------------------------
## 📂 Estructura del Repositorio 📂
aluragente-ecommerce/
*  app.py                      # Lógica principal del agente y la interfaz visual.
*  documentacion_tienda.csv    # Base de conocimiento (Términos, devoluciones, envíos).
*  requirements.txt            # Lista de dependencias del proyecto.
*  README.md                   # Documentación principal.

---------------------------------------------------------------------------------------------
## 🚀 Instrucciones para Ejecución Local 🚀
Si deseas probar el código en tu propia computadora, sigue estos pasos:

1. Clona este repositorio:
  git clone [https://github.com/Sm0LMish1/Aluragente-Ecommerce.git](https://github.com/Sm0LMish1/Aluragente-Ecommerce.git)
  cd aluragente-ecommerce

3. Instala las dependencias necesarias:
   pip install -r requirements.txt

4. Configura tus credenciales:
Crea un archivo llamado .env en la raíz del proyecto y añade tu API Key de Google Gemini de la siguiente manera:
   AluraChallenge="TU_API_KEY_AQUI"

5. Ejecuta la aplicación:
   streamlit run app.py

---------------------------------------------------------------------------------------------
## 💡 Preguntas Frecuentes y Capacidades 💡
¿Qué PUEDE hacer este agente?
*Informar sobre los tiempos de entrega y empresas de despacho (ej. Starken, Chilexpress).
*Explicar detalladamente las políticas de cambios, devoluciones y garantías.
*Aclarar dudas sobre los métodos de pago aceptados.
*Mantener el contexto de la conversación (memoria) mientras el chat esté activo.

¿Qué NO PUEDE hacer el agente?
*Responder preguntas que estén fuera del alcance de la documentación oficial (en esos casos, pedirá al cliente contactar a soporte).
*Procesar pagos, realizar ventas o solicitar datos personales confidenciales.

---------------------------------------------------------------------------------------------
## Link directo al agente (Streamlit)
--> https://aluragente-ecommerce.streamlit.app/

---------------------------------------------------------------------------------------------
## 📸 Evidencias de Funcionamiento 📸
### -- Preguntas y respuestas del usuario

<img width="1917" height="1028" alt="image" src="https://github.com/user-attachments/assets/8dd9f440-16a4-4d0f-bb62-5fe353e0afa8" />

<img width="1917" height="1031" alt="image" src="https://github.com/user-attachments/assets/b5de033c-8333-4d97-b48f-22c5dec692be" />

### -- Respuesta que se recibe al consultar algo fuera de lo especificado

<img width="1917" height="1031" alt="image" src="https://github.com/user-attachments/assets/ff9e46e8-b5ec-4cba-8337-f747da4d6668" />










