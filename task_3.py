def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<strong>{result}</strong>"
    return wrapper

def make_italics(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<em>{result}</em>"
    return wrapper

def make_paragraph(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<p>{result}</p>"
    return wrapper

@make_bold
def get_full_name(first, last):
    return f"{first} {last}"

@make_paragraph
@make_italics
def get_custom_html_greeting(first, last):
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!"

# Test cases
print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
