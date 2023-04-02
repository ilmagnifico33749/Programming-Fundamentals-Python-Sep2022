# from project.formula_teams.formula_team import FormulaTeam
from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    valid_team_names = ["Red Bull", "Mercedes"]

    def __init__(self):
        self.red_bull_team: RedBullTeam or None = None
        self.mercedes_team: MercedesTeam or None = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in self.valid_team_names:
            raise ValueError("Invalid team name!")
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        try:
            return f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. " \
                   f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. " \
                   f"{('Red Bull' if red_bull_pos < mercedes_pos else 'Mercedes')} is ahead at the {race_name} race."
        except AttributeError:
            return f"Not all teams have registered for the season."



