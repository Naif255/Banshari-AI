import streamlit as st


def render_dictionary():
    st.title("📖 مترجم الصناعية")

    search_query = st.text_input("🔍 ابحث عن مصطلح أو قطعة غيار...")

    if search_query:
        st.info(
            f'نتيجة البحث عن "{search_query}": لم يتم العثور على نتائج بعد. '
            "سيتم ربط القاموس بقاعدة البيانات قريبًا."
        )
    else:
        st.info("اكتب اسم القطعة بالعامية أو الإنجليزية للبحث عن ترجمتها ومعناها.")
