import streamlit as st
import re

def main():
    st.set_page_config(page_title="Text Analyzer",page_icon="🖹", layout="centered")

    st.markdown("""
        <style>
                .main{ background-color: #ebeced;}
                .stTextArea, .stTextInput { border-radius: 10px;}
                .stButton>button { background-color: blue; color: white; border-radius: 10px; padding: 10px}
        </style>
                         
    """, unsafe_allow_html=True)

    st.title("Text Analyzer in python")
    st.write("Analyzer your text quickly and efficiently.")

    paragraph = st.text_area("✍🏽 Enter a paragraph: ", "", height=150)

    if paragraph:
        st.markdown("---")
        st.subheader("📌Analyzer Results")

        words = paragraph.split()
        word_count = len(words)
        char_count = len(paragraph)
        col1, col2 = st.columns(2)
        col1.metric(" 🖹 Total words", word_count)
        col2.metric(" 🀇 Total Charaters", char_count)

        #search replace filter feature
        st.subheader("Serach and Replace")
        search_word = st.text_input("Enter a word to search:")
        replace_word = st.text_input("Enter a word to replace with:")

        if search_word and replace_word:
            modified_paragraph = re.sub(rf'\b{re.escape(search_word)}\b', replace_word, paragraph)
            st.success("Modified Paragraph")

        #uppercase and lowercase 
        st.subheader("🌟Uppercase and Lowear case feature")
        st.text_area("UPPERCASE;", paragraph.upper(), height=150)
        st.text_area("LOWERCASE;", paragraph.lower(), height=150)


        ope_python = "Python" in paragraph
        st.write(f"✔️ Contain 'Python': {ope_python}")
        
        #vaerage length of paragraph:
        average_word_length = char_count / word_count if word_count else 0
        st.write(f"📏 Average word Length:{average_word_length}")

    else:
        st.warning("☢️ Please enter a paragraph for analyzation.")

if __name__ == "__main__":
    main()




    
        
                                        





     