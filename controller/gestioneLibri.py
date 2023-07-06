import pickle

def inserisci_libro(data):
    with open('', 'ab') as file:
        pickle.dump(data, file)


def ricerca_libro(ISBN):
    try:
        with open('', 'rb') as f:
            while True:
                try:
                    data = pickle.load(f)
                    if data.get_ISBN() == ISBN:
                        return data
                except EOFError:
                    break
    except FileNotFoundError:
        print("Il file specificato non esiste.")
    except Exception as e:
        print(f"Si è verificato un errore: {str(e)}")

    return None


def modifica_libro(libro, new_data):
    with open('', 'rb') as f:
        objects = []
        while True:
            try:
                obj = pickle.load(f)
                if obj.get_ISBN() == libro.get_ISBN():
                    obj.set_autore(new_data['autore'])
                    obj.set_quantità(new_data['quantità'])
                    obj.set_titolo(new_data['titolo'])
                    obj.set_genere(new_data['genere'])
                objects.append(obj)
            except EOFError:
                break

    with open('', 'wb') as f:
        for obj in objects:
            pickle.dump(obj, f)


def elimina_libro(libro):
    with open('', 'rb') as f:
        objects = []
        while True:
            try:
                obj = pickle.load(f)
                if obj.get_ISBN() == libro.ISBN:
                    pass
                else:
                    objects.append(obj)
            except EOFError:
                break

    with open('', 'wb') as f:
        for obj in objects:
            pickle.dump(obj, f)