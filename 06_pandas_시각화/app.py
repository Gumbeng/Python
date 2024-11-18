import streamlit as st
import numpy as np
from gym_ui.model import DropoutModel
from gym_ui.deep_learning import deep_learning, machine_learning_best_xgb, machine_learning_best_gb ,machine_learning_best_rf
from PIL import Image

image_path_1 = "image/노이탈(헬스)2.webp"
image_path_2 = "image/노이탈(헬스).webp"
image_path_3 = "image/이탈자(헬스).webp"
image_1 = Image.open(image_path_1)
image_2 = Image.open(image_path_2)
image_3 = Image.open(image_path_3)

st.title(':muscle: 헬스장 계약 종료 예측 :running:')
st.sidebar.header('입력 정보')
st.divider()


gender = st.sidebar.selectbox('성별', options=["남자", "여자"])
near_Location = st.sidebar.selectbox('집 근처 여부', options=["O", "X"])
partner = st.sidebar.selectbox('회사 소개 여부', options=["O", "X"])
promo_friends = st.sidebar.selectbox('친구 소개 여부', options=["O", "X"])
contract_period = st.sidebar.selectbox('계약기간', options=[1, 6, 12])
Group_visits = st.sidebar.selectbox('단체 여부',  options=["O", "X"])
age = st.sidebar.number_input('나이', min_value=18, max_value=120, value=30)
avg_additional_charges_total = st.sidebar.slider('월 평균 추가 비용$', 0.001, 800.00)

lifetime = st.sidebar.number_input('(월기준)다닌날', min_value=0, value=0)
avg_class_frequency_total = st.sidebar.slider('월 평균 수업 참여 횟수', 0.001, 7.00)

gender = 0 if gender == "남자" else 1
near_Location = 0 if near_Location == "X" else 1
partner = 0 if partner == "X" else 1
promo_friends = 0 if promo_friends == "X" else 1
Group_visits = 0 if Group_visits == "X" else 1

input_data = np.array([[
    gender,
    near_Location,
    partner,
    promo_friends,
    contract_period,
    Group_visits,
    age,
    avg_additional_charges_total,
    # month_to_end_contract,
    lifetime,
    avg_class_frequency_total,
    # avg_class_frequency_current_month,
    ]])

deep_button = st.sidebar.button("딥러닝 모델로 예측")
machine_button = st.sidebar.button("머신러닝 모델로 예측")
if deep_button:
    result = deep_learning(input_data)  
    churn_probability = result  
    isTrue = churn_probability >= 0.5
    images = image_3 if isTrue else image_1
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header('예측 결과')
        st.subheader(f"예측결과: {'이탈' if isTrue else '노이탈'}")
        st.subheader(f'이탈 확률: {churn_probability * 100:.2f}%')
        st.subheader(f"{'이탈 가능성 높음' if isTrue else '이탈 가능성 낮음'}")
    with col2:
        st.image(images, width=200)
if machine_button:
    xgb = machine_learning_best_xgb(input_data)
    churn_probability = xgb[1] * 100  
    isTrue = xgb[0] >= 0.5
    images = image_3 if isTrue else image_1
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header('예측 결과')
        st.subheader(f'예측결과: {"이탈" if isTrue else "노이탈"}')
        st.subheader(f'이탈 확률: {churn_probability[0]:.2f}%')
        st.subheader(f"{'이탈 가능성 높음' if isTrue else '이탈 가능성 낮음'}")
    with col2:
        st.image(images, width=200)