def main():
    # Accept fruit
    fruit = input("Item: ").lower()
    if (n := nutrition(fruit)) is not None:
        print(n)
    else:
        pass

def nutrition(fruit):
    fruits = {"apple": 130,
          "avocado": 50,
          "banana": 110,
          "cantaloupe": 50,
          "grapefruit": 60,
          "grapes": 90,
          "honeydew melon": 50,
          "kiwifruit": 90,
          "lemon": 10,
          "lime": 20,
          "nectarine": 60,
          "orange": 80,
          "peach": 60,
          "pear": 100,
          "pineapple": 50,
          "plums": 70,
          "strawberries": 50,
          "sweet cherries": 100,
          "tangerine": 50,
          "watermelon": 80
          }
    
    if fruit in fruits:
        return f"Calories: {fruits[fruit]}"
    else:
        return None


if __name__ == "__main__":
    main()
