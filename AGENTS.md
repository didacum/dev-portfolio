# 1. Project Overview
Este proyecto es un portafolio web profesional construido íntegramente en Python utilizando el framework Reflex.

- Arquitectura: Basada en componentes reutilizables (components/) y vistas modulares (views/) que componen la página principal.

- Gestión de Datos: Se utiliza un modelo centralizado donde assets/data/data.json actúa como la única fuente de verdad para el contenido dinámico.

- Objetivo: Actualizar el portfolio a los requerimientos del usuario.

# 2. Build and Test Commands
- Instalación: pip install -r requirements.txt.

- Desarrollo: reflex run (Inicia el servidor local y el frontend).

- Producción: reflex export (Genera los estáticos para despliegue).

- Limpieza: rm -rf .web (Para forzar la regeneración del frontend ante cambios estructurales).

# 3. Code Style Guidelines
- Reflex Standard: No utilizar HTML/CSS nativo; emplear exclusivamente los componentes y el sistema de estilos de Reflex (diccionarios Python).

- SDD Workflow: Es obligatorio seguir el pipeline: Spec -> Design -> Tasks -> Apply -> Verify. Ninguna línea de código debe escribirse sin una tarea previa validada.

- Nomenclatura: Seguir PEP 8 para el código Python y usar nombres descriptivos en inglés para funciones y variables de UI.

- Git & Commits: 
  - Se deben utilizar Conventional Commits (ej: feat: add tech stack component). Cada tarea terminada en la fase de apply genera un commit atómico. 
  - Se usará el modelo Gitflow a la hora de crear nuevas features en el proyecto. 
  - El repositorio será subido al github del usuario. Será el origin. 
  - La rama main del repositorio debe estar bloqueada, ya que será la utilizada en producción. Todos los cambios se unirán a la rama main mediante pull request que debe aceptar el usuario en el repositorio remoto. 

- Se emplearán los principios SOLID y GRASP para el diseño e implementación del código.

# 4. Testing Instructions
- Verificación Visual: Durante la fase sdd-verify, el agente debe comprobar la responsividad en móviles y escritorio, asegurando que los componentes de Reflex se adapten correctamente.

- Integridad de Datos: Validar que cada campo definido en data.json se renderice sin errores de tipo o valores nulos.

- Manual QA: El orquestador debe solicitar confirmación humana tras el despliegue local antes de proceder al archive.

# 5. Security Considerations
- Auditoría de Dependencias: Ejecutar un escaneo de vulnerabilidades en el requirements.txt en cada cambio mayor (usando herramientas como safety).

- Principio de Menor Privilegio: Los agentes no tienen permiso para crear archivos fuera de la estructura del proyecto ni para acceder a variables de entorno globales.

- Protección de Datos: Prohibido hardcodear información sensible. El CV y las imágenes deben gestionarse exclusivamente desde la carpeta assets/.

- Sanitización: Asegurar que cualquier enlace externo o recurso estático cargado sea validado para evitar ataques de inyección básica o redirecciones maliciosas.