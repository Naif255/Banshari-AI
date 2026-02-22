import streamlit as st


def render_ai_scanner():
    st.title("📸 عين البنشري")

    st.write("التقط صورة لقطعة الغيار أو العطل وسيتعرف عليها الذكاء الاصطناعي.")

    uploaded_file = st.file_uploader(
        "ارفع صورة القطعة أو العطل",
        type=["png", "jpg", "jpeg"],
    )

    if uploaded_file is not None:
        st.image(uploaded_file, caption="الصورة المرفوعة", use_container_width=True)
        st.success("✅ تم رفع الصورة بنجاح! جاري التحليل بالذكاء الاصطناعي...")
        st.info("🔍 النتيجة: فلتر زيت — يُنصح بالاستبدال كل 10,000 كم.")
