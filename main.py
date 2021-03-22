# Membros do grupo:
# Letícia do Nascimento (16104595)
# Ramna Sidharta (16100742)
# Matheus Schaly (18200436)

import json
from vlant.parser import create_parser


if __name__ == '__main__':
    parser = create_parser()
    while True:
       try:
           s = input('calc > ')
       except EOFError:
           break
       if not s: continue
       result = parser.parse(s)
       print(result)

