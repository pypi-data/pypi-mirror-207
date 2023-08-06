from collections import defaultdict
from typing import Optional

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.cm import ScalarMappable

from clustree._clustree_typing import (
    CMAP_TYPE,
    COLOR_AGG_TYPE,
    EDGE_COLOR_TYPE,
    EDGE_CONFIG_TYPE,
    NODE_COLOR_TYPE,
    NODE_CONFIG_TYPE,
)
from clustree._config_helpers import data_to_color, get_aggr_func_name
from clustree._hash import hash_edge_id, hash_node_id

CONTROL_LIST = ["init", "sample_info", "node_color", "edge_color"]
DEFAULT_CONFIG = {k: True for k in CONTROL_LIST}


class ClustreeConfig:
    def __init__(
        self,
        kk: int,
        data: pd.DataFrame,
        prefix: str,
        node_color: NODE_COLOR_TYPE = None,
        node_color_aggr: COLOR_AGG_TYPE = None,
        node_cmap: CMAP_TYPE = None,
        edge_color: EDGE_COLOR_TYPE = None,
        edge_cmap: CMAP_TYPE = None,
        start_at_1: bool = True,
        _setup_cf: Optional[dict[str, bool]] = None,
    ):
        if not node_color or node_color == "prefix":
            node_color = prefix
        if not edge_color:
            edge_color = "samples"
        elif edge_color == "prefix":
            edge_color = prefix
        if not _setup_cf:
            _setup_cf = DEFAULT_CONFIG
        if not node_cmap:
            node_cmap = plt.cm.Blues
        if not edge_cmap:
            edge_cmap = plt.cm.Reds

        self.prefix = prefix
        self.kk = kk
        self.start_at_1 = start_at_1
        self.node_cf: NODE_CONFIG_TYPE = defaultdict(dict)
        self.edge_cf: EDGE_CONFIG_TYPE = defaultdict(dict)
        self.k_upper_to_node_id: dict[int, list[int]] = {}
        self.node_color_sm: Optional[ScalarMappable] = None
        self.edge_color_sm: Optional[ScalarMappable] = None
        self.node_color_legend_title: Optional[str] = None
        self.edge_color_legend_title: Optional[str] = None

        self.membership_cols = [
            f"{prefix}{str(k_upper)}" for k_upper in range(1, kk + 1)
        ]
        cluster_membership = data[self.membership_cols].to_numpy()

        if _setup_cf["init"]:
            self.init_cf()
        if _setup_cf["sample_info"]:
            self.set_sample_information(data=cluster_membership)
        if _setup_cf["node_color"]:
            self.set_node_color(
                node_color=node_color,
                aggr=node_color_aggr,
                cmap=node_cmap,
                prefix=prefix,
                data=data,
            )
        if _setup_cf["edge_color"]:
            self.set_edge_color(edge_color=edge_color, cmap=edge_cmap, prefix=prefix)

    def init_cf(self) -> None:
        for k_upper in range(1, self.kk + 1):
            if self.start_at_1:
                _iter = range(1, k_upper + 1)
            else:
                _iter = range(0, k_upper)
            for k_lower in _iter:
                ind = hash_node_id(k_upper=k_upper, k_lower=k_lower)
                self.node_cf[ind].update({"k": k_lower, "res": k_upper})

    def set_sample_information(self, data: np.ndarray) -> None:
        """

        Parameters
        ----------
        data : ndarray
            Column 0 must be cluster membership for K = 1, and so on, finally column \
            (kk - 1) must be cluster membership for K = kk

        Returns
        -------
            None
        """
        for k_upper in range(1, self.kk + 1):

            col = k_upper - 1  # use (k_upper - 1) since data is 0-indexed
            vals, counts = np.unique(data[:, col], return_counts=True)
            for k_end, node_samples in zip(vals, counts):
                # get #samples at each node
                end_hashed = hash_node_id(k_upper=k_upper, k_lower=int(k_end))
                self.node_cf[end_hashed]["samples"] = int(node_samples)

                if k_upper > 1:
                    # get #samples along each incoming edge
                    ind = data[:, col] == k_end
                    to_count = data[ind, col - 1]
                    vals, counts = np.unique(to_count, return_counts=True)
                    for k_start, edge_samples in zip(vals, counts):
                        start_hashed = hash_node_id(
                            k_upper=k_upper - 1, k_lower=int(k_start)
                        )
                        self.edge_cf[
                            hash_edge_id(
                                k_upper=k_upper,
                                k_end=int(k_end),
                                k_start=int(k_start),
                            )
                        ].update(
                            {
                                "in_prop": (float(edge_samples) / float(node_samples)),
                                "samples": int(edge_samples),
                                "start": start_hashed,
                                "end": end_hashed,
                                "res": k_upper,
                            }
                        )

    def set_node_color(
        self,
        node_color: NODE_COLOR_TYPE,
        cmap: CMAP_TYPE,
        aggr: COLOR_AGG_TYPE,
        data: pd.DataFrame,
        prefix: str,
    ) -> None:
        if node_color == prefix:
            for node_id, attr in self.node_cf.items():
                self.node_cf[node_id]["node_color"] = mpl.colors.to_rgba(
                    f"C{attr['res']}"
                )
        elif (use_samples := node_color == "samples") or (node_color in data.columns):
            # create to_parse = {node_id: value}
            if use_samples:
                to_parse = {k: v["samples"] for k, v in self.node_cf.items()}
                self.node_color_legend_title = "node: count"
            else:
                if not aggr:
                    raise ValueError(
                        "Cannot calculate node color without aggregate function"
                    )
                self.node_color_legend_title = (
                    f"node: {get_aggr_func_name(aggr=aggr)}_{node_color}"
                )
                to_parse = {
                    hash_node_id(k_upper=k_upper, k_lower=k_lower): float(val)
                    for k_upper, cluster_col in enumerate(self.membership_cols, 1)
                    for k_lower, val in data.groupby(cluster_col)[node_color]
                    .agg(aggr)
                    .to_dict()
                    .items()
                }

            # convert to_parse to {node_id: color}
            rgba, sm = data_to_color(data=to_parse, cmap=cmap)
            self.node_color_sm = sm
            for k, v in rgba.items():
                self.node_cf[k]["node_color"] = v
        else:  # fixed color, e.g., mpl.colors object
            for node_id in self.node_cf:
                self.node_cf[node_id]["node_color"] = mpl.colors.to_rgba(node_color)

    def set_edge_color(
        self,
        edge_color: EDGE_COLOR_TYPE,
        cmap: CMAP_TYPE,
        prefix: str,
    ) -> None:
        if edge_color == prefix:
            for edge_id, attr in self.edge_cf.items():
                self.edge_cf[edge_id]["edge_color"] = f"C{attr['res']}"
        elif edge_color == "samples":
            # create to_parse = {edge_id: value}
            to_parse = {k: v["samples"] for k, v in self.edge_cf.items()}

            # convert to_parse to {edge_id: color}
            rgba, sm = data_to_color(data=to_parse, cmap=cmap)
            self.edge_color_sm = sm
            self.edge_color_legend_title = "edge: count"

            for k, v in rgba.items():
                self.edge_cf[k]["edge_color"] = v
        else:  # fixed color, e.g., mpl.colors object
            for edge_id in self.edge_cf:
                self.edge_cf[edge_id]["edge_color"] = edge_color
