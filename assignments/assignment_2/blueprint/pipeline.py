import argparse
import sys
import os
# adds the blueprint dir to your path to allow the imports below
sys.path.append(os.path.dirname(os.getcwd()))

from blueprint.model import CNN
from blueprint.dataloader import CustomDataset
from blueprint.train_and_eval import train, evaluate
from blueprint.utils import read_yaml_json_to_dict

def main(config: dict) -> None:
    # config extraction
    dl_config = config['dataloader']
    train_config = config['train']
    eval_config = config['eval']

    # data loading

    # training loop

    # final evaluation
    test_loss, test_auroc = evaluate(model, test_dataloader, criterion)
    print(f"Test Loss: {test_loss:.4f}, Test AUROC: {test_auroc:.4f}")
    return

# DO NOT MODIFY THE CODE BELOW
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Run ML pipeline')
    parser.add_argument('config_file', type=str)
    args = parser.parse_args()
    config = read_yaml_json_to_dict(args.config_file)
    main(config)