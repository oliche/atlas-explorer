import sys
from collections import deque
from PyQt5.QtWidgets import QTreeView, QWidget, QVBoxLayout, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt5.QtCore import Qt

import numpy as np
from iblutil.numerical import ismember
from iblatlas.atlas import BrainRegions
import qt


class BrainTree(QWidget):

    def __init__(self, regions=None):
        super(BrainTree, self).__init__()
        self.regions = regions or BrainRegions()
        self.tree = QTreeView(self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.tree)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Height', 'Weight'])
        self.tree.header().setDefaultSectionSize(180)
        self.tree.setModel(self.model)
        self.import_brain_regions(self.regions)
        self.tree.expandAll()
        self.setWindowTitle('Allen anatomy parcellation')
        self.setGeometry(300, 100, 600, 300)
        self.show()

    def importdata(self):
        rind = np.unique(self.regions.mappings['Allen'])
        iparents = np.zeros_like(rind)
        a, b = ismember(self.regions.parent[rind], self.regions.id[rind])
        iparents[a] = b
        data = [{
            'unique_id': i,
            'parent_id': iparents[i],
            'short_name': self.regions.acronym[i],
            'height': self.regions.name[i],
            'weight': self.regions.level[i],
            'rgb': self.regions.rgb[i],
        } for i in rind]
        self.model.setRowCount(0)
        root = self.model.invisibleRootItem()
        seen = {}   # List of  QStandardItem
        values = deque(data)
        r = 0
        while values:
            value = values.popleft()
            if value['unique_id'] == 0:
                parent = root
            else:
                pid = value['parent_id']
                if pid not in seen:
                    values.append(value)
                    continue
                parent = seen[pid]
            unique_id = value['unique_id']
            qis = [QStandardItem(value[cname]) for cname in ['short_name', 'height', 'weight']]
            parent.appendRow(qis)
            color = QBrush(QColor(*value['rgb']))
            for q in qis:
                q.setData(color, Qt.BackgroundRole)
            #
            # for c in range(self.model.columnCount()):
            #     self.model.setData(self.model.index(-1, c), QBrush(QColor(255, 0, 0)), Qt.BackgroundRole)
            seen[unique_id] = parent.child(parent.rowCount() - 1)
            r += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = BrainTree()
    view.show()
    sys.exit(app.exec_())


def console():
    """ application entry point """
    qt.create_app()
    av = BrainTree()
    av.show()
    return av
