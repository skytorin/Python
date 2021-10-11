# Работа с JSON
# Сохраненеие данных в формате JSON на примере сейва настроек из игры
import json
filename = "My_Lesson_21_JSON_user_settings.txt"
myfile = open(filename, mode='w', encoding="Latin_1")
player1 = {
    'PlayerName': "Donald Dack",
    'Score': 345,
    'Awards': ["OR", "NV", "NY"]
}
player2 = {
    'PlayerName': "Vasya Pupkin",
    'Score': 347,
    'Awards': ["AR", "NB", "MW"]
}
myplayers = []
myplayers.append(player1)
myplayers.append(player2)
#--------------SAVE by JSON------------------
json.dump(myplayers, myfile)
myfile.close()

#--------------LOAD by JSON------------------
myfile = open(filename, mode='r', encoding="Latin_1")
json_data = json.load(myfile)
for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Awards N1: " + str(user['Awards'][0]))
    print("Player Awards N2: " + str(user['Awards'][1]))
    print("Player Awards N3: " + str(user['Awards'][2]))
    print("---------------------------\n\n")