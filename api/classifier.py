import os
import joblib
import numpy as np

class DepressionClassifier:
    """
    This class loads a Machine Learning model from model.joblib.
    """

    def __init__(self):
        print("initializing depression classifier....")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, 'model.joblib')

        try:
            self.model = joblib.load(model_path)
            print(f"Successfully loaded model from {model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None

    def predict(self, text):
        if self.model is None:
            return {
                "label": "Model Error",
                "is_depressed": False,
                "confidence": "Model not loaded"
            }

        try:
            print("Trying...")

            prediction = self.model.predict([text])
            pred = prediction[0]   # extract value
            print("Prediction:", pred)

            #  predict_probability
            confidence = "N/A"
            if hasattr(self.model, "predict_proba"):
                probas = self.model.predict_proba([text])[0]
                confidence = f"{int(max(probas) * 100)}%"

            # Determine depressed or not 
            if isinstance(pred, (int, np.integer)):
                is_depressed = (pred == 1)
            else:
                is_depressed = str(pred).lower() in ['depressed', '1', 'true', 'yes']

            return {
                "label": "Depressed" if is_depressed else "Not Depressed",
                "is_depressed": is_depressed,
                "confidence": confidence
            }

        except Exception as e:
            print("Exception./////////////////////////// ", str(e))
            return {
                "label": "Prediction Error",
                "is_depressed": False,
                "confidence": str(e)
            }
