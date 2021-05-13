# Membros do grupo:
# Letícia do Nascimento (16104595)
# Ramna Sidharta (16100742)
# Matheus Schaly (18200436)

import sys
import json
from vlant.parser import create_parser


if __name__ == '__main__':
    if len(sys.argv) > 3:
        print('Usage: python main.py program.lcc')
        exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        data = f.read()
        parser = create_parser()
        if len(sys.argv) == 2:
            result = parser.parse(data, debug=False, tracking=True)
        else:
            result = parser.parse(data, debug=True, tracking=True)

        if result is not list:
            result = [result]

        for node in result:
            node.validate()
