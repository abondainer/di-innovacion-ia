# Gestión de la innovación con IA · Distilled Innovation

Curso digital, sistema de prompts, plantillas y **skills de Claude** para gestionar la innovación con inteligencia artificial, basado en los talleres de Distilled Innovation *IA para la gestión de la innovación*, *Innovar para seguir siendo relevantes* y *Venture Building Estratégico*.

> Cuando generar ideas cuesta casi nada, el valor está en **destilar**: leer el entorno con criterio, decidir con evidencia y aprender más rápido que el mercado.

## Qué incluye

| Carpeta | Contenido |
| --- | --- |
| `index.html` + `assets/` | Curso web con 9 módulos, 6 visualizaciones 3D (Three.js), diagnóstico de madurez, matrices interactivas, generador de Test Card y caja de herramientas |
| `prompts/` | Sistema de prompts: 48 prompts y agentes (system prompts) en 8 archivos, **fuente única** del curso |
| `skills/` | 8 skills de Claude del Distilled AI Innovation Loop |
| `plantillas/` | 12 plantillas en Markdown + `canvas-imprimibles.html` (A4, imprimir o guardar como PDF) |
| `herramientas/` | `tablero-portafolio-innovacion.xlsx`: señales, oportunidades, portafolio, experimentos y tablero |
| `scripts/` | `build.py` (prompts → curso) y `empaquetar-skills.sh` (skills → .zip) |

## El Distilled AI Innovation Loop

`Contexto → Zoom Out → Radar → Clasificar → Priorizar → Encuadrar → Idear → Concepto → Prototipar → Probar → Decidir`

| Skill | Para qué |
| --- | --- |
| [`di-innovation-loop`](skills/di-innovation-loop/SKILL.md) | Orquesta el recorrido completo y dice qué sigue |
| [`di-ficha-contexto`](skills/di-ficha-contexto/SKILL.md) | Ficha de contexto y lectura crear · entregar · capturar valor |
| [`di-exposicion-ia`](skills/di-exposicion-ia/SKILL.md) | Cómo la IA transforma tu modelo de negocio y tu madurez |
| [`di-zoom-out`](skills/di-zoom-out/SKILL.md) | Vigilancia: 4 fuerzas, señales débiles, radar y boletín |
| [`di-retos`](skills/di-retos/SKILL.md) | Oportunidades/necesidades/problemas, horizontes y Scoping Canvas |
| [`di-ideacion-concepto`](skills/di-ideacion-concepto/SKILL.md) | Ideación, viabilidad × factibilidad y ficha de concepto |
| [`di-experimentos`](skills/di-experimentos/SKILL.md) | Supuesto asesino, prototipo con IA, Test y Learning Cards |
| [`di-hoja-de-ruta`](skills/di-hoja-de-ruta/SKILL.md) | 4 niveles × 3 horizontes, hoja de ruta 3·6·12 y comité mensual |

## Uso

**Ver el curso:** abre `index.html` con un servidor local (las escenas 3D cargan Three.js desde unpkg):

```bash
python3 -m http.server 8000
```

Luego visita `http://localhost:8000`. También funciona publicado con GitHub Pages.

**Instalar las skills en Claude (app web o escritorio):**

```bash
./scripts/empaquetar-skills.sh
```

Sube cada `.zip` de `dist/` en Configuración → Capacidades → Skills.

**Claude Code:** instala el repositorio como plugin (`.claude-plugin/plugin.json`) o copia `skills/<nombre>` en `~/.claude/skills/`.

**GPTs y Gems:** pega el contenido de `SKILL.md` (sin el encabezado entre `---`) en Instrucciones.

**Editar prompts:** modifica `prompts/*.md` (formato `### [prompt|agente] id · Título`, nota `>` y bloque ```txt) y ejecuta:

```bash
python3 scripts/build.py
```

## Reglas de juego con IA

1. La IA propone, el equipo decide. 2. Verifica antes de usar. 3. Separa hechos de hipótesis. 4. Cuida la información. 5. Itera. 6. Encadena los resultados.

## Referencias

Teece (2010) *Business Models, Business Strategy and Innovation* · OCDE/Eurostat (2018) *Manual de Oslo* · Deming Institute, *Theory of Knowledge* · Christensen Institute, *Disruptive Innovation* · Schumpeter (1942) cap. VII · Baghai, Coley y White (1999) *The Alchemy of Growth* · Osterwalder, mapa del entorno · Strategyzer, Test Card y Learning Card.

---
**Distilled Innovation®** · Tus aliados estratégicos para el crecimiento sostenible de tus negocios · [distilledinnovation.co](https://distilledinnovation.co)
