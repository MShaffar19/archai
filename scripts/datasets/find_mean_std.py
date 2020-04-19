from archai.common.config import Config
from archai.datasets import data
from torchvision import transforms
from archai.common.ml_utils import channel_norm

if __name__ == '__main__':
    conf = Config(config_filepath='confs/datasets/cifar10.yaml')

    conf_data = conf['dataset']

    ds_provider = data.create_dataset_provider(conf_data)

    train_ds, _ = ds_provider.get_datasets(True, False,
        transforms.Compose([transforms.Resize((32,32)), transforms.ToTensor()]),
        transforms.Compose([]))

    print(channel_norm(train_ds))

    exit(0)