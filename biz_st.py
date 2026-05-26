import streamlit as st

# 비즈니스 모델 분석
st.title("비즈니스 모델 분석")

st.markdown("[네이버](https://www.naver.com)")
st.markdown("[홍익대학교](https://www.hongik.ac.kr)")

st.write("이것이 일반 본문")

st.caption("캡션: 작고 흐린 글씨로 표현됨")

with st.echo():
    # 이 블록의 코드와 결과를 출력
    name = "Yena Kang"
    st.write("Hello, Streamlit!", name)

# 🎥 : 이미지, 오디오, 동영상

st.title("비즈니스 모델 분석")

st.markdown("### :orange[이미지: st.image()]")
st.image("파이썬 사진.webp", caption="파이썬 로고", width=500)
