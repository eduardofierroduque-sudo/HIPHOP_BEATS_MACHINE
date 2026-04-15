HIPHOP BEATS MACHINE V.3: MODULAR SYSTEM
Por Eduardo Fierro Duque

<img width="895" height="927" alt="image" src="https://github.com/user-attachments/assets/9ed89c07-142c-4fbe-a4e9-d94a18e47c77" />
<img width="897" height="940" alt="image" src="https://github.com/user-attachments/assets/6506eb1b-ce72-45a5-8e58-dce88f1b148f" />



Este proyecto es una estación de trabajo diseñada para automatizar la creación de ritmos urbanos utilizando inteligencia artificial. Lo que empezó como una herramienta de terminal ha evolucionado en esta versión 3 a un sistema modular completo con interfaz gráfica, permitiendo que cualquier productor o entusiasta pueda generar pistas de alta calidad sin necesidad de escribir una sola línea de código.

¿Qué hace especial a esta herramienta?
La producción musical suele ser un proceso largo. Esta máquina permite saltarse el bloqueo creativo generando una base sólida de hasta 60 segundos en cuestión de minutos. La gran diferencia de esta versión es su Arquitectura Modular: puedes elegir específicamente el género, el tipo de bajos (808s), el patrón de los hi-hats y hasta la atmósfera o el contexto del beat.

<img width="2559" height="1032" alt="image" src="https://github.com/user-attachments/assets/51e2d3cd-b063-49c6-8d89-e5177175a546" />
<img width="2551" height="1033" alt="image" src="https://github.com/user-attachments/assets/d3096cf7-71b1-4518-9487-6a447b6e689f" />


El reto técnico: Correr IA pesada en Windows
Uno de los mayores logros de este desarrollo fue superar las barreras de compatibilidad. Normalmente, los modelos de Meta (MusicGen) requieren librerías muy complejas de instalar en Windows. Para solucionar esto, desarrollé un "Cerebro Sintético" dentro del código que emula estas funciones avanzadas, permitiendo que el programa sea ligero y funcional en computadoras convencionales sin necesidad de configuraciones de servidor.

Cómo funciona el flujo de trabajo
He diseñado el sistema para que funcione como un asistente de estudio profesional:

Selección Modular: Eliges entre 12 categorías diferentes para definir el ADN de tu beat.
<img width="2504" height="531" alt="image" src="https://github.com/user-attachments/assets/7861e0e9-2af5-4b9b-bf95-fca0e01522ef" />
<img width="2551" height="587" alt="image" src="https://github.com/user-attachments/assets/902ce217-efdf-4ff0-a53b-5de4b3717060" />
<img width="2536" height="652" alt="image" src="https://github.com/user-attachments/assets/8659cfeb-7506-4dd1-8ec8-f3c4580fe401" />
<img width="2505" height="576" alt="image" src="https://github.com/user-attachments/assets/850533e5-d8d2-43e1-8de9-3c333c712b83" />
<img width="2528" height="574" alt="image" src="https://github.com/user-attachments/assets/17a08feb-a13c-4f4a-b68e-5b046ce3d3b0" />
<img width="2533" height="597" alt="image" src="https://github.com/user-attachments/assets/194b49f0-65b4-4629-91f1-41eb95d3042a" />
<img width="2548" height="602" alt="image" src="https://github.com/user-attachments/assets/f609dff9-a2eb-4dad-ac74-25e60e1daae0" />
<img width="2520" height="584" alt="image" src="https://github.com/user-attachments/assets/53f218f1-04a6-43a3-aa25-3a8c89576486" />
<img width="2497" height="582" alt="image" src="https://github.com/user-attachments/assets/432b6dc5-a72c-4b86-be28-a4e27b78f662" />
<img width="2537" height="656" alt="image" src="https://github.com/user-attachments/assets/d987039f-008e-402a-853e-fac9ea9acb0f" />
<img width="2528" height="768" alt="image" src="https://github.com/user-attachments/assets/03a2da52-e188-4d31-b351-5445d9ef0c7c" />
<img width="2532" height="583" alt="image" src="https://github.com/user-attachments/assets/5720fa0b-2218-4ed9-8b9b-765ebb1cc16d" />


Sistema de Cola: Puedes configurar varios beats seguidos y dejar que la máquina trabaje en lote mientras haces otras cosas.



Procesamiento Inteligente: El motor MusicGen crea el audio, y gracias al parche de optimización, el consumo de memoria se mantiene bajo control.

Separación de Pistas (Stems): Una vez generado el beat, el sistema puede desglosarlo en pistas independientes (Batería, Bajo, Melodía y Otros). Esto es vital para que después puedas llevar cada archivo a tu programa de edición (como FL Studio o Ableton) y mezclarlos a tu gusto.

Guía de instalación rápida
Para que todo funcione a la primera en Windows, sigue estos pasos en tu terminal:

1. Preparar el entorno:

Bash
git clone https://github.com/eduardofierroduque-sudo/HIPHOP_BEATS_MACHINE.git
cd HIPHOP_BEATS_MACHINE
python -m venv venv
.\venv\Scripts\activate
2. Instalar las librerías necesarias:
He simplificado este paso para evitar los errores comunes de compilación en Windows:

Bash
pip install --upgrade pip setuptools wheel
pip install av --only-binary=:all:
pip install spacy
python -m spacy download en_core_web_sm
pip install -r requirements.txt
3. Iniciar la máquina:

Bash
python main.py
Notas del desarrollador
Primer uso: La primera vez que generes un audio, el programa descargará el modelo de inteligencia artificial de internet. Esto puede tardar unos minutos dependiendo de tu conexión, pero solo sucede una vez.

Hardware: Si notas que tu computadora se esfuerza mucho, puedes cambiar el modelo en el código de "large" a "small" para una mayor velocidad.

Este proyecto fue desarrollado bajo una metodología de ingeniería asistida por IA, utilizando a Gemini para optimizar la lógica y resolver problemas de compatibilidad de sistemas.

© 2026 Eduardo Fierro Duque | Beats Machine V.3 – Tecnología al servicio del ritmo.

Ejemplos de pistas generadas en Beats Machine v.3:
[beat_modular_boombap_1.wav](https://github.com/user-attachments/files/26749920/beat_modular_boombap_1.wav)
[beat_modular_boombap_2.wav](https://github.com/user-attachments/files/26749923/beat_modular_boombap_2.wav)
[beat_modular_boombap_3.wav](https://github.com/user-attachments/files/26749928/beat_modular_boombap_3.wav)
[beat_modular_boombap_4.wav](https://github.com/user-attachments/files/26749931/beat_modular_boombap_4.wav)




