import abc

class RLAlgorithm:

    def __init__(self,
                n_epochs=1000,
                ):
        self._n_epochs = n_epochs

    @abc.abstractmethod
    def train(self):
        pass
    
    @abc.abstractmethod
    def evaluate(self):
        pass
        