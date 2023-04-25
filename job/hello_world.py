import numpy as np
import pandas as pd
import argparse

def main():
    print(f"imported pandas version {pd.__version__}")
    print(f"imported numpy version {np.__version__}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--var', help="arbitrary argument")
    options = parser.parse_args()
    if options.var:
        print(f"found command-line arg `var`: {options.var}")
    main()