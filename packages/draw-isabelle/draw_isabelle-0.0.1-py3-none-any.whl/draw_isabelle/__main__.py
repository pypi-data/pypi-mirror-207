from argparse import ArgumentParser

from draw_isabelle.parsing import parse_graph


def run_from_cli():

    parser = ArgumentParser()
    parser.add_argument(
        "tree_syntax", help="Copy of Isabelle angle bracket tree syntax"
    )
    args = parser.parse_args()
    print(parse_graph(args.tree_syntax))


if __name__ == "__main__":
    run_from_cli()
