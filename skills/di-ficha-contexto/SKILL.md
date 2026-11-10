---
name: di-ficha-contexto
description: Construye la ficha de contexto de una empresa y su lectura de modelo de negocio (crear, entregar y capturar valor) mediante una entrevista corta. Úsala antes de cualquier ejercicio de innovación con IA, cuando alguien diga "prepara el contexto de mi empresa", "ficha de contexto", "entiende mi negocio", o cuando las respuestas de la IA estén saliendo genéricas por falta de contexto.
---

# Ficha de contexto · Distilled Innovation

Sin contexto, la IA responde para "una empresa cualquiera". Esta skill produce el artefacto que se pega al inicio de todo el recorrido.

## Proceso

1. **Entrevista** con preguntas cortas, **de una en una**, máximo 8. Si la respuesta es vaga, pide un ejemplo concreto. Acepta "no sé" y márcalo "por validar".
2. Cubre estos campos:
   - Empresa (o descripción anonimizada) · Sector y subsector · Geografía
   - Clientes principales (segmentos B2B o B2C)
   - Propuesta de valor actual (qué vende y por qué la eligen)
   - 3 prioridades estratégicas
   - Retos o dolores actuales
   - Capacidades distintivas (tecnología, marca, red, conocimiento)
   - Restricciones (regulación, presupuesto, cultura, tecnología)
   - Recursos para innovar (personas, horas, presupuesto) — no asumas, pregunta
3. **Lectura de valor (Teece, 2010)** en tres frases:
   - **Crear valor:** segmentos y propuesta de valor.
   - **Entregar valor:** comunicación, canales de venta y distribución, atención y fidelización.
   - **Capturar valor:** fuentes de ingreso y formas de cobrar. No confundas ahorrar costos con generar ingresos.
4. **Anonimiza:** recuerda qué no se comparte con la IA y reemplaza nombres por roles o descripciones.
5. Pide al usuario **confirmar o corregir** antes de darla por cerrada.

## Formato de salida

```
FICHA DE CONTEXTO
Empresa:
Sector y subsector:
Geografía:
Clientes principales:
Propuesta de valor actual:
Prioridades estratégicas (3): 1) 2) 3)
Retos o dolores actuales:
Capacidades distintivas:
Restricciones:
Recursos para innovar:
No compartir con la IA:

CÓMO CREAMOS, ENTREGAMOS Y CAPTURAMOS VALOR
Crear:
Entregar:
Capturar:

Campos débiles / por validar:
```

Máximo 250 palabras en total.

## Reglas
- No pidas datos personales, confidenciales ni cifras sensibles.
- Separa hechos, hipótesis y datos por validar. No inventes cifras.
- No asignes responsables, tiempo ni presupuesto sin confirmación ("por acordar").
