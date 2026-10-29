
import streamlit as st

# ==================================================
# CONFIGURACIÓN
# ==================================================

st.set_page_config(
    page_title="Portafolio Académico",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# ESTILOS
# ==================================================

st.markdown("""
<style>
    .stApp {
        background-color: #F4F6F8;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #263746;
    }

    p, label {
        color: #596875;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF;
        border-color: #E1E6EB !important;
        border-radius: 12px !important;
    }

    [data-testid="stTextInput"] input,
    [data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        background-color: #FFFFFF;
        border-color: #D8E0E6;
        border-radius: 8px;
        color: #263746;
    }

    [data-testid="stTextInput"] input:focus {
        border-color: #52788C;
        box-shadow: 0 0 0 1px #52788C;
    }

    [data-testid="stLinkButton"] a {
        background-color: #456B7C;
        color: #FFFFFF !important;
        border: 1px solid #456B7C;
        border-radius: 7px;
        font-weight: 600;
        text-decoration: none;
        transition: background-color 0.2s;
    }

    [data-testid="stLinkButton"] a:hover {
        background-color: #345363;
        border-color: #345363;
        color: #FFFFFF !important;
    }

    .header-label {
        color: #52788C;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    .header-description {
        color: #687784;
        font-size: 15px;
        line-height: 1.7;
        max-width: 800px;
    }

    .category-label {
        color: #52788C;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.8px;
        text-transform: uppercase;
    }

    .project-description {
        color: #687784;
        font-size: 13px;
        line-height: 1.6;
        min-height: 65px;
    }

    hr {
        border-color: #E1E6EB;
    }

    @media (max-width: 640px) {
        .block-container {
            padding-top: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)


# ==================================================
# BASE DE PROYECTOS
# ==================================================

projects = [

    # MACHINE LEARNING

    {
        "name": "Clasificación con KNN",
        "category": "Machine Learning",
        "description": "Aplicación del algoritmo K-Nearest Neighbors para la clasificación de datos.",
        "url": "https://appconsumohora-5lqsstytnsoxpa34guwtfh.streamlit.app/"
    },
    {
        "name": "Regresión Lineal como Predictor",
        "category": "Machine Learning",
        "description": "Implementación de regresión lineal para analizar relaciones entre variables y realizar predicciones.",
        "url": "https://machine-learning-hqcjanjiambod6xmlgt3k5.streamlit.app/"
    },
    {
        "name": "Agrupamiento con K-Means",
        "category": "Machine Learning",
        "description": "Aplicación del algoritmo K-Means para agrupar datos según sus características.",
        "url": "https://app-evaluador-k94fosxofdexcissfcwctj.streamlit.app/"
    },
    {
        "name": "Predictor de Compra de Seguros",
        "category": "Machine Learning",
        "description": "Aplicación de un modelo predictivo relacionado con la compra de seguros.",
        "url": "https://regresionlineal-fhgtaykfsuwxafazbzkvzf.streamlit.app/"
    },
    {
        "name": "Árboles de Decisión",
        "category": "Machine Learning",
        "description": "Implementación de modelos de clasificación mediante árboles de decisión.",
        "url": "https://arboldecision-aszznjqnuycnfum3smcufi.streamlit.app/"
    },
    {
        "name": "Aplicación de Consumo",
        "category": "Machine Learning",
        "description": "Proyecto relacionado con el análisis de datos de consumo.",
        "url": "https://appappconsumo-djqrsp7zpehhavfucerufm.streamlit.app/"
    },
    {
        "name": "Neuronas vs Regresión",
        "category": "Machine Learning",
        "description": "Proyecto que aborda modelos neuronales y técnicas de regresión.",
        "url": "https://appneuronavsregresion-k4foox2xvfgzpw3wjft8yp.streamlit.app/"
    },
    {
        "name": "Análisis de Consumo",
        "category": "Machine Learning",
        "description": "Aplicación relacionada con el procesamiento y análisis de datos de consumo.",
        "url": "https://appconsumores-fwxqqhuqsngudmpbv9buia.streamlit.app/"
    },

    # VISIÓN ARTIFICIAL

    {
        "name": "YOLOv5",
        "category": "Visión Artificial",
        "description": "Proyecto de detección de objetos utilizando el modelo YOLOv5.",
        "url": "https://yolov5-main-nnxkuybgkqwqkehafcshgn.streamlit.app/"
    },
    {
        "name": "VisionTwo",
        "category": "Visión Artificial",
        "description": "Aplicación académica de visión artificial.",
        "url": "https://visiontwo-6lrvopkubgzbbbck9g8aag.streamlit.app/"
    },
    {
        "name": "VisionComb",
        "category": "Visión Artificial",
        "description": "Proyecto de visión artificial con una sección dedicada a YOLO.",
        "url": "https://visioncomb-main-7tn6tu6s4j2bk7fzekqvyp.streamlit.app/YOLO"
    },
    {
        "name": "Aplicación de Reconocimiento",
        "category": "Visión Artificial",
        "description": "Aplicación académica relacionada con reconocimiento y procesamiento visual.",
        "url": "https://app-rec-gxfnqppuvkccstw8youa5z.streamlit.app/"
    },

    # INTELIGENCIA ARTIFICIAL

    {
        "name": "Traductor",
        "category": "Inteligencia Artificial",
        "description": "Aplicación de traducción de textos.",
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
        "description": "Aplicación para interactuar con documentos PDF.",
        "url": "https://chatpdf-3uxzbbzwwh9k4ay4njlq3v.streamlit.app/"
    },
    {
        "name": "Arquitectura de Redes Neuronales",
        "category": "Inteligencia Artificial",
        "description": "Proyecto relacionado con la estructura y arquitectura de redes neuronales.",
        "url": "https://arquitecturaredesneuronales-r27vcyn7gsruj3vx88gpkz.streamlit.app/"
    },

    # DESARROLLO DE SOFTWARE

    {
        "name": "TM",
        "category": "Desarrollo de Software",
        "description": "Aplicación académica desarrollada con Streamlit.",
        "url": "https://tm-main-fy5tmmwwgue2bgqkc2wjms.streamlit.app/"
    },
    {
        "name": "Aplicación Multipágina",
        "category": "Desarrollo de Software",
        "description": "Aplicación web con navegación entre diferentes páginas.",
        "url": "https://multipagina-fyavpc5df95wwhkw4bmhsr.streamlit.app/"
    },

    # OTROS

    {
        "name": "IMM1",
        "category": "Otros proyectos",
        "description": "Aplicación académica publicada mediante Streamlit.",
        "url": "https://imm1-main-fmmeyteyrpye2wc8yjfguf.streamlit.app/"
    },
    {
        "name": "Proyecto Q75",
        "category": "Otros proyectos",
        "description": "Proyecto académico desplegado en Streamlit.",
        "url": "https://q75peszknjzqscgceqithx.streamlit.app/"
    }
]


# ==================================================
# ENCABEZADO
# ==================================================

st.markdown(
    '<div class="header-label">PORTAFOLIO ACADÉMICO</div>',
    unsafe_allow_html=True
)

st.title("Aplicaciones y proyectos tecnológicos")

st.markdown(
    """
    <p class="header-description">
        Recopilación de proyectos y aplicaciones prácticas desarrolladas
        en diferentes áreas de la tecnología, incluyendo Machine Learning,
        inteligencia artificial, visión artificial y desarrollo de software.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()


# ==================================================
# BUSCADOR Y FILTROS
# ==================================================

st.subheader("Catálogo de proyectos")

st.caption(
    "Consulta las aplicaciones disponibles y accede a cada proyecto."
)

categories = [
    "Todas",
    "Machine Learning",
    "Visión Artificial",
    "Inteligencia Artificial",
    "Desarrollo de Software",
    "Otros proyectos"
]

col_search, col_category = st.columns([2, 1])

with col_search:
    search = st.text_input(
        "Buscar",
        placeholder="Buscar por nombre o descripción...",
        key="project_search"
    )

with col_category:
    selected_category = st.selectbox(
        "Categoría",
        categories
    )


# ==================================================
# FILTRADO
# ==================================================

filtered_projects = []

for project in projects:

    matches_search = (
        search.strip().lower() in project["name"].lower()
        or search.strip().lower() in project["description"].lower()
    )

    matches_category = (
        selected_category == "Todas"
        or project["category"] == selected_category
    )

    if matches_search and matches_category:
        filtered_projects.append(project)


st.write(f"**{len(filtered_projects)} proyectos encontrados**")

st.write("")


# ==================================================
# TARJETAS DE PROYECTOS
# ==================================================

if filtered_projects:

    columns = st.columns(3, gap="medium")

    for index, project in enumerate(filtered_projects):

        with columns[index % 3]:

            with st.container(border=True):

                st.markdown(
                    f'<div class="category-label">{project["category"]}</div>',
                    unsafe_allow_html=True
                )

                st.subheader(project["name"])

                st.markdown(
                    f'<div class="project-description">{project["description"]}</div>',
                    unsafe_allow_html=True
                )

                st.link_button(
                    "Abrir aplicación ↗",
                    project["url"],
                    use_container_width=True
                )

else:

    st.info(
        "No se encontraron proyectos. "
        "Intenta con otro nombre o selecciona otra categoría."
    )


# ==================================================
# PIE DE PÁGINA
# ==================================================

st.divider()

st.caption(
    "Portafolio académico | Aplicaciones desarrolladas con Python y Streamlit"
)
