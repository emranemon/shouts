from textblob import TextBlob
from django import template

register = template.Library()

@register.simple_tag
def sentiment_of_my_comment(comment):
    
    blob = TextBlob(comment)
    lang = blob.detect_language()

    if lang == 'en':
        result = blob.sentiment.polarity
    elif lang=="ja" or lang=="bn":
        result = blob.translate(from_lang=lang, to='en').sentiment.polarity
    else:
        result = 0

    return format(result*100, '.2f')
