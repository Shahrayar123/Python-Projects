🔊 Sonic-Classifier: Rock vs Mine Detection This project is a binary classification system that uses Logistic Regression to distinguish between sonar signals bounced off metal cylinders (mines) and rocks. The dataset used is the Sonar Dataset from the UCI Machine Learning Repository.

📁 Dataset Name: Copy of sonar data

Source: UCI Machine Learning Repository

Description: Contains 208 samples and 60 numerical features representing sonar energy returns at various frequencies.

Target Classes:

M: Mine

R: Rock

🧠 Model Used Algorithm: Logistic Regression

Reason: It is a robust and interpretable baseline algorithm for binary classification tasks.

⚙️ Features Data Preprocessing:

Label Encoding (M → 1, R → 0)

Standardization using StandardScaler

Model Training using LogisticRegression from scikit-learn

Performance Evaluation:

Accuracy Score
📊 Sample Output

Accuracy: 85.57%
🛠 Tech Stack

Python

NumPy

Pandas

scikit-learn

Matplotlib (optional for visualization)

👨‍💻 Author Shirsha Nag If you like this project, feel free to ⭐ it!
