def application(environ, start_response):
    status = '200 OK'
    response_header = [('Content-type', 'text/html')]
    start_response(status, response_header)

    html = 'Hello World'
    return [bytes(html, 'utf-8')]

if __name__ == '__main__':
    page = application({}, print)
    print(page[0].decode())