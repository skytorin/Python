name = "vasya"
sername = "pupkin"
stroka = "Bla Bla Bla"

print("name\n sername\n stroka")
print(name.title()+ "\n" +sername.upper()+"\n\n" +stroka)
print("----------------------------------------------------")

a = " ...... dadyaVasya ,,,,, "
a = a.strip()
a = a.rstrip(",")
a = a.lstrip(".")
print(a.strip())