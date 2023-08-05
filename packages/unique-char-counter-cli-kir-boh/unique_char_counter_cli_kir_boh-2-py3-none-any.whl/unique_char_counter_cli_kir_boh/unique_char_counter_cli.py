import argparse
from collections import Counter
from functools import cache


@cache
def return_amount_once_occured_items(hashable_obj):
    hashable_obj = hashable_obj.strip()
    counter = Counter(hashable_obj)
    once_occurred_items_num = 0
    for appearances_number in counter.values():
        if appearances_number == 1:
            once_occurred_items_num += 1
    return once_occurred_items_num


def get_obj_from_cli():
    """It's expected that get_obj_from_cli pass either string or file, so that be carreful with  modifying:
        'group = parser.add_mutually_exclusive_group()'. You may need to change other funcs after modifying it"""
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s", "--string", action="store_true", help="Your string")
    group.add_argument("-f", "--file", action="store_true", help="Your file")
    parser.add_argument("hashable_obj", help="The string you wish to count")
    args = parser.parse_args()
    return args


def read_file_in_chunks(file_path):
    chunk_size = 1000
    data = ""
    with open(file_path, "r") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            data += chunk
    return data


def main():
    args = get_obj_from_cli()
    if args.file:
        data = read_file_in_chunks(args.hashable_obj)
        once_occurred_items_num = return_amount_once_occured_items(data)
        print(once_occurred_items_num)
        return once_occurred_items_num
    elif args.string:
        once_occurred_items_num = return_amount_once_occured_items(args.hashable_obj)
        print(once_occurred_items_num)
        return once_occurred_items_num


if __name__ == "__main__":
    main()
