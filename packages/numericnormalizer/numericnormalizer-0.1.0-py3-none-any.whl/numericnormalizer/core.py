import re
from typing import Optional, List

class NumericNormalizer(object):
    mappings: dict[str, dict[str, int]] = {}
    inverse_mappings: dict[str, dict[int, str]] = {}

    def __init__(self) -> None:
        # default supported languages are from Azure Language Detect languages:
        # https://learn.microsoft.com/en-us/azure/cognitive-services/language-service/language-detection/language-support
        self.register_mapping('en', {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10
        })

        self.register_mapping('pt', {
            'zero': 0,
            'um': 1,
            'dois': 2,
            'três': 3,
            'quatro': 4,
            'cinco': 5,
            'seis': 6,
            'sete': 7,
            'oito': 8,
            'nove': 9,
            'dez': 10
        })

        self.register_mapping('sq', {
            'zero': 0,
            'një': 1,
            'dy': 2,
            'tre': 3,
            'katër': 4,
            'pesë': 5,
            'gjashtë': 6,
            'shtatë': 7,
            'tetë': 8,
            'nëntë': 9,
            'dhjetë': 10
        })

        self.register_mapping('bg', {
            'нула': 0,
            'едно': 1,
            'две': 2,
            'три': 3,
            'четири': 4,
            'пет': 5,
            'шест': 6,
            'седем': 7,
            'осем': 8,
            'девет': 9,
            'десет': 10
        })

        self.register_mapping('km', {
            'សូន្យ': 0,
            'មួយ': 1,
            'ពីរ': 2,
            'បី': 3,
            'បួន': 4,
            'ប្រាំ': 5,
            'ប្រាំមួយ': 6,
            'ប្រាំពីរ': 7,
            'ប្រាំបី': 8,
            'ប្រាំបួន': 9,
            'ដប់': 10
        })

        self.register_mapping('zh_chs', {
            '零': 0,
            '一': 1,
            '二': 2,
            '三': 3,
            '四': 4,
            '五': 5,
            '六': 6,
            '七': 7,
            '八': 8,
            '九': 9,
            '十': 10
        })

        self.register_mapping('gl', {
            'cero': 0,
            'un': 1,
            'dous': 2,
            'tres': 3,
            'catro': 4,
            'cinco': 5,
            'seis': 6,
            'sete': 7,
            'oito': 8,
            'nove': 9,
            'dez': 10
        })

        self.register_mapping('kn', {
            'ಸೊನ್ನೆ': 0,
            'ಒಂದು': 1,
            'ಎರಡು': 2,
            'ಮೂರು': 3,
            'ನಾಲ್ಕು': 4,
            'ಐದು': 5,
            'ಆರು': 6,
            'ಏಳು': 7,
            'ಎಂಟು': 8,
            'ಒಂಬತ್ತು': 9,
            'ಹತ್ತು': 10
        })

        self.register_mapping('ps', {
            'صفر': 0,
            'یو': 1,
            'دوه': 2,
            'درې': 3,
            'څلور': 4,
            'پنځه': 5,
            'شپږ': 6,
            'اووه': 7,
            'اته': 8,
            'نه': 9,
            'لس': 10
        })

        self.register_mapping('pt', {
            'zero': 0,
            'um': 1,
            'dois': 2,
            'três': 3,
            'quatro': 4,
            'cinco': 5,
            'seis': 6,
            'sete': 7,
            'oito': 8,
            'nove': 9,
            'dez': 10
        })

        self.register_mapping('eu', {
            'hutsik': 0,
            'bat': 1,
            'bi': 2,
            'hiru': 3,
            'lau': 4,
            'bost': 5,
            'sei': 6,
            'zazpi': 7,
            'zortzi': 8,
            'bederatzi': 9,
            'hamar': 10
        })

        self.register_mapping('zh_cht', {
            '零': 0,
            '一': 1,
            '二': 2,
            '三': 3,
            '四': 4,
            '五': 5,
            '六': 6,
            '七': 7,
            '八': 8,
            '九': 9,
            '十': 10
        })

        self.register_mapping('as', {
            'শূন্য': 0,
            'এটা': 1,
            'দুটা': 2,
            'তিনি': 3,
            'চারি': 4,
            'পাঁচটা': 5,
            'ছয়টা': 6,
            'সাতটা': 7,
            'আটটা': 8,
            'নয়টা': 9,
            'দহ': 10
        })

        self.register_mapping('az', {
            'sıfır': 0,
            'bir': 1,
            'iki': 2,
            'üç': 3,
            'dörd': 4,
            'beş': 5,
            'altı': 6,
            'yeddi': 7,
            'səkkiz': 8,
            'doqquz': 9,
            'on': 10
        })

        self.register_mapping('ky', {
            'нөл': 0,
            'бир': 1,
            'эки': 2,
            'үч': 3,
            'төрт': 4,
            'беш': 5,
            'алты': 6,
            'жети': 7,
            'сегиз': 8,
            'тогуз': 9,
            'он': 10
        })

        self.register_mapping('zh', {
            '零': 0,
            '一': 1,
            '二': 2,
            '三': 3,
            '四': 4,
            '五': 5,
            '六': 6,
            '七': 7,
            '八': 8,
            '九': 9,
            '十': 10
        })

        self.register_mapping('ht', {
            'zero': 0,
            'yon': 1,
            'de': 2,
            'twa': 3,
            'kat': 4,
            'senk': 5,
            'sis': 6,
            'set': 7,
            'uit': 8,
            'nèf': 9,
            'dis': 10
        })

        self.register_mapping('ha', {
            'sifir': 0,
            'daya': 1,
            'biyu': 2,
            'uku': 3,
            'hudu': 4,
            'biyar': 5,
            'shida': 6,
            'bakwai': 7,
            'takwas': 8,
            'tara': 9,
            'goma': 10
        })

        self.register_mapping('af', {
            'nul': 0,
            'een': 1,
            'twee': 2,
            'drie': 3,
            'vier': 4,
            'vyf': 5,
            'ses': 6,
            'sewe': 7,
            'agt': 8,
            'nege': 9,
            'tien': 10
        })

        self.register_mapping('et', {
            'null': 0,
            'üks': 1,
            'kaks': 2,
            'kolm': 3,
            'neli': 4,
            'viis': 5,
            'kuus': 6,
            'seitse': 7,
            'kaheksa': 8,
            'üheksa': 9,
            'kümme': 10
        })

        self.register_mapping('ku', {
            'sıfır': 0,
            'yek': 1,
            'du': 2,
            'sê': 3,
            'çar': 4,
            'pênc': 5,
            'şeş': 6,
            'heft': 7,
            'heşt': 8,
            'neh': 9,
            'deh': 10
        })

        self.register_mapping('lo', {
            'ສູນ': 0,
            'ໜຶ່ງ': 1,
            'ສອງ': 2,
            'ສາມ': 3,
            'ສີ່': 4,
            'ຫ້າ': 5,
            'ຫົກ': 6,
            'ເຈັດ': 7,
            'ແປດ': 8,
            'ເກົ້າ': 9,
            'ສິບ': 10
        })

        self.register_mapping('sk', {
            'nula': 0,
            'jeden': 1,
            'dva': 2,
            'tri': 3,
            'štyri': 4,
            'päť': 5,
            'šesť': 6,
            'sedem': 7,
            'osem': 8,
            'deväť': 9,
            'desať': 10
        })

        self.register_mapping('so', {
            'khilaaf': 0,
            'kow': 1,
            'labo': 2,
            'sadex': 3,
            'afar': 4,
            'shan': 5,
            'lixaad': 6,
            'todobaad': 7,
            'siddeed': 8,
            'sagaal': 9,
            'toban': 10
        })

        self.register_mapping('ty', {
            'mu': 0,
            'henua': 1,
            'piti': 2,
            'toru': 3,
            'maha': 4,
            'pae': 5,
            'ono': 6,
            'fitu': 7,
            'valu': 8,
            'iva': 9,
            'tekau': 10
        })

        self.register_mapping('tt', {
            'нуль': 0,
            'бер': 1,
            'ике': 2,
            'үч': 3,
            'дүрт': 4,
            'биш': 5,
            'алты': 6,
            'жеты': 7,
            'сегез': 8,
            'тоңза': 9,
            'он': 10
        })

        self.register_mapping('ca', {
            'zero': 0,
            'u': 1,
            'dos': 2,
            'tres': 3,
            'quatre': 4,
            'cinc': 5,
            'sis': 6,
            'set': 7,
            'vuit': 8,
            'nou': 9,
            'deu': 10
        })

        self.register_mapping('hr', {
            'nula': 0,
            'jedan': 1,
            'dva': 2,
            'tri': 3,
            'četiri': 4,
            'pet': 5,
            'šest': 6,
            'sedam': 7,
            'osam': 8,
            'devet': 9,
            'deset': 10
        })

        self.register_mapping('rw', {
            'zero': 0,
            'rimwe': 1,
            'kabiri': 2,
            'gatatu': 3,
            'kane': 4,
            'gatanu': 5,
            'gatandatu': 6,
            'karindwi': 7,
            'umunani': 8,
            'icyenda': 9,
            'icumi': 10
        })

        self.register_mapping('ms', {
            'kosong': 0,
            'satu': 1,
            'dua': 2,
            'tiga': 3,
            'empat': 4,
            'lima': 5,
            'enam': 6,
            'tujuh': 7,
            'lapan': 8,
            'sembilan': 9,
            'sepuluh': 10
        })

        self.register_mapping('mn', {
            'тэг': 0,
            'нэг': 1,
            'хоёр': 2,
            'гурав': 3,
            'дөрөв': 4,
            'тав': 5,
            'зургаа': 6,
            'долоо': 7,
            'найм': 8,
            'ес': 9,
            'арван': 10
        })

        self.register_mapping('sl', {
            'nič': 0,
            'ena': 1,
            'dva': 2,
            'tri': 3,
            'štiri': 4,
            'pet': 5,
            'šest': 6,
            'sedem': 7,
            'osem': 8,
            'devet': 9,
            'deset': 10
        })

        self.register_mapping('es', {
            'cero': 0,
            'uno': 1,
            'dos': 2,
            'tres': 3,
            'cuatro': 4,
            'cinco': 5,
            'seis': 6,
            'siete': 7,
            'ocho': 8,
            'nueve': 9,
            'diez': 10
        })

        self.register_mapping('tk', {
            'nol': 0,
            'bir': 1,
            'iki': 2,
            'üç': 3,
            'dört': 4,
            'bäş': 5,
            'alty': 6,
            'ýedi': 7,
            'sekiz': 8,
            'dokuz': 9,
            'on': 10
        })

        self.register_mapping('dv', {
            'ހުސްގައި': 0,
            'އެއްޑީ': 1,
            'ދިވެހި': 2,
            'ތިރީ': 3,
            'މަތި': 4,
            'ދަން': 5,
            'ހަސްދު': 6,
            'ސެޓި': 7,
            'އޯގަސް': 8,
            'ނޫން': 9,
            'އަން': 10
        })

        self.register_mapping('ka', {
            'ნული': 0,
            'ერთი': 1,
            'ორი': 2,
            'სამი': 3,
            'ოთხი': 4,
            'ხუთი': 5,
            'ექვსი': 6,
            'შვიდი': 7,
            'რვა': 8,
            'ცხრა': 9,
            'ათი': 10
        })

        self.register_mapping('ml', {
            'പൂജ്യം': 0,
            'ഒന്ന്': 1,
            'രണ്ട്': 2,
            'മൂന്ന്': 3,
            'നാല്': 4,
            'അഞ്ച്': 5,
            'ആറ്': 6,
            'ഏഴ്': 7,
            'എട്ട്': 8,
            'ഒന്നാണ്': 9,
            'പത്ത്': 10
        })

        self.register_mapping('mr', {
            'शून्य': 0,
            'एक': 1,
            'दोन': 2,
            'तीन': 3,
            'चार': 4,
            'पाच': 5,
            'सहा': 6,
            'सात': 7,
            'आठ': 8,
            'नऊ': 9,
            'दहा': 10
        })

        self.register_mapping('sv', {
            'noll': 0,
            'en': 1,
            'två': 2,
            'tre': 3,
            'fyra': 4,
            'fem': 5,
            'sex': 6,
            'sju': 7,
            'åtta': 8,
            'nio': 9,
            'tio': 10
        })

        self.register_mapping('th', {
            'ศูนย์': 0,
            'หนึ่ง': 1,
            'สอง': 2,
            'สาม': 3,
            'สี่': 4,
            'ห้า': 5,
            'หก': 6,
            'เจ็ด': 7,
            'แปด': 8,
            'เก้า': 9,
            'สิบ': 10
        })

        self.register_mapping('lv', {
            'nulle': 0,
            'viens': 1,
            'divi': 2,
            'trīs': 3,
            'četri': 4,
            'pieci': 5,
            'seši': 6,
            'septiņi': 7,
            'astoņi': 8,
            'deviņi': 9,
            'desmit': 10
        })

        self.register_mapping('lt', {
            'nulis': 0,
            'vienas': 1,
            'du': 2,
            'trys': 3,
            'keturios': 4,
            'penkias': 5,
            'šešias': 6,
            'septynias': 7,
            'aštuonias': 8,
            'devynias': 9,
            'dešimt': 10
        })

        self.register_mapping('pl', {
            'zero': 0,
            'jeden': 1,
            'dwa': 2,
            'trzy': 3,
            'cztery': 4,
            'pięć': 5,
            'sześć': 6,
            'siedem': 7,
            'osiem': 8,
            'dziewięć': 9,
            'dziesięć': 10
        })

        self.register_mapping('ro', {
            'zero': 0,
            'unu': 1,
            'doi': 2,
            'trei': 3,
            'patru': 4,
            'cinci': 5,
            'șase': 6,
            'șapte': 7,
            'opt': 8,
            'nouă': 9,
            'zece': 10
        })

        self.register_mapping('sr', {
            'нула': 0,
            'један': 1,
            'два': 2,
            'три': 3,
            'четири': 4,
            'пет': 5,
            'шест': 6,
            'седам': 7,
            'осам': 8,
            'девет': 9,
            'десет': 10
        })

        self.register_mapping('hi', {
            'शून्य': 0,
            'एक': 1,
            'दो': 2,
            'तीन': 3,
            'चार': 4,
            'पांच': 5,
            'छह': 6,
            'सात': 7,
            'आठ': 8,
            'नौ': 9,
            'दस': 10
        })

        self.register_mapping('kk', {
            'нөл': 0,
            'бір': 1,
            'екі': 2,
            'үш': 3,
            'төрт': 4,
            'бес': 5,
            'алты': 6,
            'жеті': 7,
            'сегіз': 8,
            'тоғыз': 9,
            'он': 10
        })

        self.register_mapping('ne', {
            'शून्य': 0,
            'एक': 1,
            'दुई': 2,
            'तीन': 3,
            'चार': 4,
            'पाँच': 5,
            'छ': 6,
            'सात': 7,
            'आठ': 8,
            'नौ': 9,
            'दश': 10
        })

        self.register_mapping('su', {
            'nol': 0,
            'hiji': 1,
            'dua': 2,
            'tilu': 3,
            'opat': 4,
            'lima': 5,
            'genep': 6,
            'tujuh': 7,
            'dalapan': 8,
            'salapan': 9,
            'sapuluh': 10
        })

        self.register_mapping('te', {
            'సున్నా': 0,
            'ఒకటి': 1,
            'రెండు': 2,
            'మూడు': 3,
            'నాలుగు': 4,
            'ఐదు': 5,
            'ఆరు': 6,
            'ఏడు': 7,
            'ఎనిమిది': 8,
            'తొమ్మిది': 9,
            'పది': 10
        })

        self.register_mapping('ti', {
            'ምልክት': 0,
            'ኣንድ': 1,
            'ሁለት': 2,
            'ሶስት': 3,
            'አራት': 4,
            'አምስት': 5,
            'ስድስት': 6,
            'ሰባት': 7,
            'ስምንት': 8,
            'ዘጠኝ': 9,
            'አስር': 10
        })

        self.register_mapping('cs', {
            'nula': 0,
            'jedna': 1,
            'dva': 2,
            'tři': 3,
            'čtyři': 4,
            'pět': 5,
            'šest': 6,
            'sedm': 7,
            'osm': 8,
            'devět': 9,
            'deset': 10
        })

        self.register_mapping('la', {
            'nulla': 0,
            'ūnus': 1,
            'duo': 2,
            'trēs': 3,
            'quattuor': 4,
            'quīnque': 5,
            'sex': 6,
            'septem': 7,
            'octō': 8,
            'novem': 9,
            'decem': 10
        })

        self.register_mapping('nn', {
            'null': 0,
            'ein': 1,
            'to': 2,
            'tre': 3,
            'fire': 4,
            'fem': 5,
            'seks': 6,
            'sju': 7,
            'åtte': 8,
            'ni': 9,
            'ti': 10
        })

        self.register_mapping('sd', {
            'صفر': 0,
            'هڪ': 1,
            'ٻين': 2,
            'تين': 3,
            'چار': 4,
            'پنج': 5,
            'ٻه': 6,
            'سات': 7,
            'آٽه': 8,
            'نو': 9,
            'ده': 10
        })

        self.register_mapping('si', {
            'හතර': 0,
            'එක': 1,
            'දෙක': 2,
            'තුන': 3,
            'හතරක්': 4,
            'පහ': 5,
            'හය': 6,
            'හත': 7,
            'අසූත්': 8,
            'නවය': 9,
            'දහය': 10
        })

        self.register_mapping('sw', {
            'sifuri': 0,
            'moja': 1,
            'mbili': 2,
            'tatu': 3,
            'nne': 4,
            'tano': 5,
            'sita': 6,
            'saba': 7,
            'nane': 8,
            'tisa': 9,
            'kumi': 10
        })

        self.register_mapping('cy', {
            'dim': 0,
            'un': 1,
            'dau': 2,
            'tri': 3,
            'pedwar': 4,
            'pump': 5,
            'chwech': 6,
            'saith': 7,
            'wyth': 8,
            'naw': 9,
            'deg': 10
        })

        self.register_mapping('yo', {
            'ọ̀kan': 1,
            'meji': 2,
            'meta': 3,
            'merin': 4,
            'marun': 5,
            'mefa': 6,
            'meje': 7,
            'mejo': 8,
            'mesan': 9,
            'mewa': 10,
            'ọ̀dọ́': 0
        })

        self.register_mapping('jv', {
            'nol': 0,
            'siji': 1,
            'loro': 2,
            'telu': 3,
            'papat': 4,
            'lima': 5,
            'enem': 6,
            'pitu': 7,
            'wolu': 8,
            'songo': 9,
            'sepuluh': 10
        })

        self.register_mapping('fi', {
            'nolla': 0,
            'yksi': 1,
            'kaksi': 2,
            'kolme': 3,
            'neljä': 4,
            'viisi': 5,
            'kuusi': 6,
            'seitsemän': 7,
            'kahdeksan': 8,
            'yhdeksän': 9,
            'kymmenen': 10
        })

        self.register_mapping('no', {
            'null': 0,
            'en': 1,
            'to': 2,
            'tre': 3,
            'fire': 4,
            'fem': 5,
            'seks': 6,
            'syv': 7,
            'åtte': 8,
            'ni': 9,
            'ti': 10
        })

        self.register_mapping('fa', {
            'صفر': 0,
            'یک': 1,
            'دو': 2,
            'سه': 3,
            'چهار': 4,
            'پنج': 5,
            'شش': 6,
            'هفت': 7,
            'هشت': 8,
            'نه': 9,
            'ده': 10
        })

        self.register_mapping('tr', {
            'sıfır': 0,
            'bir': 1,
            'iki': 2,
            'üç': 3,
            'dört': 4,
            'beş': 5,
            'altı': 6,
            'yedi': 7,
            'sekiz': 8,
            'dokuz': 9,
            'on': 10
        })

        self.register_mapping('uz', {
            'нол': 0,
            'бир': 1,
            'икки': 2,
            'уч': 3,
            'тўрт': 4,
            'беш': 5,
            'олти': 6,
            'етти': 7,
            'саккиз': 8,
            'туққиз': 9,
            'ўн': 10
        })

        self.register_mapping('vi', {
            'không': 0,
            'một': 1,
            'hai': 2,
            'ba': 3,
            'bốn': 4,
            'năm': 5,
            'sáu': 6,
            'bảy': 7,
            'tám': 8,
            'chín': 9,
            'mười': 10
        })

        self.register_mapping('co', {
            'zeru': 0,
            'unu': 1,
            'dui': 2,
            'trè': 3,
            'quattru': 4,
            'cinque': 5,
            'sei': 6,
            'sette': 7,
            'ottu': 8,
            'novi': 9,
            'diece': 10
        })

        self.register_mapping('am', {
            'ዜሮ': 0,
            'አንድ': 1,
            'ሁለት': 2,
            'ሶስት': 3,
            'አራት': 4,
            'አምስት': 5,
            'ስድስት': 6,
            'ሰባት': 7,
            'ስምንት': 8,
            'ዘጠኝ': 9,
            'አስር': 10
        })

        self.register_mapping('hy', {
            'զրո': 0,
            'մեկ': 1,
            'երկու': 2,
            'երեք': 3,
            'չորս': 4,
            'հինգ': 5,
            'վեց': 6,
            'յոթ': 7,
            'ութ': 8,
            'ինը': 9,
            'տասը': 10
        })

        self.register_mapping('be', {
            'нуль': 0,
            'адзін': 1,
            'два': 2,
            'тры': 3,
            'чатыры': 4,
            'пяць': 5,
            'шэсць': 6,
            'сем': 7,
            'восем': 8,
            'дзевяць': 9,
            'дзесяць': 10
        })

        self.register_mapping('ru', {
            'ноль': 0,
            'один': 1,
            'два': 2,
            'три': 3,
            'четыре': 4,
            'пять': 5,
            'шесть': 6,
            'семь': 7,
            'восемь': 8,
            'девять': 9,
            'десять': 10
        })

        self.register_mapping('tg', {
            'нуқта': 0,
            'як': 1,
            'ду': 2,
            'се': 3,
            'чор': 4,
            'панҷ': 5,
            'шаш': 6,
            'ҳафт': 7,
            'ҳашт': 8,
            'нӯҳ': 9,
            'даҳ': 10
        })

        self.register_mapping('yua', {
            'baxal': 0,
            'juno': 1,
            'kaab': 2,
            'ox': 3,
            'kan': 4,
            'hoon': 5,
            'wuk': 6,
            'hu': 7,
            'ya': 8,
            'bolon': 9,
            'lahun': 10
        })

        self.register_mapping('bn', {
            'শূন্য': 0,
            'এক': 1,
            'দুই': 2,
            'তিন': 3,
            'চার': 4,
            'পাঁচ': 5,
            'ছয়': 6,
            'সাত': 7,
            'আট': 8,
            'নয়': 9,
            'দশ': 10
        })

        self.register_mapping('da', {
            'nul': 0,
            'en': 1,
            'to': 2,
            'tre': 3,
            'fire': 4,
            'fem': 5,
            'seks': 6,
            'syv': 7,
            'otte': 8,
            'ni': 9,
            'ti': 10
        })

        self.register_mapping('de', {
            'null': 0,
            'eins': 1,
            'zwei': 2,
            'drei': 3,
            'vier': 4,
            'fünf': 5,
            'sechs': 6,
            'sieben': 7,
            'acht': 8,
            'neun': 9,
            'zehn': 10
        })

        self.register_mapping('gu', {
            'શૂન્ય': 0,
            'એક': 1,
            'બે': 2,
            'ત્રણ': 3,
            'ચાર': 4,
            'પાંચ': 5,
            'છ': 6,
            'સાત': 7,
            'આઠ': 8,
            'નવ': 9,
            'દસ': 10
        })

        self.register_mapping('ig', {
            'ọ': 0,
            'ọ̀kà': 1,
            'èjìrè': 2,
            'èta': 3,
            'ènì': 4,
            'isii': 5,
            'asaa': 6,
            'asato': 7,
            'asaaọkụ': 8,
            'itoolu': 9,
            'iri': 10
        })

        self.register_mapping('ga', {
            'neamhní': 0,
            'aon': 1,
            'dó': 2,
            'trí': 3,
            'ceathair': 4,
            'cúig': 5,
            'sé': 6,
            'seacht': 7,
            'ocht': 8,
            'naoi': 9,
            'deich': 10
        })

        self.register_mapping('ja', {
            '零': 0,
            '一': 1,
            '二': 2,
            '三': 3,
            '四': 4,
            '五': 5,
            '六': 6,
            '七': 7,
            '八': 8,
            '九': 9,
            '十': 10
        })

        self.register_mapping('lb', {
            'null': 0,
            'eent': 1,
            'zwee': 2,
            'dräi': 3,
            'véier': 4,
            'fënnef': 5,
            'sechs': 6,
            'siwen': 7,
            'uecht': 8,
            'néng': 9,
            'zéng': 10
        })

        self.register_mapping('otq', {
            'lū': 0,
            'tasi': 1,
            'lua': 2,
            'tolu': 3,
            'fa': 4,
            'nima': 5,
            'ono': 6,
            'fitu': 7,
            'valu': 8,
            'siva': 9,
            'fulu': 10
        })

        self.register_mapping('to', {
            'nonga': 0,
            'taha': 1,
            'ua': 2,
            'tolu': 3,
            'fā': 4,
            'nima': 5,
            'ono': 6,
            'fitu': 7,
            'valu': 8,
            'hiva': 9,
            'fulu': 10
        })

        self.register_mapping('uk', {
            'нуль': 0,
            'один': 1,
            'два': 2,
            'три': 3,
            'чотири': 4,
            'п\'ять': 5,
            'шість': 6,
            'сім': 7,
            'вісім': 8,
            'дев\'ять': 9,
            'десять': 10
        })

        self.register_mapping('yi', {
            'נול': 0,
            'איין': 1,
            'צוויי': 2,
            'דריי': 3,
            'פיר': 4,
            'פונף': 5,
            'זעקס': 6,
            'זיבן': 7,
            'אַכט': 8,
            'נייַן': 9,
            'צען': 10
        })

        self.register_mapping('prs', {
            'صفر': 0,
            'یک': 1,
            'دو': 2,
            'سه': 3,
            'چهار': 4,
            'پنج': 5,
            'شش': 6,
            'هفت': 7,
            'هشت': 8,
            'نه': 9,
            'ده': 10
        })

        self.register_mapping('nl', {
            'nul': 0,
            'een': 1,
            'twee': 2,
            'drie': 3,
            'vier': 4,
            'vijf': 5,
            'zes': 6,
            'zeven': 7,
            'acht': 8,
            'negen': 9,
            'tien': 10
        })

        self.register_mapping('is', {
            'núll': 0,
            'einn': 1,
            'tveir': 2,
            'þrír': 3,
            'fjórir': 4,
            'fimm': 5,
            'sex': 6,
            'sjö': 7,
            'átta': 8,
            'níu': 9,
            'tíu': 10
        })

        self.register_mapping('it', {
            'zero': 0,
            'uno': 1,
            'due': 2,
            'tre': 3,
            'quattro': 4,
            'cinque': 5,
            'sei': 6,
            'sette': 7,
            'otto': 8,
            'nove': 9,
            'dieci': 10
        })

        self.register_mapping('mg', {
            'efa': 0,
            'iray': 1,
            'roa': 2,
            'telo': 3,
            'efatra': 4,
            'dimy': 5,
            'enina': 6,
            'fito': 7,
            'valo': 8,
            'sivy': 9,
            'folo': 10
        })

        self.register_mapping('mi', {
            'kore': 0,
            'tahi': 1,
            'rua': 2,
            'toru': 3,
            'whā': 4,
            'rima': 5,
            'ono': 6,
            'whitu': 7,
            'waru': 8,
            'iwa': 9,
            'tekau': 10
        })

        self.register_mapping('pa', {
            'ਸਿਫ਼ਰ': 0,
            'ਇੱਕ': 1,
            'ਦੋ': 2,
            'ਤਿੰਨ': 3,
            'ਚਾਰ': 4,
            'ਪੰਜ': 5,
            'ਛੇ': 6,
            'ਸੱਤ': 7,
            'ਅੱਠ': 8,
            'ਨੌਂ': 9,
            'ਦਸ': 10
        })
        self.register_mapping('ta', {
            'பூஜ்யம்': 0,
            'ஒன்று': 1,
            'இரண்டு': 2,
            'மூன்று': 3,
            'நான்கு': 4,
            'ஐந்து': 5,
            'ஆறு': 6,
            'ஏழு': 7,
            'எட்டு': 8,
            'ஒன்பது': 9,
            'பத்து': 10
        })

        self.register_mapping('xh', {
            'engama-0': 0,
            'engama-1': 1,
            'engama-2': 2,
            'engama-3': 3,
            'engama-4': 4,
            'engama-5': 5,
            'engama-6': 6,
            'engama-7': 7,
            'engama-8': 8,
            'engama-9': 9,
            'engama-10': 10
        })

        self.register_mapping('ar', {
            'صفر': 0,
            'واحد': 1,
            'اثنان': 2,
            'ثلاثة': 3,
            'أربعة': 4,
            'خمسة': 5,
            'ستة': 6,
            'سبعة': 7,
            'ثمانية': 8,
            'تسعة': 9,
            'عشرة': 10
        })

        self.register_mapping('he', {
            'אפס': 0,
            'אחד': 1,
            'שניים': 2,
            'שלושה': 3,
            'ארבעה': 4,
            'חמישה': 5,
            'ששה': 6,
            'שבעה': 7,
            'שמונה': 8,
            'תשעה': 9,
            'עשרה': 10
        })

        self.register_mapping('ko', {
            '영': 0,
            '일': 1,
            '이': 2,
            '삼': 3,
            '사': 4,
            '오': 5,
            '육': 6,
            '칠': 7,
            '팔': 8,
            '구': 9,
            '십': 10
        })

        self.register_mapping('mk', {
            'нула': 0,
            'еден': 1,
            'два': 2,
            'три': 3,
            'четири': 4,
            'пет': 5,
            'шест': 6,
            'седум': 7,
            'осум': 8,
            'девет': 9,
            'десет': 10
        })

        self.register_mapping('sm', {
            'leai se mea': 0,
            'tasi': 1,
            'lua': 2,
            'tolu': 3,
            'fa': 4,
            'lima': 5,
            'ono': 6,
            'fitu': 7,
            'valu': 8,
            'iva': 9,
            'fulu': 10
        })

        self.register_mapping('zu', {
            'engama-0': 0,
            'engama-1': 1,
            'engama-2': 2,
            'engama-3': 3,
            'engama-4': 4,
            'engama-5': 5,
            'engama-6': 6,
            'engama-7': 7,
            'engama-8': 8,
            'engama-9': 9,
            'engama-10': 10
        })

        self.register_mapping('fr', {
            'zéro': 0,
            'un': 1,
            'deux': 2,
            'trois': 3,
            'quatre': 4,
            'cinq': 5,
            'six': 6,
            'sept': 7,
            'huit': 8,
            'neuf': 9,
            'dix': 10
        })

        self.register_mapping('id', {
            'nol': 0,
            'satu': 1,
            'dua': 2,
            'tiga': 3,
            'empat': 4,
            'lima': 5,
            'enam': 6,
            'tujuh': 7,
            'delapan': 8,
            'sembilan': 9,
            'sepuluh': 10
        })

        self.register_mapping('iu', {
            'ᐊᒪᐃᑦ': 0,
            'ᐊᐃ': 1,
            'ᑌᓯᔭᐅᓐ': 2,
            'ᒪᓇᑦ': 3,
            'ᐅᑕᓗᐊᖅ': 4,
            'ᓄᓇ': 5,
            'ᓇᒃᑯᓇᖅ': 6,
            'ᐊᑦᑐᖅ': 7,
            'ᐱᕙᓪᓕᐊᖅ': 8,
            'ᐅᖃᓕᐊᖅ': 9,
            'ᒐᓯᕙᓪᓕᐊᖅ': 10
        })

        self.register_mapping('or', {
            'ଶୂନ୍ୟ': 0,
            'ଏକ': 1,
            'ଦୁଇ': 2,
            'ତିନି': 3,
            'ଚାରି': 4,
            'ପାଞ୍ଚ': 5,
            'ଛଅ': 6,
            'ସାତ': 7,
            'ଆଠ': 8,
            'ନଅ': 9,
            'ଦଶ': 10
        })

        self.register_mapping('sn', {
            'kubva kuna': 0,
            'motsi': 1,
            'pachena': 2,
            'tatu': 3,
            'china': 4,
            'shanu': 5,
            'tanhatu': 6,
            'nhanhano': 7,
            'sva': 8,
            'chironda': 9,
            'gumi': 10
        })

        self.register_mapping('tl', {
            'wala': 0,
            'isa': 1,
            'dalawa': 2,
            'tatlo': 3,
            'apat': 4,
            'lima': 5,
            'anim': 6,
            'pito': 7,
            'walo': 8,
            'siyam': 9,
            'sampu': 10
        })
        self.register_mapping('bo', {
            'གྲངས་ཀ་': 0,
            'གཅིག་པ་': 1,
            'གཉིས་པ་': 2,
            'གསུམ་པ་': 3,
            'བཞི་པ་': 4,
            'ལྔ་པ་': 5,
            'བདུན་པ་': 6,
            'བརྒྱད་པ་': 7,
            'དགུ་པ་': 8,
            'བརྒྱ་ཆ་': 9,
            'བཅུ་གཉིས་': 10
        })

        self.register_mapping('bs', {
            'nula': 0,
            'jedan': 1,
            'dva': 2,
            'tri': 3,
            'četiri': 4,
            'pet': 5,
            'šest': 6,
            'sedam': 7,
            'osam': 8,
            'devet': 9,
            'deset': 10
        })

        self.register_mapping('my', {
            'သုံး': 0,
            'တစ်': 1,
            'နှစ်': 2,
            'သုံးလေး': 3,
            'လေး': 4,
            'ငါး': 5,
            'ခြောက်လေး': 6,
            'ခုနစ်': 7,
            'ရှစ်': 8,
            'ကိုး': 9,
            'တစ်ဆယ်': 10
        })

        self.register_mapping('el', {
            'μηδέν': 0,
            'ένα': 1,
            'δύο': 2,
            'τρία': 3,
            'τέσσερα': 4,
            'πέντε': 5,
            'έξι': 6,
            'επτά': 7,
            'οκτώ': 8,
            'εννέα': 9,
            'δέκα': 10
        })

        self.register_mapping('mww', {
            'tsis muaj': 0,
            'ib': 1,
            'ob': 2,
            'peb': 3,
            'pluag': 4,
            'hauv': 5,
            'lauj': 6,
            'xyeej': 7,
            'yim': 8,
            'cuaj': 9,
            'tas': 10
        })

        self.register_mapping('eo', {
            'nul': 0,
            'unu': 1,
            'du': 2,
            'tri': 3,
            'kvar': 4,
            'kvin': 5,
            'ses': 6,
            'sep': 7,
            'ok': 8,
            'naŭ': 9,
            'dek': 10
        })

        self.register_mapping('fj', {
            'vosa nula': 0,
            'vosa dua': 1,
            'vosa rua': 2,
            'vosa tolu': 3,
            'vosa va': 4,
            'vosa lima': 5,
            'vosa ono': 6,
            'vosa vitu': 7,
            'vosa walu': 8,
            'vosa ciwa': 9,
            'vosa tini': 10
        })

        self.register_mapping('hu', {
            'nulla': 0,
            'egy': 1,
            'kettő': 2,
            'három': 3,
            'négy': 4,
            'öt': 5,
            'hat': 6,
            'hét': 7,
            'nyolc': 8,
            'kilenc': 9,
            'tíz': 10
        })

        self.register_mapping('mt', {
            'żero': 0,
            'wieħed': 1,
            'tnejn': 2,
            'tlieta': 3,
            'erbgħa': 4,
            'ħamsa': 5,
            'sitta': 6,
            'sebgħa': 7,
            'tmienja': 8,
            'disgħa': 9,
            'għaxra': 10
        })

        self.register_mapping('ur', {
            'صفر': 0,
            'ایک': 1,
            'دو': 2,
            'تین': 3,
            'چار': 4,
            'پانچ': 5,
            'چھ': 6,
            'سات': 7,
            'آٹھ': 8,
            'نو': 9,
            'دس': 10
        })

    def register_mapping(self, lang: str, mapping: dict[str, int]):
        self.mappings[lang] = mapping
        self.inverse_mappings[lang] = {v: k for k, v in mapping.items()}

    def get_word_number_mapping(
            self,
            lang: str = 'en'
        ) -> dict[str, int]:
        mapping: dict[str, int] = self.mappings.get(lang)
        if not mapping:
            raise NotImplementedError(f"Unsupported lang `{lang}`")
        return mapping

    def get_number_word_mapping(
            self,
            lang: str = 'en'
        ) -> dict[int, str]:
        mapping: dict[int, str] = self.inverse_mappings.get(lang)
        if not mapping:
            raise NotImplementedError(f"Unsupported lang `{lang}`")
        return mapping

    def number_to_word(
            self,
            number: int,
            lang: str = 'en') -> Optional[str]:
        return self.get_number_word_mapping(lang).get(number)

    def word_to_number(
            self,
            word: str,
            lang: str = 'en') -> Optional[int]:
        return self.get_word_number_mapping(lang).get(word)
    
    def get_supported_words(
            self,
            lang: str = 'en',
            max_number: int = None) -> List[str]:
        return [k for k, v in self.get_word_number_mapping(lang).items() if max_number is None or v < max_number]
    
    def get_supported_numbers(
            self,
            lang: str = 'en',
            max_number: int = None) -> List[int]:
        return [v for _, v in self.get_word_number_mapping(lang).items() if max_number is None or v < max_number]
    
    def get_supported_numbers_as_str(
            self,
            lang: str = 'en',
            max_number: int = None) -> List[int]:
        return [str(v) for _, v in self.get_word_number_mapping(lang).items() if max_number is None or v < max_number]

    def format_sentence(
            self,
            sentence: str,
            lang: str,
            formatting: str = "{word} ({number})",
            max_number: int = None) -> str:
        # Replace worded version with digits
        word_pattern = re.compile(r'\b(?:' + '|'.join(self.get_supported_words(
            lang=lang,
            max_number=max_number
        )) + r')\b', re.IGNORECASE)
        sentence = word_pattern.sub(lambda x: str(self.word_to_number(
            word=x.group().lower(),
            lang=lang)
        ), sentence)

        def format(**kwargs) -> str:
            formatted = formatting
            for k, v in kwargs.items():
                formatted = re.sub(fr"{{{k}}}", str(v), formatted)
            return formatted

        # append the word to the digits
        digit_pattern = re.compile(r'\b(?:' + '|'.join(self.get_supported_numbers_as_str(
            lang=lang,
            max_number=max_number
        )) + r')\b')
        sentence = digit_pattern.sub(lambda x: format(
            word=self.number_to_word(int(x.group()), lang),
            number=int(x.group())
        ), sentence)

        return sentence
