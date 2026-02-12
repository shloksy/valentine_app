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

NO_MESSAGES = [ "Are you sure?", "I think u misclicked…", "Pls no Aditi ", "Be so fr rn", "Cmon twin", "Wrong button bub", "Quit playin jit", "Ur lucky ur beautiful"]

# Load images
success_screen_img = base64.b64encode(open("images/hq720.jpg", "rb").read()).decode()

# Heart explosion & cute animation (very simple JS + emoji version)
cute_html = f"""
<div style="text-align:center; padding: 40px 0; font-family: cursive;">
    <h1 style="font-size: 3.8rem; color: #ff3366; margin:0;">YEEEEE 🥰💖</h1>
    <p style="font-size: 1.6rem; color: #ff6699; margin: 20px 0;">
        You're literally goated 😤
    </p>

    <div style="font-size: 4rem; margin: 30px 0; animation: heartBeat 1.2s infinite;">
        ❤️❤️❤️❤️❤️
    </div>

    <img src="data:image/jpeg;base64,{success_screen_img}" style="border-radius:18px;" />

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

if not st.session_state.accepted:

    st.title("✨ Will You Be My Valentine? 💕")

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:

        st.markdown("<br>" * 3, unsafe_allow_html=True)

        yes = st.button(
            "YES! 💘",
            type="primary",
            use_container_width=True,
            key="yes_btn"
        )

        # ─── IF YES IS CLICKED ───
        if yes:
            st.session_state.accepted = True
            st.session_state.no_button_disabled = True  # 🔥 hide NO immediately
            st.balloons()
            time.sleep(2)
            st.rerun()

        st.write("#")
        # ─── NO BUTTON (only when YES not clicked) ───
        if not st.session_state.no_button_disabled:

            cols = st.columns(3)
            bad_pos = random.randint(0, 2)

            with cols[bad_pos]:
                st.button(
                    "No thanks 😿",
                    key=f"no_{random.randint(1, 999999)}"
                )

else:
    # ─── SUCCESS SCREEN ───────────────────────────────────────
    st.empty()

    html(cute_html, height=850)

    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button("I want to say YES again 💕", type="primary"):
        st.session_state.accepted = False
        st.session_state.no_button_disabled = False
        st.rerun()
