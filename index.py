def application(environ, start_response):
    status = '200 OK'
    response_header = [('Content-type', 'text/html')]
    start_response(status, response_header)

    html = ''
    html += '<html>\n'
    html += ' <body>\n'
    html += ' <title>Test WSGI page for fys</title>\n'
    html += ' <div style="width: 100%; font-size: 20px; font-weight: bold; text-align: center;">\n'
    html += ' Welcome to the mod_wsgi test page\n'
    html += ' </div>\n'
    html += ' <h2>Some interesting environment variables:</h2>\n'
    html += ' <div style="width: 100%; font-family: Courier; font-size: 14px; font-weight: bold; text-align: left;">\n'
    environmentVars = ['REQUEST_METHOD', 'REQUEST_URI', 'QUERY_STRING','SCRIPT_NAME', 'HTTP_REFERER']
    for envVar in environmentVars:
        envVarValue = environ.get(envVar, '')
        html += envVar + ' = ' + envVarValue + '<br>\n'
    html += ' </div>\n'
    html += ' </body>\n'
    html += '</html>\n'
    
    return [bytes(html, 'utf-8')]

if __name__ == '__main__':
    page = application({}, print)
    print(page[0].decode())