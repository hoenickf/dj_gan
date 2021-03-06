from pipeline.ExampleGen import ExampleGen
from pipeline.StatisticGen import StatisticGen

from pipeline.Trainer import Trainer
from pipeline.Transformer import Transformer

train_raw_path, test_raw_path = ExampleGen(use_cache=False, max_examples=200)()
stats = StatisticGen(train_raw_path)()
train_transformed_path, test_transformed_path = Transformer([train_raw_path, test_raw_path], stats)()
Trainer(
    train_transformed_path,
    test_transformed_path,
    steps_per_epoch=50,
    epochs=50,
    steps_per_validation=10
)()