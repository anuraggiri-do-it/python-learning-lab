# ═══════════════════════════════════════════════════════════════
#         STANDARD LIBRARY — Essential Modules Deep Dive
# ═══════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────
# PART 1: os & sys
# ─────────────────────────────────────────────────────────────
import os, sys

# os — interact with the operating system
print(os.getcwd())                        # current working directory
print(os.listdir('.'))                    # list files in directory
print(os.path.exists('test.txt'))         # check file exists
print(os.path.join('folder', 'file.py')) # safe cross-platform path
print(os.path.basename('/a/b/c.py'))     # 'c.py'
print(os.path.splitext('file.py'))       # ('file', '.py')
print(os.environ.get('PATH', 'not set')) # read env variable
# os.makedirs('a/b/c', exist_ok=True)   # create nested dirs
# os.rename('old.txt', 'new.txt')        # rename
# os.remove('file.txt')                  # delete file

# sys — Python interpreter info
print(sys.version)                        # Python version
print(sys.platform)                       # 'win32', 'linux', 'darwin'
print(sys.argv)                           # command-line args list
print(sys.path[:3])                       # module search paths
# sys.exit(0)                             # exit (0=success, 1=error)


# ─────────────────────────────────────────────────────────────
# PART 2: pathlib — modern file paths (preferred over os.path)
# ─────────────────────────────────────────────────────────────
from pathlib import Path

p = Path('.')
print(p.resolve())                        # absolute path
print(p.is_dir())                         # True
print(list(p.glob('*.py')))              # all .py in current dir
print(list(p.rglob('*.py')))             # all .py recursively

# path building with / operator
config = Path('project') / 'config' / 'settings.json'
print(config)                             # project\config\settings.json
print(config.suffix)                      # .json
print(config.stem)                        # settings
print(config.parent)                      # project\config

# read/write (no open() needed)
tmp = Path('tmp_test.txt')
tmp.write_text('hello pathlib', encoding='utf-8')
print(tmp.read_text(encoding='utf-8'))    # hello pathlib
tmp.unlink()                              # delete


# ─────────────────────────────────────────────────────────────
# PART 3: datetime & time
# ─────────────────────────────────────────────────────────────
from datetime import datetime, date, timedelta
import time

# date & datetime basics
today    = date.today()
now      = datetime.now()
print(today)                              # 2024-01-15
print(now)                               # 2024-01-15 10:30:00.123456

# formatting & parsing
print(now.strftime('%d/%m/%Y %H:%M'))    # 15/01/2024 10:30
parsed = datetime.strptime('15/01/2024', '%d/%m/%Y')
print(parsed)

# arithmetic
tomorrow   = today + timedelta(days=1)
next_week  = today + timedelta(weeks=1)
diff       = date(2025, 1, 1) - today
print(diff.days)                          # days until 2025

# time module — measuring execution time
start = time.time()
total = sum(range(1_000_000))
end   = time.time()
print(f'Elapsed: {end - start:.4f}s')

time.sleep(0.01)                          # pause 10ms


# ─────────────────────────────────────────────────────────────
# PART 4: math & random
# ─────────────────────────────────────────────────────────────
import math, random

# math — mathematical functions
print(math.pi)                            # 3.14159...
print(math.e)                             # 2.71828...
print(math.sqrt(144))                     # 12.0
print(math.ceil(3.2))                     # 4
print(math.floor(3.9))                    # 3
print(math.factorial(10))                 # 3628800
print(math.log(100, 10))                  # 2.0  (log base 10)
print(math.log2(8))                       # 3.0
print(math.gcd(48, 18))                   # 6
print(math.isclose(0.1 + 0.2, 0.3))      # True (float comparison)
print(math.inf)                           # infinity
print(math.isnan(float('nan')))           # True

# random — random number generation
random.seed(42)                           # reproducible
print(random.randint(1, 10))             # int in [1, 10]
print(random.random())                   # float in [0.0, 1.0)
print(random.uniform(1.5, 3.5))         # float in [1.5, 3.5]
print(random.choice(['a', 'b', 'c']))   # random element
print(random.sample(range(10), 3))      # 3 unique elements
items = [1, 2, 3, 4, 5]
random.shuffle(items)                    # in-place shuffle
print(items)
print(random.gauss(0, 1))               # normal distribution


# ─────────────────────────────────────────────────────────────
# PART 5: logging — production-ready output
# ─────────────────────────────────────────────────────────────
import logging

# ANALOGY: print() = sticky note, logging = official logbook 📒
# logging has levels: DEBUG < INFO < WARNING < ERROR < CRITICAL

# basic config
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%H:%M:%S'
)

logging.debug('Detailed debug info')      # only shown if level=DEBUG
logging.info('Application started')       # general info
logging.warning('Low disk space')         # something unexpected
logging.error('File not found')           # serious problem
logging.critical('System crash!')         # fatal error

# log to file
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.WARNING)
logging.getLogger().addHandler(file_handler)

# named logger (best practice in modules)
logger = logging.getLogger(__name__)
logger.info('Using named logger')

Path('app.log').unlink(missing_ok=True)   # cleanup


# ─────────────────────────────────────────────────────────────
# PART 6: Async / Await — Asynchronous Python
# ─────────────────────────────────────────────────────────────
import asyncio

# ANALOGY: Waiter at a restaurant 🍽️
#   Synchronous = one waiter serves one table fully before next
#   Asynchronous = waiter takes order, goes to next table while
#                  kitchen cooks, comes back when food is ready
#
# Use async when: waiting for I/O (network, file, DB)
#   NOT for CPU-heavy tasks (use multiprocessing instead)

async def fetch_data(name, delay):
    print(f'{name}: starting...')
    await asyncio.sleep(delay)            # non-blocking wait (simulates I/O)
    print(f'{name}: done after {delay}s')
    return f'{name} result'

async def main():
    # run tasks CONCURRENTLY (not sequentially)
    results = await asyncio.gather(
        fetch_data('Task A', 2),
        fetch_data('Task B', 1),
        fetch_data('Task C', 3),
    )
    print(results)
    # Total time ≈ 3s (longest), NOT 2+1+3=6s

asyncio.run(main())

# async with — for async context managers (aiofiles, aiohttp)
# async for  — for async iterators (streaming data)


# ─────────────────────────────────────────────────────────────
# PART 7: Multithreading vs Multiprocessing
# ─────────────────────────────────────────────────────────────
import threading
import multiprocessing

# ANALOGY:
#   Threading       = one chef, multiple hands (shared kitchen)
#   Multiprocessing = multiple chefs, separate kitchens
#
# Python GIL (Global Interpreter Lock):
#   Only ONE thread runs Python bytecode at a time.
#   Threading = good for I/O-bound tasks (waiting on network/file)
#   Multiprocessing = good for CPU-bound tasks (math, image processing)
#
# ─────────────────────────────────────────────────────────────
# USE CASE          | TOOL
# ─────────────────────────────────────────────────────────────
# I/O bound         | threading or asyncio
# CPU bound         | multiprocessing
# Simple async I/O  | asyncio (modern, preferred)
# ─────────────────────────────────────────────────────────────

# Threading example
def print_numbers(name, count):
    for i in range(count):
        print(f'{name}: {i}')

t1 = threading.Thread(target=print_numbers, args=('Thread-1', 3))
t2 = threading.Thread(target=print_numbers, args=('Thread-2', 3))
t1.start()
t2.start()
t1.join()                                 # wait for t1 to finish
t2.join()                                 # wait for t2 to finish

# Thread-safe counter using Lock
counter = 0
lock    = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:                        # only one thread at a time
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print(f'Counter: {counter}')              # 5000 (safe with lock)

# Multiprocessing example (CPU-bound)
def square_sum(n):
    return sum(i * i for i in range(n))

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square_sum, [100_000, 200_000, 300_000, 400_000])
    print(results)
