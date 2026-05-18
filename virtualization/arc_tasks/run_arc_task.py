"""Small runner to demonstrate the ARC solver on a sample input.

Usage:
  python run_arc_task.py --list
  python run_arc_task.py task001
"""
import argparse
import os
import sys

try:
    from arc_solver import get_explanation, solve
except ImportError:
    from .arc_solver import get_explanation, solve

BASE_DIR = os.path.dirname(__file__)
SUBMISSION_DIR = os.path.join(BASE_DIR, 'submission')


def sample_grid_for_task(task_id):
    if task_id == 'task001':
        return [[1, 0, 2], [0, 3, 0], [4, 0, 5]]
    return []


def list_available_tasks() -> list[str]:
    if not os.path.isdir(SUBMISSION_DIR):
        return []
    tasks = []
    for path in sorted(os.listdir(SUBMISSION_DIR)):
        if path.lower().endswith('.onnx'):
            tasks.append(os.path.splitext(path)[0])
    return tasks


def main(argv=None):
    parser = argparse.ArgumentParser(description='ARC task runner for ONNX-based solvers.')
    parser.add_argument('task_id', nargs='?', help='Task ID to solve (e.g. task001)')
    parser.add_argument('--list', action='store_true', help='List available ONNX task models')
    args = parser.parse_args(argv)

    if args.list:
        tasks = list_available_tasks()
        if not tasks:
            print('No ONNX task models found in', SUBMISSION_DIR)
            return 1
        print('Available tasks:')
        for t in tasks:
            print('  ', t)
        return 0

    if not args.task_id:
        parser.print_usage()
        return 1

    task = args.task_id
    print('Task:', task)
    print('Explanation:', get_explanation(task))
    grid = sample_grid_for_task(task)
    if not grid:
        print('\nNo sample grid available for this task.')
        return 1

    print('\nInput grid:')
    for r in grid:
        print(r)
    out = solve(task, grid)
    print('\nOutput grid:')
    for r in out:
        print(r)
    return 0


if __name__ == '__main__':
    sys.exit(main())
