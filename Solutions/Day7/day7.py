from tree import Tree
from result import Result


TOTAL_DISK_SPACE = 70000000
FREE_SPACE_NEEDED = 30000000


def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def get_part1_result(root_tree, result):
    if root_tree.size < 100000:
        result.add_value(root_tree.size)
    for child_tree in root_tree.children:
        get_part1_result(child_tree, result)
    return result.size


def get_folders_large_enough_for_deletion(root_tree, to_clear, list_of_folders):
    if root_tree.size >= to_clear:
        list_of_folders.append(root_tree.size)
    for child_tree in root_tree.children:
        get_folders_large_enough_for_deletion(child_tree, to_clear, list_of_folders)
    return list_of_folders


def solve_part1():
    lines = retrieve_input()
    root_tree = None
    current_tree = None
    created_root = False
    for line in lines:
        if not created_root:
            root_tree = Tree("/", None)
            current_tree = root_tree
            created_root = True
            continue
        if line.startswith("$ ls"):
            continue
        if line.startswith("$ cd .."):
            current_directory_size = current_tree.size
            current_tree = current_tree.get_parent()
            current_tree.size += current_directory_size
            continue
        if line.startswith("$ cd "):
            current_tree = current_tree.get_child_by_name(line.split(" ")[2])
            continue
        if line.startswith("dir "):
            current_tree.add_directory(line)
            continue
        current_tree.add_file(line)
    while current_tree.name != "/":
        current_directory_size = current_tree.size
        current_tree = current_tree.get_parent()
        current_tree.size += current_directory_size
    result = Result(0)
    return get_part1_result(root_tree, result)


def solve_part2():
    lines = retrieve_input()
    root_tree = None
    current_tree = None
    created_root = False
    for line in lines:
        if not created_root:
            root_tree = Tree("/", None)
            current_tree = root_tree
            created_root = True
            continue
        if line.startswith("$ ls"):
            continue
        if line.startswith("$ cd .."):
            current_directory_size = current_tree.size
            current_tree = current_tree.get_parent()
            current_tree.size += current_directory_size
            continue
        if line.startswith("$ cd "):
            current_tree = current_tree.get_child_by_name(line.split(" ")[2])
            continue
        if line.startswith("dir "):
            current_tree.add_directory(line)
            continue
        current_tree.add_file(line)
    while current_tree.name != "/":
        current_directory_size = current_tree.size
        current_tree = current_tree.get_parent()
        current_tree.size += current_directory_size
    total_size_used = root_tree.size
    current_free_space = TOTAL_DISK_SPACE - total_size_used
    to_clear = FREE_SPACE_NEEDED - current_free_space
    folder_list = get_folders_large_enough_for_deletion(root_tree, to_clear, list())
    return sorted(folder_list)[0]


if __name__ == "__main__":
    print(solve_part1())  # 1086293
    print(solve_part2())  # 366028
