#!/usr/bin/env python3

from tqdm import tqdm
from mhstats import print_stats

## Generalized Monty Hall problem for N doors, with the host opening some subset
## of the doors that were not choson.

import random
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--doors', type=int, default=3, help='Total number of doors')
    parser.add_argument('-o', '--opens', type=int, default=1, help='Number of doors that Monty opens')
    parser.add_argument('-t', '--trials', type=int, default=1000000, help='Number of trials')
    args = parser.parse_args()

    n_doors:int = args.doors
    n_opens:int = args.opens
    n_trials:int = args.trials
    i_last = n_doors - n_opens - 1 # index into full list

    assert n_opens < n_doors-1, f'NUmber of doors opened must me less than the total number of doors minus 1'

    wins:dict[str, int] = {'stay': 0, 'switch': 0}
    losses:dict[str, int] = {'stay': 0, 'switch': 0}

    for _ in tqdm(range(n_trials)):
        car_door:int = random.randint(0, n_doors-1)
        final_choice:int = -1 # losing value
        first_choice:int = 0

        decision:str = random.choice(['stay', 'switch'])

        if decision == 'stay':
            final_choice = first_choice
        else:
            if first_choice == car_door:
                pass # lose
            else: # then car_door is in 1...n_doors-1
                final_choice = random.randint(1, i_last)
                if car_door > i_last and final_choice == i_last:
                    final_choice = car_door

        win:bool = final_choice == car_door

        if win:
            wins[decision] += 1
        else:
            losses[decision] += 1

    print_stats(n_trials, n_doors, n_opens, wins, losses)


if __name__ == '__main__':
    main()
