# 02 · Contexto y valor: la base de todo

Sin contexto, la IA responde para "una empresa cualquiera". Estos prompts construyen la ficha de contexto y la lectura de valor (crear, entregar, capturar) que se reutiliza en todo el recorrido.

---

### [prompt] ficha-contexto · Construye tu ficha de contexto (entrevista)
> Cualquier modelo. La IA te entrevista, una pregunta a la vez.

```txt
Actúa como consultor senior de estrategia e innovación. Vas a ayudarme a construir la ficha de contexto de mi empresa para un proceso de innovación.

Entrevístame con preguntas cortas, de una en una (máximo 8), para completar: empresa, sector y subsector, geografía, clientes principales, propuesta de valor actual, 3 prioridades estratégicas, retos actuales, capacidades distintivas y restricciones.

Reglas:
- Si mi respuesta es vaga, pídeme un ejemplo concreto.
- No me pidas datos confidenciales, personales ni cifras sensibles.
- Al final, entrega la ficha completa en máximo 200 palabras con este formato:
  FICHA DE CONTEXTO
  Empresa · Sector y subsector · Geografía · Clientes principales · Propuesta de valor actual · Prioridades estratégicas (3) · Retos o dolores actuales · Capacidades distintivas · Restricciones · No compartir con la IA
- Señala qué campos quedaron débiles.

Empieza con la primera pregunta.
```

### [prompt] valor-crear-entregar-capturar · Lee tu modelo de negocio: crear, entregar y capturar valor
> Cualquier modelo. Basado en la lectura de modelo de negocio de David Teece (2010).

```txt
Ayúdame a preparar el contexto de mi negocio. Empieza entrevistándome: en tu primera respuesta hazme tres preguntas breves y numeradas para conocer 1) qué negocio u oferta trabajaremos, a quién sirve y qué necesidad resuelve; 2) cómo entregamos, cómo cobramos y cuáles son los principales costos; 3) qué problema reciente observamos, qué evidencia tenemos y con qué personas, tiempo y presupuesto contamos.

Detente y espera mis respuestas; todavía no hagas el resumen. Si falta un dato imprescindible, haz una sola repregunta breve y vuelve a esperar. Acepta respuestas aproximadas o «no sé»; no solicites datos personales ni información confidencial.

Definiciones: crear valor se refiere a nuestros segmentos de clientes y nuestra propuesta de valor; entregar valor, a cómo comunicamos la oferta, la vendemos y distribuimos, atendemos al cliente y cuidamos la relación; capturar valor, a nuestras fuentes de ingresos y formas de cobrar.

Con lo respondido, resume cómo creamos, entregamos y capturamos valor en tres frases y registra nuestros recursos y límites. No asignes personas, tiempo ni presupuesto sin confirmación; marca lo pendiente como "por acordar". Separa hechos, hipótesis y datos por validar; no inventes cifras. Pídeme confirmar o corregir el resumen y conserva el contexto confirmado para los siguientes ejercicios.
```

### [prompt] anonimizar · Anonimiza antes de compartir
> Úsalo en una herramienta aprobada por tu empresa antes de llevar material a otros chats.

```txt
Voy a pegar un texto interno. Antes de usarlo en un proceso de innovación con IA, anonimízalo:
1. Reemplaza nombres de personas por roles ([GERENTE COMERCIAL], [CLIENTE A]).
2. Reemplaza nombres de clientes y aliados por descripciones genéricas ([CADENA DE RETAIL REGIONAL]).
3. Convierte cifras exactas sensibles en rangos u órdenes de magnitud.
4. Elimina correos, teléfonos, direcciones, números de documento y contratos.
5. Lista al final todo lo que cambiaste para que yo lo revise.

No resumas ni alteres el sentido del texto.

TEXTO:
[PEGA AQUÍ]
```
