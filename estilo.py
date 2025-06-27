import streamlit as st

def estilo_chavoso():
  #Todo nosso estilo personalizado de CSS, que foi muito facil de fazer e nao me deu nenhuma dor de cabeça hahaha juro! (:
  
    st.markdown("""
    <style>
        .stApp {
            background-image: url('https://github.com/ofeliacarvalhow/ADOISVERSAOFINALULTRA/blob/2baf622ac142ffbd75586de9fcd2e90f6ff50a72/fundo.jpg');
            background-size: cover;
            background-attachment: fixed;
        }

        body, html, .stMarkdown, .stText, .stRadio, .stSelectbox, .stSlider, .stTextInput, .stButton,
        div[data-testid="stVerticalBlock"], div[data-testid="stHorizontalBlock"],
        div[data-testid="stBlock"] {
            color: black !important;
            background-color: transparent !important;
        }

        .stRadio > label, .stSelectbox > label, .stSlider > label, .stTextInput > label,
        .stDateInput > label, .stTimeInput > label, .stNumberInput > label {
            color: black !important;
        }

        input[type="text"], input[type="number"], textarea,
        .st-bh, .st-bo, .st-bp,
        .stTextInput > div > div > input,
        .stSelectbox div[data-baseweb="select"] div[role="button"] {
            color: black !important;
            background-color: rgba(255, 255, 255, 0.0) !important;
            border: 1px solid #444 !important;
        }

        input[type="radio"] {
            accent-color: black !important;
        }

        .stSelectbox div[data-baseweb="select"] div[role="listbox"] div[data-baseweb="option"] {
            color: black !important;
            background-color: white !important;
        }

        .stSlider .st-bg, .stSlider .st-bd {
            color: black !important;
        }

        .stRadio > div[role="radiogroup"],
        .stSelectbox > div[data-baseweb="select"] {
            background-color: transparent !important;
        }

        .stRadio div[role="radiogroup"] > div {
            background-color: transparent !important;
        }

        .stRadio div[role="radiogroup"] > div > label {
            background-color: transparent !important;
        }

        .stButton > button {
            background-color: rgba(255, 255, 255, 0.5) !important;
            color: black !important;
            border: 1px solid #444 !important;
        }

        .stBlock, .stVerticalBlock, .stHorizontalBlock {
            background-color: transparent !important;
        }

        div.stMarkdown {
            background-color: transparent !important;
        }

        .css-1cpxqw2, .css-qrbaxs, .css-1h7ebrz, .css-16idsys, .css-1xarl3l,
        .css-1wivap2, .css-1v0mbdj, .css-1g0n5qn, .css-1v0mbdj, .css-1aumxhk,
        .css-r6z25j,
        .css-1fv80k9,
        .css-1d3l2iu,
        .css-1y48h6y,
        .css-1d0lmz3,
        .css-1nm0pmu,
        .css-10y5g99,
        .css-1dp5vir {
            background-color: transparent !important;
        }

        .custom-header {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-bottom: 40px;
        }

        .custom-header h1 {
            font-size: 50px;
            margin: 0;
            text-align: center;
            color: black !important;
            background-color: transparent !important;
        }
    </style>
    """, unsafe_allow_html=True)
