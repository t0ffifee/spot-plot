from operator import index
import pickle
import json

def save_dic(d, name):
    with open(f'{name}.pkl', 'wb') as f:
        pickle.dump(d, f)

def open_dic(name):
    with open(f'{name}.pkl', 'rb') as f:
        loaded_dict = pickle.load(f)
    return loaded_dict

def save_json(object, name):
    with open(name, 'w') as f:
        json.dump(object, f, indent=2)

def open_json(name):
    f = open(name)
    return json.load(f)