from django import template

register = template.Library()


@register.filter()
def censor(value):
    bad_words = ['редиска', 'тестовое']
    for word in bad_words:
        value = value.replace(word, word[0] + '*' * len(word))
    return value

register.filter('censor', censor)