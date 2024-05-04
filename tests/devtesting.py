import os.path

from graph_judge import GraphJudge


def evenjudge(filename):
    filename = os.path.basename(filename)
    num = filename.split("_")[0][1:]
    if int(num) % 2 == 0:
        return True
    else:
        return False


def main():
    gj = GraphJudge.from_directory("../testing_data")
    gj.add_judge("is_even", evenjudge)

    r = gj.run("is_even")
    even_filenames = r.filter("is_even", True).members()

    tw = 2


if __name__ == "__main__":
    main()

