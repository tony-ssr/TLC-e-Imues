# Guía de Contribución

Gracias por tu interés en mejorar el proyecto **Impacto de los TLC en Imués,
Nariño**. Este documento explica el flujo de trabajo sugerido y las reglas de
estilo para mantener una base ordenada.

## Flujo de trabajo

1. **Fork / rama**  
   - Haz fork o crea una rama desde `main` usando un nombre descriptivo:
     `feature/galeria-responsive`, `fix/accesibilidad`, etc.

2. **Issue previo**  
   - Abre un issue antes de enviar un PR si el cambio es mayor. Usa plantillas
     (bug/feature) cuando existan.

3. **Commits**  
   - Mensajes en español o inglés, formato `tipo: resumen breve`
     (`docs: actualiza README`).  
   - Agrupa cambios relacionados y evita commits enormes.

4. **Pull request**  
   - Describe el problema, la solución propuesta y pasos para probar.  
   - Adjunta capturas o gifs cuando haya cambios visuales.

## Estándares de código

- **HTML**: semántico, usa `aria-*` cuando corresponda.
- **CSS**: mantener el enfoque actual en `style.css`, favoreciendo utilidades
  reutilizables; agrupar selectores por sección.
- **JavaScript**:
  - ES6+, sin dependencias externas.
  - Nombres descriptivos (`handleScroll`, `isMenuOpen`).
  - Evitar lógica duplicada; crear helpers cuando haga falta.
- **Assets**:
  - Optimiza imágenes antes de subirlas.
  - Coloca documentos en `content/docs` y respeta el naming.

## Verificación antes del PR

- Prueba en los navegadores principales (Chrome/Edge/Firefox).
- Ejecuta `python server.py` para validar que los recursos estáticos se sirven.
- Pasa Lighthouse (Performance + Accessibility) y adjunta resultados si tu
  cambio impacta la UI.

## Código de conducta

- Respeta a la comunidad.
- Usa lenguaje inclusivo.
- Aporta retroalimentación constructiva.

¡Gracias por contribuir!

