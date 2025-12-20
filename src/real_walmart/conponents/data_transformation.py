import os
import pandas as pd
from sklearn.model_selection import train_test_split

from real_walmart.logging import logger
from real_walmart.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def convert(self):
        """
        Reads raw Walmart data, performs train-test split,
        and saves transformed datasets.
        """
        try:
            logger.info("Starting data transformation")

            # Load raw data
            df = pd.read_csv(self.config.data_path)
            logger.info(f"Dataset loaded with shape: {df.shape}")

            # Separate features and target
            X = df.drop(columns=["Weekly_Sales", "Date"], errors="ignore")
            y = df["Weekly_Sales"]

            # Train-test split
            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )

            # Combine back for saving
            train_df = pd.concat([X_train, y_train], axis=1)
            test_df = pd.concat([X_test, y_test], axis=1)

            # Ensure output directory exists
            os.makedirs(self.config.root_dir, exist_ok=True)

            # Save transformed data
            train_df.to_csv(self.config.train_data_path, index=False)
            test_df.to_csv(self.config.test_data_path, index=False)

            logger.info(
                f"Data transformation completed.\n"
                f"Train shape: {train_df.shape}, Test shape: {test_df.shape}"
            )

        except Exception as e:
            logger.error("Error during data transformation")
            raise e