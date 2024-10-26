def sing_beer_song(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
        bottles -= 1
    if bottles == 1:
        print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        print(f"Take one down and pass it around, no more bottles of beer on the wall.\n")
    print("Go to the store and buy some more!")

num_bottles = int(input("How many bottles of beer are on the wall? "))
sing_beer_song(num_bottles)