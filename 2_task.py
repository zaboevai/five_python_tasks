class Node:
    def __init__(self, name):
        self.name= name
        self.children = []

    def add_child(self, obj):
            self.children.append(obj)

# У каждого узла (Node) есть имя и потомки. Пример:

a = Node('A')
b = Node('B')
g = Node('G')
h = Node('H')
a_Goal = Node('Goal')

l = Node('L')
k = Node('K')
j = Node('J')
p = Node('P')

a.add_child(b)
b.add_child(g)

g.add_child(h)
h.add_child(l)
h.add_child(k)
h.add_child(j)
# h.add_child(a_Goal)
g.add_child(p)
p.add_child(a_Goal)


def get_tree(obj):
    if obj.name == 'Goal':
        return obj.name

    for child in obj.children:
        name = get_tree(child)
        if name:
            break
    else:
        return None

    return f'{obj.name} -> {name}'


print(get_tree(a))