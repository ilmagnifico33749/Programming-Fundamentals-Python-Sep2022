from abc import ABC, abstractmethod
from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, strength=150)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        if self.can_climb():
            strength_reduction = 30 * 1.3 if peak.calculate_difficulty_level() == "Advanced" else 30 * 2.5
            self.strength -= strength_reduction
            self.conquered_peaks.append(peak.name)
