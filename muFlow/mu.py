import argparse
import sys

from assembler import Assembler

if __name__ == "__main__":
  p = argparse.ArgumentParser(description='muFlow, the parallel processing engine')
  p.add_argument('script', help='Script to run')
  p.add_argument('--num-processes', '-n', type=int, default=0,
      help='Number of processes to spawn (default is CPU count)')
  p.add_argument('--debug', action='store_true',
      help='Debug mode: each parallel task processes only the first item in a single process')
  p.add_argument('--list', action='store_true', help='Print list of available tasks')
  p.add_argument('--info', type=str, help='Print more detailed info on a specific task')
  p.add_argument('--no-vt', action='store_true', help='Do not use VT100 escape codes')
  p.add_argument('--no-log', action='store_true', help='Do not print logs and time measurements')

  asm = Assembler()

  if '--list' in sys.argv:
    asm.printInfo()
    exit()
  if '--info' in sys.argv:
    info = sys.argv[sys.argv.index('--info') + 1]
    asm.printInfo(info)
    exit()

  args = p.parse_args()

  if args.no_vt:
    asm.preventVT100()
  if args.no_log:
    asm.preventLogging()

  with open(args.script, 'r') as script_file:
    script = [line.strip('\n') for line in script_file.readlines()]
  flow = asm.assembleFromText(lines=script,
                              num_proc=args.num_processes,
                              debug=args.debug
  )
  flow.execute()
