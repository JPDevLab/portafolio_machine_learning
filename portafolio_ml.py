
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
