# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:28:39 2024

@author: aiman
"""

import streamlit as st
import pandas as pd
import pickle
import datetime


with open(file="Accident.sav",mode="rb") as f1:
    model = pickle.load(f1)
    

st.title("Let's Find out Accident Severity")

st.sidebar.subheader('User Input Parameters')

def user_input_features():
    date_of_accident=st.sidebar.date_input(
        "Enter the Date of Accident",
        max_value=datetime.date.today(),
        value=datetime.date.today(),
        key='Accident_date'
        )
    
    Accident_months=date_of_accident.month
    day_of_week=st.sidebar.selectbox(
        'Day when Accident happend',
        ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'),key='day'
        )
    
    Junction_Control=st.sidebar.selectbox(
        'Select Junction Control where accident happend',
        ('Give way or uncontrolled','Auto traffic signal','Not at junction or within 20 metres',
         'Stop sign','Authorised person','Data missing or out of range'),key='junction_control'
        )
    
    Junction_Detail=st.sidebar.selectbox(
       "Select Junction details where accident happend",
       ('T or staggered junction','Not at junction or within 20 metres',
        'Crossroads','Roundabout','Private drive or entrance','More than 4 arms (not roundabout)',
        'Mini-roundabout','Slip road','Other junction'),key='juction_details'
       )
    Light_Conditions=st.sidebar.selectbox(
        "Light Condition at the time of Accident",('Daylight','Darkness - lights lit',
        'Darkness - no lighting','Darkness - lighting unknown','Darkness - lights unlit')
        
        )
    Local_Authority_District=st.sidebar.text_input('Local Authority District',
                    value='North Larkshire',key='Local_Authority_District')
   
    Carriageway_Hazards=st.sidebar.selectbox(
        'Carriageway Hazards at the time of accident',('Any animal in carriageway (except ridden horse)','Pedestrian in carriageway - not injured',
        'Previous accident','Vehicle load on road','Other object on road','None'),key='Carriageway_Hazards'
        )
    
    Number_of_Casualties=st.sidebar.number_input("No.of Casualties happend in Accident",
                value=1,step=1,key='Number_of_Casualties')
    
    Number_of_Vehicles=st.sidebar.number_input("Number of Vehicles involved in Accident",
            value=1,step=1,key='Number_of_Vehicles')
    
    Police_Force=st.sidebar.text_input('Name of Police Force',value='Strathclyde',key='Police_Force')
    
    Road_Surface_Conditions=st.sidebar.selectbox(
        "Road Surface Condition at the time of accident",('Dry','Wet or damp','Frost or ice',
         'Snow','Flood over 3cm. deep'),key='Road_Surface_Conditions'
        )
   
    Road_Type=st.sidebar.selectbox(
        "Type of Road on which accident happend",('Single carriageway','Dual carriageway',
        'Roundabout','One way street','Slip road'),key='Road_Type'
        )
    
    Speed_limit=st.sidebar.text_input('Speed of Vehicle at the time of accident',value=60,key='speed_limit')
    
    Time=st.time_input(
    "Enter the time of the accident:",value=datetime.time(12, 0),key="accident_time")
    
    Urban_or_Rural_Area=st.sidebar.selectbox("In which Area Accident took place",
            ('Urban','Rural'),key="Urban_or_Rural_Area")
    
    Weather_Conditions=st.sidebar.selectbox("Weather condition at the time of accident",
        ('Fine no high winds','Raining no high winds','Fine + high winds',
         'Raining + high winds','Snowing no high winds','Fog or mist','Snowing + high winds','Other'),key='Weather_Conditions'
        )
    
    Vehicle_Type=st.sidebar.selectbox("Type of Vehicle involved in Accident",
          ("Car",'Van / Goods 3.5 tonnes mgw or under','Goods 7.5 tonnes mgw and over','Motorcycle 125cc and under',
           'Bus or coach (17 or more pass seats)','Taxi/Private hire car','Motorcycle 50cc and under','Motorcycle over 500cc',
           'Motorcycle over 125cc and up to 500cc','Minibus (8 - 16 passenger seats)','Goods over 3.5t. and under 7.5t',
           'Agricultural vehicle','Other vehicle'),key='Vehicle_Type'   )                        
                                      
    
    data={
        'Accident_months':[Accident_months],
        'Day_of_Week':[day_of_week],
        'Junction_Control':[Junction_Control],
        'Junction_Detail':[Junction_Detail],
        'Light_Conditions':[Light_Conditions],
        'Local_Authority_District':[Local_Authority_District],
        'Carriageway_Hazards':[Carriageway_Hazards],
        'Number_of_Casualties':[Number_of_Casualties],
        'Number_of_Vehicles':[Number_of_Vehicles],
        'Police_Force':Police_Force,
        'Road_Surface_Conditions':Road_Surface_Conditions,
        'Road_Type':Road_Type,
        'Speed_limit':Speed_limit,
        'Time':Time,
        'Urban_or_Rural_Area':Urban_or_Rural_Area,
        'Weather_Conditions':Weather_Conditions,
        'Vehicle_Type':Vehicle_Type
        }
    return pd.DataFrame(data,index=[0])
    
df = user_input_features()
st.subheader('User Input DataFrame')
st.write(df)

if st.button("Predict"):
    prediction = model.predict(df)
    # predict_proba =model.predict_proba(df)
    
    
    if prediction==0:
        st.success('Accident Severity : Fatal')
    elif prediction==1:
        st.success('Accident Severity : Serious')
    elif prediction==2:
        st.success("Accident Severity : Slight")
    # st.subheader("Prediction Probability")
    