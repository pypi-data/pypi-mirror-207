from .react_jupyter_widget import ReactJupyterWidget

import ipywidgets as widgets
from traitlets import Dict

import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba_array, to_hex
import numpy as np

from .util import get_set_layering, inflate_kwargs

from itertools import chain

converters = {
    'edgecolor': 'Stroke',
    'edgecolors': 'Stroke',
    'facecolor': 'Fill',
    'facecolors': 'Fill',
    'color': 'Fill',
    'colors': 'Fill',
    'linewidths': 'StrokeWidth',
    'linewidth': 'StrokeWidth',
}

def to_camel_case(s):
    return ''.join([
        si.title() if i > 0 else si
        for i, si in enumerate(s.split('_'))
    ])

def prepare_kwargs(items, kwargs, prefix=''):
    return {
        prefix + converters.get(k, k):
            dict(zip(items, hex_array(v) if 'color' in k else v))
        for k, v in inflate_kwargs(items, kwargs).items()
    }

def rename_kwargs(**kwargs):
    return {
        converters.get(k, to_camel_case(k)): v
        for k, v in kwargs.items()
    }

def hex_array(values):
    return [
        to_hex(c, keep_alpha=True)
        for c in to_rgba_array(values)
    ]

def hnx_kwargs_to_props(V, E,
    nodes_kwargs={},
    edges_kwargs={},
    node_labels_kwargs={},
    edge_labels_kwargs={},
    **kwargs
):
    # reproduce default hnx coloring behaviors
    edges_kwargs = edges_kwargs.copy()
    edges_kwargs.setdefault('edgecolors', plt.cm.tab10(np.arange(len(E))%10))
    edges_kwargs.setdefault('linewidths', 2)
    
    # props = kwargs.copy()
    props = {}
    props.update(prepare_kwargs(V, nodes_kwargs, prefix='node'))
    props.update(prepare_kwargs(V, node_labels_kwargs, prefix='nodeLabel'))
    props.update(prepare_kwargs(E, edges_kwargs, prefix='edge'))
    props.update(prepare_kwargs(E, edge_labels_kwargs, prefix='edgeLabel'))
    
    # if not otherwise specified, set the edge label color
    # to be the same as the edge color
    props.setdefault('edgeLabelColor', props['edgeStroke'])

    return {**props, **rename_kwargs(**kwargs)}


def to_dict_without_nans(df):
    df = df.copy()
    df.index = df.index.astype(str)

    return {
        c: df[c].dropna().to_dict()
        for c in df
    }

def incidence_dict_astype_str(H):
    return {
        str(k): list(map(str, v))
        for k, v in H.items()
    }

@widgets.register
class HypernetxWidgetView(ReactJupyterWidget):
    pos = Dict().tag(sync=True)
    node_fill = Dict().tag(sync=True)
    edge_stroke = Dict().tag(sync=True)
    selected_nodes = Dict().tag(sync=True)
    selected_edges = Dict().tag(sync=True)
    hidden_nodes = Dict().tag(sync=True)
    hidden_edges = Dict().tag(sync=True)
    removed_nodes = Dict().tag(sync=True)
    removed_edges = Dict().tag(sync=True)

    @property
    def state(self):
        return {
            'pos': self.pos,
            'node_fill': self.node_fill,
            'edge_stroke': self.edge_stroke,
            'selected_nodes': self.selected_nodes,
            'selected_edges': self.selected_edges,
            'hidden_nodes': self.hidden_nodes,
            'hidden_edges': self.hidden_edges,
            'removed_nodes': self.removed_nodes,
            'removed_edges': self.removed_edges
        }

    def get_index(self, selection={}):
        return [
            k
            for k, v in selection.items()
            if v
        ]

    @property
    def selected_node_data(self):
        return self.node_data.loc[self.get_index(self.selected_nodes)]

    @property
    def selected_edge_data(self):
        return self.edge_data.loc[self.get_index(self.selected_edges)]

    def __init__(self, H,
        collapse=True,
        node_styles={},
        with_color=True,
        ignore_hnx_properties=False,
        **kwargs
    ):
        incidence_dict = H.edges.incidence_dict\
            if H.__class__.__name__ == 'Hypergraph'\
            else H

        incidence_dict = incidence_dict_astype_str(incidence_dict)

        def get_property(id, value, default):
            if value is None:
                return default
            elif hasattr(value, 'get'):
                return value.get(id, default)
            else:
                return value
            
        V = set(chain.from_iterable(incidence_dict.values()))
        E = list(incidence_dict)

        nodes = [{'uid': uid} for uid in V]
        
        # js friendly representation of the hypergraph
        edges = [
            {
                'uid': uid,
                'elements': elements
            }
            for uid, elements in incidence_dict.items()
        ]

        # used to convert Hnx 1.2 style properties into dataframes compatible with widget
        def prepare_properties(props):
            df = pd.concat([
                props.drop(columns=['properties', 'uid']),
                pd.DataFrame(props.properties.tolist(), index=props.properties.index)
            ], axis=1)
            
            col_mask = (~df.isnull()).any(axis=0)
            
            return df[df.columns[col_mask]]

        if not ignore_hnx_properties and hasattr(H, 'edges') and hasattr(H, 'nodes'):
            # check if Hypergraph object contains properties
            kwargs['edge_data'] = prepare_properties(H.edges.properties.loc[0])
            kwargs['node_data'] = prepare_properties(H.nodes.properties.loc[0])

        if 'node_data' in kwargs:
            self.node_data = kwargs['node_data']
            kwargs['node_data'] = to_dict_without_nans(self.node_data.T)

        if 'edge_data' in kwargs:
            self.edge_data = kwargs['edge_data']
            kwargs['edge_data'] = to_dict_without_nans(self.edge_data.T)
            
        super().__init__(
            nodes=nodes,
            edges=edges,
            **hnx_kwargs_to_props(V, E, **kwargs)
        )

@widgets.register
class HypernetxWidget(HypernetxWidgetView):
    pass
