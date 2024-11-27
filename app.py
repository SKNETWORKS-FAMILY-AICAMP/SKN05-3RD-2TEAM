import streamlit as st
from langchain.callbacks import get_openai_callback
from project_package.utils import show_map, get_chain


chain = get_chain()

# Streamlit UI 구현
def main():
    st.set_page_config(page_title="SKNETWORKS-FAMILY-AICAMP/SKN05-3rd-2Team", layout="wide")  # Set layout to wide

    if "conversation" not in st.session_state:
        st.session_state.conversation = []  
    if "documents" not in st.session_state:
        st.session_state.documents = None  
    
    # Sidebar: Location Search Feature
    st.sidebar.title("📍 위치 검색")
    location_query = st.sidebar.text_input("병원 위치를 입력하세요:")

    # 링크 CSS 바꾸기
    st.sidebar.markdown(
        """
        <style>
        a {
            color: #1ABC9C !important; 
            text-decoration: none;     /* 밑줄 제거 (필요하면 제거 가능) */
        }
        a:hover {
            text-decoration: underline; /* 링크에 마우스 올렸을 때 밑줄 추가 */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if st.sidebar.button("검색"):
        if location_query:
            show_map(location_query)

    # Main Chat Interface
    # Center-align title and description using HTML and CSS
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>🚨 응급처치 대응 매뉴얼 / 병원 조회 서비스 🚨</h1>
            <p><b>SKN05-3rd-2Team</b></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

    # Display conversation history
    for q, a in st.session_state.conversation:
        with st.chat_message("user"):
            st.write(q)
        with st.chat_message("assistant"):
            st.write(a)
    
    # Input box for new questions
    query = st.chat_input("질문을 입력하세요...")
    if query:
        with st.chat_message("user"):
            st.write(query)

        # Process the question and generate a response
        with st.spinner("답변을 생성 중입니다..."):

            with get_openai_callback() as cost:
                response = chain.stream(query)
                with st.chat_message("assistant"):
                    st.write(response)

                response_history = ""
                for token in chain.stream(query):
                    response_history += token

                st.session_state.conversation.append((query, response_history))

if __name__ == "__main__":
    main()