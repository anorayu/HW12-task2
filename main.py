from pymystem3 import Mystem

m = Mystem()
text = "Ваш текст здесь"
words = text.split()[-10:]
lemmas = m.lemmatize(" ".join(words))
print(lemmas)



