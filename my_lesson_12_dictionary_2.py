#
enemy ={
         'loc_x': 70,
         'loc_y': 50,
         'color': 'green',
         'health': 100,
         'name': 'Mudillo',
         'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}
# Например необходимо создать 3 таких же справочника в массиве
all_enemies = []
all_enemies.append(enemy.copy())
all_enemies.append(enemy.copy())
all_enemies.append(enemy.copy())
print(all_enemies)

# А если нужно создать например 10 таких справочников
for x in range(0, 10):
    all_enemies.append(enemy.copy())
for ene in all_enemies:
    print(ene)

# Меняем в нашем массиве справочников некотрые значения некоторых итемов
all_enemies[5]['health'] = 30
all_enemies[8]['name'] = 'Kozel'
all_enemies[2]['loc_x'] = all_enemies[2]['loc_x'] + 10
all_enemies[2]['loc_y'] += 10
print('--------------------------------------------------------------------------')
for ene in all_enemies:
        print(ene)