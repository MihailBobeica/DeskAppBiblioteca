import pickle


def visualizza_operatori():
    with open('../view/Operatori.pickle', 'rb') as file:
        dati = pickle.load(file)
    dati.stampa()

if __name__ == '__main__':
    visualizza_operatori()