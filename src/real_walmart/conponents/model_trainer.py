import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from real_walmart.logging import logger
from real_walmart.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        """
        Train a regression model on Walmart sales data
        and save the trained model.
        """
        try:
            logger.info("Starting model training")

            # Load training data
            train_df = pd.read_csv(self.config.train_data_path)
            logger.info(f"Training data loaded with shape: {train_df.shape}")

            # Split features and target
            X_train = train_df.drop(columns=["Weekly_Sales"])
            y_train = train_df["Weekly_Sales"]

            # Initialize model
            model = RandomForestRegressor(
                n_estimators=200,
                random_state=42
            )

            # Train model
            model.fit(X_train, y_train)
            logger.info("Model training completed")

            # Save model
            os.makedirs(self.config.root_dir, exist_ok=True)
            model_path = os.path.join(self.config.root_dir, self.config.model_name)
            joblib.dump(model, model_path)

            logger.info(f"Model saved at: {model_path}")

        except Exception as e:
            logger.error("Error occurred during model training")
            raise e
