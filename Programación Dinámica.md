Programación Dinámica - Actividad 9
## Descripción
Este proyecto resuelve los 2 problemas solicitados en la actividad usando **Programación Dinámica**:
1. Escaleras  
   Calcular cuántas formas distintas existen para llegar al escalón `N` si solo se puede subir 1 o 2 escalones por movimiento.
2. Cambio mínimo de monedas
   Dado un conjunto de monedas y una cantidad objetivo, calcular:
   - la cantidad mínima de monedas,
   - una combinación válida de monedas,
   - y la tabla DP generada.
Requisitos
- Windows + Python Launcher (`py`) o Python 3.8+.
> En este equipo se recomienda ejecutar con `py`.
 Ejecución
Desde la carpeta del proyecto:
```bash
py main.py
```
Menú del programa
Al ejecutar se muestra:

1) Resolver Escaleras  
2) Resolver Cambio mínimo de monedas  
3) Ejecutar ejemplos guía del PDF  
0) Salir
 Ejemplos esperados (según PDF)
Escaleras
- `N = 5`  
  Formas posibles: `8`  
  Tabla DP: `[1, 1, 2, 3, 5, 8]`

- `N = 7`  
  Formas posibles: `21`  
  Tabla DP: `[1, 1, 2, 3, 5, 8, 13, 21]`
 Cambio de monedas
- Monedas: `[1,3,4]`, Cantidad: `6`  
  Cantidad mínima: `2`  
  Combinación válida: `3 + 3`  
  Tabla DP: `[0,1,2,1,1,2,2]`

- Monedas: `[1,2,5]`, Cantidad: `11`  
  Cantidad mínima: `3`  
  Combinación válida: `5 + 5 + 1`  
  Tabla DP: `[0,1,1,2,2,1,2,2,3,3,2,3]`
Archivos del proyecto
- `main.py` → implementación en Python.
- `README.md` → guía de uso.
