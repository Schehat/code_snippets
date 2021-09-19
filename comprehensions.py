arr = [n for n in range(10)]
print(f"1: {arr}\n")

arr = [n * n for n in range(10)]
print(f"2: {arr}\n")

arr = [n for n in range(10) if n % 2 == 0]
print(f"3 with if: {arr}\n")

arr = [(letter, num) for letter in "abcd" for num in range(4)]
print(f"4 nested loop: {arr}\n")

names = ["Bruce", "Tony"]
heros = ["Batman", "Iron Man"]

arr = {name: hero for name, hero in zip(names, heros)}
print(f"5 create dictionary: {arr}\n")

nums = {1, 2, 6, 4, 2, 1, 4, 6, 3, 2, 1, 5, 6, 2}
arr = {n for n in nums}
print(f"6 create set: {arr}\n")

print("7 generator comprehension:")
my_gen = (n * n for n in range(10))
for n in my_gen:
    print(n)
