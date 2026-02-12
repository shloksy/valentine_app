# Valentine_Proposal.py
import streamlit as st
import random
import time
import base64
from streamlit.components.v1 import html

st.set_page_config(page_title="Be My Valentine? 💘", page_icon="❤️", layout="centered")

# ---- Session state ----
if 'accepted' not in st.session_state:
    st.session_state.accepted = False
if 'no_button_disabled' not in st.session_state:
    st.session_state.no_button_disabled = False
if 'no_clicks' not in st.session_state:
    st.session_state.no_clicks = 0
if 'no_pos' not in st.session_state:
    st.session_state.no_pos = {"top": 60, "left": 50}

# Load images
success_screen_img = base64.b64encode(open("images/hq720.jpg", "rb").read()).decode()

# ─── Helper to move NO button while avoiding YES area ───
def move_no():
    st.session_state.no_clicks += 1

    while True:
        top = random.randint(15, 85)
        left = random.randint(5, 95)

        # Avoid center area where YES button lives
        # (roughly middle column)
        if not (40 <= left <= 60 and 40 <= top <= 70):
            break

    st.session_state.no_pos = {"top": top, "left": left}
    st.rerun()

# Heart animation HTML
cute_html = f"""
<div style="text-align:center; padding: 40px 0; font-family: cursive;">
    <h1 style="font-size: 3.8rem; color: #ff3366; margin:0;">YEEEEE 🥰💖</h1>
    <p style="font-size: 1.6rem; color: #ff6699; margin: 20px 0;">
        You're literally goated 😤
    </p>

    <div style="font-size: 4rem; margin: 30px 0; animation: heartBeat 1.2s infinite;">
        ❤️❤️❤️❤️❤️
    </div>

    <img src="data:image/jpeg;base64,{success_screen_img}"
         style="max-width:720px; width:90%; height:auto; border-radius:18px;" />
</div>

<style>
@keyframes heartBeat {{
    0% {{ transform: scale(1); }}
    50% {{ transform: scale(1.25); }}
    100% {{ transform: scale(1); }}
}}
</style>
"""

# ───────────────────────────────────────────────
#               MAIN PAGE
# ───────────────────────────────────────────────

if not st.session
