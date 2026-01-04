# Simulación de Difracción de Luz

Simulación de difracción de Fraunhofer para imágenes RGB utilizando la aproximación del espectro angular.

## Descripción

Este script simula la propagación y difracción de luz a través de una apertura (imagen) en el espacio libre. Utiliza el método del espectro angular para calcular el patrón de difracción a una distancia especificada.

## Características

- Propagación independiente para cada canal de color (Rojo, Verde, Azul)
- Longitudes de onda: 650nm (R), 532nm (G), 450nm (B)
- Visualización lado a lado de la apertura original y el patrón de difracción
- Normalización de intensidad para cada canal

## Requisitos

```bash
pip install numpy matplotlib pillow
```

## Uso

1. Coloca una imagen llamada `imagen.png` en el mismo directorio que el script
2. Ejecuta el script:

```bash
python phys.py
```

## Parámetros Ajustables

- `wavelengths`: Longitudes de onda para cada canal RGB (metros)
- `dx`: Tamaño del píxel en la apertura (10 μm por defecto)
- `z`: Distancia de propagación (1 cm por defecto)

## Física

El script implementa la aproximación del espectro angular usando la función de transferencia:

$$H(f_x, f_y) = e^{-i\pi\lambda z(f_x^2 + f_y^2)}$$

donde $\lambda$ es la longitud de onda, $z$ es la distancia de propagación, y $f_x$, $f_y$ son las frecuencias espaciales.

## Autor

Victor
