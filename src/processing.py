import csv
import utils
sentences = []
with open(r'..\data\raw\corpus_raw.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        text = utils.normalizer(row['SOSPECHA_DIAGNOSTICA'])
        tokens = text.split(' ')
        tokens = [token for token in tokens if token != '']
        tokens.append('<END>')
        tokens.insert(0, '<START>')
        sentence = '!#!'.join(tokens)
        if len(sentence) > 0:
            sentences.append(sentence)
with open(r"..\data\processed\corpus.csv", "w", encoding='utf-8') as output:
    for sentence in sentences:
        output.write(sentence + '\n')

