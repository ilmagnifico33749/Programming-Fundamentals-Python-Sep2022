from abc import ABC, abstractmethod
from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, strength=200)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak: BasePeak):
        if self.can_climb():
            strength_reduction = 20 * 2 if peak.calculate_difficulty_level() == "Extreme" else 20 * 1.5
            self.strength -= strength_reduction
            self.conquered_peaks.append(peak.name)
