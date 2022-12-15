from __future__ import annotations
from typing import List, Dict
import pprint
pp = pprint.pprint


class File(object):
    def __init__(self, file_size: int, file_name: str) -> None:
        self.file_size: int = file_size
        self.file_name: str = file_name

    def __str__(self) -> str:
        return f"{self.file_name} : {self.file_size}"


class Directory(object):
    #  as you walk through it
    #  root dir only shows up once
    #  all directories will need to be summed under /
    #  each directory under root will need to be summed up

    # look for the pattern cd
    # ls is a no op
    # dir is a no op
    #  cd .. = parent_directory

    def __init__(self, parent_directory: Directory = None, directory_name: str = "/") -> None:
        # list_tuples
        self.files: List[File] = []
        # dictionary
        self.directories: Dict[str, Directory] = {}
        # parent directory
        self.parent_directory: Directory = parent_directory
        # directory name
        self.directory_name: str = directory_name

    def __str__(self) -> str:
        str_files = []
        for file in self.files:
            str_files.append(str(file))
        return f"{self.directory_name} : {str_files}"

    def add_file(self, file_size: int, file_name: str) -> None:
        new_file = File(file_size, file_name)
        self.files.append(new_file)

    def add_directory(self, directory_name: str) -> None:
        # this is the dunder init object self aka parent_directory
        new_directory = Directory(parent_directory=self, directory_name=directory_name)
        self.directories[directory_name] = new_directory
        print(f"Added directory {directory_name} to Directory class object {self.directory_name}")

    def file_sizes(self) -> List[int]:
        output = []
        for file in self.files:
            output.append(file.file_size)
        for directory in self.directories.values():
            output += directory.file_sizes()
        return output

    def file_sums(self, path="/") -> Dict[str, int]:
        output = {self.directory_name: sum(self.file_sizes())}
        for directory_name, directory in self.directories.items():
            # output[directory_name] = sum(directory.file_sizes())
            sub_dir_output = directory.file_sums(directory_name + "/")
            for file_name, file_size in sub_dir_output.items():
                output[path + file_name] = file_size
        return output


# Type hinting for class Object Directory
top_dir: Directory = Directory()
current_dir: Directory = top_dir

system_file = "day7_input.txt"

# Part 1 - parse the inout file and make the data structure in python Class
with open(system_file) as f:
    system_lines = f.readlines()

for line in system_lines:
    line = line.strip()
    # print(line)
    instructions = line.split(" ")
    if instructions[0] == "$":
        command = instructions[1]
        if command == "cd":
            cd_location = instructions[2]
            if cd_location == "/":
                current_dir = top_dir
                pp("----Top----")
            elif cd_location == "..":
                current_dir = current_dir.parent_directory
                pp("----Parent----")
            else:
                current_dir = current_dir.directories[cd_location]
                pp("----Sub Directory----")
        # elif command == "ls":
            # continue
    elif instructions[0] == "dir":
        dir_name = instructions[1]
        current_dir.add_directory(directory_name=dir_name)
    else:
        file_size = int(instructions[0])
        file_name = instructions[1]
        current_dir.add_file(file_size=file_size, file_name=file_name)

pp(str(top_dir))
pp("------------")
pp(str(top_dir.directories["fml"]))
pp("------------")
output = top_dir.file_sums()
total_filesystem_size = output["/"]
fml_size = output["/" + "fml"]
jbgpgvj_size = output["/jbgpgvj"]
qjphltd_size = output["/qjphltd"]
wlfprc_size = output["/wlfprc"]
zqvh_size = output["/zqvh"]
zzmgz_size = output["/zzmgz"]
subs_total = (fml_size + jbgpgvj_size + qjphltd_size + wlfprc_size + zqvh_size + zzmgz_size)
pp(subs_total)
pp("====================")
pp(total_filesystem_size - subs_total)
pp("====================")
pp(f"This is the output: {output}")
result = 0
for directory_size in output.values():
    if directory_size <= 100_000:
        result += directory_size

print(f" End result of all dirs ~100k or less: {result}")

filesystem = 70_000_000
top_dir_size = output["/"]
free_space = filesystem - top_dir_size
space_needed = 30_000_000 - free_space
pp(space_needed)

min_result = top_dir_size
for directory_name, directory_size in output.items():
    if directory_size >= space_needed and directory_size < min_result:
        min_result = directory_size
        pp(directory_name + ":" + str(directory_size))

