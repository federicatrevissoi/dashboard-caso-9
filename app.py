#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:43:35 2026

@author: fede
"""

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Dashboard Caso 9",
    layout="wide"
)

html_path = Path(__file__).parent / "dashboard.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=900, scrolling=True)