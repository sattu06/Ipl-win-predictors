import streamlit as st
import pickle
import pandas as pd
import time

# Load the trained model
pipe = pickle.load(open('ipl_win_predictor.pkl', 'rb'))

# IPL Logo
def fetch_ipl_logo():
    return "https://documents.iplt20.com//ipl/assets/images/ipl-logo-new-old.png"

# Team logos
team_logos = {
    "Mumbai Indians": "https://documents.iplt20.com/ipl/MI/Logos/Logooutline/MIoutline.png",
    "Chennai Super Kings": "https://www.chennaisuperkings.com/assets/images/mainlogo.png",
    "Royal Challengers Bengaluru": "https://documents.iplt20.com/ipl/RCB/Logos/Logooutline/RCBoutline.png",
    "Kolkata Knight Riders": "https://documents.iplt20.com/ipl/KKR/Logos/Logooutline/KKRoutline.png",
    "Delhi Capitals": "https://documents.iplt20.com/ipl/DC/Logos/LogoOutline/DCoutline.png",
    "Rajasthan Royals": "https://documents.iplt20.com/ipl/RR/Logos/Logooutline/RRoutline.png",
    "Punjab Kings": "https://documents.iplt20.com/ipl/PBKS/Logos/Logooutline/PBKSoutline.png",
    "Sunrisers Hyderabad": "https://documents.iplt20.com/ipl/SRH/Logos/Logooutline/SRHoutline.png",
    "Gujarat Titans": "https://documents.iplt20.com/ipl/GT/Logos/Logooutline/GToutline.png",
    "Lucknow Super Giants": "https://documents.iplt20.com/ipl/LSG/Logos/Logooutline/LSGoutline.png"
}

# Team colors for progress bars
team_colors = {
    "Mumbai Indians": "#045093",
    "Chennai Super Kings": "#fbee23",
    "Royal Challengers Bengaluru": "#da1818",
    "Kolkata Knight Riders": "#3b215d",
    "Delhi Capitals": "#17449b",
    "Rajasthan Royals": "#ea1a85",
    "Punjab Kings": "#c40732",
    "Sunrisers Hyderabad": "#f26522",
    "Gujarat Titans": "#1c2c56",
    "Lucknow Super Giants": "#2f97c1"
}

teams = list(team_logos.keys())
cities = sorted(['Kolkata', 'Mumbai', 'Delhi', 'Lucknow', 'Jaipur', 'Dharamsala', 'Chandigarh', 'Hyderabad',
                 'Abu Dhabi', 'Pune', 'Bangalore', 'Mohali', 'Chennai', 'Centurion', 'Cuttack', 'Bengaluru',
                 'Guwahati', 'Navi Mumbai', 'Raipur', 'Cape Town', 'Visakhapatnam', 'Indore', 'Ahmedabad',
                 'Johannesburg', 'East London', 'Durban', 'Bloemfontein', 'Port Elizabeth', 'Nagpur',
                 'Kimberley', 'Ranchi', 'Dubai', 'Sharjah'])

# Page config
st.set_page_config(page_title="IPL Win Predictor", layout="centered")

# Initialize prediction history
if 'history' not in st.session_state:
    st.session_state.history = []

# Header
st.markdown("""
    <div style='display: flex; align-items: center; justify-content: space-between;'>
        <img src="https://documents.iplt20.com//ipl/assets/images/ipl-logo-new-old.png" width="120">
        <h1 style='text-align: center; color: #FF4B4B; font-size: 40px;'>🏏 IPL Win Predictor 🏆</h1>
        <div style='width: 120px;'></div>
    </div>
    <hr style="border-top: 2px solid #bbb;">
""", unsafe_allow_html=True)

# Team Selection UI
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox("🏏 Batting Team", ["-- Select Team --"] + sorted(teams))
    if batting_team in team_logos:
        st.image(team_logos[batting_team], width=100)

with col2:
    valid_bowling = [team for team in sorted(teams) if team != batting_team]
    bowling_team = st.selectbox("🎯 Bowling Team", ["-- Select Team --"] + valid_bowling)
    if bowling_team in team_logos:
        st.image(team_logos[bowling_team], width=100)

selected_city = st.selectbox("📍 Host City", ["-- Select Venue --"] + cities)
target = st.number_input("🎯 Target Score", min_value=1)

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input("🔢 Current Score", min_value=0)
with col4:
    over = st.number_input("⏱ Overs", min_value=0, max_value=20)
    ball = st.number_input("⚾ Balls", min_value=0, max_value=5)
    overs = float(over) + ball / 6
with col5:
    wickets = st.number_input("❌ Wickets Fallen", min_value=0, max_value=10)

# Predict button
if st.button("🚀 Predict Win Probability"):
    if "--" in [batting_team, bowling_team, selected_city]:
        st.warning("Please select both teams and a venue.")
    else:
        runs_left = target - score
        balls_left = 120 - int(overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs if overs > 0 else 0
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        if overs == 0 or overs > 20 or wickets > 10 or balls_left <= 0 or runs_left < 0:
            st.error("⚠️ Please enter valid match conditions.")
        else:
            input_df = pd.DataFrame({
                'batting_team': [batting_team],
                'bowling_team': [bowling_team],
                'city': [selected_city],
                'runs_left': [runs_left],
                'balls_left': [balls_left],
                'wickets_left': [wickets_left],
                'total_runs_x': [target],
                'crr': [crr],
                'rrr': [rrr]
            })

            with st.spinner('Crunching the numbers... 🧠'):
                time.sleep(1.5)
                result = pipe.predict_proba(input_df)
                loss = result[0][0]
                win = result[0][1]

            # Save history
            st.session_state.history.append({
                'over': overs,
                'bat_win_prob': win * 100,
                'bowl_win_prob': loss * 100
            })

            batting_color = team_colors.get(batting_team, '#4CAF50')
            bowling_color = team_colors.get(bowling_team, '#F44336')

            st.markdown(f"""
                <div style='display: flex; justify-content: space-between; margin-top: 20px;'>
                    <span style='font-size: 20px; font-weight: bold; color: {batting_color};'>{batting_team}: {win * 100:.1f}%</span>
                    <span style='font-size: 20px; font-weight: bold; color: {bowling_color};'>{bowling_team}: {loss * 100:.1f}%</span>
                </div>
                <div style='height: 12px; background: linear-gradient(to right, {batting_color} {win * 100}%, {bowling_color} {win * 100}%); border-radius: 8px; margin-top: 5px;'></div>
            """, unsafe_allow_html=True)

            st.markdown("### 📝 Match Summary")
            st.info(f"""
            • Runs Left: {runs_left}  
            • Balls Left: {balls_left}  
            • Wickets Remaining: {wickets_left}  
            • CRR: {crr:.2f}  
            • RRR: {rrr:.2f}
            """)

            with st.expander("🎙️ Match Commentary"):
                if win > 0.75:
                    st.success(f"{batting_team} are cruising to victory! 💪")
                elif win < 0.25:
                    st.error(f"{bowling_team} are dominating right now! 🔥")
                else:
                    st.warning("It's a tight match. Anything can happen! ⏳")

