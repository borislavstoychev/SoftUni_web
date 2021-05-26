paths = {
    'GET': [],
    'POST': [],
}
command = input()
while command != "END":
    path = command[:command.rindex("/")]
    methods = command[command.rindex("/") + 1:].upper()
    paths[methods].append(path)
    command = input()

method, path, *_ = input().split()
if path in paths[method]:
    print('''HTTP/1.1 200 OK
Content-Length: 2
Content-Type: text/plain
OK''')
else:
    print('''HTTP/1.1 404 Not Found
Content-Length: 9
Content-Type: text/plain
Not Found''')


