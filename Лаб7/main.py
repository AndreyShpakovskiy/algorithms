from Tree import BinaryTree
from BPlusTree import BPlusTree
import plotly.express as px
import pandas
import time
import random

tree = BinaryTree()

for _ in range(16):
    num = random.randint(0, 150)
    tree.insert_node(tree.root, num)

# tree.insert_node(tree.root, 5)
# tree.insert_node(tree.root, 2)
# tree.insert_node(tree.root, 7)
# tree.insert_node(tree.root, 10)
# tree.print()
# tree.find(11)


def experimental_evaluation_data_bin_tree(repetitions):
    chart_data = []
    for i in range(repetitions):
        current_node_count = 100 + i * 10000
        current_tree = BinaryTree()
        for _ in range(current_node_count):
            num = random.randint(0, 160)
            current_tree.insert_node(current_tree.root, num)

        start_time = time.time()
        for _ in range(100 + i * 10000):
            current_tree.find(random.randint(0, 160))
        duration = time.time() - start_time

        chart_data.append(dict(size=current_node_count, time=duration))
    return chart_data


def draw_chart(chart_data):
    chart_data.sort(key=lambda d: d['size'])
    print(chart_data)
    fig = px.line(chart_data, x="size", y="time")
    fig.show()



print("----BPlusTree----")

b_plus_tree = BPlusTree(order=5)
for i in range(16):
    num = random.randint(0, 150)
    b_plus_tree.insert(num, num)

b_plus_tree.show()

find = random.randint(0, 160)
print(find)
print(b_plus_tree.retrieve(find))


def experimental_evaluation_data_b_plus_tree(repetitions):
    chart_data = []

    for i in range(repetitions):
        current_tree = BPlusTree(5)
        current_node_count = 100 + i * 10000
        for j in range(current_node_count):
            num = random.randint(0, 160)
            current_tree.insert(num, j)

        start_time = time.time()
        for _ in range(100 + i * 10000):
            current_tree.retrieve(random.randint(0, 160))
        duration = time.time() - start_time

        chart_data.append(dict(size=current_node_count, time=duration))
    return chart_data


draw_chart(experimental_evaluation_data_bin_tree(10))
draw_chart(experimental_evaluation_data_b_plus_tree(20))
