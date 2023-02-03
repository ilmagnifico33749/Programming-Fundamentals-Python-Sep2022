def sorting_cheeses(**queijo_dict):

        queijo_dict = sorted(queijo_dict.items(), key=lambda x: (-len(x[1]), x[0]))

        lista_final = []

        for (queijo_nome, queijo_quantidade) in queijo_dict:
            lista_final.append(queijo_nome)
            queijo_quantidade_lista = sorted(queijo_quantidade, reverse=True)
            lista_final += queijo_quantidade_lista

        return '\n'.join(map(str, lista_final))

# #############################################
# Test_Code_1:
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
# ----------------------------------------------
# Output_1:
# Camembert
# 500
# 430
# 105
# 100
# 100
# Parmesan
# 135
# 120
# 102
# #############################################
# Test_code_2:
# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )
# ----------------------------------------------
# Output_2:
# Brie
# 150
# 125
# Feta
# 515
# 150
# Parmigiano
# 215
# 165
# #############################################
