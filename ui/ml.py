import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time

# 스타일 적용
st.markdown(
    """
    <style>
        .big-font { font-size:30px !important; font-weight: bold; text-align: center; }
        .sub-header { font-size:22px !important; font-weight: bold; }
        .info-box { background-color: #f0f2f6; padding: 15px; border-radius: 10px; }
        .button { font-size:18px; font-weight: bold; color: white; background-color: #ff4b4b; padding: 10px 20px; border-radius: 5px; }
    </style>
    """,
    unsafe_allow_html=True,
)

def run_ml():
    # 제목 정리
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B;">
            💍 다이아몬드 품질 및 가격 예측하기
        </h2>
        <p style="font-size: 24px; text-align: center; color: ##4C82C2;">
            <b>머신 러닝 (ML)<b>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 큰 제목
    st.markdown('<p style="font-size: 24px; font-weight: bold; color: #333; font-family: Arial, sans-serif;">💎 ML 기반 다이아몬드 가격 예측</p>', unsafe_allow_html=True)

    # 정보 박스 스타일
    st.markdown('<p style="font-size: 16px; color: #555; font-family: Arial, sans-serif; background-color: #f0f0f0; padding: 15px; border-radius: 8px; box-shadow: 0px 2px 10px rgba(0,0,0,0.1);">다이아몬드의 외관 정보를 입력하면 예상 다이아몬드 가격을 예측해드립니다.</p>', unsafe_allow_html=True)
    st.text('')

    # 하위 제목
    st.markdown('<p style="font-size: 22px; font-weight: bold; color: #333; font-family: Arial, sans-serif; border-bottom: 3px solid #4CAF50; padding-bottom: 10px;">📌 다이아몬드 정보 입력</p>', unsafe_allow_html=True)
    st.text('')

    menu_cut = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']
    menu_color = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
    menu_clarity = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

    carat = st.number_input('⚖️ 캐럿 (1캐럿 = 0.2g)', min_value=0.0, step=0.01, value=0.75)  
    
    st.subheader('')
    st.image("image/proportions.jpg", width=300)
    col1, col2, col3 = st.columns(3)
    with col1:
        x = st.number_input('📏 다이아몬드 세로 Width (mm)', min_value=0.0, step=0.01, value=5.0)
    with col2:
        y = st.number_input('📏 다이아몬드 가로 Width (mm)', min_value=0.0, step=0.01, value=5.0)
    with col3:
        z = st.number_input('📏 다이아몬드 Depth (mm)', min_value=0.0, step=0.01, value=3.0)

    table = st.number_input('📏 다이아몬드 Table (mm)', min_value=0, value=55)

    st.subheader('')
    st.image("image/brilliance-diamond-cut-chart.webp", width=500) # 커팅 퀄리티 사진
    cut = st.selectbox('🔪 다이아몬드 커팅 퀄리티', menu_cut)
    st.subheader('')
    st.image("image/color.png", width=400) # 컬러 분류 사진
    color = st.selectbox('🎨 다이아몬드 컬러', menu_color)
    st.subheader('')
    st.image("image/diamond-clarity-scale.jpg", width=400) # 투명도 분류 사진
    clarity = st.selectbox('🔍 다이아몬드 투명도', menu_clarity)

    classifier = joblib.load('model/classifier.pkl')

    cut_dict = {'Excellent':0, 'Fair':1, 'Good':2, 'Poor':3, 'Very Good':4}
    color_dict = {'D':0, 'E':1, 'F':2, 'G':3, 'H':4, 'I':5, 'J':6}
    clarity_dict = {'I1':0, 'IF':1, 'SI1':2, 'SI2':3, 'VS1':4, 'VS2':5, 'VVS1':6, 'VVS2':7}


    data_classify = np.array([carat, cut_dict[cut], color_dict[color], clarity_dict[clarity], ((x+y)/2)/z, table, z]).reshape(1, 7)
    new_data_classify = pd.DataFrame(data_classify)

    st.text('')

    if st.button('📊 품질 예측'):
        st.markdown('<p class="sub-header">🔍 예측 결과</p>', unsafe_allow_html=True)

        pred_group = classifier.predict(new_data_classify)
        
        label_group = {0:'중형', 1:'대형', 2:'소형'}[pred_group[0]]
        st.success(f'💎 의뢰하신 다이아몬드는 **{label_group}**등급이군요!')
        
        with st.spinner('⏳ 가격 예측을 실시하는 중...'):
            time.sleep(2)

            regressor = joblib.load('model/regressor.pkl')
            data_predict = np.array([carat, cut_dict[cut], color_dict[color], clarity_dict[clarity], ((x+y)/2)/z, table, z]).reshape(1, 7)

            pred_price = regressor.predict(data_predict)[0]
            pred_price = int(pred_price.round())

            if pred_price >= 0:
                new_price = format(pred_price, ',')
                st.subheader(f'💎 예상 다이아몬드 가격: **{new_price} 달러**')
            else:
                st.error('❌ 예측이 불가능한 데이터입니다.')