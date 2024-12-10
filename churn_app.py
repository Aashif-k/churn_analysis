import streamlit as st
import pandas as pd
import numpy as np
import pickle

pickle_in = open('xgb_model.pkl','rb')
xgb_model = pickle.load(pickle_in)
def predic(state,area_code,account_length,voice_plan,voice_messages,intl_plan,
           intl_mins,intl_calls,intl_charge,day_mins,day_calls,day_charge,eve_mins
           ,eve_calls,eve_charge,night_mins,night_calls,night_charge,customer_calls):
    prediction = xgb_model.predict([[state,area_code,account_length,voice_plan,voice_messages,intl_plan,
           intl_mins,intl_calls,intl_charge,day_mins,day_calls,day_charge,eve_mins
           ,eve_calls,eve_charge,night_mins,night_calls,night_charge,customer_calls]])
    print(prediction)
    return prediction
def main():
  st.title("churn prediciton")
  state=st.number_input("state")
  area_code=st.number_input("Area.code")
  account_length=st.number_input("account.length")
  voice_plan=st.number_input("voice.plan")
  voice_messages=st.number_input("voice.messages")
  intl_plan=st.number_input("intl.plan")
  intl_mins=st.number_input("intl.mins")
  intl_calls=st.number_input("intl.calls")
  intl_charge=st.number_input("intl.charge")
  day_mins=st.number_input("day.mins")
  day_calls=st.number_input("day.calls")
  day_charge=st.number_input("day.charge")
  eve_mins=st.number_input("eve.mins")
  eve_calls=st.number_input("eve.calls")
  eve_charge=st.number_input("eve.charge")
  night_mins=st.number_input("night.mins")
  night_calls=st.number_input("night.calls")
  night_charge=st.number_input("night.charge")
  customer_calls=st.number_input("customer.calls")
  result=""
  if st.button("predict"):
    result=predic(state,area_code,account_length,voice_plan,voice_messages,intl_plan,
           intl_mins,intl_calls,intl_charge,day_mins,day_calls,day_charge,eve_mins
           ,eve_calls,eve_charge,night_mins,night_calls,night_charge,customer_calls)
  st.success('The output is {}'.format(result))
if __name__=='__main__':
  main()