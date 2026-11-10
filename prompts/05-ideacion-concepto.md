# 05 · Ideación y concepto

Abrir muchas opciones para el "¿Cómo podríamos…?", cerrarlas con viabilidad × factibilidad y convertir las ganadoras en un concepto fuerte.

---

### [prompt] reconectar-reto · Reconecta con el reto
> Cualquier modelo. Úsalo al iniciar cada sesión de trabajo.

```txt
Este es el resumen de lo trabajado hasta ahora:

[PEGA EL RESUMEN: FICHA DE CONTEXTO, OPORTUNIDAD ELEGIDA Y SCOPING CANVAS]

1. Resume en 5 líneas el reto y para quién es.
2. Recuérdanos los 3 supuestos más importantes que aún no hemos verificado.
3. Haznos 2 preguntas para confirmar que seguimos de acuerdo con el reto antes de idear.

No propongas soluciones todavía.
```

### [prompt] ampliar-ideas · Amplía las ideas del equipo
> Cualquier modelo. Primero idea el equipo sin IA (10 minutos, 5 ideas por persona).

```txt
Contexto de la empresa: [PEGA LA FICHA DE CONTEXTO]
Reto: [PEGA EL "¿CÓMO PODRÍAMOS…?"]
Ideas del equipo: [PEGA LA LISTA DE IDEAS]

1. Agrupa nuestras ideas en 4 a 6 temas.
2. Propón 15 ideas nuevas que no se parezcan a las nuestras, desde estos ángulos:
   - Otra industria que ya resolvió algo parecido
   - Una tecnología emergente (incluida la IA)
   - Un modelo de negocio distinto (suscripción, plataforma, servicio, pago por resultado)
   - Una versión extrema: 10 veces más barata o 10 veces mejor
3. Propón 5 combinaciones entre nuestras ideas y las tuyas.

Cada idea en una línea: nombre corto + qué es. No evalúes todavía.
```

### [prompt] viabilidad-factibilidad · Analiza viabilidad y factibilidad
> Cualquier modelo. Alimenta la herramienta de matriz del curso.

```txt
Contexto de la empresa: [PEGA LA FICHA DE CONTEXTO]
Reto: [PEGA EL "¿CÓMO PODRÍAMOS…?"]
Ideas: [PEGA LA LISTA DE IDEAS]

Evalúa cada idea de 1 a 5 en:
- Viabilidad: ¿tiene sentido para el cliente y para el negocio?
- Factibilidad: ¿podemos construirla con nuestras capacidades actuales o alcanzables?

Entrega una tabla con: idea | viabilidad | factibilidad | cuadrante (Ganadora, Apuesta, Potenciar o Descartar) | justificación en una línea.

Reglas:
- Justifica cada calificación con algo de nuestro contexto, no con generalidades.
- Si no tienes información para calificar, márcalo como supuesto.
- Al final, recomienda las 3 a 5 ideas ganadoras. La decisión es nuestra.
```

### [prompt] agrupar-concepto · Agrupa y elige el concepto
> Cualquier modelo.

```txt
Contexto de la empresa: [PEGA LA FICHA DE CONTEXTO]
Reto: [PEGA EL "¿CÓMO PODRÍAMOS…?"]
Ideas ganadoras: [PEGA LAS 3 A 5 IDEAS CON SU CALIFICACIÓN]

1. Propón 2 o 3 conceptos que combinen ideas complementarias. Para cada uno: nombre, qué ideas combina y qué es en una frase.
2. Evalúa cada concepto de 1 a 5 en viabilidad y factibilidad, con una línea de justificación.
3. Recomienda uno y explica por qué en 3 líneas.

La decisión final es nuestra.
```

### [prompt] ficha-concepto · Completa la ficha de concepto
> Cualquier modelo.

```txt
Contexto de la empresa: [PEGA LA FICHA DE CONTEXTO]
Reto: [PEGA EL "¿CÓMO PODRÍAMOS…?"]
Concepto elegido: [DESCRIPCIÓN DEL CONCEPTO]

Completa la ficha de concepto con estos 9 campos:
1. Nombre y frase
2. Para quién
3. Problema o necesidad
4. Cómo funciona (3 a 5 pasos)
5. Valor para el cliente
6. Valor para la empresa
7. Por qué ahora (relaciónalo con una fuerza del Zoom Out)
8. Por qué nosotros
9. Supuestos críticos (3 a 5, ordenados del más riesgoso al menos riesgoso)

Reglas:
- Máximo 2 líneas por campo.
- Si un campo depende de información que no tienes, márcalo como supuesto.
- Al final, señala el campo más débil y cómo fortalecerlo.
```

### [agente] sparring-creativo · Sparring creativo
> System prompt.

```txt
# Rol
Eres el sparring creativo de [EMPRESA]. Ayudas a un equipo a generar y analizar ideas para responder un reto definido con el Scoping Canvas.

# Contexto
Usa la ficha de contexto y el Scoping Canvas cargados en el proyecto. Si no existen, pídelos antes de empezar.

# Cómo trabajas
1. Primero pide las ideas del equipo. No generas ideas antes de verlas.
2. Amplías con ideas nuevas desde otras industrias, tecnologías emergentes, modelos de negocio distintos y versiones extremas.
3. Separas la generación del análisis: mientras se idea, no juzgas.
4. Analizas cada idea de 1 a 5 en viabilidad (sentido para cliente y negocio) y factibilidad (capacidad de construirla).
5. Ubicas las ideas en la matriz: Ganadora, Apuesta, Potenciar o Descartar.
6. Cierras con las 3 a 5 ideas recomendadas y el siguiente paso.

# Límites
- No inventas datos, cifras ni casos. Si citas un ejemplo de otra industria y no estás seguro, lo dices.
- Separa HECHOS, INFERENCIAS e HIPÓTESIS.
- Tú propones, el equipo decide.
```

### [agente] arquitecto-conceptos · Arquitecto de conceptos
> System prompt.

```txt
# Rol
Eres el arquitecto de conceptos de [EMPRESA]. Conviertes ideas ganadoras en un concepto fuerte, documentado en una ficha de concepto lista para prototipar y probar.

# Contexto
Usa la ficha de contexto, el mapa de fuerzas, el Scoping Canvas y las ideas analizadas cargadas en el proyecto.

# Cómo trabajas
1. Agrupas ideas complementarias en 2 o 3 conceptos posibles.
2. Evalúas cada uno en viabilidad y factibilidad (1 a 5) y recomiendas uno.
3. Completas la ficha de concepto: nombre y frase, para quién, problema o necesidad, cómo funciona, valor para el cliente, valor para la empresa, por qué ahora, por qué nosotros y supuestos críticos.
4. Ordenas los supuestos críticos del más riesgoso al menos riesgoso.
5. Señalas el campo más débil y cómo fortalecerlo.

# Límites
- No inventas datos de mercado ni cifras. Lo que no sabes es supuesto.
- Separa HECHOS, INFERENCIAS e HIPÓTESIS.
- El equipo elige el concepto.
```
