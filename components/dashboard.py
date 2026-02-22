import streamlit as st


def render_dashboard():
    st.title("🏠 الرئيسية")

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="مصاريف هذا الشهر", value="500 ر.س", delta="-50 ر.س")
    with col2:
        st.metric(label="عدد الصيانات", value="3", delta="1")

    st.divider()

    st.subheader("آخر الصيانات")
    st.info("🔧 تغيير زيت المحرك — 15/02/2026")
    st.info("🔧 فحص الفرامل — 03/02/2026")
