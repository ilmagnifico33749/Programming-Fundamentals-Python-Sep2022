#Getting 92/100 from Judge 11/12 verif; I can't deal with this right now


from project.formula_teams.formula_team import FormulaTeam
from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam
from project.f1_season_app import F1SeasonApp


# ###############################################################
# Test_Code_1:
from project.f1_season_app import F1SeasonApp

f1_season = F1SeasonApp()

print(f1_season.register_team_for_season("Red Bull", 2000000))
print(f1_season.register_team_for_season("Mercedes", 2500000))

print(f1_season.new_race_results("Nurburgring", 1, 7))
print(f1_season.new_race_results("Silverstone", 10, 1))
# ----------------------------------------------------------------
# Output_1:
# Red Bull has joined the new F1 season.
# Mercedes has joined the new F1 season.
# Red Bull: The revenue after the race is 1270000$. Current budget 3270000$. Mercedes: The revenue after the race is -150000$. Current budget 2350000$. Red Bull is ahead at the Nurburgring race.
# Red Bull: The revenue after the race is -240000$. Current budget 3030000$. Mercedes: The revenue after the race is 900000$. Current budget 3250000$. Mercedes is ahead at the Silverstone race.
# ###############################################################