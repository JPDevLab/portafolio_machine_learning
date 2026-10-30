
import streamlit as st
from pathlib import Path

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="Portafolio Académico",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# PROYECTOS
# =====================================================

projects = [

    {
        "name": "Clasificación con KNN",
        "category": "Machine Learning",
        "description": "Clasificación de datos mediante el algoritmo K-Nearest Neighbors.",
        "url": "https://appconsumohora-5lqsstytnsoxpa34guwtfh.streamlit.app/"
    },
    {
        "name": "Regresión Lineal",
        "category": "Machine Learning",
        "description": "Modelo de regresión lineal para analizar relaciones entre variables y realizar predicciones.",
        "url": "https://machine-learning-hqcjanjiambod6xmlgt3k5.streamlit.app/"
    },
    {
        "name": "Agrupamiento con K-Means",
        "category": "Machine Learning",
        "description": "Agrupamiento de datos mediante técnicas de aprendizaje no supervisado.",
        "url": "https://app-evaluador-k94fosxofdexcissfcwctj.streamlit.app/"
    },
    {
        "name": "Predicción de Compra de Seguros",
        "category": "Machine Learning",
        "description": "Aplicación de modelos predictivos relacionados con la compra de seguros.",
        "url": "https://regresionlineal-fhgtaykfsuwxafazbzkvzf.streamlit.app/"
    },
    {
        "name": "Árboles de Decisión",
        "category": "Machine Learning",
        "description": "Clasificación y análisis mediante modelos basados en árboles de decisión.",
        "url": "https://arboldecision-aszznjqnuycnfum3smcufi.streamlit.app/"
    },
    {
        "name": "Aplicación de Consumo",
        "category": "Machine Learning",
        "description": "Aplicación relacionada con el análisis de información de consumo.",
        "url": "https://appappconsumo-djqrsp7zpehhavfucerufm.streamlit.app/"
    },
    {
        "name": "Neuronas vs Regresión",
        "category": "Machine Learning",
        "description": "Exploración de modelos neuronales y técnicas de regresión.",
        "url": "https://appneuronavsregresion-k4foox2xvfgzpw3wjft8yp.streamlit.app/"
    },
    {
        "name": "Análisis de Consumo",
        "category": "Machine Learning",
        "description": "Procesamiento y análisis de datos relacionados con el consumo.",
        "url": "https://appconsumores-fwxqqhuqsngudmpbv9buia.streamlit.app/"
    },
    {
        "name": "YOLOv5",
        "category": "Visión Artificial",
        "description": "Detección de objetos utilizando el modelo de visión artificial YOLOv5.",
        "url": "https://yolov5-main-nnxkuybgkqwqkehafcshgn.streamlit.app/"
    },
    {
        "name": "VisionTwo",
        "category": "Visión Artificial",
        "description": "Aplicación académica relacionada con el procesamiento visual.",
        "url": "https://visiontwo-6lrvopkubgzbbbck9g8aag.streamlit.app/"
    },
    {
        "name": "VisionComb",
        "category": "Visión Artificial",
        "description": "Proyecto de visión artificial con una sección dedicada a YOLO.",
        "url": "https://visioncomb-main-7tn6tu6s4j2bk7fzekqvyp.streamlit.app/YOLO"
    },
    {
        "name": "Reconocimiento",
        "category": "Visión Artificial",
        "description": "Aplicación académica relacionada con el reconocimiento visual.",
        "url": "https://app-rec-gxfnqppuvkccstw8youa5z.streamlit.app/"
    },
    {
        "name": "Traductor",
        "category": "Inteligencia Artificial",
        "description": "Aplicación interactiva para la traducción de textos.",
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
        "description": "Aplicación para consultar e interactuar con documentos PDF.",
        "url": "https://chatpdf-3uxzbbzwwh9k4ay4njlq3v.streamlit.app/"
    },
    {
        "name": "Redes Neuronales",
        "category": "Inteligencia Artificial",
        "description": "Exploración de arquitecturas y estructuras de redes neuronales.",
        "url": "https://arquitecturaredesneuronales-r27vcyn7gsruj3vx88gpkz.streamlit.app/"
    },
    {
        "name": "TM",
        "category": "Desarrollo de Software",
        "description": "Aplicación académica desarrollada con Streamlit.",
        "url": "https://tm-main-fy5tmmwwgue2bgqkc2wjms.streamlit.app/"
    },
    {
        "name": "Aplicación Multipágina",
        "category": "Desarrollo de Software",
        "description": "Aplicación web organizada mediante diferentes páginas.",
        "url": "https://multipagina-fyavpc5df95wwhkw4bmhsr.streamlit.app/"
    },
    {
        "name": "IMM1",
        "category": "Otros proyectos",
        "description": "Proyecto académico publicado mediante Streamlit.",
        "url": "https://imm1-main-fmmeyteyrpye2wc8yjfguf.streamlit.app/"
    },
    {
        "name": "Proyecto Q75",
        "category": "Otros proyectos",
        "description": "Aplicación académica desplegada mediante Streamlit.",
        "url": "https://q75peszknjzqscgceqithx.streamlit.app/"
    }
]

# =====================================================
# CATEGORÍAS
# =====================================================

categories = [
    "Todas",
    "Machine Learning",
    "Visión Artificial",
    "Inteligencia Artificial",
    "Desarrollo de Software",
    "Otros proyectos"
]

# =====================================================
# PORTADA
# =====================================================

with st.container(border=True):

    st.caption("COLECCIÓN DE PROYECTOS ACADÉMICOS")

    left, right = st.columns([2.2, 1])

    with left:

        st.title("Tecnología aplicada al aprendizaje.")

        st.write(
            "Un espacio dedicado a recopilar y presentar "
            "aplicaciones, experimentos y proyectos prácticos "
            "desarrollados en diferentes áreas de la computación."
        )

        st.write("")

        st.button(
            "Explorar proyectos ↓",
            type="primary",
            use_container_width=False,
            on_click=lambda: st.session_state.update(
                {"show_catalog": True}
            )
        )

    with right:

        st.markdown("### Áreas de trabajo")

        st.write("01 · Machine Learning")
        st.write("02 · Visión Artificial")
        st.write("03 · Inteligencia Artificial")
        st.write("04 · Desarrollo de Software")

# =====================================================
# INDICADORES
# =====================================================

st.write("")

total_projects = len(projects)
total_categories = len(set(p["category"] for p in projects))
total_apps = len(set(p["url"] for p in projects))

c1, c2, c3 = st.columns(3)

c1.metric("Proyectos", total_projects)
c2.metric("Categorías", total_categories)
c3.metric("Aplicaciones", total_apps)

st.divider()

# =====================================================
# PROYECTOS DESTACADOS
# =====================================================

st.subheader("Proyectos destacados")

st.caption(
    "Una selección de aplicaciones disponibles para explorar."
)

featured = [
    {
        "name": "Clasificación con KNN",
        "description": "Clasificación de datos mediante K-Nearest Neighbors.",
        "url": projects[0]["url"],
        "image": "knn.png"
    },
    {
        "name": "Árboles de Decisión",
        "description": "Modelos de clasificación basados en árboles de decisión.",
        "url": projects[4]["url"],
        "image": "ArbolesDecision.png"
    }
]

featured_cols = st.columns(2, gap="large")

for col, item in zip(featured_cols, featured):

    with col:

        with st.container(border=True):

            image_path = Path(item["image"])

            if image_path.exists():
                st.image(str(image_path), use_container_width=True)

            st.caption("PROYECTO DESTACADO")
            st.subheader(item["name"])
            st.write(item["description"])

            st.link_button(
                "Explorar aplicación ↗",
                item["url"],
                use_container_width=True
            )

st.divider()

# =====================================================
# CATÁLOGO
# =====================================================

st.subheader("Explorar catálogo")

st.caption(
    "Encuentra los proyectos según su nombre, descripción o categoría."
)

search_col, category_col = st.columns([1.7, 1])

with search_col:

    search = st.text_input(
        "Buscar proyecto",
        placeholder="Ej. YOLOv5, regresión, redes neuronales...",
        label_visibility="collapsed"
    )

with category_col:

    selected_category = st.selectbox(
        "Categoría",
        categories,
        label_visibility="collapsed"
    )

# =====================================================
# FILTROS
# =====================================================

filtered_projects = []

for project in projects:

    search_text = search.strip().lower()

    matches_search = (
        search_text in project["name"].lower()
        or search_text in project["description"].lower()
    )

    matches_category = (
        selected_category == "Todas"
        or project["category"] == selected_category
    )

    if matches_search and matches_category:
        filtered_projects.append(project)

st.write(
    f"**{len(filtered_projects)} resultados**"
)

# =====================================================
# TARJETAS
# =====================================================

if filtered_projects:

    cols = st.columns(3, gap="large")

    for index, project in enumerate(filtered_projects):

        with cols[index % 3]:

            with st.container(border=True):

                st.caption(project["category"].upper())

                st.markdown(f"#### {project['name']}")

                st.write(project["description"])

                st.link_button(
                    "Ver aplicación ↗",
                    project["url"],
                    use_container_width=True
                )

else:

    st.info(
        "No encontramos proyectos con esos criterios. "
        "Prueba con otro término o categoría."
    )

# =====================================================
# PIE DE PÁGINA
# =====================================================

st.divider()

footer_left, footer_right = st.columns(2)

with footer_left:
    st.caption("PORTAFOLIO ACADÉMICO · PROYECTOS TECNOLÓGICOS")

with footer_right:
    st.caption("Desarrollado con Python y Streamlit")
