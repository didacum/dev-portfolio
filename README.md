# Código Fuente - Portafolio Web Personal

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.8.28+-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://reflex.dev)
[![Vercel](https://img.shields.io/badge/Deploy-Vercel-black?style=for-the-badge&logo=vercel&logoColor=white&labelColor=101010)](https://vercel.com)

Este repositorio contiene exclusivamente el código fuente de mi portafolio profesional web, donde expongo mis proyectos, experiencia técnica y certificaciones orientadas al desarrollo de software y la ciberseguridad.

El sitio está desarrollado íntegramente en [Python](https://python.org) utilizando el framework [Reflex](https://reflex.dev) para generar un frontend estático (HTML, CSS, JS) sin escribir código web nativo.

> **Reconocimiento:** La arquitectura base y el diseño visual de este proyecto parten de la [plantilla open-source creada por Brais Moure (Mouredev)](https://github.com/mouredev/portafolio-template). He adaptado y extendido el código para ajustarlo a mis necesidades específicas y requerimientos técnicos.

## 🏗️ Arquitectura y Estructura

El proyecto sigue principios SOLID y de diseño modular, estructurándose en:

* `assets/data/data.json`: Actúa como la única fuente de verdad (Single Source of Truth). Todo el contenido dinámico del portafolio se modifica aquí, sin tocar la lógica visual.
* `portafolio/components/`: Componentes UI reutilizables (botones, tarjetas, badges).
* `portafolio/views/`: Secciones modulares que componen la página principal (header, experiencia, proyectos, etc.).
* `portafolio/styles/`: Centralización de constantes gráficas y diseño responsivo.

## 📄 Licencia y Derechos de Autor

Este repositorio tiene una licencia dual para separar la arquitectura de software de mi información personal:

**1. Contenido y Activos Personales (Todos los derechos reservados)**
Toda la información personal, datos, textos biográficos, el archivo `assets/data/data.json`, fotografías, imágenes (`assets/`), y currículum vitae (`cv.pdf`) son de mi exclusiva propiedad. **No se permite su copia, reproducción, clonación, distribución ni uso bajo ninguna circunstancia.** 
**2. Código Fuente**
La arquitectura base de este proyecto es un fork adaptado del [portafolio-template](https://github.com/mouredev/portafolio-template) original de Brais Moure, el cual se distribuye bajo la [Apache License 2.0](./LICENSE). Las modificaciones específicas, refactorizaciones y nuevos componentes añadidos en este repositorio son obra derivada y se proveen únicamente con fines de exhibición técnica. No autorizo la redistribución ni el uso comercial de mis modificaciones de software ("as-is") para crear otros portafolios web sin consentimiento previo.