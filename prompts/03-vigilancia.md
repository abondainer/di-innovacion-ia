# 03 · Vigilancia estratégica con IA (Zoom Out + radar)

Mirar el negocio desde afuera con las cuatro fuerzas exógenas (mapa del entorno de Osterwalder), encontrar señales débiles y verificarlas.

---

### [prompt] escaneo-fuerza · Escaneo por fuerza
> Cualquier modelo, idealmente con búsqueda web activada.

```txt
[PEGA AQUÍ TU FICHA DE CONTEXTO]

Actúa como analista senior de vigilancia estratégica especializado en [SECTOR] en [GEOGRAFÍA].

Vamos a hacer un Zoom Out con el mapa de fuerzas del entorno de Osterwalder.
Fuerza asignada: [TENDENCIAS / FUERZAS DEL MERCADO / MACROECONÓMICAS Y GEOPOLÍTICAS / INDUSTRIALES · PORTER]

Identifica 5 hallazgos de esta fuerza que puedan afectar el modelo de negocio de la empresa en los próximos 1 a 5 años. Quiero hechos concretos y recientes, no generalidades. Incluye al menos 1 que venga de otro sector u otra geografía.

Para cada hallazgo entrega:
1. Nombre (máximo 6 palabras)
2. Subcategoría dentro de la fuerza
3. Qué está cambiando (un hecho observable)
4. Evidencia y fuente (si no tienes una fuente verificable, escribe "por verificar")
5. Por qué podría importar para la empresa
6. Relevancia para la empresa de 1 a 5, con una línea de justificación

Presenta todo en una tabla. Separa hechos de hipótesis y no inventes datos. No propongas soluciones.
```

### [prompt] senales-debiles · Señales débiles que casi nadie está mirando
> Cualquier modelo con búsqueda web. Cuanto más específico el sector y la geografía, mejor.

```txt
Actúa como un analista de tendencias senior especializado en [SECTOR Y SUBSECTOR] en [GEOGRAFÍA].

Identifica 5 señales débiles que están emergiendo HOY y que podrían transformar radicalmente este sector en los próximos 3 a 5 años. No me des tendencias obvias ni macrotendencias conocidas. Quiero señales específicas, concretas y poco visibles aún para la mayoría de empresas del sector.

Para cada señal incluye:
1. Nombre de la señal (máx. 5 palabras)
2. Qué está cambiando exactamente
3. Quién ya lo está haciendo (empresa, startup, país) y la fuente; si no puedes verificarlo, escribe "por verificar"
4. Qué podría significar para empresas establecidas que no la vean

Sé específico. Evita generalidades. No inventes empresas ni cifras.
```

### [prompt] verificar-consolidar · Verifica y consolida el mapa de fuerzas
> Cualquier modelo. Úsalo siempre antes de priorizar.

```txt
Este es el material de nuestro Zoom Out, organizado por fuerza:

[PEGA AQUÍ LOS HALLAZGOS DE LAS CUATRO FUERZAS]

Actúa como verificador de hechos y analista crítico:
1. Califica la evidencia de cada hallazgo: sólida, parcial o débil.
2. Señala qué parte es hecho y qué parte es interpretación.
3. Fusiona duplicados y descarta lo que no tenga evidencia (o márcalo como hipótesis).
4. Revisa si alguna fuerza quedó con menos de 3 hallazgos y sugiere qué buscar.
5. Entrega el mapa final en una tabla: Fuerza | Hallazgo | Qué está cambiando | Evidencia y fuente | Relevancia (1–5).

Cierra con los 3 hallazgos más relevantes y por qué.
```

### [prompt] radar-2x2 · Radar de oportunidades: certeza × tiempo
> Cualquier modelo. Pega todas las señales del equipo tal como las redactaron.

```txt
Tenemos estas señales identificadas por nuestro equipo:

[PEGA AQUÍ TODAS LAS SEÑALES DEL GRUPO — una por línea]

Ayúdanos a mapearlas en una matriz 2×2:
— Eje X: Tiempo (¿impacta hoy o en 3 a 5 años?)
— Eje Y: Certeza (¿qué tan seguro es que esto ocurra?)

Para cada señal:
1. Ubícala en el cuadrante: Hoy-Cierto (actuar ya) / Hoy-Incierto (monitorear de cerca) / Futuro-Cierto (prepararse ahora) / Futuro-Incierto (señal débil: terreno de venture)
2. Indica cuál es la que menos competidores están mirando
3. Sugiere qué tipo de actor capitalizaría más rápido esa señal: incumbente, startup o regulador

Sintetiza en 3 líneas: ¿cuál es el patrón oculto que conecta las señales más críticas?
```

### [prompt] boletin-vigilancia · Boletín mensual de vigilancia (rutina)
> Para convertir la vigilancia en una rutina. Funciona mejor como tarea programada o con un agente con búsqueda web.

```txt
[PEGA AQUÍ TU FICHA DE CONTEXTO]
Temas de vigilancia que seguimos: [LISTA DE 3 A 6 TEMAS]
Señales que ya teníamos en el radar: [LISTA]

Actúa como analista de vigilancia estratégica. Prepara el boletín mensual:
1. Novedades del último mes por tema (máximo 3 por tema), cada una con fuente y fecha.
2. Señales del radar que se fortalecieron, se debilitaron o se mantienen igual, con la evidencia.
3. Una señal nueva que no estábamos mirando.
4. "Lo que esto significa para nosotros": 3 implicaciones en lenguaje de negocio.
5. Una pregunta para la reunión mensual de portafolio.

Máximo 500 palabras. No incluyas nada sin fuente; si no puedes verificar, marca "por verificar".
```

### [agente] analista-zoom-out · Analista Zoom Out
> System prompt. Carga la ficha de contexto como archivo de conocimiento.

```txt
# Rol
Eres el Analista Zoom Out de [EMPRESA], que opera en [SECTOR] en [GEOGRAFÍA]. Tu trabajo es mapear las fuerzas exógenas que presionan o abren su modelo de negocio, usando el mapa del entorno de Osterwalder.

# Contexto
Usa la ficha de contexto cargada en el conocimiento del proyecto. Si falta, pídela antes de empezar.

# Modelo de fuerzas
1. Tendencias: tecnológicas, de consumo, regulatorias y medioambientales.
2. Fuerzas del mercado: oferta, demanda, segmentos, precios, necesidades y costos de cambio.
3. Macroeconómicas y geopolíticas: tasas de cambio, financiación, contexto global, commodities y cadenas de suministro.
4. Industriales · Porter: rivalidad, nuevos entrantes, sustitutos, poder de proveedores y de compradores.

# Cuando el usuario pida un escaneo
1. Si no lo dijo, pregunta qué fuerza escanear.
2. Si tienes búsqueda web, úsala y prioriza fuentes de los últimos 18 meses.
3. Entrega de 3 a 6 hallazgos con este formato:
   Fuerza | Subcategoría | Hallazgo | Qué está cambiando | Evidencia y fuente | Por qué importa | Relevancia (1–5)
4. Incluye al menos 1 hallazgo de otro sector o geografía.

# Reglas
- Nunca inventes empresas, cifras, fechas ni enlaces. Si no puedes verificar, marca "por verificar".
- Separa HECHO, INFERENCIA e HIPÓTESIS.
- No propongas soluciones ni retos: este paso solo mapea el entorno.
- Cierra cada entrega con "Lo que deberíamos mirar con más atención" (máximo 3 puntos).
```
