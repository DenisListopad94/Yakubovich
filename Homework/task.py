# 1
#
# file = open("1.txt", "w+", encoding="UTF8")
# file.write("Hello World!\nHello Java\nHello Python!\nHello TypeScript\nHello Denis!\n")
# file.close()
#
# file = open("1.txt", "r", encoding="UTF8")
# some_str = file.read()
# file.close()
# some_str = some_str.split("\n")
# for elem in some_str:
#     if elem.endswith("!"):
#         print(elem)

# 2
# file = open("2.txt", "w+", encoding="UTF8")
# file.write("1 2 3 4 5 6 7 8 9 10")
# file.close()
#
# file = open("2.txt", "r", encoding="UTF8")
# some_str = file.read()
# file.close()
# temp = 1
# numbers = some_str.split(" ")
# for elem in numbers:
#     temp *= int(elem)
# temp = str(temp)
# file = open("2.txt", "w", encoding="UTF8")
# file.write(temp)
# file.close()
# 4
# file = open("questions.txt", "w+", encoding="UTF8")
# file.write("What is the name of the capital of the United States of America?\n")
# file.write("What is the name of the capital of Belarus?\n")
# file.write("What is the name of the capital of Germany\n")
# file.write("What is the name of the capital of Russia\n")
# file.write("What is the name of the capital of Italia\n")
# file.write("What is the name of the capital of Spain\n")
# file.write("What is the name of the capital of China?\n")
# file.write("What is the name of the capital of Turkey?\n")
# file.write("What is the name of the capital of India?\n")
# file.write("What is the name of the capital of Japan?")
# file.close()
# file = open("answers.txt", "w+", encoding="UTF8")
# file.write("Washington\n")
# file.write("Minsk\n")
# file.write("Berlin\n")
# file.write("Moscow\n")
# file.write("Rome\n")
# file.write("Madrid\n")
# file.write("Beijing\n")
# file.write("Ankara\n")
# file.write("Delhi\n")
# file.write("Tokyo")
# # file.close()
# file = open("questions.txt", "r", encoding="UTF8")
# questions = file.read()
# file.close()
# questions = questions.split("\n")
# file = open("answers.txt", "r", encoding="UTF8")
# answers = file.read()
# file.close()
# answers = answers.split("\n")
# count = 0
# correct_answers = dict(zip(questions, answers))
# for question, answer in correct_answers.items():
#     print(question)
#     my_answer = input()
#     if my_answer == answer:
#         print("It's correct")
#         count += 1
#     else:
#         print("It's wrong")
# print(count)
#
# 5
# import json
#
# dict1 = {
#     12345: ("Rick", 31),
#     23456: ("Nick", 21),
#     34567: ("Travis", 42),
#     45678: ("John", 41),
#     56789: ("Max", 32)
# }
#
# with open("5.json", "w", encoding="UTF-8") as file_dict:
#     json.dump(dict1, file_dict)
# 6