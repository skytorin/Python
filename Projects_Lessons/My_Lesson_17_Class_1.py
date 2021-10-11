# Выполняем импорт функций из другого файла
from My_Lesson_17_Class_Hero import *
# ----------- MAIN --------------------------------
myhero1 = My_Lesson_17_Class_Hero("Vurdalak", 5, "Orc")
myhero2 = My_Lesson_17_Class_Hero("Alexander", 4, "Human")

myhero1.show_hero()
myhero2.show_hero()
myhero1.level_up()
myhero2.level_up()
myhero1.move()
myhero2.move()
myhero1.set_health(70)
myhero2.set_health(40)
myhero1.show_hero()
myhero2.show_hero()