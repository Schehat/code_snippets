def student_info(*args, **kwargs):
    print(args)  # positional arguments
    print(kwargs)  # optional arguments


student_info("Math", "Art", name="Schehat", age=20)

courses = ("Math", "Art")
info = {"name": "Schehat", "age": 20}

print("\n does take everything as a args & does not unpack the values:")
student_info(courses, info)  # output not exactly what we want

print("\n differentiates between args and kwargs & unpacks the values:")
student_info(*courses, **info)  # this is what we want


def student_info2(subject1, subject2, name=None, age=None):
    print(subject1, subject2, name, age)


print("\nmore common to specify parameters but pass args & kwargs")
student_info2(*courses, **info)
