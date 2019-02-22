#!/usr/bin/env python
import sys
import os
import logging
import subprocess

OUTPUT = ''

def main():

  logging.basicConfig(filename='bar.log', level=logging.INFO, format='%(asctime)s = %(message)s');

  os.system('cls' if os.name == 'nt' else 'clear');

  while True:
    print u'\U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A';
    print u'\U0001F37A  SHitty Improvised Tap System \U0001F37A';
    print u'\U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A';
    print;

    print OUTPUT;

    scan_loop();

    os.system('cls' if os.name == 'nt' else 'clear');

def scan_loop():
  sys.stdout.write('Ready to scan: ');
  line = sys.stdin.readline();
  line = line.strip(' \t\n\r');

  global OUTPUT;

  if line == 'stats':
    OUTPUT = subprocess.check_output(['cat bar.log | cut -d \'=\' -f2 | sed -e \'s/^ *//\' -e \'s/ *$//\' | sort -h | uniq -c'], shell=True);
  elif line == '':
    OUTPUT = '';
  elif line.strip().lower() in ["help", "?", "h"]:
    OUTPUT = '  stats: Print the current stats\n'
  else:
    OUTPUT = '';
    logging.info(line);

if __name__ == '__main__':
  try:
    main();
  except KeyboardInterrupt:
    # do nothing here
    os.system('cls' if os.name == 'nt' else 'clear');
    pass;
