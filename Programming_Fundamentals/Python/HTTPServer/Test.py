from urllib.parse import urlparse , parse_qs

def display():
    address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
    parts =  urlparse(address)
    query = parse_qs(parts.query)
    print(query)

display()