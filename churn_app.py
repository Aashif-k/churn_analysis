import streamlit as st
import pandas as pd
import numpy as np
import pickle
head_css="""
<style>
[data-testid="stHeader"]{
background-color: #889E73;
opacity: 1.0;
}
</style>
"""
side_css="""
<style>
[data-testid="stSidebar"]{
position: Relative;
background-image: url("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDY1Z2I5eGtyNmk0ODQ3ZXR2MDZ4OHFlcnQ0cWFrdno3b2RkeTQxcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WGOlH30rfQWUo/giphy.gif");
width: 100%;
height: 100%;
background-size: auto auto;
}
</style>
"""
page_pg_img="""
<style>
[data-testid="stAppViewContainer"]{
position: Relative;
background-image: url("https://img.freepik.com/free-photo/newspaper-background-concept_23-2149501639.jpg?t=st=1737541856~exp=1737545456~hmac=1920514c5558ac13db21c9fd536ac3dd59bfecd149946cd1c62233789e01b2ee&w=996");
width: 100%;
height: 100%;
background-size: auto auto;
}
</style>
"""
out_cs="""
<style>
[data-testid="stAlertContainer"]{
background-color: #A94A4A;
color: #FFF6DA;
opacity: 1.0;
}
</style>
"""
pickle_in = open('xgb_model1.pkl','rb')
xgb_model1 = pickle.load(pickle_in)
def predic(voice_plan,intl_plan,
           intl_mins,intl_calls,day_mins,day_charge,eve_mins
           ,eve_charge,night_mins,night_charge,customer_calls):
    prediction = xgb_model1.predict([[voice_plan,intl_plan,
           intl_mins,intl_calls,day_mins,day_charge,eve_mins
           ,eve_charge,night_mins,night_charge,customer_calls]])
    print(prediction)
    return prediction
def main():
  st.title(":blue[churn analysis]")
  st.markdown(side_css,unsafe_allow_html=True)
  st.markdown(head_css,unsafe_allow_html=True)
  st.markdown(page_pg_img,unsafe_allow_html=True)
  st.sidebar(
  Text=st.selectbox("voice.plan",options=['Yes','No'])
  if Text =='Yes':
      voice_plan=1
  else:
      voice_plan=0
  intp=st.sidebar.selectbox("intl.plan",options=['Yes','No'])
  if intp == 'Yes':
    intl_plan=1
  else:
    intl_plan=0
  intl_mins=st.number_input("intl.mins",step=0.1,min_value=3.30,max_value=17.20)
  intl_calls=st.number_input("intl.calls",step=1,min_value=1,max_value=20)
  day_mins=st.number_input("day.mins",step=0.1,min_value=35.1,max_value=324.7)
  day_charge=st.number_input("day.charge",step=1,min_value=0,max_value=1904)
  eve_mins=st.number_input("eve.mins",step=1,min_value=0,max_value=1818)
  eve_charge=st.number_input("eve.charge",step=0.1,min_value=5.5,max_value=28.5)
  night_mins=st.number_input("night.mins",step=0.1,min_value=65.7,max_value=336.1)
  night_charge=st.number_input("night.charge",step=0.1,min_value=2.9,max_value=15.1)
  customer_calls=st.number_input("customer.calls",step=1,min_value=0,max_value=9)
           )
  result=""
  l,ll,lm,m,rm,lr,r = st.columns(7)
  if m.button("predict"):
    result=predic(voice_plan,intl_plan,
           intl_mins,intl_calls,day_mins,day_charge,eve_mins
           ,eve_charge,night_mins,night_charge,customer_calls)
  st.markdown(out_cs,unsafe_allow_html=True)
  st.success('The output is {}'.format(result)) 
if __name__=='__main__':
  main()
