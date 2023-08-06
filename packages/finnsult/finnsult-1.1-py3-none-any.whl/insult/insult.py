#!/usr/bin/env python3
# Import the modules
import subprocess
import sys
import random
import yaml
import argparse
import os


def read_settings():
   # Find out which path this script is in
   path = os.path.dirname(__file__)
   # Read settings.yml
   with open(f'{path}/settings.yml','r') as settings:
      return list(yaml.safe_load_all(settings))[0]

def main():
   # Run the read_settings function
   settings = read_settings()


   # Find out the defaults
   default_voice = settings['voice']
   default_slay_mode = settings['slay_mode']
   default_burn_mode = settings['burn_mode']
   default_sucker_mode = settings['sucker_mode']


   # Set up argparse
   parser = argparse.ArgumentParser(description='Insult someone')
   parser.add_argument('name', help='The name of the person to insult', nargs='?')
   parser.add_argument('-v', '--voice', help='The voice to use', required=False, default=default_voice)
   parser.add_argument('-sl', '--slay', help='Add "slay" to the end', required=False, action='store_true', default = default_slay_mode)
   parser.add_argument('-b', '--burn', help='Add "burn" to the end', required=False, action='store_true', default = default_burn_mode)
   parser.add_argument('-su', '--sucker', help='Add "sucker" to the end', required=False, action='store_true', default = default_slay_mode)
   parser.add_argument('-l', '--list', help='List the available voices', required=False, action='store_true')
   parser.add_argument('-u', '--update', help='Update the script', required=False, action='store_true')
   args = parser.parse_args()


   # Find out which path this script is in
   path = sys.path[0]
   # Update the script by runing git pull in the script directory
   if args.update:
      subprocess.run(['git', '-C', path, 'pull'])
      sys.exit()


   # List the voices
   if args.list:
      subprocess.run(['say', '-v', '?'])
      sys.exit()


   # If no name is given, print the help message and exit
   if not args.name:
      parser.print_help()
      sys.exit()


   # Get name and title case it
   name = args.name.title()


   # Create a list of insults
   insults = settings['insults']


   # Choose a random insult
   random.seed()
   insult = random.choice(insults).format(name = name)



   # Add slay, sucker, and/or burn to the end
   if args.slay:
      insult += '. SLAY!'
   if args.burn:
      insult += '. BURN!'
   if args.sucker:
      insult += '. SUCKER!'
   subprocess.run(['say', '-v', args.voice, insult])

if __name__ == "__main__":
   main()