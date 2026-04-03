import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score
import pickle

# Load dataset
df = pd.read_csv("data.csv")

# Drop unused columns
df.drop(['date','street','country'],axis=1,inplace=True)

# Encode categorical features
df['city'] = LabelEncoder().fit_transform(df['city'])
df['statezip'] = LabelEncoder().fit_transform(df['statezip'])

# Define features and target
x = df.drop("price",axis=1)   #input
y = df["price"]    #output

# Train/test split
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42,test_size=0.2)

# Train model
model = RandomForestRegressor(n_estimators=100,random_state=42)
model.fit(x_train,y_train)

# Predict and calculate R^2 (accuracy)
y_pred = model.predict(x_test)
accuracy = r2_score(y_test,y_pred)

# Show accuracy
print(f"Model Accuracy (R^2 Score):{accuracy:.4f}")

#Save the model
with open("model.pkl","wb") as f:
    pickle.dump((model,x.columns),f)