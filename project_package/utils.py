from project_package.naver_api import search_location
from project_package.rag_chainer import EmergencyRAGChainer
import folium
import streamlit as st

def get_chain():
   chainer = EmergencyRAGChainer(db_path='./db/chromadb_1')
   chain = chainer.create_rag_chain()

   return chain

def clean_html(raw_html):
    """Remove HTML tags from a string."""
    import re
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', raw_html)

# Show map on the sidebar
def show_map(location_query):
    location_data = search_location(location_query)
    if location_data["items"]:
        for item in location_data["items"]:
            title = clean_html(item["title"])
            address = clean_html(item["address"])
            category = item.get("category", "카테고리 정보 없음")
            roadAddress = item.get("roadAddress", "도로명 주소 정보 없음")
            link = item.get("link", "#")
            mapx = item.get("mapx")
            mapy = item.get("mapy")

            if mapx and mapy:
                # 경도 (mapx)와 위도 (mapy) 값 변환
                mapx = float(mapx) / 10000000  # 경도 (소수점 7자리로 변환)
                mapy = float(mapy) / 10000000  # 위도 (소수점 7자리로 변환)

                # Folium 지도 생성
                m = folium.Map(location=[mapy, mapx], zoom_start=15)
                folium.Marker([mapy, mapx], popup=title).add_to(m)

                # Folium 지도를 HTML로 변환하여 표시
                map_html = m._repr_html_()
                
                with st.sidebar:
                    # 병원 정보와 지도 표시
                    st.markdown(
                        f"""<div>
                        <a href="{link}" target="_blank"><b>{title}</b></a><br>
                        📍 {address}<br>
                        🪧 {roadAddress}<br>
                        👩‍⚕️ {category}<br><br>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                    # 사이드바에 HTML 지도를 표시
                    st.components.v1.html(map_html, height=250, width=400)  # 사이드바 크기 내에 지도 표시

    else:
        st.sidebar.write("위치를 찾을 수 없습니다.")