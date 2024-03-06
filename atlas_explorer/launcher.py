from pathlib import Path
import numpy as np
from atlas_explorer.gui import atlasview  # mouais il va falloir changer ça
self = atlasview()

""" Roadmap
    - swap volumes combox (label RGB option / density)
    - overlay brain regions with transparencye
    - overlay volumes (for example coverage with transparency)
    - overlay plots: probes channels
    - tilted slices
    - coordinate swaps: add Allen / Needles / Voxel options
    - should we add horizontal slices ?
"""

# # add brain regions feature:
# reg_values = np.load(Path(atlasview.__file__).parent.joinpath('region_values.npy'))
# av.add_regions_feature(reg_values, 'Blues', opacity=0.7)
#
# # add scatter feature:
# chans = np.load(
#     Path(atlasview.__file__).parent.joinpath('channels_test.npy'), allow_pickle=True)
# av.add_scatter_feature(chans)
# self.ctrl.fig_tree.uiTreeRegions
#
# self.ctrl.fig_tree.show()


## %%
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
#
# departments = ['Sales', 'Marketing', 'HR']
# employees = {
#     'Sales': ['John', 'Jane', 'Peter'],
#     'Marketing': ['Alice', 'Bob'],
#     'HR': ['David'],
# }
# tree = self.ctrl.fig_tree.uiTreeRegions
# tree.setColumnCount(2)
# tree.setHeaderLabels(["Name", "Type"])
#
# data = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
#         "Project B": ["file_b.csv", "photo.jpg"],
#         "Project C": []}
#
# items = []
# for key, values in data.items():
#     item = QTreeWidgetItem([key])
#     for value in values:
#         ext = value.split(".")[-1].upper()
#         child = QTreeWidgetItem([value, ext])
#         item.addChild(child)
#     items.append(item)
#
# tree.insertTopLevelItems(0, items)
#
# root_model = QTreeWidgetItem()
# self.tree.setModel(root_model)
# self._populateTree(tree, root_model.invisibleRootItem())
#
#
# def _populateTree(self, children, parent):
#     for child in sorted(children):
#         child_item = QTreeWidgetItem(child)
#         parent.appendRow(child_item)
#         if isinstance(children, types.DictType):
#             self._populateTree(children[child], child_item)