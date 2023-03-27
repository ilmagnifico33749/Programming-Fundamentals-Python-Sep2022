# Code Redacting problem
# #########################################################################
# Orig_Code:
# class Robot:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def sensors_amount():
#         return 1
#
#
# class MedicalRobot(Robot):
#     @staticmethod
#     def medical_robot_sensors_amount():
#         return 6
#
#
# class ChefRobot(Robot):
#     @staticmethod
#     def chef_robot_sensors_amount():
#         return 4
#
#
# class WarRobot(Robot):
#     @staticmethod
#     def war_robot_sensors_amount():
#         return 12
#
#
# def number_of_robot_sensors(robot):
#     if isinstance(robot, Robot):
#         print(robot.sensors_amount())
#     if isinstance(robot, MedicalRobot):
#         print(robot.medical_robot_sensors_amount())
#     elif isinstance(robot, ChefRobot):
#         print(robot.chef_robot_sensors_amount())
#     elif isinstance(robot, WarRobot):
#         print(robot.war_robot_sensors_amount())
#
#
# basic_robot = Robot('Robo')
# da_vinci = MedicalRobot('Da Vinci')
# moley = ChefRobot('Moley')
# griffin = WarRobot('Griffin')
#
# number_of_robot_sensors(basic_robot)
# number_of_robot_sensors(da_vinci)
# number_of_robot_sensors(moley)
# number_of_robot_sensors(griffin)
# ------------------------------------------------------------
# New_Code:
class Robot:
    def __init__(self, name):
        self.name = name

    def sensors_amount(self):
        return 1


class MedicalRobot(Robot):
    def sensors_amount(self):
        return 6


class ChefRobot(Robot):
    def sensors_amount(self):
        return 4


class WarRobot(Robot):
    def sensors_amount(self):
        return 12

basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

print(basic_robot.sensors_amount())
print(da_vinci.sensors_amount())
print(moley.sensors_amount())
print(griffin.sensors_amount())
#########################################################################
