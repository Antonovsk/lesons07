""" Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку

разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
Фраза может состоять из одного слова, если во фразе несколько слов, 
то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите "Парам пам-пам",
если с ритмом все в порядке и "Пам парам", если с ритмом все не в порядке

Ввод: пара-ра-рам рам-пам-папой па-ра-по-дам

Вывод: Парам пам-пам """

def check_rhythm(poem):
  phrases = poem.split()
  syllables_in_phrase = []
  for phrase in phrases:
    syllables = 0
    for word in phrase.split('-'):
      syllables += sum(1 for letter in word if letter in 'аеиоуыэюяАЕИОУЫЭЮЯ')
    syllables_in_phrase.append(syllables)
  if len(set(syllables_in_phrase)) == 1:
    return "Парам пам-пам"
  else:
    return "Пам парам"

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)



