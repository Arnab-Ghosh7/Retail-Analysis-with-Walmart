import pandas as pd
import joblib

from real_walmart.config.configuration import ConfigurationManager
from real_walmart.logging import logger


class PredictionPipeline:
    def __init__(self):
        # Load model evaluation config to get model path
        self.config = ConfigurationManager().get_model_evaluation_config()
        self.model = joblib.load(self.config.model_path)
        logger.info("Prediction model loaded successfully")

    def predict(self, input_data: dict):
        """
        Predict weekly sales based on input features.

        Args:
            input_data (dict): feature_name -> value

        Returns:
            float: predicted Weekly_Sales
        """
        try:
            # Convert input dict to DataFrame
            input_df = pd.DataFrame([input_data])

            logger.info(f"Input data received for prediction: {input_data}")

            # Make prediction
            prediction = self.model.predict(input_df)[0]

            logger.info(f"Prediction completed: {prediction}")

            return prediction

        except Exception as e:
            logger.error("Error occurred during prediction")
            raise e
