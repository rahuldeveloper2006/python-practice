#generate different random sentences
import random
subjects=['he','she','they','the cat','my friends']
verbs=['eates','palys','writes','reades','watches']
objects=['a book','the guiter','pizza','a movie','the news paper']
#now we generate random sentence
subject=random.choice(subjects)
verb=random.choice(verbs)
object=random.choice(objects)
sentence=f"{subject} {verb} {object}."
print(sentence)