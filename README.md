# HIPHOP BEATS MACHINE

Desarrollado por Eduardo Fierro Duque.

Una aplicación en Python diseñada para automatizar la creación de instrumentales y ritmos urbanos utilizando Inteligencia Artificial. Este proyecto permite generar, modular y exportar pistas de audio en formato .wav, abarcando desde el clásico sonido underground y boom bap hasta variaciones como el trap y el future hip-hop.

## El Planteamiento

La idea principal nace de una pasión genuina por la producción musical y la necesidad de optimizar el proceso creativo. HipHop Beats Machine funciona como una herramienta de asistencia técnica y creativa para productores. En lugar de secuenciar cada elemento de percusión manualmente, el sistema interpreta parámetros de estilo, métrica y tempo para estructurar pistas completas directamente desde la terminal, entregando un punto de partida sólido para la composición y el sampling.

## Estudio de Separación Especializado en Hip Hop

Una de las características más potentes y diferenciadoras de esta herramienta es la integración de un módulo avanzado de separación de pistas, pensado específicamente para las necesidades de un productor urbano. Utilizando modelos de inteligencia artificial (Demucs), la máquina no solo genera el beat maestro, sino que realiza un proceso automático de "Stem Separation". 

Este estudio de separación interno analiza la pista generada y la desglosa en cuatro canales de audio fundamentales:
1. Drums (Aislamiento de bombos, cajas, hi-hats y percusiones)
2. Bass (Líneas de bajo y subgraves 808s)
3. Melody (Samples principales, sintetizadores y acompañamientos armónicos)
4. Other (Efectos, scratches y texturas adicionales)

Este método de trabajo entrega un control total sobre la mezcla final. Permite exportar cada elemento por separado a un DAW (Digital Audio Workstation) para procesarlos de manera individual, aplicar técnicas clásicas de "chopping", ecualizar el bombo y la caja con compresión paralela, o reestructurar el beat completo manteniendo la esencia del Hip Hop tradicional.

## Metodología y Flujo de Trabajo

Este proyecto fue construido bajo un enfoque de desarrollo avanzado asistido por Inteligencia Artificial. La conceptualización, la resolución de problemas lógicos y la estructuración del código en Python fueron co-creados utilizando a Gemini como copiloto de programación.

El flujo de trabajo se dividió en cuatro fases estratégicas para asegurar un producto final robusto y profesional:

1. Arquitectura y Lógica Base: Sesiones de diseño algorítmico para establecer un sistema escalable en Python, definiendo la lógica de generación y la exportación de archivos limpios a los directorios correspondientes.
2. Modularidad de Estilos: Separación estricta del entorno de ejecución principal (main.py) y el diccionario de parámetros musicales (styles.py). Esto asegura que se puedan agregar nuevos subgéneros o modificar el groove del boom bap sin alterar el núcleo lógico del programa.
3. Integración de Síntesis de Audio: Conexión de las directrices generadas en código con los modelos de generación sonora, traduciendo variables de tempo y textura en ondas de audio reales de alta fidelidad.
4. Procesamiento y Separación (Post-Producción): Implementación del modelo de separación para aislar las frecuencias del archivo exportado y generar las sub-pistas (Stems) de forma automática tras la creación del beat.

## Motores de IA Utilizados

Para lograr la autonomía del sistema y una calidad de estudio real, el proyecto integra Inteligencia Artificial en múltiples niveles operativos:

Lógica y Desarrollo (Gemini): Utilizado durante toda la fase de ingeniería de software para estructurar la sintaxis de Python, depurar errores de consola, optimizar flujos de datos y diseñar la arquitectura modular del repositorio.

Separación de Audio (Demucs): Implementado para el aislamiento preciso de pistas, separando el beat maestro en sus componentes rítmicos y melódicos esenciales.

Generación de Audio (Meta MusicGen): Encargado de la síntesis de los sonidos y la generación inicial de las ondas de audio basándose en las variables de estilo definidas en el código.

## Instalación y Entorno Local

Para replicar este proyecto y ejecutar la máquina de beats y su estudio de separación en un equipo local, es necesario contar con Python instalado y ejecutar los siguientes comandos en la terminal:

git clone https://github.com/eduardofierroduque-sudo/HIPHOP_BEATS_MACHINE.git
pip install -r requirements.txt
python main.py

------------------------------------------------------------------------------------------------------------------------------

# HIPHOP BEATS MACHINE

Developed by Eduardo Fierro Duque.

A Python application designed to automate the creation of instrumental and urban beats using Artificial Intelligence. This project allows you to generate, modulate, and export audio tracks in .wav format, covering everything from the classic underground and boom bap sound to variations like trap and future hip-hop.

## The Approach

The main idea stems from a genuine passion for music production and the need to optimize the creative process. HipHop Beats Machine works as a technical and creative assistance tool for producers. Instead of manually sequencing each percussion element, the system interprets style, metric, and tempo parameters to structure complete tracks directly from the terminal, delivering a solid starting point for composition and sampling.

## Hip Hop Specialized Separation Studio

One of the most powerful and distinctive features of this tool is the integration of an advanced track separation module, designed specifically for the needs of an urban producer. Using artificial intelligence models (Demucs), the machine not only generates the master beat but also performs an automatic "Stem Separation" process. 

This internal separation studio analyzes the generated track and breaks it down into four fundamental audio channels:
1. Drums (Isolation of kicks, snares, hi-hats, and percussions)
2. Bass (Basslines and 808 sub-bass)
3. Melody (Main samples, synthesizers, and harmonic accompaniments)
4. Other (Effects, scratches, and additional textures)

This workflow delivers total control over the final mix. It allows you to export each element separately to a DAW (Digital Audio Workstation) to process them individually, apply classic chopping techniques, equalize the kick and snare with parallel compression, or restructure the entire beat while maintaining the essence of traditional Hip Hop.

## Methodology and Workflow

This project was built under an advanced development approach assisted by Artificial Intelligence. The conceptualization, logical problem-solving, and Python code structuring were co-created using Gemini as a programming copilot.

The workflow was divided into four strategic phases to ensure a robust and professional final product:

1. Core Architecture and Logic: Algorithmic design sessions to establish a scalable system in Python, defining the generation logic and the export of clean files to the corresponding directories.
2. Style Modularity: Strict separation of the main execution environment (main.py) and the musical parameter dictionary (styles.py). This ensures that new subgenres can be added or the boom bap groove modified without altering the logical core of the program.
3. Audio Synthesis Integration: Connecting the code-generated guidelines with sound generation models, translating tempo and texture variables into real, high-fidelity audio waves.
4. Processing and Separation (Post-Production): Implementation of the separation model to isolate the frequencies of the exported file and generate the sub-tracks (Stems) automatically after the creation of the beat.

## AI Engines Used

To achieve system autonomy and real studio quality, the project integrates Artificial Intelligence at multiple operational levels:

Logic and Development (Gemini): Used throughout the software engineering phase to structure Python syntax, debug console errors, optimize data flows, and design the repository's modular architecture.

Audio Separation (Demucs): Implemented for precise track isolation, separating the master beat into its essential rhythmic and melodic components.

Audio Generation (Meta MusicGen): Responsible for the synthesis of sounds and the initial generation of audio waves based on the style variables defined in the code.

## Installation and Local Environment

To replicate this project and run the beats machine and its separation studio on a local computer, you must have Python installed and run the following commands in the terminal:

git clone https://github.com/eduardofierroduque-sudo/HIPHOP_BEATS_MACHINE.git
pip install -r requirements.txt
python main.py
