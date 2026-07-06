# Corrección de Perspectiva y Mejora de Documentos

**Trabajo Final Integrador 2026 — Técnicas de Procesamiento Digital de Imágenes**
Profesor: Juan Ignacio Bonini·

## Integrantes

**Valentín Imperio**

\---

## Problema

Cuando fotografiamos una hoja o documento con el celular en lugar de usar un escáner, el resultado suele tener **perspectiva inclinada**, **fondo no deseado** (mesa, sombra) y **contraste desparejo** por la iluminación ambiente. Esto dificulta leer, archivar o compartir el documento como si fuera un escaneo real.

Este proyecto resuelve ese problema: recibe una **foto de un documento** y devuelve una **versión "escaneada"**, recortada, enderezada y con contraste mejorado — el mismo problema que resuelven apps como CamScanner o Adobe Scan, pero implementado desde cero con técnicas clásicas de procesamiento digital de imágenes.

## Enfoque

Se optó por un **pipeline clásico de visión por computadora** (sin machine learning) porque el problema —encontrar una hoja rectangular sobre un fondo y corregir su perspectiva— tiene una geometría bien definida que puede resolverse con detección de bordes, contornos y transformaciones geométricas, sin necesitar un dataset de entrenamiento.

La solución se separó en **componentes de una sola responsabilidad** (carga, mejora, detección, transformación geométrica y guardado), coordinados por un orquestador (`DocumentScanner`). Esto permite that el mismo Core sea reutilizable desde una CLI, una futura interfaz gráfica, o una API, sin reescribir la lógica de procesamiento.

## Técnicas utilizadas

| Técnica                                        | Propósito                                                                                                                                   |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Redimensionado                                 | Acelerar la detección de bordes trabajando sobre una copia más chica (se guarda el `ratio` para escalar el resultado a la imagen original). |
| Escala de grises                               | Simplificar la imagen a un solo canal antes de detectar bordes.                                                                             |
| Desenfoque gaussiano                           | Reducir ruido de alta frecuencia que generaría bordes falsos.                                                                               |
| Detección de bordes de Canny                   | Encontrar los contornos del documento frente al fondo.                                                                                      |
| Cierre morfológico                             | Unir cortes pequeños en el borde detectado para que forme un contorno cerrado.                                                              |
| Búsqueda y aproximación poligonal de contornos | Quedarse con el contorno más grande que se aproxime a un polígono de 4 vértices (la hoja).                                                  |
| Transformación de perspectiva                  | Enderezar el documento como si se hubiera escaneado de frente.                                                                              |
| CLAHE                                          | Mejorar el contraste local sin quemar zonas claras ni oscuras.                                                                              |
| Filtro de nitidez                              | Realzar el texto/detalle del documento final.                                                                                               |

## Flujo

El procesamiento de cada imagen sigue el siguiente flujo:

Imagen original
│
▼
Redimensionado
│
▼
Escala de grises
│
▼
Filtro Gaussiano
│
▼
Detección de bordes (Canny)
│
▼
Operaciones morfológicas
(Dilatación + Erosión)
│
▼
Búsqueda de contornos
│
▼
Aproximación poligonal
(approxPolyDP)
│
▼
Corrección de perspectiva
(Warp Perspective)
│
▼
CLAHE
│
▼
Sharpen
│
▼
Documento escaneado

```



## Estructura del repositorio

```

TP-Final-Procesamiento-de-Imagenes/
├── core/  
│ ├── \_\_init\_\_.py
│ ├── loader.py  
│ ├── enhancer.py  
│ ├── detector.py  
│ ├── transformer.py  
│ ├── saver.py  
│ └── scanner.py  
├── images/
│ ├── input/  
│ └── output/  
├── main.py  
├── requirements.txt
└── README.md

````

## Uso / Ejecución verificable

1. Colocar las fotos a procesar dentro de `images/input/` (formatos aceptados: `.jpg`, `.jpeg`, `.png`, `.bmp`).
2. Ejecutar:

```bash
   python main.py
````

3. El programa recorre `images/input/`, procesa cada imagen con `DocumentScanner` y guarda el resultado en `images/output/` con el prefijo `scanned\_`.
4. La consola informa el estado de cada imagen (`Documento detectado correctamente`, o el error si no se pudo detectar un documento).

##

##

## Limitaciones

- El detector busca contornos con **exactamente 4 vértices** y área mínima (`> 5000 px`); si el documento está muy arrugado, doblado, o el fondo tiene un color/textura muy similar al papel, Canny puede no aislar un contorno limpio y el programa lanza `ValueError` ("No se encontró ningún documento en la imagen").
- Funciona mejor con **buena iluminación uniforme** y **contraste marcado entre el documento y el fondo**; sombras fuertes sobre uno de los bordes pueden romper la detección.
- No corrige documentos con **bordes curvos** (por ejemplo, una hoja no del todo plana), ya que la transformación de perspectiva asume 4 esquinas rectas.
