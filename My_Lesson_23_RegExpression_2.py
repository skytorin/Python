# Парсинг файла
import re

input_filename = "./My_Lesson_23_RegExpression_2_infile.txt"
output_filename = "./My_Lesson_23_RegExpression_2_outfile.txt"

inputfile = open(input_filename, mode='r', encoding='Latin-1')
outfile = open(output_filename, mode='w', encoding='Latin-1')
mytext = inputfile.read()

lookfor = r"[\w.-]+@(?!yandex)[A-Za-z]+\.ru"

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    outfile.write(item + "\n")

print("Total: " + str(len(results)))

