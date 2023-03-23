class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(round(float_value))

    @classmethod
    def from_roman(cls, value):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arabic_number = 0
        for index_rom_num in range(len(value)):
            if index_rom_num != 0 and rom_val[value[index_rom_num]] > rom_val[value[index_rom_num-1]]:
                arabic_number += rom_val[value[index_rom_num]] - (2 * rom_val[value[index_rom_num-1]])
            else:
                arabic_number += rom_val[value[index_rom_num]]

        return cls(arabic_number)


    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))


# #######################################
# Test_Code_1:
first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("IV")
print(second_num.value)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
# --------------------------------------
# Output_1:
# 10
# 4
# value is not a float
# wrong type
# #######################################
