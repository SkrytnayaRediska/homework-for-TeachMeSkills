import json
import pandas


def Language_search (sl):
    st = input('Select a language: ')
    for dicts in sl:
        for key, value in dicts.items():  # а без функции работает!
            if key == 'languages' and st in value:
                print([i for i in {k: v for k, v in dicts.items() if k == 'name'}.values()])

    Online()


def Research_name(data, name = ''):
    for dicts in data:
        for key, value in dicts.items():
            if key == 'name' and value == name:
                return { k : v for k, v in dicts.items() }
    else:
        return 'Person not found!'


def Name_search ():
    with open('first_assignment.json', 'r') as f:
        print(f"Search result: {Research_name(json.load(f), input('input name: ').title())}")
    Online()


def Add (sl):
    sl_add = {
        "name": input('input Name: ').title(),
        "birthday": input('input your birthday: '),
        "height": input('input your height: '),
        "weight": input('input your  weight: '),
        "car": True if input('Do you have a car: ') == 'yes' else False,
        "languages": [input('What languages do you know: ').title() for i in
                      range(0, int(input('How many languages do you know?: ')))]

    }
    print('\n')
    sl.append(sl_add)

    with open('first_assignment.json', 'w') as f:
        json.dump(sl, f, indent=3)

    Online()


def Json_to_csv(sl):  # 1 json to csv
    pandas.DataFrame(sl).to_csv('first.assigment.csv')
    print('Executed!!!\n')


def Online():
    print('Shall we continue(yes/no)?')
    if input('Make a choice: ') == 'no':
        exit()
    else:
        print(end= '\n')
        pass


def Menu(sl):
    print(f'1: Would you like to add your dates?:\n2: Do you want to find data by name(yes/no)?:\n3: Well look for people by language(yes/no)?:\n''4: Json_to_csv ')
    choice = input('Make a choice(1, 2, 3, 4 or exit! ): ')

    if choice == '1':
        Add(sl)

    if choice == '2':
        Research_name(sl)

    if choice == '3':
        Language_search(sl)

    if choice == '4':
        Json_to_csv(sl)

    if choice == 'exit':
        exit()

# def Research_language(langs, lang):
#     for dicts in langs:
#         for key, value in dicts.items():
#             if key == 'languages' and lang in value:
#                 return [i for i in {k:v for k,v in dicts.items() if k == 'name'}.values()]  не работает не понимаю почему ищет, но толкьо первое вхождние!!!
#     else:
#         return 'This language is not detected!!'





data = """
    [
        {
            "name": "John Smith",
            "birthday": "02.10.1990",
            "height": 175,
            "weight": 76.5,
            "car": true,
            "languages": ["C++", "Python"]
        },
        {
            "name": "Alexey Alexeev",
            "birthday": "05.06.1986",
            "height": 197,
            "weight": 101.2,
            "car": false,
            "languages": ["Pascal", "Delphi"]
        },
        {
            "name": "Maria Ivanova",
            "birthday": "28.08.1998",
            "height": 165,
            "weight": 56.1,
            "car": true,
            "languages": ["C#", "C++", "C"]
        }
    ]
    """
sl = json.loads(data)
with open('first_assignment.json', 'w') as file:
    json.dump(sl, file, indent=3)

while True:
    Menu(sl)





























