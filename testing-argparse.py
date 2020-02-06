import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dominance', default=False, action='store_true',
    help='This is a new argument which determines if dominance LD scores should be computed.'
    'It is important to note that this flag only functions to produce new LD SCORES, and does'
    'not modify any regressions. To impact regressions, you must input dominance LD scores and betas.')

if __name__ == "__main__":
    args = parser.parse_args()
    print args.dominance