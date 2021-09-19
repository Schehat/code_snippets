import os

os.chdir(os.path.dirname(__file__))

for f in os.listdir():
    if f == os.path.basename(__file__):
        continue
    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split()

    f_num = f_num.zfill(2)  # padding with zeros otherwise 10 would come after 1

    os.rename(f, (f"{f_num}-{f_title}{f_ext}"))
