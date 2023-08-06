# numericnormalizer
 
This is a basic library used for NLP that can perform conversions between numbers in numerical format and alphabetical / character format.

## Installation
`pip install numericnormalizer`

## Usage
### importing the module
```Python
from numericnormalizer import normalizer
```

### Convert a number to a word (i.e. 5 -> 'five')
```Python
normalizer.number_to_word(5, lang='en')
>> "five"


normalizer.number_to_word(5, lang='zh')
>> "五"
```

### Convert a word to a number (i.e. 'five' -> 5)
```Python
normalizer.word_to_number('five', lang='en')
>> 5


normalizer.number_to_word('五', lang='zh')
>> 5
```

### Format numbers in a sentence
#### Example 1: default formatting
```Python
normalizer.format_sentence(
    sentence='What are the 6 principles of intercultural adaption?',
    lang='zh'
)
>> "What are the six (6) principles of intercultural adaption?"
```

#### Example 2: Custom Formatting
```Python
normalizer.format_sentence(
    sentence='I have 4 apples and five oranges.',
    lang='zh',
    formatting='{number} [{word}]',  # custom formatting
)
>> "I have 4 [four] apples and 5 [five] oranges."
```

#### Example 3: Number restricting
```Python
normalizer.format_sentence(
    sentence='I have 4 apples and five oranges.',
    lang='zh',
    max_number=4  # restrict the max_number
)
>> "I have four (4) apples and five oranges."
```

## Language Support
The supported languages are from the [Azure Language Detect List](https://learn.microsoft.com/en-us/azure/cognitive-services/language-service/language-detection/language-support):
- Afrikaans (af)
- Albanian (sq)
- Amharic (am)
- Arabic (ar)
- Armenian (hy)
- Assamese (as)
- Azerbaijani (az)
- Bashkir (ba)
- Basque (eu)
- Belarusian (be)
- Bengali (bn)
- Bosnian (bs)
- Bulgarian (bg)
- Burmese (my)
- Catalan (ca)
- Central Khmer (km)
- Chinese (zh)
- Chinese Simplified (zh_chs)
- Chinese Traditional (zh_cht)
- Chuvash (cv)
- Corsican (co)
- Croatian (hr)
- Czech (cs)
- Danish (da)
- Dari (prs)
- Divehi (dv)
- Dutch (nl)
- English (en)
- Esperanto (eo)
- Estonian (et)
- Faroese (fo)
- Fijian (fj)
- Finnish (fi)
- French (fr)
- Galician (gl)
- Georgian (ka)
- German (de)
- Greek (el)
- Gujarati (gu)
- Haitian (ht)
- Hausa (ha)
- Hebrew (he)
- Hindi (hi)
- Hmong Daw (mww)
- Hungarian (hu)
- Icelandic (is)
- Igbo (ig)
- Indonesian (id)
- Inuktitut (iu)
- Irish (ga)
- Italian (it)
- Japanese (ja)
- Javanese (jv)
- Kannada (kn)
- Kazakh (kk)
- Kinyarwanda (rw)
- Kirghiz (ky)
- Korean (ko)
- Kurdish (ku)
- Lao (lo)
- Latin (la)
- Latvian (lv)
- Lithuanian (lt)
- Luxembourgish (lb)
- Macedonian (mk)
- Malagasy (mg)
- Malay (ms)
- Malayalam (ml)
- Maltese (mt)
- Maori (mi)
- Marathi (mr)
- Mongolian (mn)
- Nepali (ne)
- Norwegian (no)
- Norwegian Nynorsk (nn)
- Odia (or)
- Pasht (ps)
- Persian (fa)
- Polish (pl)
- Portuguese (pt)
- Punjabi (pa)
- Queretaro Otomi (otq)
- Romanian (ro)
- Russian (ru)
- Samoan (sm)
- Serbian (sr)
- Shona (sn)
- Sindhi (sd)
- Sinhala (si)
- Slovak (sk)
- Slovenian (sl)
- Somali (so)
- Spanish (es)
- Sundanese (su)
- Swahili (sw)
- Swedish (sv)
- Tagalog (tl)
- Tahitian (ty)
- Tajik (tg)
- Tamil (ta)
- Tatar (tt)
- Telugu (te)
- Thai (th)
- Tibetan (bo)
- Tigrinya (ti)
- Tongan (to)
- Turkish (tr)
- Turkmen (tk)
- Upper Sorbian (hsb)
- Uyghur (ug)
- Ukrainian (uk)
- Urdu (ur)
- Uzbek (uz)
- Vietnamese (vi)
- Welsh (cy)
- Xhosa (xh)
- Yiddish (yi)
- Yoruba (yo)
- Yucatec Maya (yua)
- Zulu (zu)

However for the `format_sentence` feature, as this is an early release not all languages have been tested thoroughly. It is currently designed to only check languages that deal with spaces as it relies on regex word match notation

## Number support
Currently only support numbers 0 - 10. No negatives.
