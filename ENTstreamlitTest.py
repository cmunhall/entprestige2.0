from pyvis.network import Network
from pyvis.network import Network
net = Network(height='80%', width='80%')
import pandas as pd
import networkx as nx
import streamlit as st
import streamlit.components.v1 as components

st.title("Network Visualization of Top 10 ENT Programs")

data = pd.read_csv('~/Desktop/prestigedata.csv')

sources = data['source']
targets = data['target']
weights = data['weight']
size = data['audience.size']
label = data['label']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e [1] 
    w = e[2]

    net.add_node(src, src, title=src)
    net.add_node(dst, dst, title=dst)
    net.add_edge(src, dst, value=w)


net.show_buttons(filter_=True)
net.show('testentgraph.html')