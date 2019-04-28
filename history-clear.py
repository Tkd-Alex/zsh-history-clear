#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime

OLDER_THAN = 30 * 6 #DAYS
LESS_THAN = 3
START_WITH = [ 'git commit', 'git add' ]
REMOVE_WITH_EXCEPTION = True
REMOVE_DUPLICATE = True

if __name__ == '__main__':
    with open("zsh_history", "rb") as f:
      content = f.readlines()

    content.reverse()
    print("Load history len: {}".format(len(content)))
    index_to_remove = []

    commands_extracted = []

    for i in range(0, len(content)):
        remove_line = False
        try:
            line = content[i].decode('utf-8').lower().replace('\n', '')
            if line.startswith(': '):
                data = line.replace(': ', '').split(':')
                timestamp = int(float(data[0].strip()))
                if OLDER_THAN != None and (datetime.now() - datetime.fromtimestamp(timestamp) ).days >= OLDER_THAN:
                    remove_line = True
                command = data[1].strip().replace('0;', '')
                if REMOVE_DUPLICATE is True:
                    if command not in commands_extracted:
                        commands_extracted.append(command)
                    else:
                        remove_line = True

                if LESS_THAN != None and len(command) <= LESS_THAN:
                    remove_line = True
                elif START_WITH != None:
                    for startswith in START_WITH:
                        if command.startswith(startswith):
                            remove_line = True
                            break
            else:
                remove_line = True
        except Exception:
            if REMOVE_WITH_EXCEPTION is True:
                remove_line = True

        if remove_line is True:
            index_to_remove.append(i)

    print("Line to remove: {}".format(len(index_to_remove)))
    newhistory = [ content[i].decode('utf-8').strip('\n') for i in range(0, len(content)) if i not in index_to_remove ]
    print("New history len: {}".format(len(newhistory)))

    with open('zsh_history', 'w') as f:
        f.write('\n'.join(newhistory))