import streamlit as st
import random
from difflib import SequenceMatcher

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Guess The Cricketer",
    page_icon="🏏",
    layout="centered"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

/* =========================
   PAGE
   ========================= */

.stApp {
    background: #07182d;
}

.block-container {
    max-width: 680px;
    padding-top: 0.8rem;
    padding-bottom: 1rem;
}


/* =========================
   TITLE
   ========================= */

.title {
    text-align: center;
    margin-bottom: 10px;
}

.title h1 {
    color: #7cff21 !important;
    font-size: 34px !important;
    font-weight: 900 !important;
    margin: 0 !important;
}

.title p {
    color: #9db8d3 !important;
    font-size: 12px !important;
    margin: 2px 0 0 0 !important;
}


/* =========================
   STATS
   ========================= */

.stat-box {
    background: #102b49;
    border: 1px solid #2d587e;
    border-radius: 11px;
    padding: 7px 4px;
    text-align: center;
}

.stat-label {
    color: #9bb5cf !important;
    font-size: 10px !important;
    font-weight: 700 !important;
}

.stat-number {
    color: #ffffff !important;
    font-size: 21px !important;
    font-weight: 900 !important;
}


/* =========================
   GAME AREA
   ========================= */

.game-box {
    background: #0a2038;
    border: 1px solid #28577e;
    border-radius: 14px;
    padding: 14px;
    margin-top: 10px;
}


/* =========================
   WHO AM I
   ========================= */

.who-title {
    text-align: center;
    color: #ffffff !important;
    font-size: 21px !important;
    font-weight: 900 !important;
    margin-bottom: 4px;
}

.who-subtitle {
    text-align: center;
    color: #7895b2 !important;
    font-size: 12px !important;
    margin-bottom: 10px;
}


/* =========================
   MYSTERY PLAYER
   ========================= */

.mystery {
    text-align: center;
    background: #08182b;
    border-radius: 10px;
    padding: 7px;
    margin-bottom: 10px;
}

.mystery-icon {
    font-size: 34px;
}

.mystery-text {
    color: #718da9 !important;
    font-size: 11px !important;
}


/* =========================
   CLUE
   ========================= */

.clue-box {
    background: #153a5d;
    border-left: 4px solid #ffd400;
    border-radius: 8px;
    padding: 11px;
    color: #ffffff !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    margin: 8px 0;
}

.clue-number {
    text-align: center;
    color: #ffd400 !important;
    font-size: 12px !important;
    font-weight: 800 !important;
    margin: 7px 0;
}


/* =========================
   INPUT
   ========================= */

div[data-testid="stTextInput"] label {
    color: #ffffff !important;
    font-size: 13px !important;
    font-weight: 700 !important;
}

div[data-testid="stTextInput"] input {
    background: #061426 !important;
    color: #ffffff !important;

    border: 1px solid #3974a3 !important;
    border-radius: 9px !important;

    min-height: 40px !important;
    font-size: 14px !important;
}

div[data-testid="stTextInput"] input::placeholder {
    color: #7692ae !important;
    opacity: 1 !important;
}


/* =========================
   ALL BUTTONS
   ========================= */

div.stButton > button {
    width: 100% !important;
    min-height: 40px !important;

    background: #153b61 !important;
    color: #ffffff !important;

    border: 1px solid #477da5 !important;
    border-radius: 9px !important;

    font-size: 14px !important;
    font-weight: 800 !important;
}

div.stButton > button p {
    color: #ffffff !important;
}

div.stButton > button:hover {
    background: #1c4d79 !important;
    color: #ffffff !important;

    border-color: #72d9ff !important;
}


/* =========================
   GUESS BUTTON
   ========================= */

div[data-testid="stFormSubmitButton"] > button {
    width: 100% !important;
    min-height: 40px !important;

    background: #6ee51b !important;
    color: #071400 !important;

    border: none !important;
    border-radius: 9px !important;

    font-size: 14px !important;
    font-weight: 900 !important;
}

div[data-testid="stFormSubmitButton"] > button p {
    color: #071400 !important;
}


/* =========================
   RESULT
   ========================= */

.result-box {
    background: #073a32;
    border: 1px solid #16c99a;
    border-radius: 9px;
    padding: 9px;
    margin-top: 9px;
    text-align: center;
    color: #ffffff !important;
    font-size: 14px !important;
    font-weight: 700 !important;
}


/* =========================
   START INFO
   ========================= */

.info-box {
    background: #102f52;
    border: 1px solid #2f6696;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
    color: #d8e9f8 !important;
    font-size: 13px !important;
}


/* =========================
   FINAL
   ========================= */

.final-box {
    background: #102b49;
    border: 2px solid #ffd400;
    border-radius: 16px;
    padding: 22px;
    text-align: center;
}

.final-box h1 {
    color: #ffd400 !important;
    font-size: 32px !important;
    margin: 5px !important;
}

.final-score {
    color: #7cff21 !important;
    font-size: 36px !important;
    font-weight: 900 !important;
}


/* =========================
   MOBILE
   ========================= */

@media (max-width: 600px) {

    .block-container {
        padding: 0.5rem;
    }

    .title h1 {
        font-size: 28px !important;
    }

    .game-box {
        padding: 10px;
    }

    .clue-box {
        font-size: 13px !important;
    }

    .stat-number {
        font-size: 19px !important;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# PLAYER DATABASE
# ============================================================

players = [

    # INDIA
    {
        "name": "MS Dhoni",
        "aliases": ["dhoni", "msd", "ms dhoni"],
        "clues": [
            "🇮🇳 I represented India.",
            "🧤 I am famous for wicketkeeping.",
            "🏆 I captained India to a T20 World Cup victory.",
            "💛 I am strongly associated with Chennai Super Kings."
        ]
    },

    {
        "name": "Virat Kohli",
        "aliases": ["virat", "kohli", "virat kohli"],
        "clues": [
            "🇮🇳 I represented India.",
            "🏏 I am a right-handed batter.",
            "👑 Fans call me the King.",
            "🔥 I am famous for scoring international centuries."
        ]
    },

    {
        "name": "Rohit Sharma",
        "aliases": ["rohit", "rohit sharma", "hitman"],
        "clues": [
            "🇮🇳 I represented India.",
            "🏏 I am a right-handed opening batter.",
            "💯 I have scored multiple ODI double centuries.",
            "🎯 Fans call me the Hitman."
        ]
    },

    {
        "name": "Suresh Raina",
        "aliases": ["raina", "suresh raina", "mr ipl"],
        "clues": [
            "🇮🇳 I represented India.",
            "🏏 I was known for white-ball cricket.",
            "💛 I am strongly associated with Chennai Super Kings.",
            "👑 I am called Mr. IPL."
        ]
    },

    {
        "name": "Sachin Tendulkar",
        "aliases": ["sachin", "tendulkar", "sachin tendulkar"],
        "clues": [
            "🇮🇳 I am an Indian cricket legend.",
            "🏏 I was known for technically brilliant batting.",
            "💯 I scored 100 international centuries.",
            "🏆 I was part of India's 2011 World Cup-winning team."
        ]
    },

    {
        "name": "Jasprit Bumrah",
        "aliases": ["bumrah", "jasprit", "jasprit bumrah"],
        "clues": [
            "🇮🇳 I represented India.",
            "⚡ I am a fast bowler.",
            "🎯 I have an unusual bowling action.",
            "🔥 I am famous for my yorkers."
        ]
    },

    {
        "name": "Ravindra Jadeja",
        "aliases": ["jadeja", "jaddu", "ravindra jadeja"],
        "clues": [
            "🇮🇳 I represented India.",
            "🏏 I am a left-handed batter.",
            "🎯 I am a left-arm spinner.",
            "💛 I am strongly associated with Chennai Super Kings."
        ]
    },

    {
        "name": "Hardik Pandya",
        "aliases": ["hardik", "pandya", "hardik pandya"],
        "clues": [
            "🇮🇳 I represented India.",
            "🏏 I am an all-rounder.",
            "⚡ I bowl fast-medium pace.",
            "💙 I have played for Mumbai Indians."
        ]
    },

    {
        "name": "KL Rahul",
        "aliases": ["rahul", "kl rahul", "k l rahul"],
        "clues": [
            "🇮🇳 I represented India.",
            "🏏 I am a right-handed batter.",
            "🧤 I can also keep wickets.",
            "🔥 I have played across formats."
        ]
    },

    {
        "name": "Yuvraj Singh",
        "aliases": ["yuvi", "yuvraj", "yuvraj singh"],
        "clues": [
            "🇮🇳 I am an Indian cricket legend.",
            "🏏 I was a left-handed all-rounder.",
            "🔥 I hit six sixes in an over.",
            "🏆 I was Player of the Tournament in the 2011 World Cup."
        ]
    },

    # AUSTRALIA
    {
        "name": "Ricky Ponting",
        "aliases": ["ponting", "ricky", "ricky ponting"],
        "clues": [
            "🇦🇺 I represented Australia.",
            "🏏 I was a right-handed batter.",
            "🧢 I captained Australia.",
            "🏆 I won multiple World Cups as captain."
        ]
    },

    {
        "name": "Steve Smith",
        "aliases": ["smith", "steve smith"],
        "clues": [
            "🇦🇺 I represent Australia.",
            "🏏 I am a right-handed batter.",
            "🧠 I have an unusual batting technique.",
            "🔥 I am highly successful in Test cricket."
        ]
    },

    {
        "name": "David Warner",
        "aliases": ["warner", "david warner"],
        "clues": [
            "🇦🇺 I represented Australia.",
            "🏏 I am a left-handed opener.",
            "💥 I am known for aggressive batting.",
            "🧡 I have played for Sunrisers Hyderabad."
        ]
    },

    {
        "name": "Glenn Maxwell",
        "aliases": ["maxwell", "glenn maxwell", "maxi"],
        "clues": [
            "🇦🇺 I represent Australia.",
            "🏏 I am an explosive all-rounder.",
            "💥 I am famous for innovative shots.",
            "❤️ I have played for Royal Challengers Bengaluru."
        ]
    },

    {
        "name": "Pat Cummins",
        "aliases": ["cummins", "pat cummins"],
        "clues": [
            "🇦🇺 I represent Australia.",
            "⚡ I am a fast bowler.",
            "🧢 I have captained Australia.",
            "🏆 I have won major ICC trophies."
        ]
    },

    # ENGLAND
    {
        "name": "Ben Stokes",
        "aliases": ["stokes", "ben stokes"],
        "clues": [
            "🏴 I represent England.",
            "🏏 I am an all-rounder.",
            "🔥 I am known for pressure performances.",
            "🏆 I was part of England's 2019 World Cup-winning team."
        ]
    },

    {
        "name": "Jos Buttler",
        "aliases": ["buttler", "jos buttler"],
        "clues": [
            "🏴 I represent England.",
            "🧤 I am a wicketkeeper-batter.",
            "💥 I am known for aggressive batting.",
            "🏆 I was part of England's 2019 World Cup-winning team."
        ]
    },

    {
        "name": "Joe Root",
        "aliases": ["root", "joe root"],
        "clues": [
            "🏴 I represent England.",
            "🏏 I am a right-handed batter.",
            "🎯 I can bowl off-spin.",
            "🔥 I am one of England's leading Test run-scorers."
        ]
    },

    # SOUTH AFRICA
    {
        "name": "AB de Villiers",
        "aliases": [
            "ab",
            "abd",
            "ab de villiers",
            "ab devilliers",
            "ab de villers",
            "devilliers"
        ],
        "clues": [
            "🇿🇦 I represented South Africa.",
            "🏏 I was famous for innovative batting.",
            "⚡ I could score extremely quickly.",
            "🔥 Fans called me Mr. 360."
        ]
    },

    {
        "name": "Jacques Kallis",
        "aliases": ["kallis", "jacques kallis"],
        "clues": [
            "🇿🇦 I represented South Africa.",
            "🏏 I was an all-rounder.",
            "💪 I was excellent with bat and ball.",
            "🏆 I am regarded as one of cricket's greatest all-rounders."
        ]
    },

    {
        "name": "Quinton de Kock",
        "aliases": ["de kock", "quinton", "quinton de kock"],
        "clues": [
            "🇿🇦 I represented South Africa.",
            "🧤 I am a wicketkeeper-batter.",
            "🏏 I am left-handed.",
            "💥 I am known for aggressive opening batting."
        ]
    },

    # PAKISTAN
    {
        "name": "Babar Azam",
        "aliases": ["babar", "babar azam"],
        "clues": [
            "🇵🇰 I represent Pakistan.",
            "🏏 I am a right-handed batter.",
            "⭐ I have been ranked among the world's top batters.",
            "🧢 I have captained Pakistan."
        ]
    },

    {
        "name": "Shaheen Afridi",
        "aliases": ["shaheen", "shaheen afridi"],
        "clues": [
            "🇵🇰 I represent Pakistan.",
            "⚡ I am a left-arm fast bowler.",
            "🎯 I am known for swing bowling.",
            "🔥 I am one of Pakistan's key pace bowlers."
        ]
    },

    # SRI LANKA
    {
        "name": "Kumar Sangakkara",
        "aliases": ["sanga", "sangakkara", "kumar sangakkara"],
        "clues": [
            "🇱🇰 I represented Sri Lanka.",
            "🧤 I was a wicketkeeper-batter.",
            "🏏 I was left-handed.",
            "🔥 I was one of Sri Lanka's greatest batters."
        ]
    },

    {
        "name": "Lasith Malinga",
        "aliases": ["malinga", "lasith malinga"],
        "clues": [
            "🇱🇰 I represented Sri Lanka.",
            "⚡ I was a fast bowler.",
            "🎯 I was famous for yorkers.",
            "🌀 My sling-arm action was instantly recognizable."
        ]
    },

    # WEST INDIES
    {
        "name": "Chris Gayle",
        "aliases": ["gayle", "chris gayle", "universe boss"],
        "clues": [
            "🌴 I represented the West Indies.",
            "🏏 I am a powerful left-handed batter.",
            "💥 I am famous for huge sixes.",
            "🔥 I am known as the Universe Boss."
        ]
    },

    {
        "name": "Brian Lara",
        "aliases": ["lara", "brian lara"],
        "clues": [
            "🌴 I represented the West Indies.",
            "🏏 I was a left-handed batter.",
            "💯 I am famous for huge Test innings.",
            "👑 I am considered one of cricket's greatest batters."
        ]
    },

    # NEW ZEALAND
    {
        "name": "Kane Williamson",
        "aliases": ["kane", "williamson", "kane williamson"],
        "clues": [
            "🇳🇿 I represent New Zealand.",
            "🏏 I am a right-handed batter.",
            "🧠 I am known for calm batting.",
            "🧢 I have captained New Zealand."
        ]
    },

    {
        "name": "Brendon McCullum",
        "aliases": ["baz", "mccullum", "brendon mccullum"],
        "clues": [
            "🇳🇿 I represented New Zealand.",
            "🏏 I was an aggressive batter.",
            "🧤 I also kept wickets.",
            "💥 I was known for attacking cricket."
        ]
    },

    # AFGHANISTAN
    {
        "name": "Rashid Khan",
        "aliases": ["rashid", "rashid khan"],
        "clues": [
            "🇦🇫 I represent Afghanistan.",
            "🎯 I am a leg-spinner.",
            "⚡ I bowl quickly through the air.",
            "🔥 I am a major T20 cricket star."
        ]
    }
]


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "started": False,
    "player": None,
    "clue": 0,
    "score": 0,
    "round": 1,
    "finished": False,
    "game_over": False,
    "message": ""
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# FUNCTIONS
# ============================================================

def choose_player():

    st.session_state.player = random.choice(players)

    st.session_state.clue = 0
    st.session_state.finished = False
    st.session_state.message = ""


def start_game():

    st.session_state.started = True
    st.session_state.score = 0
    st.session_state.round = 1
    st.session_state.game_over = False

    choose_player()


def normalize(text):

    return "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )


def is_correct(answer, player):

    answer = normalize(answer)

    if not answer:
        return False

    possible_answers = [
        player["name"]
    ] + player["aliases"]

    for option in possible_answers:

        option = normalize(option)

        # Exact match
        if answer == option:
            return True

        # Small spelling mistake
        similarity = SequenceMatcher(
            None,
            answer,
            option
        ).ratio()

        if similarity >= 0.78:
            return True

    return False


def submit_answer(answer):

    player = st.session_state.player

    if is_correct(answer, player):

        points = 10 - (
            st.session_state.clue * 2
        )

        if points < 4:
            points = 4

        st.session_state.score += points

        st.session_state.message = (
            f"🎉 Correct! {player['name']}  •  "
            f"⭐ +{points} points"
        )

        st.session_state.finished = True

    else:

        if st.session_state.clue < 3:

            st.session_state.clue += 1

            st.session_state.message = (
                "❌ Not quite! Here's another clue."
            )

        else:

            st.session_state.message = (
                f"❌ The answer was {player['name']}."
            )

            st.session_state.finished = True


def next_round():

    if st.session_state.round >= 5:

        st.session_state.game_over = True

    else:

        st.session_state.round += 1
        choose_player()


# ============================================================
# START SCREEN
# ============================================================

if not st.session_state.started:

    st.markdown(
        """
        <div class="title">
            <h1>🏏 GUESS THE CRICKETER</h1>
            <p>Think you know cricket? Prove it!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
            💡 Guess early to score more points!
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown("### 🎮 How to play")

    st.write("🕵️ A cricketer is selected randomly.")
    st.write("💡 You get 4 clues.")
    st.write("⭐ Fewer clues = more points.")
    st.write("🔥 Small spelling mistakes are allowed.")
    st.write("🏆 Complete 5 rounds.")

    st.write("")

    st.button(
        "🔥 START GAME",
        on_click=start_game,
        use_container_width=True
    )


# ============================================================
# FINAL SCREEN
# ============================================================

elif st.session_state.game_over:

    st.markdown(
        f"""
        <div class="final-box">

            <div style="font-size:50px;">
                🏆
            </div>

            <h1>
                GAME COMPLETE!
            </h1>

            <p>
                You completed all 5 rounds!
            </p>

            <div class="final-score">
                {st.session_state.score} / 50
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    score = st.session_state.score

    if score >= 45:

        st.success(
            "👑 CRICKET GOD! Absolutely insane!"
        )

    elif score >= 35:

        st.success(
            "🔥 CRICKET MASTER!"
        )

    elif score >= 25:

        st.info(
            "👏 Great job!"
        )

    elif score >= 15:

        st.warning(
            "😄 Not bad!"
        )

    else:

        st.error(
            "😂 Time to watch more cricket!"
        )

    st.write("")

    st.button(
        "🔄 PLAY AGAIN",
        on_click=start_game,
        use_container_width=True
    )


# ============================================================
# GAME SCREEN
# ============================================================

else:

    # TITLE
    st.markdown(
        """
        <div class="title">
            <h1>🏏 GUESS THE CRICKETER</h1>
            <p>Who am I?</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # STATS
    col1, col2, col3 = st.columns(3)

    points = 10 - (
        st.session_state.clue * 2
    )

    if points < 4:
        points = 4

    with col1:

        st.markdown(
            f"""
            <div class="stat-box">
                <div class="stat-label">
                    ROUND
                </div>

                <div class="stat-number">
                    {st.session_state.round}/5
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="stat-box">
                <div class="stat-label">
                    ⭐ SCORE
                </div>

                <div class="stat-number">
                    {st.session_state.score}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="stat-box">
                <div class="stat-label">
                    🏆 POINTS
                </div>

                <div class="stat-number">
                    {points}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # PROGRESS
    st.progress(
        st.session_state.round / 5
    )

    # GAME BOX
    st.markdown(
        '<div class="game-box">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="who-title">🔍 WHO AM I?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="who-subtitle">Identify the mystery cricketer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="mystery">

            <div class="mystery-icon">
                🏏❓
            </div>

            <div class="mystery-text">
                MYSTERY PLAYER
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    player = st.session_state.player

    # CURRENT CLUE
    current_clue = player["clues"][
        st.session_state.clue
    ]

    st.markdown(
        f"""
        <div class="clue-box">
            {current_clue}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="clue-number">
            💡 CLUE {st.session_state.clue + 1} / 4
        </div>
        """,
        unsafe_allow_html=True
    )

    # ANSWER AREA
    if not st.session_state.finished:

        with st.form("guess_form"):

            answer = st.text_input(
                "Your answer",
                placeholder="Enter cricketer name..."
            )

            guess = st.form_submit_button(
                "🔥 GUESS",
                use_container_width=True
            )

            if guess:

                if answer.strip():

                    submit_answer(answer)
                    st.rerun()

                else:

                    st.warning(
                        "Please enter a name."
                    )

        if st.button(
            "💡 NEXT CLUE",
            use_container_width=True
        ):

            if st.session_state.clue < 3:

                st.session_state.clue += 1
                st.session_state.message = ""

                st.rerun()

            else:

                st.warning(
                    "All clues are already revealed."
                )

    # RESULT
    if st.session_state.message:

        st.markdown(
            f"""
            <div class="result-box">
                {st.session_state.message}
            </div>
            """,
            unsafe_allow_html=True
        )

    # NEXT ROUND
    if st.session_state.finished:

        st.write("")

        if st.session_state.round < 5:

            st.button(
                "➡️ NEXT ROUND",
                on_click=next_round,
                use_container_width=True
            )

        else:

            st.button(
                "🏆 FINAL SCORE",
                on_click=next_round,
                use_container_width=True
            )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )
