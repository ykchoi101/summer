import streamlit as st
import time
import random
import session_two

st.header('st.session_state 세션 테스트')
def main():
    if 'user_list' not in st.session_state:
        st.session_state.user_list = []


main() #함수에서 세션기술

@st.cache_data
def slow_cal(x):
  
    time.sleep(1)
    cal = x*100
    return cal

dice = [1,2,3,4,5,6]
pick = random.choice(dice)
st.write('pick = ',pick)
result = slow_cal(pick)
st.write('slow_cal(x)함수 결과 = ' , result)
# (.venv) C:\~~> streamlit run session_first.py










