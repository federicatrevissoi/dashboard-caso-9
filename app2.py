#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:09:38 2026

@author: fede
"""

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Caso 9 — Pricing & Sales Analytics", layout="wide")

st.markdown("""
    <style>
        .block-container { padding: 0rem; max-width: 100%; }
        header, footer, #MainMenu { visibility: hidden; height: 0; }
    </style>
""", unsafe_allow_html=True)

html_content = (Path(__file__).parent / "dashboard.html").read_text(encoding="utf-8")
components.html(html_content, height=1100, scrolling=True)