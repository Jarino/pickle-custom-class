import pickle

with open('custom_class.pickle', 'rb') as f:
    cc = pickle.load(f)

print('Pickle loaded, model: {}'.format(cc.model))
