# 06 · Prototipar con IA y experimentar

Encontrar el supuesto que puede matar la idea, construir el prototipo más simple que lo pruebe y diseñar experimentos con criterio de éxito y de fracaso.

---

### [prompt] supuesto-asesino · Mapa de supuestos: la IA como socio de Venture Capital
> Cualquier modelo. El prompt más poderoso del recorrido.

```txt
Somos un equipo de una empresa establecida y estamos evaluando este reto / concepto:

[RETO O FICHA DE CONCEPTO]

Actúa como un socio de un fondo de Venture Capital que tiene que decidir si invertir en esto. Tu trabajo es destruir nuestros supuestos antes de que el mercado lo haga.

Identifica los 6 supuestos más críticos que tendrían que ser verdad para que esto sea exitoso. Clasifícalos en deseabilidad (¿lo quieren?), viabilidad (¿genera valor para el negocio?) o factibilidad (¿podemos hacerlo?). Para cada supuesto:
— Nombre del supuesto (máx. 8 palabras)
— Por qué es crítico: si falla, ¿qué pasa?
— Nivel de certeza: Evidencia / Supuesto / Desconocido
— Señala cuál es el SUPUESTO ASESINO: el más crítico Y el menos validado de todos

Al final, dime en una línea: ¿qué es lo primero que harías para validar o descartar esto en menos de 4 semanas y con un presupuesto mínimo?
```

### [prompt] elegir-prototipo · Elige el supuesto y el tipo de prototipo
> Cualquier modelo.

```txt
Ficha de concepto: [PEGA LA FICHA DE CONCEPTO]

1. Ordena los supuestos críticos según dos criterios: qué tan importante es para que el concepto funcione y qué tan poca evidencia tenemos. Recomienda el más riesgoso.
2. Para ese supuesto, recomienda el tipo de prototipo más simple entre: storyboard, landing page, mockup de pantallas, simulación con IA o Mago de Oz. Explica por qué en 2 líneas.
3. Describe qué debe incluir el prototipo para probar ese supuesto (máximo 5 elementos).
```

### [prompt] construir-prototipo · Construye el prototipo (landing o app)
> Para Lovable, v0, Gamma, Claude (artifacts) u otra herramienta generativa.

```txt
Crea una [LANDING PAGE / APP DE 3 PANTALLAS] para validar este concepto:

Nombre: [NOMBRE]
Qué es: [FRASE DEL CONCEPTO]
Para quién: [SEGMENTO]
Problema que resuelve: [PROBLEMA]
Cómo funciona: [3 A 5 PASOS]
Supuesto que queremos probar: [SUPUESTO]

Incluye:
- Un titular claro con la propuesta de valor
- 3 beneficios concretos para el cliente
- Una explicación visual de cómo funciona
- Un llamado a la acción que permita medir el interés (ej.: "Quiero probarlo", formulario de registro)

Estilo: limpio, profesional, en español. No uses datos ni testimonios inventados.
```

### [prompt] storyboard · Crea un storyboard de 6 escenas
> Cualquier modelo con generación de imágenes.

```txt
Ficha de concepto: [PEGA LA FICHA DE CONCEPTO]

Crea un storyboard de 6 escenas que cuente la experiencia de un cliente con este concepto:
1. Situación inicial y problema
2. Momento en que descubre la solución
3. Primer uso
4. Momento de valor ("ajá")
5. Resultado
6. Qué hace después (vuelve, recomienda, paga)

Para cada escena: título, descripción de 2 líneas y una instrucción para generar la imagen en estilo ilustración simple.
```

### [prompt] simulacion-ia · Simula el servicio con un agente (prototipo conversacional)
> Para un Proyecto de Claude, GPT o Gem que actúa como el servicio.

```txt
Vas a simular el servicio [NOMBRE DEL CONCEPTO] para probarlo con clientes reales en una conversación.

Qué es: [FRASE DEL CONCEPTO]
Para quién: [SEGMENTO]
Qué entrega en cada interacción: [ENTREGABLE: recomendación, diagnóstico, plan…]

Reglas de la simulación:
1. Saluda y explica en 2 líneas qué puedes hacer.
2. Haz máximo 3 preguntas para entender la situación del usuario.
3. Entrega el resultado en el formato [FORMATO].
4. Al final pregunta: "¿Qué tan útil fue esto de 1 a 5 y qué te faltó?" y "¿Pagarías por esto? ¿Cuánto?".
5. No prometas resultados, no des asesoría legal, médica ni financiera y aclara que es un prototipo.
```

### [prompt] experimentos · Diseña 3 experimentos de menor a mayor esfuerzo
> Cualquier modelo.

```txt
Nuestro supuesto asesino es: [SUPUESTO]

Diseña 3 experimentos posibles para validarlo, de menor a mayor inversión de tiempo y dinero.

Para cada experimento usa este formato:
— Nombre del experimento
— Qué hacemos exactamente (acción concreta, no genérica)
— Con quién (perfil específico de persona o segmento a contactar)
— En cuánto tiempo es ejecutable desde cero
— Criterio de éxito: ¿qué resultado confirma que el supuesto ES verdad?
— Criterio de fracaso: ¿qué resultado nos dice que debemos pivotar o detener?

El experimento 1 debe ser ejecutable esta semana, sin presupuesto.
El experimento 3 puede tomar hasta 4 semanas y un presupuesto acotado: [PRESUPUESTO].

Sé muy concreto. Nada de "hacer entrevistas": dime exactamente a quién, qué pregunta clave y cómo mido la respuesta. Prioriza medir comportamiento (lo que la gente hace) sobre opinión.
```

### [prompt] test-card · Escribe la Test Card
> Cualquier modelo. Formato de Strategyzer.

```txt
Ficha de concepto: [PEGA LA FICHA DE CONCEPTO]
Prototipo: [DESCRIBE EL PROTOTIPO]
Supuesto a probar: [SUPUESTO]

Escribe una Test Card:
- Creemos que… (el supuesto, en una frase concreta)
- Para verificarlo, vamos a… (el experimento usando el prototipo)
- Y mediremos… (una métrica observable)
- Estamos en lo correcto si… (un umbral numérico y un plazo)

Agrega: costo estimado (bajo, medio o alto), tiempo para obtener datos y nivel de confianza de la evidencia (bajo, medio o alto). Todo umbral es provisional y lo aprueba el equipo.
```

### [prompt] revisar-test-card · Revisa la Test Card
> Cualquier modelo.

```txt
Esta es nuestra Test Card: [PEGA LA TEST CARD]

Revísala con estas preguntas:
1. ¿El supuesto es uno solo y es concreto?
2. ¿El experimento prueba ese supuesto o algo distinto?
3. ¿La métrica mide comportamiento real (lo que la gente hace) y no solo opinión?
4. ¿El criterio de éxito tiene número y plazo?
5. ¿Hay un criterio de fracaso explícito?

Para cada punto débil, propón una versión mejorada.
```

### [prompt] learning-card · Completa la Learning Card
> Cualquier modelo, después de la prueba.

```txt
Test Card: [PEGA LA TEST CARD]
Resultados de la prueba: [PEGA DATOS Y OBSERVACIONES]

Completa la Learning Card:
- Creíamos que…
- Observamos…
- De esto aprendimos que…
- Por lo tanto, vamos a… (seguir, ajustar o detener, con el siguiente paso)

Reglas:
- Separa lo que muestran los datos de lo que interpretamos.
- Si la evidencia es débil, dilo y propón la siguiente prueba.
```

### [agente] disenador-experimentos · Diseñador de experimentos
> System prompt.

```txt
# Rol
Eres el diseñador de experimentos de [EMPRESA]. Conviertes supuestos críticos en pruebas claras usando la Test Card y la Learning Card.

# Contexto
Usa la ficha de concepto y la descripción del prototipo cargadas en el proyecto.

# Cómo trabajas
1. Tomas un supuesto a la vez, empezando por el más riesgoso (supuesto asesino).
2. Escribes la Test Card: Creemos que… / Para verificarlo, vamos a… / Y mediremos… / Estamos en lo correcto si…
3. Verificas que la métrica mida comportamiento real y que el criterio tenga número, plazo y criterio de fracaso.
4. Estimas costo, tiempo y nivel de confianza de la evidencia.
5. Después de la prueba, completas la Learning Card: Creíamos que… / Observamos… / De esto aprendimos que… / Por lo tanto, vamos a…
6. Cierras con una decisión recomendada: seguir, ajustar o detener.

# Límites
- No inventas resultados ni interpretas datos que no existen.
- Separa HECHOS, INFERENCIAS e HIPÓTESIS.
- El equipo toma la decisión final.
```
