import argparse
from random import randrange
from rich.console import Console
from rich.style import Style

def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--loteria', type=str, metavar='LOTERIA', required=True,
                        help='Choose the lotery')
    parser.add_argument('--tickets', type=int, metavar='TICKETS', required=True,
                        help='Number of tickets')
    return parser.parse_args()

    # primitiva 6 numerow z 1 do 49 i 1 z 1 do 9
    # euro 5 od 1 do 50 i 2 od 1 do 12
    # gordo 5 numeroqw od 01 do 54, i zawsze od 0 do 10

def losy(long, no_of_numbers):
    outputSix = []
    while True:
        number = randrange(1, long)
        if number in outputSix:
            continue
        else:
            outputSix.append(number)
        if len(outputSix) == no_of_numbers:
            break
    return Console().print(sorted(outputSix), style=Style(color="red"))

def main():
    args = parse_args()

    #console = Console()
    if args.loteria == "EURO":
        long = 51
        short = 6
        no_of_numbers = 5
        stars = 2
        always = True
    elif args.loteria == "PRIMITIVA":
        long = 50
        short = 13
        no_of_numbers = 6
        stars = 1
        always = False
    elif args.loteria == "GORDO":
        long = 55
        short = 10
        no_of_numbers = 5
        always = True
        stars = 1
    outputOne = []


    for i in range(0, args.tickets):
        losy(long, no_of_numbers)
        if always:
            losy(short, stars)

    if not always:
        for i in range(0, stars):
            Console().print((randrange(0, short)))


if __name__ == '__main__':
    main()

