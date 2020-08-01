from tello import Tello
import sys
from datetime import datetime
import time

start_time = str(datetime.now())

file_name = sys.argv[1]

f = open(file_name, "r")
commands = f.readlines()

tello = Tello()
for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()
        print(command)
        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print('delay {}'.format(sec))
            time.sleep(sec)
            pass
        else:
            tello.send_command(command)

log = tello.get_log()

with open('log/' + start_time + '.txt', 'x') as out:
    for stat in log:
        stat.print_stats()
        sentence = stat.return_stats()
        out.write(sentence)
