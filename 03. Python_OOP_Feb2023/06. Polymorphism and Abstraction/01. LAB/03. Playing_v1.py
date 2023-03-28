
def start_playing(current_object):
    return current_object.play()


# ################################
# Test_Code_1:
class Guitar:
    def play(self):
        return "Playing the guitar"
guitar = Guitar()
print(start_playing(guitar))
# --------------------------------
# Output_1:
# Playing the guitar
# ################################
# Test_Code_2:
class Children:
    def play(self):
        return "Children are playing"
children = Children()
print(start_playing(children))
# ---------------------------------
# Output_2:
# Children are playing
# ################################
