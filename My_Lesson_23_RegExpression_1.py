# Работа с регулярными выражениями, поиск по шаблону
import re

mytext = "Vasya ddddd 2000 wwwwwwww, 1972: dsffsfdf, aaaa@mail.ru" \
         "fdfdsfdsfsdff@Vb.com, 1999, 434343343, Nick, Kolya, 555" \
         "1777.ru, 2004, dfdsfssf , 1983, 66666666666, 1@ackom.net" \
         "ea@hotmail.gov, 2005, 43555555 привет,  привет, 201f25f"
"""
\d = Any Digit [0-9]
\D = Any non DIGIT
\w = Any Alphabet symbol [A-Z a-z]
\W = Any non Alphabet symbol
\s = Backspace
\S = non Backspace
"""
#textlookfor = r"mail"
#textlookfor = r"\d\d\d"
#textlookfor = r"[0-9]{3}"
#textlookfor = r"\w{6}\s"
#textlookfor = r"[A-Z][a-z]+"
textlookfor = r"@\w+\.\w+"

allresults = re.findall(textlookfor, mytext)

print (allresults)

