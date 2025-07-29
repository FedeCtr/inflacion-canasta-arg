# Análisis de Inflación y Canasta Básica en Argentina

Este proyecto realiza un análisis visual y estadístico de la evolución de la Canasta Básica Alimentaria (CBA), la Canasta Básica Total (CBT) y el Salario Mínimo Vital y Móvil (SMVM) en Argentina, utilizando datos oficiales del INDEC.

---

## Objetivos

- Visualizar el impacto de la inflación en el costo de vida y poder adquisitivo.
- Comparar la evolución de las canastas básicas con el salario mínimo.
- Identificar sectores económicos con mayor inflación mensual.
- Practicar herramientas de análisis y visualización de datos en Python.

---

## Tecnologías y librerías usadas

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook (VS Code)

---

## Contenido del repositorio

- /data/ : Archivos CSV con los datasets usados (Canasta Básica, Salario Mínimo, IPC)
- /notebooks/ : Notebook analisis_inflacion_canasta.ipynb con el análisis completo y gráficos
- .gitignore : Configuración para ignorar archivos no necesarios

---

## Resultados principales

El notebook incluye:

- Gráficos de línea que muestran la evolución de CBA, CBT y SMVM desde 2016 hasta 2025.
- Visualizaciones que demuestran la pérdida del poder adquisitivo del salario mínimo.
- Mapas de calor y gráficos de barras apiladas para analizar la inflación por sectores económicos.
- Un gráfico interactivo con Plotly para explorar los datos dinámicamente.
- Conclusiones y análisis escritos para explicar los resultados.

---

## Cómo usar el proyecto

1. Clonar el repositorio:
git clone https://github.com/FedeCtr/inflacion-canasta-arg.git

2. Crear y activar el entorno virtual (opcional pero recomendado):
python -m venv env

Windows
env\Scripts\activate

Linux / Mac
source env/bin/activate

3. Instalar dependencias:
pip install -r requirements.txt

4. Abrir el notebook y ejecutar las celdas:
code notebooks/analisis_inflacion_canasta.ipynb

---

## Fuentes de datos

- INDEC - Canasta Básica (https://www.indec.gob.ar)
- Datos propios descargados y preparados para análisis

---

## Contacto

- GitHub: https://github.com/FedeCtr

---

Gracias por visitar este proyecto.  
Este análisis es parte de mi formación en programación y análisis de datos.

