import json

FILE_PATH = 'data.json'

def get_data():
    with open (FILE_PATH) as file:
        return json.load(file)
id = 4
def id_():
    global id 
    id += 1
    return id
def creat():
    data = get_data()
    new = {
        'id': id_(), 
        "brand":input('enter brand of product: '), 
        "model":input('enter model of product: '), 
        "year":int(input('enter year of product: ')), 
        "description":input('enter description of product: '), 
        "price":round(float(input('enter price of product: ')),2)
    } 

    data.append(new)
    with open (FILE_PATH, 'w') as file:
        json.dump(data, file)
    return 'The product was added!'

def listing():
    data = get_data()
    for i in data:
        print(f'{i}\n')
    with open (FILE_PATH, 'w') as file:
        json.dump(data, file)
    return 'listed'

def retrieve():
    data = get_data()
    
    id_ = int(input('enter id of product: '))
    
    product = list(filter(lambda x: x['id'] == id_, data))[0]
    
    if product: return product 
    else: return 'The product not found'



def update():
    data = get_data()
    print(data)
    id = int(input('enter id of product: '))
    update = list(filter(lambda x: x['id'] == id, data))[0]

    indx = data.index(update)
    choice = input('what do u wanna change?\nModel - 1, Description - 2, Year - 3, Price - 4\nEnter: ')

    if choice == '1':
        data[indx]['model'] = input('enter new model: ')
    elif choice == '2':
        data[indx]['description'] = input('enter new descripion: ')
    elif choice == '3':
        data[indx]['year'] = int(input('enter new year: '))
    elif choice == '4':
        data[indx]['price'] = round(float(input('enter new price: ')), 2)
    
    else:
        return 'cancel!'

    with open (FILE_PATH, 'w') as file:
        json.dump(data, file)

    return 'changed'
        

def delete():
    data = get_data()
    id = int(input('enter id of product: '))
    prod = list(filter(lambda x: x ['id'] == id, data))
    if not prod:
        return 'No such  product'
    indx = data.index(prod[0])
    data.pop(indx)
    json.dump(data, open(FILE_PATH, 'w'))
    return 'the product was deleted!'
