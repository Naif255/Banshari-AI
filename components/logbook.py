import streamlit as st
import pandas as pd


def render_logbook():
    st.title("📋 سجل المصاريف والصيانة")

    data = pd.DataFrame(
        {
            "التاريخ": ["2026-02-15", "2026-02-03", "2026-01-20"],
            "نوع الصيانة": ["تغيير زيت المحرك", "فحص الفرامل", "تبديل فلتر الهواء"],
            "التكلفة (ر.س)": [150, 200, 150],
        }
    )

    st.dataframe(data, use_container_width=True, hide_index=True)
