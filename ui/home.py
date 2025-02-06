import streamlit as st


def run_home():
    # 제목 스타일 개선
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B;">
            💍 다이아몬드 품질 및 가격 예측 개요
        </h2>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 설명 부분 스타일 개선
    st.markdown(
        """
        <p style="font-size: 18px; text-align: center;">
            과거 데이터를 분석하여 이를 토대로 새로운 다이아몬드의 품질과 가격을 예측하는 앱입니다.
        </p>
        """, 
        unsafe_allow_html=True
    )

    # 데이터 출처 강조
    st.info("📌 데이터 출처: **diamonds.csv** (Kaggle), **new_diamonds.csv** (일부 수정)")

    # EDA 및 ML 설명
    st.markdown(
        """
        ✅ **과거 데이터 확인하기**: 기존 다이아몬드 데이터 분석  
        ✅ **다이아몬드 품질 및 가격 예측하기**: 신규 다이아몬드 데이터의 예상 품질 및 가격 예측  
        ✅ **앱 정보**: 앱 기초 정보 제공
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")


    # 이미지 추가 (가운데 정렬)
    st.image("image/main_home.png")

    st.markdown("---")