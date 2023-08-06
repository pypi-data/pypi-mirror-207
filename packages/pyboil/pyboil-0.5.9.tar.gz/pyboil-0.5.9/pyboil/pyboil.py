from pyboil.parser import parser
import shutil, os, sys

def launch():
    args = parser.parse_args()

    final_path = f"{os.pardir}/template"
    shutil.copytree(final_path, '.')

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

if __name__ == "__main__":
    launch()