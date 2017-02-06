import sys
import os
import logging

def main():

  logging.basicConfig(filename='bar.log', level=logging.INFO, format='%(asctime)s = %(message)s')

  os.system('cls' if os.name == 'nt' else 'clear')

  while True:
    print u'\U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A';
    print u'\U0001F37A  SHitty Improvised Tap System \U0001F37A';
    print u'\U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A';
    print;

    scan_loop();

    os.system('cls' if os.name == 'nt' else 'clear')

def scan_loop():
  sys.stdout.write('Ready to scan: ');
  line = sys.stdin.readline();
  line.strip('\n')
  logging.info(line);

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    # do nothing here
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
