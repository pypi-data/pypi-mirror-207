from pyboil.parser import parser
import shutil, os
from os.path import dirname, abspath

def launch():
    args = parser.parse_args()
    args = vars(args)

    final_path = f"{dirname(abspath(__file__))}/template/base/"
    shutil.copytree(final_path, './', dirs_exist_ok=True)

    with open('./setup.py') as f:
        setup = f.read()

    print(setup)

    setup = setup.replace('{NAME}', args['NAME'])
    setup = setup.replace('{VERSION}', args['VERSION'])
    setup = setup.replace('{DESCRIPTION}', args['DESCRIPTION'])
    setup = setup.replace('{AUTHOR}', args['AUTHOR'])
    setup = setup.replace('{EMAIL}', args['EMAIL'])
    setup = setup.replace('{URL}', args['URL'])

    with open('./setup.py', 'w') as f:
        f.write(setup)

    if os.path.exists('./__pycache__'):
        shutil.rmtree('./__pycache__')

    os.mkdir(f'./{args["NAME"]}')

    with open(f'./{args["NAME"]}/__init__.py', 'w') as f:
        f.write('# Package init file')

if __name__ == "__main__":
    launch()