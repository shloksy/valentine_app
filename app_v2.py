import random
import streamlit as st

st.set_page_config(page_title="Valentine", layout="wide")

NO_MESSAGES = [
    "Are you sure?",
    "I think u misclicked…",
    "Pls no Aditi ",
    "Be so fr rn",
    "Last chance twin",
]

# --- Session state init ---
if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

if "no_log" not in st.session_state:
    st.session_state.no_log = []

if "no_pos" not in st.session_state:
    # values in percent
    st.session_state.no_pos = {"top": 45, "left": 55}

def randomize_no_position():
    # keep it reasonably on-screen
    st.session_state.no_pos = {
        "top": random.randint(15, 75),
        "left": random.randint(10, 85),
    }

def handle_no():
    i = st.session_state.no_clicks
    if i < len(NO_MESSAGES):
        st.session_state.no_log.append(NO_MESSAGES[i])
    st.session_state.no_clicks += 1
    randomize_no_position()
    st.rerun()

def handle_yes():
    st.session_state.accepted = True
    st.rerun()

# --- CSS to position the No button randomly ---
st.markdown(
    f"""
    <style>
      /* Ensure the container can position children */
      .valentine-stage {{
        position: relative;
        height: 70vh;
        border: 1px solid rgba(0,0,0,0.08);
        border-radius: 12px;
        padding: 24px;
        overflow: hidden;
      }}

      /* Place the "No" button container absolutely */
      .no-button-wrap {{
        position: absolute;
        top: {st.session_state.no_pos["top"]}%;
        left: {st.session_state.no_pos["left"]}%;
        transform: translate(-50%, -50%);
        z-index: 3;
      }}

      /* Make bottom messages area stick to bottom inside stage */
      .bottom-log {{
        position: absolute;
        left: 24px;
        right: 24px;
        bottom: 18px;
        z-index: 2;
      }}

      /* Slightly enlarge buttons */
      div.stButton > button {{
        padding: 0.7rem 1.1rem;
        font-size: 1.05rem;
        border-radius: 10px;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- UI ---
if not st.session_state.accepted:
    st.markdown("## Will you be my Valentine?")

    # Placeholder for image/gif on the yes/no screen
    st.markdown("### (Place your picture/gif here)")
    st.caption("Replace this section with st.image(...) or st.video(...) later.")

    # Create a "stage" area to hold floating No button + messages
    st.markdown('<div class="valentine-stage">', unsafe_allow_html=True)

    # YES button (normal layout)
    col1, col2, col3 = st.columns([1, 1, 6])
    with col1:
        st.button("Yes", on_click=handle_yes)

    # NO button (floating). We render it inside an HTML wrapper.
    # When no_clicks >= len(NO_MESSAGES), hide the No button entirely.
    if st.session_state.no_clicks < len(NO_MESSAGES):
        st.markdown('<div class="no-button-wrap">', unsafe_allow_html=True)
        st.button("No", key="no_btn", on_click=handle_no)
        st.markdown("</div>", unsafe_allow_html=True)

    # Bottom message log
    st.markdown('<div class="bottom-log">', unsafe_allow_html=True)
    if st.session_state.no_log:
        st.markdown("**" + st.session_state.no_log[-1] + "**")
    else:
        st.markdown("&nbsp;", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown("## you+me forever")

    # Placeholder for image/gif on the accepted screen
    st.markdown("### (Place your picture/gif here)")
    st.caption("Replace this with st.image(...) or st.video(...) later.")

    # Optional reset for testing
    if st.button("Reset"):
        st.session_state.accepted = False
        st.session_state.no_clicks = 0
        st.session_state.no_log = []
        st.session_state.no_pos = {"top": 45, "left": 55}
        st.rerun()
