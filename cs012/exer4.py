"""Exercise 2.2: Generators."""


def dict_of_line(csv_file: str) -> dict:
    """Generator yielding lines of the CSV file called"""
    def read_file(csv_file: str) -> list:
        """Function defined in the local scope of the dict_of_line function."""
        with open(csv_file) as fhandle:
            headings = fhandle.readline().strip().split(",")
            data = fhandle.read().split("\n")[:-1]
        return headings, data

    headings, data = read_file(csv_file)

    for line in data:
        intermediate = list(zip(headings, line.split(",")))
        yield {item[0]: item[1] for item in intermediate}


if __name__ == '__main__':
    print(type(dict_of_line("dragons.csv")))
    print(dict_of_line("dragons.csv").__next__())
