import pickle

class AbstractCustom():

    def train(self):
        assert False, "Not implemented"


class CustomClass(AbstractCustom):
    def __init__(self, name):
        self.name = name
    
    def train(self):
        self.model = {
            'a': 1,
            'b': 2,
            'c': 3
        }
        print('Model {} natrenovany'.format(self.name))


if __name__ == '__main__':
    with open('custom_class.pickle', 'wb') as f:
        from custom_class import CustomClass
        cc = CustomClass('jarinov model')
        cc.train()
        pickle.dump(cc, f)
        print('pickle dumped')

