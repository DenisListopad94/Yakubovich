# 1

# import re

# pattern = r"\bcat\s\b"
# your_str = " Cat catfish cat Cat cat category africate"
# cats = re.findall(pattern, your_str, re.IGNORECASE)
# print(cats)

# 2

# import re

# pattern = r"\bz\S{3}z\b"
# your_str = " zzzzz"
# z = re.findall(pattern, your_str)
# print(z)

# 3

# import re

# pattern = r"\b[8|9]\d{9}\b"
# your_str = "8123456781 9123456781"
# numbers = re.findall(pattern, your_str)
# print(numbers)

# 4

# import re
#
# pattern = r"\b[eyuioa]\S+\b"
# your_str = "eerrer dfs wer we sad qw 12e l l;sa d ASF SAF"
# numbers = re.findall(pattern, your_str, re.IGNORECASE)
# print(numbers)


# 5

# import re
#
# pattern = r"[-+]?\d+"
# your_str = "8123456781 9123456781"
# numbers = re.findall(pattern, your_str)
# print(numbers)

# 6

# import re

# result = re.sub(r"[H|h]uman", "computer", "human is the human, is the Human")
# print(result)

# 7

# import re
#
# pattern = r"\d\d\/\d\d\/\d{4}"
# your_str = "28/06/2005"
# numbers = re.findall(pattern, your_str)
# print(numbers)

# import re
#
# pattern = r"\d[[.|b]|[b|.]]"
# your_str = "asd b asd b asdb sdsdfgb"
# numbers = re.findall(pattern, your_str)
# print(numbers)