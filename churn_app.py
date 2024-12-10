import streamlit as st
import pandas as pd
import numpy as np
import pickle

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
  st.title("churn prediciton")
  Text=st.selectbox("voice.plan",options=['Yes','No'])
  if Text =='Yes':
      voice_plan=1
  else:
      voice_plan=0
  intp=st.selectbox("intl.plan",options=['Yes','No'])
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
  result=""
  if st.button("predict"):
    result=predic(voice_plan,intl_plan,
           intl_mins,intl_calls,day_mins,day_charge,eve_mins
           ,eve_charge,night_mins,night_charge,customer_calls)
  st.success('The output is {}'.format(result))
 # Make the prediction
 input_data = np.array([voice_plan,intl_plan, intl_mins, intl_calls,
                        day_mins,day_charge, eve_mins,eve_charge,
                        night_mins,night_charge,customer_calls]).reshape(1, -1)
prediction = xgb_model1.predict(input_data)
prediction_prob = xgb_model1.predict_proba(input_data)[0][1]  # Probability of churn

    # Display the result
if prediction[0] == 1:
        st.error(f"Prediction: The customer is likely to churn. (Probability: {prediction_prob:.2f})")
else:
        st.success(f"Prediction: The customer is likely to stay. (Probability: {1 - prediction_prob:.2f})")
if __name__=='__main__':
  main()
