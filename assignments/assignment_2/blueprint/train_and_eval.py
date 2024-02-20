from sklearn.metrics import roc_auc_score

def train(model, dataloader, criterion, optimizer):
    raise NotImplementedError
    return loss

def evaluate(model, dataloader, criterion):
    raise NotImplementedError
    return loss, auroc