def createHeader(title, styleFile):
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="{styleFile}">
        <title>{title}</title>
    </head>
    '''

def createFooter():
    return '</html>'

def createBody(content):
    return f'<body>{content}</body>'

def stationsTable(stations):
    table = '''
    <table><tr>
        <th>Address</th>
        <th>Brand</th>
        <th>Location</th>
        <th>Trading Name</th>
        <th>Price</th>
    </tr>
    '''
    for station in stations:
        table += f'''
            <tr class="{station.day}">
                <td>{station.address}</th>
                <td>{station.brand}</th>
                <td>{station.location}</th>
                <td>{station['trading-name']}</th>
                <td>{station.price}</th>
            </tr>
        '''

    table += '</table>'
    return table

