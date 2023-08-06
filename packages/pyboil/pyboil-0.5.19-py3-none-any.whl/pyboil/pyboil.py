from pyboil.parser import parser
import shutil
from os.path import dirname, abspath

def launch():
    args = parser.parse_args()
    args = vars(args)

    final_path = f"{dirname(abspath(__file__))}/template/base/"
    shutil.copytree(final_path, './', dirs_exist_ok=True)

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