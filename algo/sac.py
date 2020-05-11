from algo.RLAlgorithm import RLAlgorithm

class SACAlgorithm(RLAlgorithm):

    def __init__(self, n_epochs=1000):
        super().__init__(n_epochs=n_epochs)
        