from googletrans import Translator
from rest_framework.decorators import api_view
from rest_framework.response import Response

translater = Translator()


def detect_source_language(text):
    det = str(translater.detect(text))
    return det[14:det.find(",")]


def confidence(text):
    text = str(translater.detect(text))
    return float(text[text.rindex("=") + 1:len(text) - 1])

def translate_to(text, source, destination):
    translation = translater.translate(text, src=source, dest=destination)
    string_translation = str(translation)
    translated_text = str(translation)[
                      string_translation.find("text=") + 5: string_translation.find("pronunciation=") - 2]
    return translated_text

@api_view(['POST'])
def translate_text(request):
    text = request.data.get('text', '')
    destination_language = request.data.get('destination_language', '')

    source = detect_source_language(text)
    conf = confidence(text)
    translation = translate_to(text, source, destination_language)
    destination = destination_language

    response_data = {
        'source': source,
        'confidence': conf,
        'translation': translation,
        'destination': destination,
    }
    return Response(response_data)


# @api_view(['GET'])
# def get_languages(request):
#     translator = Translator()
#
#     def get_translation(language_name, dest_lang):
#         if dest_lang == 'en':
#             return language_name
#         return translator.translate(language_name, dest=dest_lang).text
#
#     languages_list = []
#     a = 1
#     for code, language in LANGUAGES.items():
#         print(a)
#         a = a + 1
#         english_name = language
#         uzbek_name = get_translation(language, 'uz')
#         russian_name = get_translation(language, 'ru')
#
#         languages_list.append({
#             'code': code,
#             'names': {
#                 'en': english_name,
#                 'uz': uzbek_name,
#                 'ru': russian_name,
#             }
#         })
#
#     return Response(languages_list)
