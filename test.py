from transformers import BertConfig, BertModel

configuration = BertConfig()
model = BertModel(configuration)
configuration = model.config
