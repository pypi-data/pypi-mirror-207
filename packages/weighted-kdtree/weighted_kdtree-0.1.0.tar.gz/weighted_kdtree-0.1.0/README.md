# kdtreePython
KDTree implementation with the support of weights.

Example:

1. Creating kdtree
```
from weighted_kdtree import kdtree
points = [(12,34), (25,36), (9,10), (5, 15), (30, 20), (20, 27)]
weights = [10, 20, 12, 20, 30, 28]
kd_tree = kdtree.KDTree(points, weights)
```

2. Preorder Traversal 
```
kdtree.KDTree.preorderTraversal(kd_tree.root)
[[(9, 10)], [(12, 34)], [(5, 15)], [(30, 20)], [(25, 36)], [(20, 27)]]
```

3. Weights
```
kd_tree.root.val, kd_tree.root.weight["weight"],  kd_tree.root.weight["minWeight"],  kd_tree.root.weight["maxWeight"]
((20, 27), 28, 30, 10)
```