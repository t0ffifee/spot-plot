import pickle

def save_dic(d, name):
    with open(f'{name}.pkl', 'wb') as f:
        pickle.dump(d, f)

def open_dic(name):
    with open(f'{name}.pkl', 'rb') as f:
        loaded_dict = pickle.load(f)
    return loaded_dict