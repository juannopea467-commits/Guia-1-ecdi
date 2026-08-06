# Guía de trabajo 1: Campo de pendientes

## Ejercicio 1
Ecuación: y' = -y - sin(x), condición inicial y(0)=1  
- Comando en GeoGebra: `CampoDirecciones(-y - sin(x))`  
- Solución particular: `ResuelveEDO(-y - sin(x),(0,1))`

## Ejercicio 2
Ecuación: y' = y(3-y)(y-2)  
- Puntos críticos: y=0, y=2, y=3  
- Comandos en WolframAlpha:  
  - `Roots[y*(3-y)*(y-2)=0,y]`  
  - `Reduce[y*(3-y)*(y-2)>0,y]`  
  - `Reduce[y*(3-y)*(y-2)<0,y]`

## Ejercicio 3
Modelo de población: dP/dt = P(P-1)(2-P)  
- Puntos críticos: P=0, P=1, P=2  
- Interpretación:  
  - Si P(0)=3 → decrece hacia 2000 ejemplares.  
  - Si P(0)=1.5 → crece hacia 2000 ejemplares.  
  - Si P(0)=0.5 → tiende a desaparecer.
