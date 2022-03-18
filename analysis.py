from pathlib import Path
from typing import Callable
from argparse import ArgumentParser
from distutils.util import strtobool
from logging import error
from os import path

DEFAULT_FILE = '2022-03-18_celestial_VIP_NA.txt'
DEFAULT_DIR = Path(__file__).parent # this script lives here
DEFAULT_FP = DEFAULT_DIR / DEFAULT_FILE

def no_decay(i: int) -> int:
    return 1

def define_gamma_decay(gamma: float=.999) -> Callable:
    def gamma_decay(i: int) -> float:
        return gamma**i
    return gamma_decay

def pop_sort(chars: dict) -> dict:
    return dict(sorted(chars.items(), key=lambda kv:kv[1][0], reverse=True))

def name_sort(chars: dict) -> dict:
    return dict(sorted(chars.items()))

def process_data(fp: str=DEFAULT_FP, decay: Callable = no_decay, sort: Callable = pop_sort) -> dict:
    with open(fp) as file:
        lines = file.readlines()
    chars = dict()
    i=0
    for line in lines:
        line = line.rstrip()
        if line not in chars:
            chars[line] = [1, i] # total, highest
        else:
            chars[line][0] += decay(i)
        i += 1
    chars = sort(chars)
    return chars

def print_results(chars: dict) -> None:
    for char in chars:
        print(f"{char}:\tpop score {chars[char][0]:.2f},\thighest placement: {chars[char][1]}")

def save_results(fp: str, chars: dict, gamma: float, sort: str) -> None:
    file = path.split(fp)[1].split('.')[0]
    with open(DEFAULT_DIR / f'results__{file}__gamma={gamma}__by_{sort}.txt', 'w+') as fp:
        for char, v in chars.items():
            fp.write(f"{char},{v[0]},{v[1]}\n")

def main():
    parser = ArgumentParser()
    parser.add_argument('--fp', type=str, default=DEFAULT_FP, help='file path to ranked list of characters')
    parser.add_argument('--gamma', type=float, default=1, help='enable gamma decay and specify gamma decay factor; gamma of 1 disables gamma decay')
    parser.add_argument('--sort', type=str, default='pop', help='choose method for sorting results: options are "pop" or "name"')
    parser.add_argument('--save', type=lambda x: bool(strtobool(x)), default=False, nargs='?', const=True, help='flag for saving results to a file')
    parser.add_argument('--print', type=lambda x: bool(strtobool(x)), default=False, nargs='?', const=True, help='flag for printing results to terminal')
    args=parser.parse_args()
    if not args.print and not args.save:
        print("...what do you want me to do with the results?")
        return
    decay = define_gamma_decay(args.gamma) if args.gamma!=1 else no_decay
    if args.sort=='pop':
        sort = pop_sort
    elif args.sort=='name':
        sort = name_sort
    else:
        error(f' sort method {args.sort} does not exist')
    results = process_data(args.fp, decay, sort)
    if args.print:
        print_results(results)
    if args.save:
        save_results(args.fp, results, args.gamma, args.sort)

if __name__ == "__main__":
    main()