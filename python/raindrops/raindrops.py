# First attempt

# def convert(number):
#     number = int(number)
#     result = ""
#     if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
#         return str(number)
#     else:
#         if number % 3 == 0:
#             result += "Pling"
#         if number % 5 == 0:
#             result += "Plang"
#         if number % 7 == 0:
#             result += "Plong"
#     return result


# Inspired by https://exercism.io/tracks/python/exercises/raindrops/solutions/d2c30600afd94eb2996f8db20f2edf60

def convert(number):
    result = "Pling" if number % 3 == 0 else ""
    result += "Plang" if number % 5 == 0 else ""
    result += "Plong" if number % 7 == 0 else ""
    return result or str(number)


# Inspired by https://exercism.io/tracks/python/exercises/raindrops/solutions/52093dd786f640c2bf7c23b325d0286d

# def convert(number):
#     result = ""
#     divisor_drop = {3: "Pling", 5: "Plang", 7: "Plong"}
#     for (divisor, drop) in divisor_drop.items():
#         result += drop if number % divisor == 0 else ""
#     return result or str(number)
