<<<<<<< HEAD
# 🎚️ Procesamiento de Audio con Filtros Digitales

**Interfaces de Hardware y Software — Proyecto de Interfaz HMI en Streamlit**

---

## 📄 Descripción

Este proyecto implementa un sistema de **procesamiento de señales de audio** mediante filtros digitales (pasa bajas, pasa altas y pasa banda).
La interfaz gráfica fue desarrollada con **Streamlit** y permite:

- Cargar archivos de audio `.wav`, `.mp3`, `.aac`
- Aplicar filtros digitales configurables
- Visualizar el audio en el **dominio del tiempo** y en el **dominio de la frecuencia (FFT)**
- Exportar el resultado en diferentes formatos

---

## ⚙️ Requisitos

- Python 3.10 instalado

### Instalación de dependencias:

```bash
pip install streamlit numpy matplotlib scipy soundfile pydub
```

---

## 🧠 Estructura del Código

Archivo principal: `app.py`

| Función | Descripción |
|--------|-------------|
| `leer_audio_general(file)` | Carga audio `.wav`, `.mp3`, `.aac` y lo convierte a array numpy mono |
| `aplicar_filtro(data, fs, tipo, fc_low, fc_high, orden)` | Aplica filtro digital Butterworth según parámetros |
| `aplicar_fft(data, fs)` | Calcula la FFT para visualización del espectro |
| `st.line_chart()` | Muestra forma de onda |
| `st.pyplot()` | Muestra el espectro de frecuencias |
| `sf.write()` | Guarda audio filtrado |
| `AudioSegment.export()` | Exporta en formato `.mp3`, `.aac` o `.wav` |

---

## 🧪 Instrucciones de Uso

### Paso 1️⃣: Cargar audio

- Selecciona un archivo de audio en formato `.wav`, `.mp3`, o `.aac`.
- Se mostrará la forma de onda del audio cargado.

![Paso 1 - Cargar audio](assets/Screenshot_cargar_audio.png)

---

### Paso 2️⃣: Aplicar filtro

- Elige un tipo de filtro:
  - `Pasa-bajas`
  - `Pasa-altas`
  - `Pasa-banda`
- Ajusta:
  - Orden del filtro
  - Frecuencia(s) de corte
- Presiona **Aplicar filtro** para procesar el audio.

![Paso 2 - Aplicar filtro](assets/Screenshot_aplicar_filtro.png)

---

### 🔉 Visualización de Audio Filtrado

- Se reproducen el audio original y el filtrado.
- Se visualizan ambas formas de onda para comparar.

![Audio Filtrado - Formas de onda](assets/Screenshot_audio_filtrado.png)

---

### Paso 3️⃣: Transformada de Fourier (FFT)

- Presiona el botón **Aplicar FFT**.
- Se comparan los espectros de frecuencia (FFT) del audio original y filtrado.

![Paso 3 - FFT](assets/Screenshot_fft.png)

---

### 💾 Guardar Resultado

- Selecciona el formato de exportación (`.wav`, `.mp3`, `.aac`).
- Presiona el botón **Guardar Resultado**.
- Finalmente, haz clic en **⬇️ Descargar archivo**.

![Guardar Resultado](assets/Screenshot_guardar_resultado.png)

---

## 🚀 Ejecutar la Aplicación

Para correr la aplicación:

```bash
streamlit run app.py
```

Esto abrirá una pestaña en tu navegador con la interfaz de usuario lista para usarse.

---

## 👩‍💻 Autor

**Ana Valeria Pérez Pérez**
*Proyecto académico — Interfaces de Hardware y Software*

---
=======
# 🎚️ Procesamiento de Audio con Filtros Digitales

**Interfaces de Hardware y Software — Proyecto de Interfaz HMI en Streamlit**

---

## 📄 Descripción

Este proyecto implementa un sistema de **procesamiento de señales de audio** mediante filtros digitales (pasa bajas, pasa altas y pasa banda).
La interfaz gráfica fue desarrollada con **Streamlit** y permite:

- Cargar archivos de audio `.wav`, `.mp3`, `.aac`
- Aplicar filtros digitales configurables
- Visualizar el audio en el **dominio del tiempo** y en el **dominio de la frecuencia (FFT)**
- Exportar el resultado en diferentes formatos

---

## ⚙️ Requisitos

- Python 3.10 instalado

### Instalación de dependencias:

```bash
pip install streamlit numpy matplotlib scipy soundfile pydub
```

---

## 🧠 Estructura del Código

Archivo principal: `app.py`

| Función | Descripción |
|--------|-------------|
| `leer_audio_general(file)` | Carga audio `.wav`, `.mp3`, `.aac` y lo convierte a array numpy mono |
| `aplicar_filtro(data, fs, tipo, fc_low, fc_high, orden)` | Aplica filtro digital Butterworth según parámetros |
| `aplicar_fft(data, fs)` | Calcula la FFT para visualización del espectro |
| `st.line_chart()` | Muestra forma de onda |
| `st.pyplot()` | Muestra el espectro de frecuencias |
| `sf.write()` | Guarda audio filtrado |
| `AudioSegment.export()` | Exporta en formato `.mp3`, `.aac` o `.wav` |

---

## 🧪 Instrucciones de Uso

### Paso 1️⃣: Cargar audio

- Selecciona un archivo de audio en formato `.wav`, `.mp3`, o `.aac`.
- Se mostrará la forma de onda del audio cargado.

![Paso 1 - Cargar audio](assets/Screenshot_cargar_audio.png)

---

### Paso 2️⃣: Aplicar filtro

- Elige un tipo de filtro:
  - `Pasa-bajas`
  - `Pasa-altas`
  - `Pasa-banda`
- Ajusta:
  - Orden del filtro
  - Frecuencia(s) de corte
- Presiona **Aplicar filtro** para procesar el audio.

![Paso 2 - Aplicar filtro](assets/Screenshot_aplicar_filtro.png)

---

### 🔉 Visualización de Audio Filtrado

- Se reproducen el audio original y el filtrado.
- Se visualizan ambas formas de onda para comparar.

![Audio Filtrado - Formas de onda](assets/Screenshot_audio_filtrado.png)

---

### Paso 3️⃣: Transformada de Fourier (FFT)

- Presiona el botón **Aplicar FFT**.
- Se comparan los espectros de frecuencia (FFT) del audio original y filtrado.

![Paso 3 - FFT](assets/Screenshot_fft.png)

---

### 💾 Guardar Resultado

- Selecciona el formato de exportación (`.wav`, `.mp3`, `.aac`).
- Presiona el botón **Guardar Resultado**.
- Finalmente, haz clic en **⬇️ Descargar archivo**.

![Guardar Resultado](assets/Screenshot_guardar_resultado.png)

---

## 🚀 Ejecutar la Aplicación

Para correr la aplicación:

```bash
streamlit run app.py
```

Esto abrirá una pestaña en tu navegador con la interfaz de usuario lista para usarse.

---

## 👩‍💻 Autor

**Ana Valeria Pérez Pérez**
*Proyecto académico — Interfaces de Hardware y Software*

---
>>>>>>> c6404e3ca0673e74ee88904a23c022c8edec4327
