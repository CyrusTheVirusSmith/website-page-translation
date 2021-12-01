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
#langs_list = GoogleTranslator.get_supported_languages()
#langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)
#print(langs_dict)

tbg = GoogleTranslator(source='auto', target='bg').translate_file('java_app_text.txt')
tbn = GoogleTranslator(source='auto', target='bn').translate_file('java_app_text.txt')


#print(translated)
f = codecs.open('java_app_text-bg.txt', 'w', 'utf-8')
f.write(tbg)
f.close
f = codecs.open('java_app_text-bn.txt', 'w', 'utf-8')
f.write(tbn)
f.close