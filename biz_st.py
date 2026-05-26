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

st.markdown("# :blue[데이터 테이블]")

st.markdown("### :orange[Pandas 데이터프레임]")

import pandas as pd

df = pd.DataFrame(
    {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [24, 34, 45]
    }
)

st.dataframe(df)

st.markdown("### :orange[지표(Metric)]")

col1, col2, col3 = st.columns(3)

col1.metric("Temperature", "70 °F", "1.2 °F")
col1.wirte("이것은 온도 지표입니다.")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.markdown("""
| 이름 | 학번 | 학과 |
|------|------|------|
| 홍길동 | 20230001 | 컴퓨터공학과 |
| 김철수 | 20230002 | 전자공학과 |
| 이영희 | 20230003 | 기계공학과 |
""")
