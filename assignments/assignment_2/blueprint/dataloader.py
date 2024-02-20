from keras.utils import Sequence

class CustomDataset(Sequence):
    def __init__(self, data, labels):
        raise NotImplementedError

    def __len__(self):
        # this function returns the length of your dataset
        raise NotImplementedError

    def __getitem__(self, idx): 
        # this function returns an item from the dataset given its index
        # implement any additional preprocessing steps in this function
        # such as downsampling
        raise NotImplementedError
        return X, y