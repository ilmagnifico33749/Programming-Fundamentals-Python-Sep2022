# ####################################################
# # Code_To_Correct_1:
# class RubberDuck(Duck):
#     @staticmethod
#     def quack():
#         return "Squeek"
#
#     @staticmethod
#     def walk():
#         """Rubber duck can walk only if you move it"""
#         raise Exception('I cannot walk by myself')
#
#     @staticmethod
#     def fly():
#         """Rubber duck can fly only if you throw it"""
#         raise Exception('I cannot fly by myself')
#
#
# class RobotDuck(Duck):
#     HEIGHT = 50
#
#     def __init__(self):
#         self.height = 0
#
#     @staticmethod
#     def quack():
#         return 'Robotic quacking'
#
#     @staticmethod
#     def walk():
#         return 'Robotic walking'
#
#     def fly(self):
#         """can only fly to specific height but
#         when it reaches it starts landing automatically"""
#         if self.height == RobotDuck.HEIGHT:
#             self.land()
#         else:
#             self.height += 1
#
#     def land(self):
#         self.height = 0
# ####################################################
# Corrected_Code_1:

from abc import ABC, abstractmethod


class Duck:
    Flying_Max_Height = int()
    def __init__(self, height=0):
        self.height = height

    @staticmethod
    @abstractmethod
    def quack():
        pass

    @staticmethod
    @abstractmethod
    def walk():
        pass

    @staticmethod
    @abstractmethod
    def fly():
        pass
    #
    # @staticmethod
    # @abstractmethod
    # def land():
    #     pass


class RubberDuck(Duck):
    def __init__(self):
        super().__init__()

    @staticmethod
    def quack():
        return "Squeek"

    @staticmethod
    def walk():
        """Rubber duck can walk only if you move it"""
        raise Exception('I cannot walk by myself')

    @staticmethod
    def fly():
        """Rubber duck can fly only if you throw it"""
        raise Exception('I cannot fly by myself')


class RobotDuck(Duck):
    Flying_Max_Height = 50

    def __init__(self, height=49):
        super().__init__(height)

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.Flying_Max_Height:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0
####################################################
# Test_1:
robot_duck = RobotDuck()
print(robot_duck.height)
robot_duck.fly()
print(robot_duck.height)
robot_duck.land()
print(robot_duck.height)
while robot_duck.height < robot_duck.Flying_Max_Height:
    robot_duck.fly()
else:
    print(f"Max Height Reached!")

####################################################
