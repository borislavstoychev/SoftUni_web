from urllib import parse

test = [
    "http://www.google.bg/search?q=C%23",
    "https://mysite.com/show?n%40m3=p3%24h0",
    "http://url-decoder.com/i%23de%25?id=23",
]

[print(parse.unquote(url)) for url in test]

