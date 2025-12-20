import os
import pandas as pd
from real_walmart.logging import logger
from real_walmart.entity import DataValidationConfig


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None

            # Read dataset
            df = pd.read_csv("artifacts/data_ingestion/Walmart_Store_sales.csv")
            all_columns = list(df.columns)

            for col in self.config.required_columns:
                if col not in all_columns:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                    return validation_status

            validation_status = True
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
