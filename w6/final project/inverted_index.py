from collections import Counter
import argparse
import json


class InvertedIndex:
    def __init__(self, word_to_docs_mapping):
        self.word_to_docs_mapping = word_to_docs_mapping

    def __getitem__(self, key):
        return self.word_to_docs_mapping[key]

    def query(self, words):
        """for each word in query check its list of articles from
        self.word_to_docs_mapping and add it to the list
        create counter and get articles that are in all words"""
        common = list()
        for word in words:
            for list_item in \
                    list(self.word_to_docs_mapping.__getitem__(word)):
                common.append(list_item)
        counter = Counter(common)
        res = set()
        for key, val in counter.items():
            if val >= len(words):
                res.add(key)
        return res

    def dump(self, filepath):
        data = {}
        for item in self.word_to_docs_mapping.items():
            data[item[0]] = list(item[1])
        with open(filepath, 'w') as file:
            json.dump(data, file)

    @classmethod
    def load(cls, filepath):
        with open(filepath, 'r') as file:
            data = json.load(file)
        inverted_index_object = {}
        for item in data.items():
            inverted_index_object[item[0]] = set(item[1])
        return inverted_index_object


def load_document(filepath):
    """ create a sorted list splitting each string by \t
    create dictionary from sorted list"""
    with open(filepath, encoding="utf8") as file:
        all_lines = file.readlines()

    formatted_strings = \
        sorted(list(map(lambda line: line.split('\t', 1), all_lines)),
               key=lambda line: int(line[0]))
    index_dict = {int(row[0]): row[1].strip() for row in formatted_strings}
    return index_dict


def build_inverted_index(articles):
    """go through each article word and add it into the dictionary
    adding/updating the article number where the word is met"""
    inverted_index = {}
    for key, value in articles.items():
        array = value.split()
        for word in array:
            if inverted_index.get(word):
                inverted_index[word].add(key)
            else:
                inverted_index.setdefault(word, {key})
    return InvertedIndex(inverted_index)


def main(command_line=None):
    parser = argparse.ArgumentParser('Inverted Index CLI')
    subparsers = parser.add_subparsers(dest='command')

    build = \
        subparsers.add_parser('build', help='Constructing an inverted index')
    build.add_argument(
        '--dataset',
        help='path to dataset to build Inverted Index',
        required=True
    )
    build.add_argument(
        '--index',
        help='path for Inverted Index dump',
        required=True
    )

    query = subparsers.add_parser('query', help='find common articles')
    query.add_argument(
        '--index',
        help='path to load Inverted Index',
        required=True
    )
    query.add_argument(
        '--query_file',
        help='query_file with collection of queries'
             ' to run against Inverted Index',
        required=True
    )

    args = parser.parse_args(command_line)
    if args.command == 'build':
        inverted_index = build_inverted_index(load_document(args.dataset))
        inverted_index.dump(args.index)
    elif args.command == 'query':
        inverted_index = InvertedIndex.load(args.index)

        with open(args.query_file, 'r') as file:
            arr = []
            for line in file:
                arr.append(line.rstrip().split())
        for line in arr:
            output = inverted_index.query(line)
            print(*sorted(output), sep=',')


if __name__ == '__main__':
    main()
