# EXPERIMENT STEPS

# 1. Visualize Word Embeddings
embedding_weights = model.layers[0].get_weights()[0]
embedding_weights = model1.layers[0].get_weights()[0]
# Ensure 'deep' is in the tokenizer's vocabulary before trying to access its embedding
if 'deep' in tokenizer.word_index:
    print("Embedding for word 'deep':", embedding_weights[tokenizer.word_index['deep']])
else:
    print("Word 'deep' not in the tokenizer's vocabulary.")
# 2. Compare Similarity
from numpy import dot
from numpy.linalg import norm

def cosine_sim(a, b):
    return dot(a, b) / (norm(a) * norm(b))

vec1 = embedding_weights[tokenizer.word_index['deep']]
vec2 = embedding_weights[tokenizer.word_index['learning']]
print("Similarity:", cosine_sim(vec1, vec2))

# 3. Vary Embedding Dimension
# Change output_dim (e.g., 2, 4, 8, 50) and observe:
embedding_dims = [2, 4, 8, 50]

for dim in embedding_dims:
    print(f"\n=== Embedding dimension: {dim} ===")
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=dim, input_length=padded.shape[1], name="embedding")
    ])
    embedding_matrix = model.layers[0].get_weights()[0]
    print("Shape of embedding matrix:", embedding_matrix.shape)
    print("First 3 word vectors:\n", embedding_matrix[1:4])  # skip 0 (padding), show first 3 words
    # Show embedding for first input sentence
    output = model.predict(padded[:1])
    print("Embedding output shape for first sentence:", output.shape)
    print("Embedding output for first sentence:\n", output)

# 4. Unknown words
new_sentence = ["Deep learning with bananas is amazing"]
new_seq = tokenizer.texts_to_sequences(new_sentence)
print("Tokenized new sentence: ", new_seq)

padded_new_seq = pad_sequences(new_seq, maxlen=padded_way1.shape[1], padding='post')
print("Padded new sequence: ", padded_new_seq)

embedding_output = model1.predict(padded_new_seq)
print("Embedding output: ", embedding_output)

embedding_matrix = model1.layers[0].get_weights()[0]
print("Embedding for unknown (OOV) token: ", embedding_matrix[0])

# 5. Visualize in 2D
import matplotlib.pyplot as plt

words = list(tokenizer.word_index.keys())
vectors = embedding_weights[1:len(words)+1]  # skip 0 index

plt.scatter(vectors[:,0], vectors[:,1])
for i, word in enumerate(words):
    plt.annotate(word, (vectors[i,0], vectors[i,1]))
plt.show()

# 6. Inspect Padding
print("Padded sequences:\n", padded)
print("Tokenizer word index:", tokenizer.word_index)
print("\nWhich numbers are zero (padding)? In padded sequences, 0 means padding.")
embedding_matrix = model.layers[0].get_weights()[0]
print("Embedding for padding token (index 0):", embedding_matrix[0])

# Show all embeddings for a sentence, highlighting padding
print("\nEmbeddings for the first sentence (each row is a word or padding):")
for idx, word_idx in enumerate(padded[0]):
    if word_idx == 0:
        print(f"Position {idx}: [PAD] -> {embedding_matrix[0]}")
    else:
        for word, i in tokenizer.word_index.items():
            if i == word_idx:
                print(f"Position {idx}: {word} -> {embedding_matrix[word_idx]}")
                break

# 7. Change a Single Word
print("\n--- Changing a single word in a sentence ---")
original_sentence = "machine learning is fun"
new_sentence = "machine learning is great"  # changed 'fun' to 'great' (possibly OOV)

seq_orig = tokenizer.texts_to_sequences([original_sentence])
seq_new = tokenizer.texts_to_sequences([new_sentence])
pad_orig = pad_sequences(seq_orig, maxlen=padded.shape[1], padding='post')
pad_new = pad_sequences(seq_new, maxlen=padded.shape[1], padding='post')

embed_orig = model.predict(pad_orig)
embed_new = model.predict(pad_new)

print(f"Original sentence: '{original_sentence}'\nPadded: {pad_orig}")
print(f"New sentence:      '{new_sentence}'\nPadded: {pad_new}")

print("\nEmbedding vectors for original sentence:")
print(embed_orig[0])

print("\nEmbedding vectors for new sentence (compare last row):")
print(embed_new[0])

# Compare the last word's embedding (should be different if 'great' is in vocab, or padding index if not)
print("\nWas 'great' in the vocabulary?")
if tokenizer.word_index.get('great', None):
    print("Yes, here's its embedding:", embedding_matrix[tokenizer.word_index['great']])
else:
    print("No, 'great' is unknown, so its integer index is 0 and its embedding is the same as padding:", embedding_matrix[0])

# 8. Manual Vector Example
import numpy as np
v1 = np.array([1, 2])
v2 = np.array([2, 4])
print("Cosine similarity:", cosine_sim(v1, v2))

