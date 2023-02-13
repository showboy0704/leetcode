from collections import Counter


class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        foods, tables = set(), dict()
        for _, table, food in orders:
            if int(table) not in tables:
                tables[int(table)] = Counter()
            tables[int(table)][food] += 1
            foods.add(food)
        dispalys = [['Table'] + sorted(foods)]
        print(tables)
        for table, meals in sorted(tables.items()):
            display = [str(table)]
            for food in sorted(foods):
                display.append(str(meals[food]))
            dispalys.append(display)

        return dispalys


if __name__ == '__main__':
    orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"], [
        "Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
    print(f"{orders}")
    print('----------Answer Below----------')
    print(Solution().displayTable(orders))
