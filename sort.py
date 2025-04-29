"""
Aplicación de Streamlit para detección y seguimiento de vehículos usando YOLOv8 y Deep SORT.

Esta aplicación permite cargar un video, detectar vehículos y hacer seguimiento por clase
seleccionada, mostrando el ID de cada objeto rastreado y ofreciendo una descarga del video
procesado.
"""

import os
import tempfile

import cv2
import streamlit as st
import torch
from deep_sort_realtime.deepsort_tracker import DeepSort
from ultralytics import YOLO

# Configurar página
st.set_page_config(
    page_title="Detección y Seguimiento de Vehículos", layout="wide"
)
st.title("🚗 Detección y Seguimiento de Vehículos con YOLOv8 + Deep SORT")


@st.cache_resource
def load_model():
    """
    Carga el modelo YOLO entrenado y lo mueve al dispositivo disponible (GPU o CPU).

    Returns:
        YOLO: modelo cargado.
    """
    model = YOLO(
        "/home/anavale/mi_yolo_ikomia/proyecto_seguimiento_autos/modelo_100/best.pt"
    )
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    return model


@st.cache_resource
def load_tracker():
    """
    Inicializa el rastreador Deep SORT.

    Returns:
        DeepSort: instancia del rastreador.
    """
    return DeepSort(max_age=30)


model = load_model()
tracker = load_tracker()

CLASS_NAMES = ["Car", "Motorcycle", "Truck", "Bus", "Bicycle"]
CLASS_COLORS = {
    0: (0, 255, 0),
    1: (255, 0, 0),
    2: (0, 0, 255),
    3: (255, 255, 0),
    4: (255, 0, 255),
}

uploaded_file = st.file_uploader(
    "Carga tu video", type=["mp4", "avi", "mov", "mkv"]
)
output_format = st.selectbox(
    "Elige el formato de salida", ["mp4", "avi", "mov"]
)
selected_class = st.selectbox(
    "Selecciona la clase que quieres visualizar", CLASS_NAMES
)

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_path = tfile.name

    cap = cv2.VideoCapture(video_path)

    temp_out = tempfile.NamedTemporaryFile(
        delete=False, suffix=f".{output_format}"
    )
    output_path = temp_out.name

    if output_format == "mp4":
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    else:
        fourcc = cv2.VideoWriter_fourcc(*"XVID")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        cap.get(cv2.CAP_PROP_FPS),
        (
            int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        ),
    )

    frame_display = st.empty()
    progress_bar = st.progress(0)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_idx = 0

    st.info("⏳ Procesando el video...")

    class_counters = {cls_name: 0 for cls_name in CLASS_NAMES}
    track_id_per_class = {}

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)
        detections = []

        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()
            confidences = result.boxes.conf.cpu().numpy()
            classes = result.boxes.cls.cpu().numpy()

            for box, conf, cls in zip(boxes, confidences, classes):
                cls = int(cls)
                if cls < len(CLASS_NAMES) and conf > 0.5:
                    if CLASS_NAMES[cls] == selected_class:
                        x1, y1, x2, y2 = box
                        w, h = x2 - x1, y2 - y1
                        detections.append(([x1, y1, w, h], conf, cls))

        tracks = tracker.update_tracks(detections, frame=frame)

        for track in tracks:
            if not track.is_confirmed():
                continue

            ltrb = track.to_ltrb()
            x1, y1, x2, y2 = map(int, ltrb)
            cls = track.get_det_class()

            if CLASS_NAMES[cls] != selected_class:
                continue

            if track.track_id not in track_id_per_class:
                track_id_per_class[track.track_id] = class_counters[
                    CLASS_NAMES[cls]
                ]
                class_counters[CLASS_NAMES[cls]] += 1

            custom_id = track_id_per_class[track.track_id]
            color = CLASS_COLORS.get(cls, (0, 255, 0))
            label = f"ID {custom_id} {CLASS_NAMES[cls]}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                2,
            )

        out.write(frame)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_display.image(
            frame_rgb, channels="RGB", use_container_width=True
        )

        frame_idx += 1
        progress_bar.progress(min(frame_idx / frame_count, 1.0))

    cap.release()
    out.release()

    st.success("✅ Procesamiento terminado!")

    with open(output_path, "rb") as file:
        st.download_button(
            label=f"📥 Descargar video procesado ({output_format})",
            data=file,
            file_name=f"video_procesado.{output_format}",
            mime=f"video/{output_format}",
        )

    os.unlink(video_path)
    os.unlink(output_path)
