class ExercisePlan:
    exercise_plan_id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration

    @staticmethod
    def get_next_id():
        next_exercise_plan_id = ExercisePlan.exercise_plan_id + 1
        return next_exercise_plan_id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours)

    def __repr__(self):
        return f"Plan <{self.exercise_plan_id}> with duration {self.duration} minutes"
