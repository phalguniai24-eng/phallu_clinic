import streamlit as st
import base64

st.set_page_config(
    page_title="Friendship Clinic",
    page_icon="🏥",
    layout="centered"
)

with open("styles_clinic.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


if "welcome" not in st.session_state:

    st.session_state.welcome = True


# -------------------
# Background
# -------------------

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("assets/cute_bg.jpg")

st.markdown(
f"""
<style>

.stApp {{
    background: transparent;
}}

.stApp::before {{

    content:"";

    position:fixed;

    top:0;
    left:0;

    width:100%;
    height:100%;

    background:url("data:image/jpg;base64,{bg}");

    background-size:cover;
    background-position:center;

    filter:blur(10px);

    transform:scale(1.1);

    z-index:-2;
}}

.stApp::after {{

    content:"";

    position:fixed;

    top:0;
    left:0;

    width:100%;
    height:100%;

    background:rgba(255,255,255,0.25);

    z-index:-1;
}}

</style>
""",
unsafe_allow_html=True
)

st.markdown("""
<div class="clinic-title">
🏥 Dr. PHALLU's CLINIC
</div>

<div class="clinic-subtitle">
Official Emotional Support Prescription Center
</div>
""", unsafe_allow_html=True)

st.write("")

name = "ADIII 🤍"

with st.sidebar:

    st.markdown("# 🩺 Quick Navigation")

    st.markdown("""
- [🏠 Home](#home)
- [🩺 Diagnosis](#diagnosis)
- [💊 Prescription](#prescription)
- [🌸 Mood Scan](#mood-scan)
- [🚨 Emergency Kit](#emergency-kit)
- [📸 Memory Vault](#memory-vault)
- [🎵 Our Soundtrack](#our-soundtrack)
- [💌 Confidential Letter](#confidential-letter)
""")

st.markdown("""
<div style="
text-align:center;
padding:30px;
margin-bottom:20px;
">

<div style="
font-size:120px;
font-weight:900;
color:#a4512d;
text-shadow:0px 5px 25px rgba(242,140,82,0.4);
">
ADIII 🤍
</div>

<div style="
font-size:22px;
color:#7a5f52;
">
Official Friendship Clinic Patient
</div>

</div>
""", unsafe_allow_html=True)
st.info(
    "💗 Reminder: Even wizards take breaks. You are allowed to rest too."
)

st.markdown("""
<div class="quote-card">

"Please stop carrying the whole world by yourself."

<br><br>

— Phal🤍

</div>
""", unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "Stress Level",
        "99%",
        "-1%"
    )

with col2:
    st.metric(
        "Hug Requirement",
        "Unlimited",
        "∞"
    )

with col3:
    st.metric(
        "Best Friend Approval",
        "100%",
        "+100%"
    )

st.markdown("""
<div class="verdict-card">

🏥 Today's Medical Verdict

<br><br>

Patient is exhausted.

<br>

Patient is overthinking.

<br>

Patient is loved.

<br><br>

Further testing unnecessary.

</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="clinic-card">', unsafe_allow_html=True)
st.markdown("""
<div class="glass-card">
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-card">

<h2>🩺 Patient Record</h2>

<b>Patient Name</b><br>
ADIII 🤍

<br><br>

<b>Age</b><br>
Too young to be this stressed.

<br><br>

<b>Date</b><br>
Immediately.

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div id="diagnosis"></div>

<div class="section-card">

<h2>🩺 Official Diagnosis</h2>

☑ Acute Overworking Syndrome

<br><br>

<b>Symptoms Observed</b>

<ul>
<li>Excessive hard work</li>
<li>Constant overthinking</li>
<li>Random sighing at 2 AM</li>
<li>Acting strong even when exhausted</li>
<li>Forgetting how amazing he actually is</li>
</ul>

<b>Severity</b>

<br>

⭐ ⭐ ⭐ ⭐ ⭐

<br><br>

(Critical levels of needing love, rest and ice cream.)

</div>
""", unsafe_allow_html=True)

st.markdown('<div id="prescription"></div>', unsafe_allow_html=True)

st.markdown("""
<div id="prescription"></div>

# 💊 Prescription Board
""", unsafe_allow_html=True)

p1,p2,p3,p4 = st.columns(4)

if "prescription_message" not in st.session_state:
    st.session_state.prescription_message = ""

with p1:
    if st.button("🍦 Ice Cream"):
        st.session_state.prescription_message = """
🍦 Ice Cream Prescription

Take immediately.
Doctor's orders.
No excuses.
"""

with p2:
    if st.button("🫂 Hugs"):
        st.session_state.prescription_message = """
🫂 Hug Prescription

Unlimited refills.
No appointment required.
"""

with p3:
    if st.button("😴 Sleep"):
        st.session_state.prescription_message = """
😴 Sleep Prescription

Minimum 8 hours.
This treatment is mandatory.
"""

with p4:
    if st.button("💬 Venting"):
        st.session_state.prescription_message = """
💬 Venting Session Prescription

Available 24/7.
Your designated emotional support human is standing by.
"""

if st.session_state.prescription_message:

    st.markdown(
        f"""
        <div class="prescription-response">

        {st.session_state.prescription_message.replace(chr(10), "<br><br>")}
        "<br>"

        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)


st.markdown("""
<div class="section-card">

<h2>💌 Important Note</h2>

Dear Patient,

<br><br>

You don't have to have everything figured out.

You don't have to be strong every second.

You're trying.

You're growing.

And you're doing so much better than you think.

Until things get easier, I'll be here.


No pressure.

<br>

No fixing.

<br>

Just here.

🫶

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="section-card">

<h2>👨‍⚕️ Prescribed By</h2>

<b>Dr. Phallu</b>

<br><br>

Bachelor of Being Perfect

<br>

Master of Caring Too Much

<br><br>

License No:

BESTIE-FOREVER-001

<br><br>

✓ Lifetime Validity

</div>
""", unsafe_allow_html=True)

st.markdown("""
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<div class="section-card">

<h2>🌸 Official Medical Observation</h2>

The patient is trying very hard.

Possibly too hard.

Recommended treatment:

More kindness towards himself.

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div id="mood-scan"></div>

## 🌸 Today's Mood Scan
""",
unsafe_allow_html=True)

mood = st.slider(
    "How are we feeling today?",
    0,
    10,
    5
)

if mood <= 3:

    st.markdown("""
                
    <div class="love-box">
    🫂 Doctor's Advice:

    Immediate hugs required.
    </div>
    """, unsafe_allow_html=True)

elif mood <= 6:

    st.markdown("""
    <div class="love-box">
    🌸 Mild stress detected.

    Additional self-care recommended.
    </div>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
    <div class="love-box">
    🤍 Patient condition stable.

    Continue being amazing.
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div id="emergency-kit"></div>
""",unsafe_allow_html=True)

st.markdown("""
<div id="emergency-kit"></div>

<h2 style="
text-align:center;
font-size:38px;
color:#FFF8F2;
margin-bottom:10px;
">
🚨 Emergency Support Dashboard
</h2>

<p style="
text-align:center;
font-size:18px;
color:#6f564f;
margin-bottom:30px;
">
Select the treatment currently required by the patient.
</p>
""", unsafe_allow_html=True)

# -------------------------
# ROW 1
# -------------------------

col1,col2,col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="emergency-card">
    🩹<br>
    <b>Stress Relief</b><br>
    Immediate Comfort Protocol
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Treatment", key="stress"):

        st.markdown("""
        <div class="response-card">
        🫂 Prescription Issued

        <br><br>

        One hug has been approved.

        Additional hugs may be requested
        at any time.

        </div>
        """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="emergency-card">
    😭<br>
    <b>Critical Motivation Drop</b><br>
    Recovery Assistance
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Treatment", key="giveup"):

        st.markdown("""
        <div class="response-card">

        🌷 Reminder

        <br><br>

        One difficult day does not define you.

        You have survived every hard day so far.

        You're stronger than this moment.

        </div>
        """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="emergency-card">
    💌<br>
    <b>Best Friend Missing</b><br>
    Emotional Emergency
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Treatment", key="bestie"):

        st.markdown("""
        <div class="response-card">

        Congratulations.

        <br><br>

        You have unlocked:

        <br><br>

        One human

        who believes in you endlessly.

        <br><br>

        Unlimited validity.

        </div>
        """, unsafe_allow_html=True)

# -------------------------
# ROW 2
# -------------------------

col4,col5 = st.columns(2)

with col4:

    st.markdown("""
    <div class="emergency-card">
    🥺<br>
    <b>Need Reassurance</b><br>
    Confidence Restoration
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Treatment", key="reassure"):

        st.markdown("""
        <div class="response-card">

        🤍 Medical Opinion

        <br><br>

        You are doing far better than
        you think you are.

        Progress is still progress.

        </div>
        """, unsafe_allow_html=True)

with col5:

    st.markdown("""
    <div class="emergency-card">
    🍦<br>
    <b>Ice Cream Emergency</b><br>
    Urgent Intervention
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Treatment", key="icecream"):

        st.markdown("""
        <div class="response-card">

        🍦 Treatment Approved

        <br><br>

        Ice cream has been prescribed.

        Effective immediately.

        No second opinion required.

        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
   

import random

compliments = [
    "You make people's days better than you realize.",
    "You are stronger than your bad days.",
    "Someone is proud of you right now.",
    "You deserve rest without guilt.",
    "You are doing enough."
]

if st.button("✨ Generate Random Compliment"):
    st.markdown(
    f"""
    <div class="love-box">
    ✨ {random.choice(compliments)}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div id="memory-vault"></div>

<h2 style="
text-align:center;
font-size:42px;
color:#FFF8F2;
margin-bottom:10px;
">
📸 Memory Vault
</h2>

<p style="
text-align:center;
font-size:18px;
color:#6f564f;
margin-bottom:30px;
">
Just so that you forget your beloved Avinash for a whole minute
</p>
""", unsafe_allow_html=True)

# -------------------------
# MEMORY SELECTOR
# -------------------------

left,right = st.columns([1,1.5])

with left:

    memory = st.radio(
        "Select Archive File",
        [
            "🌸 Chuntu Adi Era",
            "🧥 The Jacket Incident",
            "🏍️ I Can Ride Forever",
            "👑 King's Legendary Rant",
            "🎵 Dilliwali Girlfriend",
            "🐷 Pinky"
        ]
    )

photo_map = {

    "🌸 Chuntu Adi Era":"assets/photo1.jpg",

    "🧥 The Jacket Incident":"assets/photo2.jpg",

    "🏍️ I Can Ride Forever":"assets/photo3.jpg",

    "👑 King's Legendary Rant":"assets/photo4.jpg",

    "🎵 Dilliwali Girlfriend":"assets/photo5.jpg",

    "🐷 Pinky":"assets/photo6.jpg"
}

caption_map = {

    "🌸 Chuntu Adi Era":"1"
    ,

    "🧥 The Jacket Incident":"2"
    ,

    "🏍️ I Can Ride Forever":"3"
    ,

    "👑 King's Legendary Rant":"4"
    ,

    "🎵 Dilliwali Girlfriend":"5"
    ,

    "🐷 Pinky":"6"
    
}

with right:

    colA,colB,colC = st.columns([1,2,1])

    with colB:

        st.image(
            photo_map[memory],
            width=800
        )

        st.markdown(
            f"""
            <div class="memory-caption">
            {caption_map[memory]}
            </div>
            """,
            unsafe_allow_html=True
        )


st.markdown("""
<div id="our-soundtrack"></div>

<h2 style="
text-align:center;
font-size:42px;
color:#FFF8F2;
font-weight:900;
margin-bottom:10px;
">
🎧 A FEW MOMENTS BEFORE THE GUNSHOT
</h2>

<p style="
text-align:center;
font-size:20px;
color:white;
line-height:1.3;
">

This one just happens to be ours.
</p>
""", unsafe_allow_html=True)

st.image(
    "assets/spotify_qr.png",
    width=300
)

st.markdown("""
<br><br>
### 🌙 Night-Time Recovery Protocol

Tonight's instructions:

✔ Eat the ice cream

✔ Stop solving everyone's problems

✔ Drink some water and not diet coke

✔ Get some sleep

✔ Be a little kinder to yourself
            
<br><br>

Doctor's orders. 🤍
""", unsafe_allow_html=True)

st.markdown(
    """
<div style="
text-align:center;
font-size:11px;
color:#777;
">

Side effects of this prescription may include smiling involuntarily,
feeling cared for,
and accidentally realizing how loved you are. 🤍

</div>
""",
    unsafe_allow_html=True
)
st.markdown('<div id="confidential-letter"></div>', unsafe_allow_html=True)
if st.button("🔐 Open Confidential Letter"):

    st.markdown("""
    <div class="clinic-card">

    <h2 style="text-align:center;">
    💌 Confidential Letter
    </h2>

    Dear Adiii,

    

    I know you've been carrying a lot lately.

    More than most people realize.

    You keep showing up.

    You keep trying.

    You keep moving forward.

    
    And that's something worth being proud of.

    
    Please remember:

    You don't always have to be strong. You don't always have to have answers. Sometimes resting is productive too. 
    And no matter what happens, there's at least one person who cares about you very, very much.

    <br><br>

    🤍

    </div>
    """,
    unsafe_allow_html=True)
