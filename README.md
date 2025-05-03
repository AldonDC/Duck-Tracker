# Duck-Tracker 🦆

Sistema avanzado de seguimiento de patos en tiempo real utilizando YOLOv8 y Filtros de Kalman.

## Características Principales 🌟

- Detección precisa de patos usando YOLOv8
- Seguimiento en tiempo real con IDs consistentes
- Diferenciación entre patos amarillos y negros
- Sistema de tracking avanzado con Filtros de Kalman
- Visualización en tiempo real con cuadrícula
- Generación de videos procesados con visualización dual
- Almacenamiento de datos de tracking en formato JSON
- Visualización de trayectorias y predicciones
- Manejo de oclusiones y patos perdidos
- Límite configurable de patos a detectar (por defecto 7)

## Requisitos 📋

```bash
numpy
opencv-python
matplotlib
ultralytics
scipy
tqdm
```

## Instalación 🔧

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/Duck-Tracker.git
cd Duck-Tracker
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Asegúrate de tener el modelo YOLOv8 entrenado en la ruta correcta:

```
/path/to/DuckTracking.v1i.yolov8/yolo_training_results/chick_detector2/weights/best.pt
```

## Uso 🚀

### Ejecución Básica

```python
from duck_tracker_advanced import DuckTrackerAdvanced

tracker = DuckTrackerAdvanced(
    model_path="path/to/model.pt",
    min_confidence=0.3,
    max_ducks=7
)

# Procesar un video
tracker.process_video(
    video_path="path/to/video.mp4",
    output_dir="output",
    save_frames=True,
    display=True
)
```

### Parámetros Configurables

- `min_confidence`: Confianza mínima para detecciones (default: 0.3)
- `min_distance`: Distancia mínima entre detecciones (default: 20)
- `max_frames`: Máximo número de frames a procesar (default: 400)
- `max_ducks`: Número máximo de patos a trackear (default: 7)
- `max_tracking_history`: Frames en historial de tracking (default: 30)
- `max_distance_threshold`: Distancia máxima para asociación (default: 50)
- `track_timeout`: Frames antes de considerar un track perdido (default: 10)
- `reid_threshold`: Umbral para re-identificación (default: 0.7)

## Estructura de Salida 📁

```
output_video/
├── output_video.mp4          # Video procesado con vista dual
├── tracking_data.json        # Datos de tracking en formato JSON
└── trayectorias_patos.png    # Visualización de trayectorias
```

## Características del Sistema de Tracking 🎯

- **Filtro de Kalman**: Predicción de movimiento y manejo de oclusiones
- **Re-identificación**: Sistema para mantener IDs consistentes
- **Manejo de Pérdidas**: Sistema para recuperar patos perdidos
- **Visualización Dual**:
  - Vista original con bounding boxes
  - Vista 2D con trayectorias y predicciones

## Limitaciones Conocidas ⚠️

- Rendimiento óptimo hasta 7 patos simultáneos
- Mejor funcionamiento con buena iluminación
- Puede haber confusión en casos de oclusión prolongada

## Contribuciones 🤝

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de crear un pull request.

## Licencia 📄

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
