import streamlit as st
import pickle
import pandas as pd


teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings', 
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah','Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title("IPL win Predictor")
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox("Select the batting team",sorted(teams))
with col1:
    bowling_team = st.selectbox("Select the bowling team",sorted(teams))

Select_city = st.selectbox("Select host city",sorted(cities))
target = st.number_input('Target')

col3, col4, col5 =st.columns(3)

with col3:
    Score = st.number_input('Score')
with col3:
    Overs = st.number_input('Overs completed')
with col3:
    Wickets = st.number_input('Wickets out')

if st.button("Predict Probability"):
    runs_left = target - Score
    balls_left = 120 - (Overs*6)
    Wickets = 10 - Wickets
    crr = Score/Overs
    rrr = (runs_left*6)/balls_left
    
    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[Select_city],'runs_left':[runs_left],'balls_left':[balls_left],
            	'wickets':[Wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    result = pipe.predict_proba(input_df)
    # st.table(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.text(batting_team + " - " + str(round(win*100)) + "%")
    st.text(bowling_team + " - " + str(round(loss*100)) + "%")