import streamlit as st
from pathlib import Path
import base64


def prepare_icon(icon):
    icon = icon.read_text().replace("#f0f0f0", "grey").encode("utf-8")
    icon = base64.b64encode(icon).decode("utf-8")
    return f"data:image/svg+xml;base64,{icon}"


icons = Path("./../st_link_analysis/frontend/src/assets/icons").glob("*svg")
icons = sorted(list(icons), key=lambda x: x.stem)
icons = [{"name": icon.stem, "preview": prepare_icon(icon)} for icon in icons]
n_icons = len(icons)

st.markdown("## Supported Icons")
st.dataframe(
    icons,
    width=300,
    height=(n_icons + 1) * 35 + 2,
    column_config={"preview": st.column_config.ImageColumn()})
