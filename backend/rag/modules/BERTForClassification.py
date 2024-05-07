import keras
class BERTForClassification(keras.Model):

    def __init__(self, bert_model, num_classes):
        super().__init__()
        self.bert = bert_model
        self.bert.trainable = False
        self.fc1 = keras.layers.Dense(256, activation='relu')
        self.fc2 = keras.layers.Dense(30, activation='relu')
        self.fc3 = keras.layers.Dense(num_classes, activation='softmax')

    def call(self, inputs):
        x = self.bert(inputs)[1]
        x = self.fc1(x)
        x = self.fc2(x)
        return self.fc3(x)