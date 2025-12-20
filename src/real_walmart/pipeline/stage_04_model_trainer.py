from real_walmart.config.configuration import ConfigurationManager
from real_walmart.conponents.model_trainer import ModelTrainer
from real_walmart.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()

        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()