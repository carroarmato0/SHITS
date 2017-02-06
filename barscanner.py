import sys
import os

TAP = {}
OUTPUT = ""

def main():

  os.system('cls' if os.name == 'nt' else 'clear')

  while True:

    print u'\U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A';
    print u'\U0001F37A  SHitty Improvised Tap System \U0001F37A';
    print u'\U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A \U0001F37A';
    print;

    print OUTPUT;

    scan_loop();

    os.system('cls' if os.name == 'nt' else 'clear')

def scan_loop():
  sys.stdout.write('Ready to scan: ');
  line = sys.stdin.readline();

  if line in TAP:
      OUTPUT = "line not in tap";

  print_tap();

def print_tap():
  for item in TAP:
    print item;

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    # do nothing here
    pass
