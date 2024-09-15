import os
import pandas as pd
import joblib
from flask import Flask, request, jsonify, render_template
from preprocessing import preprocess_data

# Initialize the Flask application
app = Flask(__name__)

# Load the secret key from environment variables
app.config['myenv'] = os.getenv('myenv', 'myenv2024')

# Load the trained model and tokenizer
model = joblib.load('nb_pipeline_count.joblib')  # Load the model using joblib

# Load the class labels (dialects)
class_labels = pd.read_csv('y_train.csv', encoding='utf-8')['dialect'].unique()

# Define the maximum number of words and sequence length
MAX_NB_WORDS = 50000
MAX_SEQUENCE_LENGTH = 60

# Load preprocessed data and other necessary objects
X_train_vec, X_test_vec, y_train, y_test, class_weight_dict, vectorizer = preprocess_data(
    'X_train.csv', 'X_test.csv', 'y_train.csv', 'y_test.csv', vectorizer_type='count'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.get('text')

    if data:
        # Preprocess the input text using the loaded vectorizer
        sequence = vectorizer.transform([data])
        
        # Make a prediction
        prediction = model.predict(sequence)

        # Return the prediction as JSON
        return render_template('index.html', prediction=prediction[0])
    else:
        return render_template('index.html', error='No text provided for prediction')

if __name__ == '__main__':
    app.run(debug=False)