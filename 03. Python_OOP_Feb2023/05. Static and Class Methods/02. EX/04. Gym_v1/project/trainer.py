class Trainer:
    trainer_id = 1
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def get_next_id():
        next_trainer_id = Trainer.trainer_id + 1
        return next_trainer_id

    def __repr__(self):
        return f"Trainer <{self.trainer_id}> {self.name}"
