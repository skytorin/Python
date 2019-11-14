#         (----item----)
#         (key)  (value)
enemy ={
         'loc_x': 70,
         'loc_y': 50,
         'color': 'green',
         'health': 100,
         'name': 'Mudillo',
}
print(enemy)
print("Location X = " + str(enemy['loc_x']))
print("Location Y = " + str(enemy['loc_y']))
print("His NAME is = " + enemy['name'])

# Вывод всех ключей итемов
print(enemy.keys())
# Вывод всех значений итемов
print(enemy.values())

# Добавляем новый итем с  ключем и значением в справочник
enemy['rank'] = 'Admiral'
print(enemy)

# Удаление итема
del enemy['rank']
print(enemy)

# Изенение итемов и проверка некоторых значений
enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'
print(enemy)










