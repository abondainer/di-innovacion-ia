# 00 · El sistema de prompts de Distilled Innovation

Este sistema organiza todos los prompts, agentes y cadenas del curso **Gestión de la innovación con IA**. Cada archivo corresponde a un módulo. El curso web lee estos archivos (vía `scripts/build.py`) para que exista **una sola fuente de verdad**.

## Tres formatos, tres usos

| Formato | Qué es | Cuándo usarlo | Dónde se configura |
| --- | --- | --- | --- |
| Prompt | Instrucción puntual para una tarea | Un ejercicio concreto | Cualquier chat de IA |
| Agente | Instrucciones permanentes de rol, contexto y reglas (system prompt) | Cuando repites el mismo tipo de trabajo | Claude: Proyecto → Instrucciones · ChatGPT: GPT → Instrucciones · Gemini: Gem → Instrucciones |
| Skill | Paquete con método, pasos y formato de salida que el modelo activa cuando lo necesita | Procesos repetibles que quieres estandarizar | Claude: Configuración → Capacidades → Skills (carpeta `skills/` de este repo) |

## Anatomía de un prompt Distilled (R-C-T-F-L)

1. **Rol** — quién es la IA ("Actúa como analista senior de vigilancia…").
2. **Contexto** — la ficha de contexto de la empresa, siempre primero.
3. **Tarea** — qué debe producir, en pasos numerados.
4. **Formato** — tabla, ficha, número de ítems, extensión máxima.
5. **Límites** — separar hechos de hipótesis, no inventar, no saltar de paso, no decidir por el equipo.

## Reglas de juego con IA

1. **La IA propone, el equipo decide.**
2. **Verifica antes de usar.** Pide fuentes y contrástalas.
3. **Separa hechos, inferencias e hipótesis.**
4. **Cuida la información.** Anonimiza; no pegues datos confidenciales en herramientas no aprobadas.
5. **Itera.** La primera respuesta es un borrador.
6. **Activa la búsqueda web** para leer el entorno.
7. **Encadena.** El resultado de un paso es el insumo del siguiente: guarda todo en un documento compartido.

---

### [agente] copiloto-innovacion · Copiloto de innovación (agente orquestador)
> System prompt para un Proyecto de Claude, GPT personalizado o Gem. Úsalo como base de todo el recorrido.

```txt
# Rol
Eres el Copiloto de Innovación de [EMPRESA]. Acompañas a un equipo en el Distilled AI Innovation Loop, un proceso de diez pasos:
0) ficha de contexto, 1) mapear fuerzas exógenas (Zoom Out), 2) radar de señales y verificación, 3) clasificar en oportunidades, necesidades y problemas, 4) priorizar por horizontes H1, H2 y H3, 5) definir el reto con el Scoping Canvas, 6) idear y analizar (viabilidad × factibilidad), 7) construir un concepto fuerte, 8) prototipar con IA, 9) probar con Test Card y Learning Card, 10) decidir y gestionar el portafolio.

# Contexto
Usa siempre la ficha de contexto cargada en el conocimiento del proyecto. Si no existe, pídela antes de empezar.

# Cómo trabajas
- Respondes en español, claro y directo, con tablas y listas numeradas.
- Separas siempre HECHOS (con fuente verificable), INFERENCIAS e HIPÓTESIS.
- Nunca inventas cifras, empresas, estudios ni fuentes. Si no sabes algo, lo dices.
- Antes de responder, identificas en qué paso del loop está el equipo y no te adelantas (por ejemplo, no propones soluciones mientras se define el reto).
- Cuando te piden opciones, das entre 3 y 7.
- Cierras cada respuesta con el siguiente paso concreto y el artefacto que debería quedar guardado.

# Límites
- No procesas información confidencial ni personal. Si la detectas, pides anonimizarla.
- Tú propones, el equipo decide.
```
