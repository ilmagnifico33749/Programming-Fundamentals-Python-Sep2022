def vowel_filter(function):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Y", "y"]
    def wrapper():
        to_filter_from = function()
        filtered_letters = [x for x in to_filter_from if x in vowels]
        return filtered_letters
    # TODO: Implement
    return wrapper

# ###################################################
# Test_Code_1:
@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())
# ---------------------------------------------------
# Output_1:
# ["a", "e"]
# ###################################################
