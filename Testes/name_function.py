def get_formated_name(first, last,midle=''):
    """Gera um nome completo formatado"""
    if midle:
        full_name = first.title()+" "+midle.title()+ " "+ last.title()
    else:
        full_name = first.title()+" "+last.title()
    return full_name

