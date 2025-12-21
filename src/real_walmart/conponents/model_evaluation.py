import os
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from real_walmart.logging import logger
from real_walmart.entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate(self):
        """
        Evaluate trained regression model on test data
        and save evaluation metrics.
        """
        try:
            logger.info("Starting model evaluation")

            # Load test data
            test_df = pd.read_csv(self.config.test_data_path)
            logger.info(f"Test data loaded with shape: {test_df.shape}")

            X_test = test_df.drop(columns=["Weekly_Sales"])
            y_test = test_df["Weekly_Sales"]

            # Load trained model
            model = joblib.load(self.config.model_path)
            logger.info("Trained model loaded successfully")

            # Predictions
            y_pred = model.predict(X_test)

            # Metrics (version-safe)
            mse = mean_squared_error(y_test, y_pred)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            metrics = {
                "rmse": rmse,
                "mae": mae,
                "r2_score": r2
            }

            # Save metrics
            os.makedirs(self.config.root_dir, exist_ok=True)
            metrics_df = pd.DataFrame([metrics])
            metrics_df.to_csv(self.config.metric_file_name, index=False)

            logger.info(f"Model evaluation completed: {metrics}")

        except Exception as e:
            logger.error("Error occurred during model evaluation")
            raise e
