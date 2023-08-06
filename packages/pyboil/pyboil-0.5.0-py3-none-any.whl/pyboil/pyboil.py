from pyboil.parser import parser
import shutil

def pyboil():
    args = parser.parse_args()

    shutil.copytree("template", '.')

    with open('./setup.py') as f:
        setup = f.read()

    setup.replace('{NAME}', args['NAME'])
    setup.replace('{VERSION}', args['VERSION'])
    setup.replace('{DESCRIPTION}', args['DESCRIPTION'])
    setup.replace('{AUTHOR}', args['AUTHOR'])
    setup.replace('{EMAIL}', args['EMAIL'])
    setup.replace('{URL}', args['URL'])

    with open('./setup.py', 'w') as f:
        f.write(setup)