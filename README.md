
# 🏏 IPL Win Predictor

A real-time web application that predicts the winning probability of an IPL team during a match based on current match stats. Built using Streamlit and a machine learning model trained on historical IPL data.

---

## 🚀 Features

- Interactive UI with IPL-themed visuals and logos  
- Real-time win probability prediction using a trained ML model  
- Dynamic match summary and team-specific color themes  
- Context-based match commentary for an engaging experience

---

## 📊 Tech Stack

- **Frontend**: Streamlit  
- **Backend/ML**: Scikit-learn, Pandas, Pickle  
- **Model**: Classification model trained on match conditions (overs, wickets, runs, etc.)

---

## ⚙️ Installation

1. Clone this repo:
    ```bash
    git clone https://github.com/yourusername/ipl-win-predictor.git
    cd ipl-win-predictor
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    streamlit run app4.py
    ```

---

## 📁 Files

| File | Description |
|------|-------------|
| `app4.py` | Streamlit app script |
| `ipl_win_predictor.pkl` | Pretrained machine learning model |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## 📌 How It Works

1. User inputs match context:
   - Batting and Bowling Team
   - Host City
   - Target and Current Scores
   - Overs Bowled and Wickets Lost

2. Model calculates features like:
   - Runs Left
   - Balls Left
   - Current and Required Run Rates

3. The classification model predicts the probability of the batting team winning.

---

## 📷 Screenshots
My app Predication
![image](https://github.com/user-attachments/assets/ae8cf8d5-5f21-4a6a-ae05-61590325627a)
![image](https://github.com/user-attachments/assets/483650b7-c9fe-4736-8531-9709df35789b)
Actual 
![image](https://github.com/user-attachments/assets/947165cf-36ef-4f54-a4a6-0d603a316e58)


---

## 🤝 Contributions

- **Srijan Agrawal** ([andromeda1130](https://github.com/andromeda1130)):  
  Responsible for model creation, data preprocessing, and refining the feature set to improve prediction accuracy.

- **Satyam Raj** ([sattu06](https://github.com/sattu06)):  
  Designed and implemented the frontend using Streamlit, integrated the trained model, and tested the application for seamless user experience.

---

## 📜 License

MIT License
