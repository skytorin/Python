# Создание функции для заболнения библиотеки
def create_record(name, telephone, address):
    """Create Record"""
    record = {
        'name': name,
        'telephone': telephone,
        'address': address
    }
    return  record

user1 = create_record("Vasya", "+7955123456789", "Moscow")
user2 = create_record("Petya", "+7944987654321", "London")

print(user1)
print(user2)


# Функция с возмозностью указания произвольного кол-ва персон, заранее не определенных (указывается в конце определения)
def give_award(medal, *persons):
    """Give Medal to persons"""
    for person in persons:
        print("Tovarish " + person.title() + " nagrajdaetsya medaliyu " + medal)

give_award("Za Berlin", "Vasya", "petya")
give_award("Za London", "petya", "alexander", "Valentin")







