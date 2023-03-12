import csv
import random

with open('sentences.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    sentences = list(reader)
    random_sentence = random.choice(sentences)[0]

print(random_sentence)
