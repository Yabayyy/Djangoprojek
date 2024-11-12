from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    Remove all values of arg from the given string
    """
    
    return value.replace(arg, '')

# register.filter('cut', cut)