import requests
import streamlit as st
from resource.config import naver_client_id, naver_client_secret

def search_location(query):
    """Search location using Naver API."""
    url = "https://openapi.naver.com/v1/search/local.json"
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret,
    }
    params = {"query": query, "display": 5}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()  
    else:
        st.sidebar.error("네이버 API 요청 실패.")
        return {"items": []}
