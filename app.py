import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="بنشري الجوال", page_icon="🚗", layout="centered")

# Hide default Streamlit UI elements for native mobile app feel
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* RTL support */
    .main .block-container {
        direction: rtl;
        text-align: right;
    }

    /* Bottom navigation styling */
    .stHorizontalBlock {
        direction: ltr;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Bottom navigation menu
selected = option_menu(
    menu_title=None,
    options=["الرئيسية", "عين البنشري", "السجل", "المترجم"],
    icons=["house", "camera", "journal-text", "book"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#262730"},
        "icon": {"color": "#fafafa", "font-size": "18px"},
        "nav-link": {
            "font-size": "14px",
            "text-align": "center",
            "margin": "0px",
            "color": "#fafafa",
        },
        "nav-link-selected": {"background-color": "#ff4b4b"},
    },
)

# Dynamic routing based on selected menu item
if selected == "الرئيسية":
    from components.dashboard import render_dashboard

    render_dashboard()
elif selected == "عين البنشري":
    from components.ai_scanner import render_ai_scanner

    render_ai_scanner()
elif selected == "السجل":
    from components.logbook import render_logbook

    render_logbook()
elif selected == "المترجم":
    from components.dictionary import render_dictionary

    render_dictionary()
