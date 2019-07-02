import itertools
import collections
import scipy.sparse
print('loading corpus')
sentences = []
with open(r"..\data\processed\corpus.csv", encoding='utf-8') as file:
    for line in file:
        line = line.rstrip()
        tokens = line.split('!#!')
        sentences.append(tokens)
sentences = sentences[:100000]
vocabulary = list(
    sorted(
        list(
            set(
                list(
                    itertools.chain.from_iterable(sentences)
                )
            )
        )
)
)
print('computing probability distributions')
distribution_dict = {}
for word in vocabulary:
    for sentence in sentences:
        if ((word in sentence) & (word != '<END>')):
            index = sentence.index(word)
            next_word = sentence[index+1]
            if word not in distribution_dict:
                distribution_dict[word] = collections.Counter({next_word : 1})
            else:
                distribution_dict[word].update([next_word])
print('filling probability distribution matrix')
distribution_matrix = scipy.sparse.csr_matrix((len(vocabulary),len(vocabulary)))
for i,word_vocabulary in enumerate(vocabulary):
    if word_vocabulary != '<END>':
        current_word_counter = distribution_dict[word_vocabulary]
        for word,count in current_word_counter.items():
            distribution_matrix[i,vocabulary.index(word)] = count
distribution_matrix[vocabulary.index('<END>'),vocabulary.index('<END>')] = 1
print('normalizing the probability distribution matrix')
for i in range(len(vocabulary)):
    distribution_matrix[i,:] = distribution_matrix[i,:] / distribution_matrix[i,:].sum()
print('saving the model')
with open(r"..\models\vocabulary.txt", "w", encoding='utf-8') as output:
    for word in vocabulary:
        output.write(word + '\n')
scipy.sparse.save_npz(r"..\models\model.npz", distribution_matrix, compressed=True)
print('completed')
