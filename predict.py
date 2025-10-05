import joblib
import pandas as pd
import numpy as np

def load_model():
    """Load the trained model and scaler"""
    model = joblib.load('models/ridge_model.pkl')
    scaler = joblib.load('models/scaler.pkl')
    return model, scaler

def predict_default_probability(applicant_data):
    """
    Predict default probability for new applicant(s)
    
    Parameters:
    applicant_data: DataFrame with 26 features
    
    Returns:
    predictions: array of probabilities (0-1)
    """
    # Load model and scaler
    model, scaler = load_model()
    
    # Scale the data
    applicant_scaled = scaler.transform(applicant_data)
    
    # Predict
    predictions = model.predict(applicant_scaled)
    
    # Ensure predictions are in valid range
    predictions = np.clip(predictions, 0, 1)
    
    return predictions

def make_decision(probability, threshold=0.5):
    """
    Make loan decision based on probability threshold
    
    Parameters:
    probability: default probability (0-1)
    threshold: decision threshold
    
    Returns:
    decision and risk level
    """
    if probability < 0.4:
        risk = "LOW RISK"
        decision = "APPROVE - Standard terms"
    elif probability < 0.55:
        risk = "MEDIUM RISK"
        decision = "APPROVE - Monitor closely or higher interest rate"
    else:
        risk = "HIGH RISK"
        decision = "REJECT or require substantial collateral"
    
    return risk, decision

# Example usage
if __name__ == "__main__":
    # Example: Load new applicant data
    # new_applicant = pd.read_csv('data/new_applicant.csv')
    
    # Predict
    # probs = predict_default_probability(new_applicant)
    # print(f"Default probability: {probs[0]:.4f}")
    
    pass