! pip install streamlit -q
!wget -q -O - ipv4.icanhazip.com
! streamlit run app.py & npx localtunnel --port 
%%writefile app.py
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
sonar_data = pd.read_csv('Copy of sonar data.csv', header=None)

# Prepare data
X = sonar_data.drop(columns=60, axis=1)
y = sonar_data[60]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, stratify=y, random_state=1)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Streamlit UI
st.title("Rock vs Mine Prediction (Sonar Data)")
st.image("pic.jpeg", width=120)
st.write("Enter the 60 sonar signal values:")

# Input features
input_data = []
for i in range(60):
    val = st.number_input(f"Feature {i+1}", value=0.0, format="%.5f")
    input_data.append(val)

# Prediction
if st.button("Predict"):
    input_np = np.asarray(input_data).reshape(1, -1)
    prediction = model.predict(input_np)
    if prediction[0] == 'R':
        st.success("The object is a **Rock** 🪨")
    else:
        st.success("The object is a **Mine** 💣")

# Accuracy Display
st.write("### Model Accuracy")
train_acc = accuracy_score(model.predict(X_train), y_train)
test_acc = accuracy_score(model.predict(X_test), y_test)
st.write(f"Training Accuracy: **{train_acc:.2f}**")
st.write(f"Testing Accuracy: **{test_acc:.2f}**")
