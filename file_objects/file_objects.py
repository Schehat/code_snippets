import os

# # open file, not recommended that way
# # r: read, w: write, a: append, r+: read & write
# f = open(f"{os.path.join(os.path.dirname(__file__), 'text.txt')}", "r", encoding="UTF-8")

# print(f"get file path: {f.name}")
# print(f"get mode of file: {f.mode}\n")

# f.close()

# context manager best practice due to file closes automatically after the block, also in exceptions
# in w mode: when file exists it will be overwritten otherwise the file will be created
with open(
    f"{os.path.join(os.path.dirname(__file__), 'text2.txt')}", "w", encoding="UTF-8"
) as f:
    # reading:
    # after read reads the entire file it returns an empty string
    # print(f"f.read: {f.read()}\n")

    # print(f"f.readlines: {f.readlines()}\n")  # list with lines as elements
    # print(f"f.readline: {f.readline()}\n", end='')  # goes line by line

    # for line in f:
    #     print(f.readline(), end="")

    # print(f.read(100))  # prints first 100 characters

    # size_to_read = 10
    # f_contents = f.read(size_to_read)

    # f.seek(0)  # sets cursor to 0

    # f_contents = f.read(size_to_read)

    # print(f"\n current position {f.tell()}\n")

    # while len(f_contents) > 0:
    #     print(f_contents, end="***")
    #     f_contents = f.read(size_to_read)

    f.write("Test")
    f.seek(0)
    f.write("R")  # will overwrite the T in Test

# copy text file
with open(
    f"{os.path.join(os.path.dirname(__file__), 'text.txt')}", "r", encoding="UTF-8"
) as rf:
    with open(
        f"{os.path.join(os.path.dirname(__file__), 'test_copy.txt')}",
        "w",
        encoding="UTF-8",
    ) as wf:
        for line in rf:
            wf.write(line)

# copy jpg file
# encoding vanishes & mode rb & wb for binary
with open(
    f"{os.path.join(os.path.dirname(__file__), 'astronaut.jpg')}",
    "rb",
) as rf:
    with open(
        f"{os.path.join(os.path.dirname(__file__), 'astronaut_copy.jpg')}", "wb"
    ) as wf:
        for line in rf:
            wf.write(line)

with open(
    f"{os.path.join(os.path.dirname(__file__), 'astronaut.jpg')}",
    "rb",
) as rf:
    with open(
        f"{os.path.join(os.path.dirname(__file__), 'astronaut_chunk.jpg')}", "wb"
    ) as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
