# El Impacto de los TLC en Imués, Nariño

[![Stack](https://img.shields.io/badge/stack-HTML%20%7C%20CSS%20%7C%20JS-blue)](#)

Sitio informativo que documenta, mediante narrativa visual y entrevistas de
campo, cómo los Tratados de Libre Comercio transformaron la economía campesina
del municipio de Imués, Nariño. El proyecto combina storytelling, recursos
multimedia y microinteracciones accesibles para facilitar la divulgación
académica.

## Características clave

- **Narrativa estructurada** en secciones (Contexto, Impacto, Galería,
  Preguntas, Conclusiones) con anclas y scroll suave.
- **Animaciones progresivas** mediante Intersection Observer y efectos parallax
  suaves que resaltan el contenido sin comprometer el rendimiento.
- **Galería multimedia** con material fotográfico local y enlace directo al
  repositorio de entrevistas completas en Google Drive.
- **Accesibilidad básica**: etiquetas `aria`, navegación por teclado y contraste
  controlado en los componentes principales.
- **Servidor opcional en Python** (`server.py`) para un despliegue sencillo sin
  dependencias externas.

## Estructura del proyecto

```
.
├── content/
│   ├── docs/          # Entrevistas y testimonios en texto
│   └── image/         # Fotografías (JPG)
├── index.html         # Página principal
├── scrips.js          # Interacciones y animaciones
├── style.css          # Estilos responsivos
├── server.py          # Servidor HTTP opcional (Python)
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

## Requisitos

- Navegador moderno con soporte ES6.
- Opcional: Python 3.10+ para ejecutar `server.py`.

## Ejecución local

### 1. Uso directo (recomendado)

1. Clona el repositorio o descarga el ZIP.
2. Abre `index.html` con tu navegador o utiliza la extensión Live Server.

### 2. Servidor ligero con Python

```bash
python server.py
```

El script publica el sitio en `http://127.0.0.1:8000`.

## Scripts útiles

| Comando            | Descripción                                  |
| ------------------ | -------------------------------------------- |
| `python server.py` | Inicia el servidor HTTP simple               |
| `npm install`      | *Opcional* si decides agregar tooling futuro |

## Contenido disponible

- **Fotografías** (`content/image`) optimizadas para web.
- **Transcripciones y notas** (`content/docs`) usadas en la investigación.
- **Drive**: el botón dentro de la sección Galería enlaza al material completo.

## Roadmap sugerido

1. Internacionalización (ES/EN) con `next-i18next` o i18next básico.
2. Conversión a Next.js App Router para despliegues rápidos en Vercel.
3. Optimización de imágenes a WebP y carga diferida.
4. Automatizar pruebas de accesibilidad (Lighthouse/Pa11y).

## Cómo contribuir

Consulta `CONTRIBUTING.md` para conocer el flujo de trabajo propuesto, estilo de
código y verificación previa al enviar pull requests.

## Licencia

Distribuido bajo la licencia MIT. Consulta `LICENSE` para más detalles.

