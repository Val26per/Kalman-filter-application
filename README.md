# 🚗 Detección y Seguimiento de Vehículos con YOLOv8 + Deep SORT

Aplicación de **Streamlit** para la detección y seguimiento de vehículos en video usando **YOLOv8** y **Deep SORT**.  
Permite cargar un video, seleccionar la clase a rastrear, visualizar las detecciones en tiempo real y descargar el video procesado.

---

## 📋 Requisitos

- Python >= 3.8
- pip (actualizado)
- Git (opcional, si quieres clonar repositorio)

---

## ⚙️ Instalación

### 1. Crear y activar un entorno virtual

```bash
# Crear un entorno virtual
python3 -m venv venv

# Activar el entorno virtual
# En Linux/Mac
source venv/bin/activate

# En Windows
venv\Scripts\activate
```

---

### 2. Actualizar pip

```bash
pip install --upgrade pip
```

---

### 3. Instalar las dependencias

```bash
pip install streamlit opencv-python torch torchvision torchaudio ultralytics deep_sort_realtime
```

> **Nota:**  
> - `ultralytics` instala YOLOv8.  
> - `deep_sort_realtime` instala el rastreador DeepSORT.

---

## 📁 Organización esperada

Debes tener el modelo YOLOv8 entrenado (`best.pt`) en la ruta correcta, por ejemplo:

```bash
/home/usuario/mi_yolo_ikomia/proyecto_seguimiento_autos/modelo_100/best.pt
```

O bien modifica en el código esta línea para apuntar a tu propio modelo:

```python
model = YOLO('/ruta/a/tu/modelo/best.pt')
```

---

## 🚀 Ejecución del proyecto

### 1. Ejecutar la app de Streamlit

```bash
streamlit run app.py
```

(donde `app.py` es tu archivo con el código principal)

---

## 🧠 ¿Cómo funciona la aplicación?

1. Se carga el modelo YOLOv8 preentrenado para detección de vehículos.
2. Se inicializa un rastreador DeepSORT para hacer seguimiento de los objetos detectados.
3. El usuario sube un video en formato `.mp4`, `.avi`, `.mov` o `.mkv`.
4. Se puede seleccionar la clase que se desea rastrear: Car, Motorcycle, Truck, Bus, Bicycle.
5. Se procesan los frames uno por uno:
   - YOLOv8 detecta los vehículos.
   - DeepSORT asigna IDs únicos y da seguimiento.
6. Se muestra el video procesado en tiempo real en la app.
7. Al finalizar, se puede **descargar el video** procesado.

---

## 🔥 Ejemplo rápido de uso

1. Corre `streamlit run app.py`.
2. Abre el navegador (normalmente se abre automático en `http://localhost:8501`).
3. Sube un video.
4. Selecciona la clase que quieres seguir (por ejemplo: **Car**).
5. Espera a que termine el procesamiento.
6. Descarga tu video con detecciones e IDs rastreados.

---

## ⚠️ Notas importantes

- Si tienes GPU con CUDA, el modelo YOLOv8 se usará automáticamente en GPU.
- Puedes modificar el archivo para ajustar:
  - El umbral de confianza (`confidence threshold`).
  - Procesar todas las clases en vez de una sola.
- Si tu video es muy pesado, el procesamiento puede tardar varios minutos.

---

## 📚 Referencias

- [YOLOv8 - Ultralytics](https://docs.ultralytics.com/)
- [Deep SORT - Realtime Tracker](https://github.com/levan92/deep_sort_realtime)

---
