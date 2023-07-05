#Task 1

def make_bold(func):
    def wrap():
        return'<strong>' + func() + '</strong>'      
    return wrap

@make_bold
def get_html_greeting():
    return'Hello, World!'
print(get_html_greeting())
