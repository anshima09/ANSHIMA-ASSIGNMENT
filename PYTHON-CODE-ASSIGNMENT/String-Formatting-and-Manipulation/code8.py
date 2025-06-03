import re

def remove_html_tags(html):
    return re.sub(r'<[^>]+>', '', html)


html_input = "<p>Hello, Anshima <b>How are you</b></p>"
print("original html string: ",html_input)
print("Removed html tags string: ",remove_html_tags(html_input)) 