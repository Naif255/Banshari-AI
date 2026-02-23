import streamlit as st
import google.generativeai as genai
from PIL import Image


def render_ai_scanner():
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    except Exception:
        st.error("مفتاح الذكاء الاصطناعي مفقود.")
        return

    st.title("📸 عين البنشري")

    uploaded_file = st.file_uploader(
        "ارفع صورة القطعة أو العطل",
        type=['png', 'jpg', 'jpeg'],
    )

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, use_container_width=True)

        if st.button("افحص السيارة"):
            with st.spinner("جاري فحص القطعة بالذكاء الاصطناعي..."):
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content([
                    "أنت مهندس ميكانيكا سيارات محترف في السعودية. قم بتحليل هذه الصورة بدقة. "
                    "1. ما هو اسم القطعة أو الرمز؟ "
                    "2. هل يوجد بها تلف أو مشكلة واضحة؟ "
                    "3. أعطني نصيحة عملية وسريعة باللغة العربية العامية المبسطة.",
                    img,
                ])
                st.success(response.text)
