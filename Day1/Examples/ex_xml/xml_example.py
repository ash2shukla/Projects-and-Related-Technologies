# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
from lxml import etree


def parse_existing():
    # Read xml file
    file_pointer = open('Sample_XML.xml')
    root = etree.fromstring(file_pointer.read())
    print('The note node=', root)
    print(etree.tostring(root, pretty_print=True))
    # Each Tag and content is called an element.
    # Each element's name is called tag
    print('Root Element Tag=', root.tag)
    # Each element can be thought of as a dictionary with key = values
    # Whole XML can be thought of as a list
    # We can iterate over whole xml
    print('Children of Root')
    for element in root:
        print(element.tag)


    print('Getting Names of attributes in element')
    print(root.keys())
    print('Getting value of a specific tag')
    print(root.get('id'))
    print('Getting text between tags')
    print(root.text)


def create_new():
    # Lets suppose we need to create a xml as-
    # <body class="container">
    #   <div class="card">
    #       <p> Paragraph content </p>
    #   </div>
    # </body>
    print('Created XML')
    body = etree.Element('body')
    body.set('class', 'container')

    div = etree.Element('div')
    div.set('class', 'card')

    p = etree.Element('p')
    p.text = 'Paragraph Content'

    div.append(p)
    body.append(div)

    print(etree.tostring(body, pretty_print=True).decode())


def main():
    parse_existing()
    create_new()


if __name__ == "__main__":
    main()
