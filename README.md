🚀 LuxEstimate – House Price Prediction Using Machine Learning

I'm excited to share LuxEstimate, a machine learning project I built that predicts the price of residential houses based on key features like size, number of rooms, and build condition. 🏡💡

This project is built using Linear Regression, a simple yet powerful ML algorithm that identifies relationships between a property's features and its market price. It was chosen for its superior accuracy compared to other models like Random Forest, KNN, and Decision Tree in this case.

🔍 What LuxEstimate Does:
LuxEstimate is a Flask-based web app that allows users to input features such as:

Bedrooms

Bathrooms

Living area (sqft)

Lot size

Number of floors

Waterfront presence

View rating

Condition rating

Year built

Sqft above ground

Sqft basement

Using these, the model instantly predicts a house’s price and displays it through a user-friendly web interface.

🧠 Core ML Algorithm: Linear Regression
price = β0 + β1×bedrooms + β2×bathrooms + ... + βn×yr_built + ε

Linear Regression was the best performing model with the following evaluation:

✅ R² Score: 0.460

✅ Mean Absolute Error: ~137,660

✅ Prediction: More consistent and closer to real market price than other models

🛠️ Tech Stack & Libraries Used:
Python

Flask – for the web interface

scikit-learn – for training ML models

Pandas & NumPy – for data manipulation

Joblib – for saving and loading the model

📈 Model Comparison:
Linear Regression: ✅ Best performer

Random Forest: Underpredicted by a large margin

Decision Tree: Overfitted on high values

KNN: Averaged predictions, lacked precision

💻 Project Type:
ML + Web App (End-to-End Machine Learning Deployment)

📂 Project Name: LuxEstimate
🏷️ Use Case: Real estate price prediction for buyers, sellers, and agents
🔗 Excited to grow further in ML, data science, and full-stack AI deployment. Open to collaborations and feedback!
