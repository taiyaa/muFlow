import argparse
import sys

from assembler import Assembler

if __name__ == "__main__":
  p = argparse.ArgumentParser(description='muFlow, the parallel processing engine')
  p.add_argument('script', help='Script to run')
  p.add_argument('--num-processes', '-n', type=int, default=0,
      help='Number of processes to spawn (default is CPU count)')
  p.add_argument('--report-step', '-r', type=float, default=0.1,
      help='Report parallel task progress every so often (0 or negative disables')
  p.add_argument('--debug', action='store_true',
      help='Debug mode: each parallel task processes only the first item in a single process')
  #TODO p.add_argument('--task-list', action='store_true', help='Print list of available tasks')

  asm = Assembler()

  args = p.parse_args()

  with open(args.script, 'r') as script_file:
    script = [line.strip('\n') for line in script_file.readlines()]
  flow = asm.assembleFromText(lines=script,
                              num_proc=args.num_processes,
                              report_step=args.report_step,
                              debug=args.debug
  )
  flow.execute()