#from googletrans import Translator

#trans = Translator()
#t = trans.translate(
#    'hello', src= 'en', dest='de'
#)
#print(f'Source: {t.src}')
#print(f'Destination: {t.dst}')
#print(f'{t.origon} -> {t.text}')
from deep_translator import GoogleTranslator
import codecs
langs_list = GoogleTranslator.get_supported_languages()
langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)
print(langs_dict)
translated = GoogleTranslator(source='auto', target='afrikaans').translate_file('C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-en_0.html')
print(translated)
f = codecs.open('C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af0.html', 'w', 'utf-8')
f.write(translated)
f.close