# Importing the reqiured libraries
from transformers import AutoTokenizer, AutoModelForSequenceClassification, \
                         TrainingArguments, Trainer
from transformers import BertConfig, AlbertConfig, DistilBertConfig, RobertaConfig, XLNetConfig, DebertaConfig, DebertaV2Config, MegaConfig, GPT2Config, BigBirdConfig
from transformers import BertTokenizerFast

from sklearn.metrics import classification_report
from transformers import AutoModelForSequenceClassification

# Use data_collector to convert our samples to PyTorch tensors and concatenate them with the correct amount of padding
from transformers import DataCollatorWithPadding

# Define a new Trainer with all the objects we constructed so far
from transformers import TrainingArguments, Trainer

from datasets import load_dataset
import numpy as np

from evaluate import load
import datetime
import warnings
warnings.filterwarnings("ignore")


def compute_metric(eval_pred):
    '''
    : Loading the metric to use.
    '''
    #load_accuracy = load_metric("accuracy")
    #load_f1 = load_metric("f1")
    #load_precision = load_metric('precision')
    load_recall = load('recall')
    
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    #accuracy = load_accuracy.compute(predictions=predictions, references=labels)["accuracy"]
    #f1_score = load_f1.compute(predictions=predictions, references=labels)["f1"]
    #precision = load_precision.compute(predictions=predictions, references=labels)["precision"]
    recall = load_recall.compute(predictions=predictions, references=labels)["recall"]
    return {"recall": recall}

class Final_model:
    def __init__(self, max_length, dropout, hidden_layer, num_heads, activation, model_used, 
                 vocab_size, path, lr, weight, epochs, tokenizer_file, tokenizer, train_data, test_data):
        self.max_length = max_length
        self.dropout = dropout
        self.hidden_layer = hidden_layer
        self.num_heads = num_heads
        self.activation = activation
        self.model_used = model_used
        self.vocab_size = vocab_size
        self.path = path
        self.lr = lr
        self.weight = weight
        self.epochs = epochs
        self.tokenizer_file = tokenizer_file
        self.tokenizer = tokenizer
        self.train_data = train_data
        self.test_data = test_data
        
    def loading_train_dataset(self):
        '''
        : Converting the train dataset into the format that is 
        : required by the transformers model
        '''
        dataset_train = load_dataset("csv", data_files={"train":[f'./{self.train_data}']})

        return dataset_train
    
    def loading_test_dataset(self):
        '''
        : Converting the test dataset into the format that is 
        : required by the transformers model
        '''
        dataset_test = load_dataset("csv", data_files={"test": [f'./{self.test_data}']})
        return dataset_test
    
    def tokenize_function(self, examples):
        '''
        : Tokenizing the words and converting into input ids
        '''
        self.tokenizer = BertTokenizerFast(tokenizer_file= f"./{self.tokenizer_file}")
        result = self.tokenizer(examples["text"], max_length=self.max_length)
        if self.tokenizer.is_fast:
            result["word_ids"] = [result.word_ids(i) for i in range(len(result["input_ids"]))]
        return result
    
    def configuring_model(self, dropout, hidden_layer, num_heads, activation, model_used):
        '''
        : Custom model configurations.
        : Can create multiple models in different configurations
        : Models used:
                     - BERT
                     - AlBERT
                     - DistilBERT
                     - RoBERTa
                     - XLNet
                     - XLNet_large
                     - BERT_large
                     - DeBERTa
                     - DeBERTaV2
                     - BigBird
                     - GPT2
                     - MegatronBERT
        : To see models config use modelConfig() class
        : To do: More models can be added
        '''
        if self.model_used == 'BERT':
            my_config = BertConfig(attention_probs_dropout_prob= self.dropout, hidden_dropout_prob= self.dropout,
                                   hidden_act= f"{self.activation}", num_attention_heads= self.num_heads,
                                   num_hidden_layers= self.hidden_layer, vocab_size= self.vocab_size)
            
            my_config.save_pretrained(save_directory=f"{self.path}")
            
            model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased', num_labels= 2, config = f"{self.path}/config.json")
        elif self.model_used == 'AlBERT':
            my_config = AlbertConfig(attention_probs_dropout_prob=self.dropout, hidden_dropout_prob=self.dropout,
                                     hidden_act= f"{self.activation}", num_attention_heads= self.num_heads,
                                     num_hidden_layers= self.hidden_layer, vocab_size= self.vocab_size)
            
            my_config.save_pretrained(save_directory=f"{self.path}")
            
            model = AutoModelForSequenceClassification.from_pretrained('albert-base-v2', num_labels= 2, config = f"{self.path}/config.json")
        elif self.model_used == 'DistilBERT':
            my_config = DistilBertConfig(attention_dropout= self.dropout, dropout= self.dropout,
                                         activation= f"{self.activation}", n_heads= self.num_heads,
                                         n_layers= self.hidden_layer, vocab_size= self.vocab_size)
            
            my_config.save_pretrained(save_directory= f"{self.path}")
            
            model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels = 2, config = f"{self.path}/config.json")
        elif self.model_used == 'RoBERTa':
            my_config = RobertaConfig(attention_probs_dropout_prob= self.dropout, hidden_dropout_prob= self.dropout,
                                      hidden_act= f"{self.activation}", num_attention_heads= self.num_heads,
                                      num_hidden_layers= self.hidden_layer, vocab_size= self.vocab_size)
            
            my_config.save_pretrained(save_directory=f"{self.path}")
            
            model = AutoModelForSequenceClassification.from_pretrained('roberta-base', num_labels = 2, config = f"{self.path}/config.json")
        elif self.model_used == 'XLNet':
            my_config = XLNetConfig(dropout= self.dropout, ff_activation= f"{self.activation}",
                                    n_layer= self. hidden_layer, n_head= self.num_heads,
                                    vocab_size= self.vocab_size)
            
            my_config.save_pretrained(save_directory=f"{self.path}")
            
            model = AutoModelForSequenceClassification.from_pretrained('xlnet-base-cased', num_labels = 2, config = f"{self.path}/config.json")
        elif self.model_used == 'XLNet_large':
            my_config = XLNetConfig(dropout= self.dropout, ff_activation= f"{self.activation}",
                                    n_layer= self. hidden_layer, n_head= self.num_heads,
                                    vocab_size= self.vocab_size)
            
            my_config.save_pretrained(save_directory=f"{self.path}")
            
            model = AutoModelForSequenceClassification.from_pretrained('xlnet-large-cased', num_labels = 2, config = f"{self.path}/config.json")
        elif self.model_used == 'BERT_large':
            my_config = BertConfig(attention_probs_dropout_prob= self.dropout, hidden_dropout_prob= self.dropout,
                                   hidden_act= f"{self.activation}", num_attention_heads= self.num_heads,
                                   num_hidden_layers= self.hidden_layer, vocab_size= self.vocab_size)
            
            my_config.save_pretrained(save_directory=f"{self.path}")
            
            model = AutoModelForSequenceClassification.from_pretrained('bert-large-uncased', num_labels= 2, config = f"{self.path}/config.json")
        elif self.model_used == 'DeBERTa':
            my_config = DebertaConfig(attention_probs_dropout_prob= self.dropout, hidden_act= f"{self.activation}",
                                      hidden_dropout_prob= self.dropout, pooler_hidden_act=f"{self.activation}",
                                      vocab_size=self.vocab_size, num_attention_heads= self.num_heads, pooler_dropout= self.dropout,
                                      num_hidden_layers= self.hidden_layer)
            my_config.save_pretrained(save_directory=f"{self.path}")
        elif self.model_used == 'DeBERTaV2':
            my_config = DebertaV2Config(attention_probs_dropout_prob=self.dropout, hidden_act= f"{self.activation}",
                                        hidden_dropout_prob= self.dropout, pooler_dropout=self.dropout,
                                        vocab_size=self.vocab_size, num_attention_heads=self.num_heads,
                                        num_hidden_layers= self.hidden_layer)
            my_config.save_pretrained(save_directory=f"{self.path}")
        elif self.model_used == 'BigBird':
            my_config = BigBirdConfig(attention_probs_dropout_prob=self.dropout, hidden_act=f'{self.activation}',
                                      hidden_dropout_prob=self.dropout, num_attention_heads=self.num_heads,
                                      num_hidden_layers=self.hidden_layer, vocab_size=self.vocab_size)
            my_config.save_pretrained(save_directory=f"{self.path}")
        elif self.model_used == 'GPT2':
            my_config = GPT2Config(attn_pdrop=self.dropout, embd_pdrop=self.dropout, n_head=self.num_heads,
                                   n_layer=self.hidden_layer, vocab_size=self.vocab_size, activation_function=f"{self.activation}")
            my_config.save_pretrained(save_directory=f'{self.path}')
        elif self.model_used == 'Mega':
            my_config = MegaConfig(attention_probs_dropout_prob=self.dropout, hidden_dropout_prob=self.dropout, activation=self.activation,
                                   num_hidden_layers=self.num_heads, nffn_hidden_size=self.hidden_layer, vocab_size=self.vocab_size)
            my_config.save_pretrained(save_directory=f"{self.path}")
        return model
        
    def data_collat(self):
        '''
        : Data collators are objects that will form a batch by using a list of dataset elements as input. 
        : These elements are of the same type as the elements of train_dataset or eval_dataset.
        : To be able to build batches, data collators may apply some processing (like padding). 
        '''
        data_collator = DataCollatorWithPadding(tokenizer= self.tokenizer, max_length= self.max_length)
        return data_collator
        
    def args(self):
        '''
        : Training arguments for the model.
        : Using this, the model can be trained.
        '''
        training_args = TrainingArguments(output_dir= f"./OUTPUT/{datetime.datetime.now()}",
                                                 overwrite_output_dir=True,
                                                 do_train= True,
                                                 do_eval= True,
                                                 do_predict= True,
                                                 auto_find_batch_size= True,
                                                 learning_rate= self.lr,
                                                 weight_decay= self.weight,
                                                 save_strategy='epoch',
                                                 #per_device_train_batch_size=16,
                                                 #per_device_eval_batch_size=16,
                                                 seed = 2023,
                                                 #bf16= True,
                                                 fp16= True,
                                                 num_train_epochs= self.epochs)
        return training_args
    
    def getting_train_data(self):
        '''
        : Using the tokenizer on train dataset to get the data to use 
        '''
        dataset_train = self.loading_train_dataset()
        tokenized_datasets_train = dataset_train.map(self.tokenize_function, batched=True)

        tokenized_train = tokenized_datasets_train['train']

        return tokenized_train
    
    def getting_test_data(self):
        '''
        : Using the tokenizer on test dataset to get the data to use
        '''
        dataset_test = self.loading_test_dataset()
        tokenized_datasets_test = dataset_test.map(self.tokenize_function, batched=True)
        tokenized_test = tokenized_datasets_test['test']
        return tokenized_test

    def model_trainer(self):
        '''
        : Initializing the trainer 
        '''
        trainer = Trainer(model= self.configuring_model(self.dropout, self.hidden_layer, self.num_heads, self.activation, self.model_used),
                          data_collator= self.data_collat(),
                          train_dataset= self.getting_train_data(),
                          eval_dataset= self.getting_test_data(),
                          #tokenizer= self.tokenize_function(),
                          args= self.args(),
                          compute_metrics= compute_metric)
        return trainer

    
    def main(self):
        training = self.model_trainer()
        training.train()
        training.evaluate()
        predictions = training.predict(self.getting_test_data()) # predictions
        print(classification_report(self.getting_test_data()['label'], predictions.predictions.argmax(axis =-1)))
        