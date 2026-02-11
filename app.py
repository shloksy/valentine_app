import streamlit as st
import random

st.set_page_config(page_title="Valentine 💘", page_icon="💘", layout="centered")

# ---- EDIT THESE ----
ASK_SCREEN_MEDIA = None  # put a URL or upload below; None = placeholder
YES_SCREEN_MEDIA = None  # put a URL or upload below; None = placeholder

NO_MESSAGES = [
    "Are you sure? 😳",
    "I think u misclicked…",
    "Pls no Aditi 😭",
    "Be so fr rn",
    "Last chance twin 😤",
]

# ---- Session state init ----
if "stage" not in st.session_state:
    st.session_state.stage = "ask"  # "ask" or "yes"
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0
if "button_position" not in st.session_state:
    st.session_state.button_position = {"left": "50%", "top": "50%"}

def reset():
    st.session_state.stage = "ask"
    st.session_state.no_clicks = 0
    st.session_state.button_position = {"left": "50%", "top": "50%"}

def click_no():
    st.session_state.no_clicks += 1
    # Generate random position
    st.session_state.button_position = {
        "left": f"{random.randint(10, 90)}%",
        "top": f"{random.randint(10, 90)}%"
    }

def click_yes():
    st.session_state.stage = "yes"

# ---- Styles: shrinking No button via CSS ----
# We'll render the No button inside a container with a scaling transform.
# After 5 clicks, we hide it.
scale_steps = [1.0, 0.85, 0.7, 0.55, 0.4, 0.25]
no_clicks = st.session_state.no_clicks
scale = scale_steps[min(no_clicks, len(scale_steps) - 1)]

hide_no = no_clicks >= 5

st.markdown(
    """
    <style>
      .val-title { text-align: center; font-size: 42px; font-weight: 800; margin-top: 10px; }
      .val-sub { text-align: center; font-size: 18px; margin-bottom: 10px; opacity: 0.9; }
      .center { display: flex; justify-content: center; }
      .msg { text-align: center; font-size: 20px; margin-top: 10px; }
      .media-box { display:flex; justify-content:center; margin-top: 10px; margin-bottom: 10px; }
      .hint { text-align:center; font-size: 12px; opacity: 0.7; margin-top: 30px; }
      .moving-button { position: fixed; z-index: 999; }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.session_state.stage == "ask":
    st.markdown('<div class="val-title">Will you be my Valentine? 💝</div>', unsafe_allow_html=True)

    # ---- Media placeholder (ASK screen) ----
    st.markdown('<div class="media-box">', unsafe_allow_html=True)
    if ASK_SCREEN_MEDIA:
        # If it's a gif/video/image URL, st.image handles images/gifs, st.video handles videos.
        # Easiest: use st.image for gif/image URLs.
        st.image(ASK_SCREEN_MEDIA, use_container_width=False)
    else:
        st.info("📷 Placeholder: put a picture/GIF here (see uploader below).")
    st.markdown('</div>', unsafe_allow_html=True)

    # Optional uploader so YOU can upload media when deploying
    with st.expander("Upload media (optional)"):
        up1 = st.file_uploader("Ask-screen media (png/jpg/gif)", type=["png","jpg","jpeg","gif"], key="up1")
        if up1:
            st.image(up1, use_container_width=False)

        up2 = st.file_uploader("Yes-screen media (png/jpg/gif)", type=["png","jpg","jpeg","gif"], key="up2")
        if up2:
            st.image(up2, use_container_width=False)

    # ---- Message changes after No clicks ----
    if no_clicks > 0:
        msg = NO_MESSAGES[min(no_clicks - 1, len(NO_MESSAGES) - 1)]
        st.markdown(f'<div class="msg">{msg}</div>', unsafe_allow_html=True)

    # ---- Buttons row ----
    col1, col2 = st.columns(2)

    with col1:
        st.button("Yes ✅", on_click=click_yes, use_container_width=True)

    with col2:
        if not hide_no:
            # Position the No button at a random location
            left = st.session_state.button_position["left"]
            top = st.session_state.button_position["top"]
            
            st.markdown(f"""
                <div class="moving-button" style="left: {left}; top: {top}; transform: translate(-50%, -50%) scale({scale});">
            """, unsafe_allow_html=True)
            st.button("No ❌", on_click=click_no)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown('<div class="msg">Okay… I'll take that as a Yes</div>', unsafe_allow_html=True)

    st.markdown('<div class="hint">Tip: once hosted, she just opens a link and clicks.</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="val-title">you + me forever 💘</div>', unsafe_allow_html=True)
    st.markdown('<div class="val-sub">(I knew you'd say yes 😎)</div>', unsafe_allow_html=True)

    st.markdown('<div class="media-box">', unsafe_allow_html=True)
    if YES_SCREEN_MEDIA:
        st.image(YES_SCREEN_MEDIA, use_container_width=False)
    else:
        st.success("🎁 Placeholder: put a picture/GIF here for the celebration screen.")
    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.button("Back", on_click=reset, use_container_width=True)
    with c2:
        st.button("Reset", on_click=reset, use_container_width=True)
