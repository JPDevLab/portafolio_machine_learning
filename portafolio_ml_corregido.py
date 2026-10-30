
import streamlit as st
from textwrap import dedent

def render_html(markup):
    st.markdown(dedent(markup).strip(), unsafe_allow_html=True)

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

st.set_page_config(
    page_title="Portafolio | Desarrollador de Software",
    page_icon="JP",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

render_html("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #e6edf3;
    }

    [data-testid="stSidebar"] {
        background-color: #151b26;
        border-right: 1px solid #263244;
    }

    .hero {
        background: linear-gradient(120deg, #17263d, #182033, #202b45);
        border: 1px solid #30415c;
        padding: 42px;
        border-radius: 18px;
        margin-bottom: 30px;
    }

    .hero-label {
        color: #80b5ff;
        font-size: 13px;
        letter-spacing: 2px;
        font-weight: 600;
        text-transform: uppercase;
    }

    .hero h1 {
        color: #ffffff;
        font-size: 38px;
        margin: 12px 0;
    }

    .hero p {
        color: #b9c6d8;
        font-size: 16px;
        line-height: 1.7;
        max-width: 750px;
    }

    .project-card {
        background: #171e29;
        border: 1px solid #293547;
        border-radius: 12px;
        padding: 22px;
        min-height: 205px;
        margin-bottom: 18px;
        transition: 0.2s ease;
    }

    .project-card:hover {
        border-color: #5599ef;
        transform: translateY(-3px);
    }

    .project-category {
        color: #80b5ff;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }

    .project-card h3 {
        color: #ffffff;
        font-size: 18px;
        margin: 12px 0;
    }

    .project-card p {
        color: #aab7c7;
        font-size: 13px;
        line-height: 1.6;
        min-height: 60px;
    }

    .project-link {
        display: inline-block;
        color: #80b5ff !important;
        text-decoration: none !important;
        font-size: 13px;
        font-weight: 600;
        margin-top: 12px;
    }

    .project-link:hover {
        color: #ffffff !important;
    }

    .section-title {
        font-size: 23px;
        font-weight: 600;
        color: #ffffff;
        margin-top: 25px;
        margin-bottom: 5px;
    }

    .section-description {
        color: #8b98a9;
        font-size: 14px;
        margin-bottom: 22px;
    }

    .footer {
        border-top: 1px solid #293547;
        padding-top: 20px;
        margin-top: 45px;
        text-align: center;
        color: #7d8999;
        font-size: 12px;
    }

    #MainMenu, footer {
        visibility: hidden;
    }
</style>
""")


# --------------------------------------------------
# INFORMACIÓN DE LOS PROYECTOS
# --------------------------------------------------

projects = [

    # MACHINE LEARNING

    {
        "name": "Clasificación con KNN",
        "category": "Machine Learning",
        "description": "Aplicación del algoritmo K-Nearest Neighbors para clasificar datos y analizar similitudes.",
        "url": "https://appconsumohora-5lqsstytnsoxpa34guwtfh.streamlit.app/"
    },
    {
        "name": "Regresión Lineal",
        "category": "Machine Learning",
        "description": "Implementación de modelos de regresión lineal para analizar relaciones y realizar predicciones.",
        "url": "https://machine-learning-hqcjanjiambod6xmlgt3k5.streamlit.app/"
    },
    {
        "name": "Agrupamiento K-Means",
        "category": "Machine Learning",
        "description": "Agrupamiento de datos mediante técnicas de aprendizaje no supervisado.",
        "url": "https://app-evaluador-k94fosxofdexcissfcwctj.streamlit.app/"
    },
    {
        "name": "Predicción de compra de seguros",
        "category": "Machine Learning",
        "description": "Modelo de aprendizaje automático orientado a predecir comportamientos relacionados con la compra de seguros.",
        "url": "https://regresionlineal-fhgtaykfsuwxafazbzkvzf.streamlit.app/"
    },
    {
        "name": "Árboles de Decisión",
        "category": "Machine Learning",
        "description": "Clasificación y toma de decisiones mediante modelos basados en árboles.",
        "url": "https://arboldecision-aszznjqnuycnfum3smcufi.streamlit.app/"
    },
    {
        "name": "Consumo Total vs Hora",
        "category": "Machine Learning",
        "description": "Análisis de consumo energético en relación con las horas del día.",
        "url": "https://arboldecision-aszznjqnuycnfum3smcufi.streamlit.app/"
    },
    {
        "name": "Aplicación de Consumo",
        "category": "Machine Learning",
        "description": "Herramienta de análisis y procesamiento de información relacionada con el consumo.",
        "url": "https://appappconsumo-djqrsp7zpehhavfucerufm.streamlit.app/"
    },
    {
        "name": "Neuronas vs Regresión",
        "category": "Machine Learning",
        "description": "Aplicación orientada a explorar modelos neuronales y su comparación con técnicas de regresión.",
        "url": "https://appneuronavsregresion-k4foox2xvfgzpw3wjft8yp.streamlit.app/"
    },
    {
        "name": "Análisis de Consumo",
        "category": "Machine Learning",
        "description": "Aplicación relacionada con el análisis y modelado de datos de consumo.",
        "url": "https://appconsumores-fwxqqhuqsngudmpbv9buia.streamlit.app/"
    },
    {
        "name": "Aplicación Q75",
        "category": "Machine Learning",
        "description": "Proyecto experimental desarrollado y desplegado mediante Streamlit.",
        "url": "https://q75peszknjzqscgceqithx.streamlit.app/"
    },

    # VISIÓN ARTIFICIAL

    {
        "name": "YOLOv5",
        "category": "Visión Artificial",
        "description": "Implementación de detección de objetos utilizando el modelo de visión artificial YOLOv5.",
        "url": "https://yolov5-main-nnxkuybgkqwqkehafcshgn.streamlit.app/"
    },
    {
        "name": "VisionTwo",
        "category": "Visión Artificial",
        "description": "Aplicación experimental enfocada en procesamiento y análisis de imágenes.",
        "url": "https://visiontwo-6lrvopkubgzbbbck9g8aag.streamlit.app/"
    },
    {
        "name": "VisionComb",
        "category": "Visión Artificial",
        "description": "Proyecto de visión artificial con integración de modelos y herramientas de detección.",
        "url": "https://visioncomb-main-7tn6tu6s4j2bk7fzekqvyp.streamlit.app/YOLO"
    },
    {
        "name": "App de Reconocimiento",
        "category": "Visión Artificial",
        "description": "Aplicación relacionada con reconocimiento y procesamiento de información visual.",
        "url": "https://app-rec-gxfnqppuvkccstw8youa5z.streamlit.app/"
    },

    # INTELIGENCIA ARTIFICIAL Y NLP

    {
        "name": "Traductor",
        "category": "Inteligencia Artificial",
        "description": "Herramienta de traducción desarrollada mediante una aplicación web interactiva.",
        "url": "https://traductor-tradw-nevxykgdc8iybbqrnjtlhd.streamlit.app/"
    },
    {
        "name": "ISTM NLP",
        "category": "Inteligencia Artificial",
        "description": "Proyecto relacionado con el procesamiento del lenguaje natural.",
        "url": "https://istmnlp-main-gp2vhfd2bkcklsbqwlaxzj.streamlit.app/"
    },
    {
        "name": "ChatPDF",
        "category": "Inteligencia Artificial",
        "description": "Aplicación para interactuar con documentos PDF mediante herramientas de inteligencia artificial.",
        "url": "https://chatpdf-3uxzbbzwwh9k4ay4njlq3v.streamlit.app/"
    },
    {
        "name": "Arquitectura de Redes Neuronales",
        "category": "Inteligencia Artificial",
        "description": "Exploración de arquitecturas y conceptos relacionados con redes neuronales.",
        "url": "https://arquitecturaredesneuronales-r27vcyn7gsruj3vx88gpkz.streamlit.app/"
    },

    # OTROS PROYECTOS

    {
        "name": "TM",
        "category": "Desarrollo de Software",
        "description": "Proyecto de desarrollo de software implementado y desplegado mediante Streamlit.",
        "url": "https://tm-main-fy5tmmwwgue2bgqkc2wjms.streamlit.app/"
    },
    {
        "name": "Aplicación Multipágina",
        "category": "Desarrollo de Software",
        "description": "Aplicación web multipágina desarrollada con Streamlit.",
        "url": "https://multipagina-fyavpc5df95wwhkw4bmhsr.streamlit.app/"
    },
    {
        "name": "IMM1",
        "category": "Desarrollo de Software",
        "description": "Proyecto experimental de desarrollo e implementación de aplicaciones.",
        "url": "https://imm1-main-fmmeyteyrpye2wc8yjfguf.streamlit.app/"
    }
]


# --------------------------------------------------
# BARRA LATERAL
# --------------------------------------------------

with st.sidebar:

    st.markdown("## JP | Portfolio")

    st.caption("Desarrollo de Software")

    st.divider()

    st.markdown("### Navegación")

    section = st.radio(
        "Selecciona una sección",
        ["Inicio", "Proyectos"],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### Información")

    st.write("**Proyectos registrados**")
    st.markdown(f"## {len(projects)}")

    st.caption("Aplicaciones desarrolladas y desplegadas en Streamlit.")


# --------------------------------------------------
# INICIO
# --------------------------------------------------

if section == "Inicio":

    render_html("""
    <div class="hero">
        <div class="hero-label">PORTAFOLIO DE DESARROLLO</div>
        <h1>Desarrollo de Software e Inteligencia Artificial</h1>
        <p>
            Bienvenido a mi portafolio. Aquí encontrarás una recopilación
            de proyectos y aplicaciones desarrolladas utilizando diferentes
            tecnologías, algoritmos de Machine Learning, inteligencia
            artificial y herramientas de desarrollo de software.
        </p>
    </div>
    """)

    st.markdown('<div class="section-title">Explora mi trabajo</div>',
                unsafe_allow_html=True)

    st.markdown(
        '<div class="section-description">Proyectos organizados por áreas de desarrollo.</div>',
        unsafe_allow_html=True
    )

    categories = [
        ("Machine Learning", "Modelos predictivos, clasificación y análisis de datos."),
        ("Visión Artificial", "Detección de objetos y procesamiento de imágenes."),
        ("Inteligencia Artificial", "Procesamiento de lenguaje natural y aplicaciones inteligentes."),
        ("Desarrollo de Software", "Aplicaciones web y proyectos de programación.")
    ]

    cols = st.columns(2)

    for i, (name, description) in enumerate(categories):

        with cols[i % 2]:

            total = sum(
                1 for p in projects if p["category"] == name
            )

            render_html(f"""
            <div class="project-card">
                <div class="project-category">ÁREA DE DESARROLLO</div>
                <h3>{name}</h3>
                <p>{description}</p>
                <strong style="color:#80b5ff;">{total} proyectos</strong>
            </div>
            """)

    st.divider()

    st.markdown("### Proyectos destacados")

    featured = [
        "YOLOv5",
        "ChatPDF",
        "Clasificación con KNN"
    ]

    cols = st.columns(3)

    for i, name in enumerate(featured):

        project = next(p for p in projects if p["name"] == name)

        with cols[i]:

            render_html(f"""
            <div class="project-card">
                <div class="project-category">{project["category"]}</div>
                <h3>{project["name"]}</h3>
                <p>{project["description"]}</p>
                <a class="project-link"
                   href="{project["url"]}" target="_blank">
                   Explorar proyecto →
                </a>
            </div>
            """)


# --------------------------------------------------
# PROYECTOS
# --------------------------------------------------

elif section == "Proyectos":

    st.markdown('<div class="section-title">Mis proyectos</div>',
                unsafe_allow_html=True)

    st.markdown(
        '<div class="section-description">Explora las aplicaciones y desarrollos disponibles.</div>',
        unsafe_allow_html=True
    )

    categories = ["Todas las categorías"] + sorted(
        set(p["category"] for p in projects)
    )

    col1, col2 = st.columns([2, 1])

    with col1:

        search = st.text_input(
            "Buscar proyecto",
            placeholder="Escribe el nombre de un proyecto..."
        )

    with col2:

        selected_category = st.selectbox(
            "Filtrar por categoría",
            categories
        )

    filtered_projects = []

    for project in projects:

        matches_search = (
            search.lower() in project["name"].lower()
            or search.lower() in project["description"].lower()
        )

        matches_category = (
            selected_category == "Todas las categorías"
            or project["category"] == selected_category
        )

        if matches_search and matches_category:
            filtered_projects.append(project)

    st.caption(
        f"Mostrando {len(filtered_projects)} de {len(projects)} proyectos"
    )

    if filtered_projects:

        cols = st.columns(3)

        for i, project in enumerate(filtered_projects):

            with cols[i % 3]:

                render_html(f"""
                <div class="project-card">
                    <div class="project-category">
                        {project["category"]}
                    </div>

                    <h3>{project["name"]}</h3>

                    <p>{project["description"]}</p>

                    <a class="project-link"
                       href="{project["url"]}"
                       target="_blank">
                       Ver aplicación →
                    </a>
                </div>
                """)

    else:

        st.info("No se encontraron proyectos con esos criterios.")


# --------------------------------------------------
# PIE DE PÁGINA
# --------------------------------------------------

render_html("""
<div class="footer">
    Portafolio de Desarrollo de Software
    <br>
    Diseñado y desarrollado con Python y Streamlit
</div>
""")
