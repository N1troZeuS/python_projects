from transliterate import translit
from num2words import num2words

print(translit("Greetings to all! Here is the text in English. The result of the program is the pronunciation of each word in English in Russian letters! To understand how it works, try changing this text to something else! Made by Inspire! P. S. In the lines of code below you can specify numbers, their pronunciation in English in Russian letters will be the result of the code! I really hope you figure it out!", 'ru'))

print("78 - " + translit(num2words(78, lang='en'), 'ru'))
print("15 - " + translit(num2words(15, lang='en'), 'ru'))
print("3 - " + translit(num2words(3, lang='en'), 'ru'))
print("40 - " + translit(num2words(40, lang='en'), 'ru'))
print("8 - " + translit(num2words(8, lang='en'), 'ru'))