# Practice 1
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Embedding

sentences = [
    "machine learning is fun",
    "deep learning is powerful",
    "artificial intelligence is the future",
    "learning never stops"
]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
output_token = tokenizer.texts_to_sequences(sentences)

print("Vocabulary: ", tokenizer.word_index)
print("Integer sequences: ", output_token)

padded_senten = pad_sequences(output_token)

model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=8, input_length=padded_senten.shape[1])
])

output_final = model.predict(padded_senten)

print("Final output is: ", output_final)

# Practice 2
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding

texts = [
    "Natural language processing is fascinating",
    "Neural networks can learn complex patterns",
    "Keras makes deep learning accessible",
    "Embeddings turn words into vectors"
]

tokenizer = Tokenizer() # implement the function first
tokenizer.fit_on_texts(texts) # fit that function on to our texts
output_senten = tokenizer.texts_to_sequences(texts) # from texts to sequences

padded_way1 = pad_sequences(output_senten, padding='post')
padded_way2 = pad_sequences(output_senten, maxlen=3)

vocab_size = len(tokenizer.word_index) + 1
embed_dim1 = 6
embed_dim2 = 4

model1 = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embed_dim1, input_length=padded_way1.shape[1])
])
output_model1 = model1.predict(padded_way1)

model2 = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embed_dim2, input_length=padded_way2.shape[1])
])
output_model2 = model2.predict(padded_way2)

print("Padded way 1 is: ", padded_way1)
print("Padded way 2 is: ", padded_way2)
print("Shape of embedding output 1 is: ", output_model1.shape)
print("Shape of embedding output 2 is: ", output_model2.shape)
print("Embedding vectors for the 1st sentence - model 1: ", output_model1[0])
print("Embedding vectors for the 1st sentence - model 2: ", output_model2[0])

# Bonus exploration
print("what each integer represents: ", tokenizer.word_index)

