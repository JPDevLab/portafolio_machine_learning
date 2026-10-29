
import streamlit as st

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

st.set_page_config(
    page_title="Portafolio Académico | Machine Learning",
    page_icon="📚",
    layout="wide"
)

# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

st.markdown("""
<style>
    .stApp {
        background-color: #f5f6f8;
        color: #252d38;
    }

    [data-testid="stHeader"] {
        background-color: #f5f6f8;
    }

    [data-testid="stSidebar"] {
        background-color: #ffffff;
    }

    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    .header-box {
        background: #ffffff;
        border: 1px solid #e1e5eb;
        border-radius: 12px;
        padding: 34px;
        margin-bottom: 28px;
    }

    .header-label {
        color: #52758a;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    .header-box h1 {
        color: #263746;
        font-size: 32px;
        margin: 12px 0;
        font-weight: 650;
    }

    .header-box p {
        color: #687582;
        font-size: 15px;
        line-height: 1.7;
        max-width: 800px;
        margin-bottom: 0;
    }

    .section-heading {
        color: #263746;
        font-size: 23px;
        font-weight: 650;
        margin-bottom: 5px;
    }

    .section-subtitle {
        color: #7a8793;
        font-size: 14px;
        margin-bottom: 20px;
    }

    .project-card {
        background: #ffffff;
        border: 1px solid #e1e5eb;
        border-radius: 11px;
        padding: 21px;
        min-height: 220px;
        margin-bottom: 16px;
        transition: border-color 0.2s ease;
    }

    .project-card:hover {
        border-color: #8ba9b8;
    }

    .category-tag {
        display: inline-block;
        background: #edf2f5;
        color: #52758a;
        padding: 5px 9px;
        border-radius: 5px;
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .project-card h3 {
        color: #293b49;
        font-size: 17px;
        font-weight: 650;
        margin-top: 16px;
        margin-bottom: 10px;
    }

    .project-card p {
        color: #727e89;
        font-size: 13px;
        line-height: 1.6;
        min-height: 62px;
    }

    .project-link {
        color: #416c83 !important;
        font-size: 13px;
        font-weight: 650;
        text-decoration: none !important;
    }

    .project-link:hover {
        color: #263746 !important;
    }

    .stats-box {
        background: #ffffff;
        border: 1px solid #e1e5eb;
        border-radius: 10px;
        padding: 18px;
        text-align: center;
    }

    .stats-number {
        font-size: 25px;
        color: #416c83;
        font-weight: 700;
    }

    .stats-label {
        font-size: 12px;
        color: #7a8793;
    }

    .footer {
        border-top: 1px solid #e1e5eb;
        margin-top: 35px;
        padding-top: 20px;
        text-align: center;
        color: #89939c;
        font-size: 12px;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PROYECTOS
# --------------------------------------------------

projects = [

    # MACHINE LEARNING

    {
        "name": "Clasificación con KNN",
        "category": "Machine Learning",
        "description": "Aplicación del algoritmo K-Nearest Neighbors para clasificar datos a partir de sus características.",
        "url": "https://appconsumohora-5lqsstytnsoxpa34guwtfh.streamlit.app/"
    },
    {
        "name": "Regresión Lineal como Predictor",
        "category": "Machine Learning",
        "description": "Aplicación de regresión lineal para estudiar relaciones entre variables y realizar predicciones.",
        "url": "https://machine-learning-hqcjanjiambod6xmlgt3k5.streamlit.app/"
    },
    {
        "name": "Agrupamiento con K-Means",
        "category": "Machine Learning",
        "description": "Implementación del algoritmo K-Means para el agrupamiento de datos.",
        "url": "https://app-evaluador-k94fosxofdexcissfcwctj.streamlit.app/"
    },
    {
        "name": "Predicción de Compra de Seguros",
        "category": "Machine Learning",
        "description": "Proyecto de predicción relacionado con la compra de seguros.",
        "url": "https://regresionlineal-fhgtaykfsuwxafazbzkvzf.streamlit.app/"
    },
    {
        "name": "Árboles de Decisión",
        "category": "Machine Learning",
        "description": "Aplicación de modelos basados en árboles de decisión.",
        "url": "https://arboldecision-aszznjqnuycnfum3smcufi.streamlit.app/"
    },
    {
        "name": "Aplicación de Consumo",
        "category": "Machine Learning",
        "description": "Proyecto relacionado con el análisis de información de consumo.",
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
        "description": "Aplicación relacionada con el análisis de datos de consumo.",
        "url": "https://appconsumores-fwxqqhuqsngudmpbv9buia.streamlit.app/"
    },

    # VISIÓN ARTIFICIAL

    {
        "name": "YOLOv5",
        "category": "Visión Artificial",
        "description": "Proyecto que utiliza YOLOv5, un modelo de detección de objetos mediante visión artificial.",
        "url": "https://yolov5-main-nnxkuybgkqwqkehafcshgn.streamlit.app/"
    },
    {
        "name": "VisionTwo",
        "category": "Visión Artificial",
        "description": "Aplicación de visión artificial. Consulta la plataforma para conocer sus funcionalidades.",
        "url": "https://visiontwo-6lrvopkubgzbbbck9g8aag.streamlit.app/"
    },
    {
        "name": "VisionComb",
        "category": "Visión Artificial",
        "description": "Proyecto de visión artificial con una sección de detección YOLO.",
        "url": "https://visioncomb-main-7tn6tu6s4j2bk7fzekqvyp.streamlit.app/YOLO"
    },
    {
        "name": "Aplicación de Reconocimiento",
        "category": "Visión Artificial",
        "description": "Proyecto de reconocimiento mediante una aplicación interactiva.",
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
        "description": "Proyecto relacionado con el procesamiento del lenguaje natural (NLP).",
        "url": "https://istmnlp-main-gp2vhfd2bkcklsbqwlaxzj.streamlit.app/"
    },
    {
        "name": "ChatPDF",
        "category": "Inteligencia Artificial",
        "description": "Aplicación para trabajar con documentos PDF mediante una interfaz conversacional.",
        "url": "https://chatpdf-3uxzbbzwwh9k4ay4njlq3v.streamlit.app/"
    },
    {
        "name": "Arquitectura de Redes Neuronales",
        "category": "Inteligencia Artificial",
        "description": "Proyecto relacionado con la arquitectura y estructura de redes neuronales.",
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
        "description": "Implementación de una aplicación web con navegación entre diferentes páginas.",
        "url": "https://multipagina-fyavpc5df95wwhkw4bmhsr.streamlit.app/"
    },

    # OTROS PROYECTOS

    {
        "name": "IMM1",
        "category": "Otros proyectos",
        "description": "Proyecto académico publicado mediante Streamlit.",
        "url": "https://imm1-main-fmmeyteyrpye2wc8yjfguf.streamlit.app/"
    },
    {
        "name": "Proyecto Q75",
        "category": "Otros proyectos",
        "description": "Aplicación académica disponible en Streamlit.",
        "url": "https://q75peszknjzqscgceqithx.streamlit.app/"
    }

]


# --------------------------------------------------
# ENCABEZADO
# --------------------------------------------------

st.markdown("""
<div class="header-box">

    <div class="header-label">
        COLECCIÓN DE PROYECTOS ACADÉMICOS
    </div>

    <h1>Portafolio de Aplicaciones Tecnológicas</h1>

    <p>
        Espacio dedicado a recopilar y presentar diferentes proyectos
        académicos relacionados con Machine Learning, inteligencia
        artificial, visión artificial y desarrollo de software.
        Cada sección contiene aplicaciones y ejercicios prácticos
        desarrollados durante el proceso de aprendizaje.
    </p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ESTADÍSTICAS
# --------------------------------------------------

categories = [
    "Machine Learning",
    "Visión Artificial",
    "Inteligencia Artificial",
    "Desarrollo de Software",
    "Otros proyectos"
]

stat_cols = st.columns(3)

stats = [
    (len(projects), "Proyectos registrados"),
    (len(categories), "Áreas de trabajo"),
    (len(set(p["url"] for p in projects)), "Aplicaciones diferentes")
]

for col, (number, label) in zip(stat_cols, stats):

    with col:

        st.markdown(f"""
        <div class="stats-box">
            <div class="stats-number">{number}</div>
            <div class="stats-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# --------------------------------------------------
# CATÁLOGO DE PROYECTOS
# --------------------------------------------------

st.markdown(
    '<div class="section-heading">Catálogo de proyectos</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Consulta las aplicaciones disponibles y accede a cada proyecto.'
    '</div>',
    unsafe_allow_html=True
)


# BUSCADOR Y FILTROS

col1, col2 = st.columns([2, 1])

with col1:

    search = st.text_input(
        "Buscar",
        placeholder="Buscar por nombre o descripción...",
        label_visibility="visible"
    )

with col2:

    selected_category = st.selectbox(
        "Categoría",
        ["Todas"] + categories
    )


# FILTRAR PROYECTOS

filtered_projects = []

for project in projects:

    matches_search = (
        search.lower() in project["name"].lower()
        or search.lower() in project["description"].lower()
    )

    matches_category = (
        selected_category == "Todas"
        or project["category"] == selected_category
    )

    if matches_search and matches_category:
        filtered_projects.append(project)


st.markdown(
    f"**{len(filtered_projects)} proyectos encontrados**"
)

st.markdown("<br>", unsafe_allow_html=True)


# MOSTRAR TARJETAS

if filtered_projects:

    cols = st.columns(3)

    for index, project in enumerate(filtered_projects):

        with cols[index % 3]:

            st.markdown(f"""
            <div class="project-card">

                <span class="category-tag">
                    {project["category"]}
                </span>

                <h3>{project["name"]}</h3>

                <p>{project["description"]}</p>

                <a class="project-link"
                   href="{project["url"]}"
                   target="_blank">
                   Abrir aplicación ↗
                </a>

            </div>
            """, unsafe_allow_html=True)

else:

    st.info("No se encontraron proyectos con esos criterios.")


# --------------------------------------------------
# PIE DE PÁGINA
# --------------------------------------------------

st.markdown("""
<div class="footer">
    Portafolio académico de aplicaciones tecnológicas
    <br>
    Desarrollado con Python y Streamlit
</div>
""", unsafe_allow_html=True)
