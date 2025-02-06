import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os
from matplotlib import rc

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd()]
    font_files = fm.findSystemFonts(fontpaths=font_dirs)
    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)

plt.rcParams['axes.unicode_minus'] = False
system_os = platform.system()
if system_os == "Darwin":  # macOS
    font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
elif system_os == "Windows":  # Windows
    font_path = "C:/Windows/Fonts/malgun.ttf"
else:  # Linux
    rc('font', family='NanumGothic')

def run_eda():
    fontRegistered()
    plt.rc('font', family='NanumGothic')

    # 제목 정리
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B;">
            📊 과거 데이터 확인하기
        </h2>
        <p style="font-size: 24px; text-align: center; color: ##4C82C2;">
            <b>탐색적 데이터 분석 (EDA)<b>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 데이터 불러오기
    st.info("📌 **축적된 과거 데이터** (new_diamonds.csv)")
    df = pd.read_csv("data/new_diamonds.csv")
    df["type"].replace([0, 1, 2], ['중형', '대형', '소형'], inplace=True)
    
    # 데이터프레임 출력
    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    # 기본 통계 데이터 버튼
    if st.button("📈 기본 통계 데이터 보기"):
        st.dataframe(df.describe())

    st.markdown("---")

    # 최대/최소 데이터 확인
    st.info("📌 **최대/최소 데이터 확인하기**")

    menu2 = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
    selected_column = st.selectbox("📌 비교할 컬럼 선택", menu2)

    # 최댓값 데이터
    st.markdown("✅ **최댓값 데이터**")
    st.dataframe(df.loc[df[selected_column] == df[selected_column].max(), :])

    # 최솟값 데이터
    st.markdown("✅ **최솟값 데이터**")
    st.dataframe(df.loc[df[selected_column] == df[selected_column].min(), :])

    st.markdown("---")

    st.info("🔪 **커팅 퀄리티별 평균 다이아몬드 가격 분석**")
    df_yearly = df.groupby("cut")["price"].mean()
    fig1 = plt.figure()
    df_yearly.plot(kind="bar", figsize=(10, 5), color="skyblue")
    plt.ylabel("다이아몬드 가격 ($)")
    plt.xlabel("커팅 퀄리티")
    plt.xticks(rotation=0)
    plt.title("커팅 퀄리티별 다이아몬드 평균 가격")
    st.pyplot(fig1)

    st.markdown("---")

    st.info("🎨 **컬러별 평균 다이아몬드 가격 비교**")
    df_genre = df.groupby("color")["price"].mean().sort_values()
    fig2 = plt.figure()
    df_genre.plot(kind="barh", figsize=(10, 5), color="lightcoral")
    plt.xlabel("다이아몬드 가격 ($)")
    plt.ylabel("컬러")
    plt.title("컬러별 다이아몬드 평균 가격")
    st.pyplot(fig2)

    st.markdown("---")

    st.info("🔍 **투명도별 평균 다이아몬드 가격 비교**")
    df_mpaa = df.groupby("clarity")["price"].mean().sort_values()
    fig3 = plt.figure()
    df_mpaa.plot(kind="barh", figsize=(8, 5), color="lightgreen")
    plt.xlabel("다이아몬드 가격 ($)")
    plt.ylabel("투명도")
    plt.xticks(rotation = 0)
    plt.title("투명도별 다이아몬드 평균 가격")
    st.pyplot(fig3)

    st.markdown("---")