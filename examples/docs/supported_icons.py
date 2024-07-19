import streamlit as st
from pathlib import Path


def prepare_svg(svg: Path) -> str:
    return f"""\
        <tr>
            <td>{svg.stem}</td>
            <td>{svg.read_text().replace("#f0f0f0", "grey")}</td>
        </tr> """


icons = Path("./../st_link_analysis/frontend/src/assets/icons").glob("*svg")
icons = sorted(list(icons), key=lambda x: x.stem)
icons = "".join([prepare_svg(icon) for icon in icons])
icons = f"""\
<html>
    <head>
        <style>
            table {{
                margin: 0 auto;
                width: 80%;
            }}
        </style>
    </head>
    <table>
        <tr>
            <th>Name</th>
            <th>Icon</th>
        </tr>
        {icons}
    </table>
</html>
"""

st.markdown("## Supported Icons")
st.markdown(icons, unsafe_allow_html=True)
