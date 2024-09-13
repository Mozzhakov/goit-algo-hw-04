from pathlib import Path

with open('pets_data.txt', 'w', encoding="utf-8") as file:
    file.write('60b90c1c13067a15887e1ae1,Tayson,3\n')
    file.write('60b90c2413067a15887e1ae2,Vika,1\n')
    file.write('60b90c2e13067a15887e1ae3,Barsik,2\n')
    file.write('60b90c3b13067a15887e1ae4,Simon,12\n')
    file.write('60b90c4613067a15887e1ae5,Tessi,5')

path_to_pets = Path('pets_data.txt')

def get_cats_info(path):
    try:
        with open(path, 'r', encoding="utf-8") as pets_data:
            pets_list = []
            for line in pets_data:
                cat_id, name, age = line.strip().split(',')
                pet_dict = {'id': cat_id, 'name': name, "age": age}
                pets_list.append(pet_dict)
            print(pets_list)           
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occured: {e}")

get_cats_info(path_to_pets)