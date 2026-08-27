import streamlit as st
import random
from difflib import SequenceMatcher

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Guess The Cricketer",
    page_icon="🏏",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Poppins:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(circle at 50% 0%, #173d70 0%, #07152b 38%, #020814 100%);
    color: white;
}

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Hide Streamlit default elements */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main container */
.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Game title */
.game-title {
    text-align: center;
    margin-bottom: 8px;
}

.game-title .small-title {
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 5px;
    color: #ffffff;
}

.game-title .big-title {
    font-family: 'Anton', sans-serif;
    font-size: clamp(52px, 9vw, 92px);
    line-height: 0.95;
    letter-spacing: 2px;
    color: #8cff2e;
    text-shadow:
        0 4px 0 #176400,
        0 8px 20px rgba(0,0,0,0.7);
}

.game-subtitle {
    display: inline-block;
    margin-top: 12px;
    padding: 8px 24px;
    border-radius: 30px;
    background: linear-gradient(90deg, #ffb300, #ffd54f);
    color: #171717;
    font-weight: 800;
}

/* Stadium decoration */
.stadium {
    height: 90px;
    margin: 20px -10px 25px -10px;
    border-radius: 50% 50% 0 0;
    background:
        radial-gradient(circle at 20% 70%, #ffffff 0 3px, transparent 5px),
        radial-gradient(circle at 80% 70%, #ffffff 0 3px, transparent 5px),
        linear-gradient(
            to bottom,
            #0d2343 0%,
            #08172c 60%,
            #0d4d20 100%
        );
    border-bottom: 3px solid #3f9b35;
}

/* Stats */
.stat-card {
    background: linear-gradient(145deg, #102d50, #07182d);
    border: 1px solid #2d6ba9;
    border-radius: 18px;
    padding: 16px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.35);
}

.stat-label {
    color: #a9c4e4;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
}

.stat-value {
    font-size: 34px;
    font-weight: 800;
    margin-top: 2px;
}

.stat-icon {
    font-size: 25px;
}

/* Section title */
.section-title {
    background: linear-gradient(90deg, #1476d4, #08437e);
    border: 2px solid #35a7ff;
    border-radius: 20px 20px 5px 5px;
    padding: 13px 20px;
    text-align: center;
    font-size: 25px;
    font-weight: 800;
    margin-top: 25px;
}

/* Mystery player */
.mystery-card {
    min-height: 135px;
    background:
        radial-gradient(circle at 50% 30%, rgba(37,104,171,0.35), transparent 45%),
        linear-gradient(145deg, #071a35, #041020);
    border: 1px solid #24558a;
    border-radius: 5px 5px 18px 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    margin-bottom: 12px;
}

.mystery-icon {
    font-size: 65px;
}

.mystery-text {
    color: #8da8c7;
    font-weight: 600;
}

/* Clue cards */
.clue-card {
    background: linear-gradient(145deg, #10284a, #07172d);
    border: 1px solid #284d77;
    border-radius: 14px;
    padding: 15px 18px;
    margin: 10px 0;
    font-size: 17px;
    font-weight: 600;
}

.clue-active {
    border: 2px solid #ffd400;
    box-shadow: 0 0 18px rgba(255,212,0,0.18);
}

.clue-locked {
    color: #607997;
}

/* Clue counter */
.clue-counter {
    text-align: center;
    color: #ffd400;
    font-size: 20px;
    font-weight: 800;
    margin: 18px 0;
}

/* Rules */
.rules-card {
    background: linear-gradient(145deg, #28185a, #130c30);
    border: 1px solid #8b5cff;
    border-radius: 18px;
    padding: 20px;
    margin-top: 25px;
}

.rules-title {
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 15px;
}

.rule {
    margin: 12px 0;
    color: #e6dcff;
}

/* Result */
.result-card {
    background: linear-gradient(145deg, #063c35, #031f1c);
    border: 2px solid #18d5a0;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    margin: 20px 0;
}

.result-title {
    font-size: 28px;
    font-weight: 800;
}

.result-score {
    color: #8cff2e;
    font-size: 38px;
    font-weight: 800;
}

/* Final screen */
.final-card {
    background:
        radial-gradient(circle at 50% 20%, rgba(255,196,0,0.18), transparent 40%),
        linear-gradient(145deg, #10294a, #050e1c);
    border: 2px solid #ffd400;
    border-radius: 25px;
    padding: 35px 25px;
    text-align: center;
    margin-top: 30px;
}

.final-trophy {
    font-size: 70px;
}

.final-title {
    font-family: 'Anton', sans-serif;
    font-size: 48px;
    color: #ffd400;
}

/* Streamlit buttons */
.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 14px;
    border: 1px solid #4e8ac4;
    background: linear-gradient(145deg, #173c68, #0b203c);
    color: white;
    font-size: 16px;
    font-weight: 800;
    transition: 0.2s;
}

.stButton > button:hover {
    border-color: #8cff2e;
    color: #8cff2e;
    transform: translateY(-2px);
}

div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(90deg, #55d914, #a2ff38) !important;
    color: #082000 !important;
    border: none !important;
    font-size: 17px !important;
}

/* Text input */
.stTextInput input {
    background: #07182c !important;
    color: white !important;
    border: 1px solid #3570a7 !important;
    border-radius: 12px !important;
    min-height: 48px !important;
    font-size: 16px !important;
}

.stTextInput input:focus {
    border-color: #8cff2e !important;
    box-shadow: 0 0 10px rgba(140,255,46,0.2) !important;
}

/* Progress */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #3b9cff, #8cff2e);
}

/* Mobile */
@media (max-width: 700px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .game-title .small-title {
        font-size: 15px;
        letter-spacing: 3px;
    }

    .game-title .big-title {
        font-size: 55px;
    }

    .stat-value {
        font-size: 27px;
    }

    .clue-card {
        font-size: 15px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# PLAYER DATABASE
# =========================================================

players = [

    {
        "name": "MS Dhoni",
        "aliases": ["dhoni", "msd", "ms dhoni"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🧤 I am famous for my wicketkeeping.",
            "🏆 I captained India to the 2007 T20 World Cup.",
            "🦁 I am strongly associated with Chennai Super Kings."
        ]
    },

    {
        "name": "Virat Kohli",
        "aliases": ["kohli", "virat", "virat kohli"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🏏 I am a right-handed batter.",
            "👑 I am popularly called the King of Indian cricket.",
            "🔥 I am famous for scoring hundreds."
        ]
    },

    {
        "name": "Rohit Sharma",
        "aliases": ["rohit", "rohit sharma", "hitman"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🏏 I am a right-handed opening batter.",
            "💯 I have scored multiple ODI double centuries.",
            "🎯 Fans often call me the Hitman."
        ]
    },

    {
        "name": "Suresh Raina",
        "aliases": ["raina", "suresh raina", "mr ipl"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🏏 I was known mainly for white-ball cricket.",
            "💛 I am strongly associated with Chennai Super Kings.",
            "👑 I am popularly called Mr. IPL."
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
            "🇮🇳 I am an Indian cricketer.",
            "⚡ I am a fast bowler.",
            "🎯 My unusual bowling action makes me easy to recognize.",
            "🔥 I am famous for my yorkers."
        ]
    },

    {
        "name": "Ravindra Jadeja",
        "aliases": ["jadeja", "jaddu", "ravindra jadeja"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🏏 I am a left-handed batter.",
            "🎯 I am a left-arm spinner.",
            "💛 I have a strong association with Chennai Super Kings."
        ]
    },

    {
        "name": "Hardik Pandya",
        "aliases": ["hardik", "pandya", "hardik pandya"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🏏 I am an all-rounder.",
            "⚡ I bowl right-arm fast-medium.",
            "💙 I have played for Mumbai Indians."
        ]
    },

    {
        "name": "KL Rahul",
        "aliases": ["rahul", "kl rahul", "k l rahul"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🏏 I am a right-handed batter.",
            "🧤 I can also keep wickets.",
            "🔥 I have played across all three formats."
        ]
    },

    {
        "name": "Yuvraj Singh",
        "aliases": ["yuvi", "yuvraj", "yuvraj singh"],
        "clues": [
            "🇮🇳 I am an Indian cricket legend.",
            "🏏 I was a left-handed batter and all-rounder.",
            "🔥 I once hit six sixes in an over.",
            "🏆 I was Player of the Tournament at the 2011 World Cup."
        ]
    },

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
            "🧠 I am known for an unusual batting technique.",
            "🔥 I have been highly successful in Test cricket."
        ]
    },

    {
        "name": "David Warner",
        "aliases": ["warner", "david warner"],
        "clues": [
            "🇦🇺 I represented Australia.",
            "🏏 I am a left-handed opening batter.",
            "💥 I am known for aggressive batting.",
            "🔥 I have played for Sunrisers Hyderabad."
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
            "🏆 I have won major ICC trophies with Australia."
        ]
    },

    {
        "name": "Ben Stokes",
        "aliases": ["stokes", "ben stokes"],
        "clues": [
            "🏴 I represent England.",
            "🏏 I am an all-rounder.",
            "🔥 I am known for performing under pressure.",
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
            "🎯 I occasionally bowl off-spin.",
            "🔥 I am one of England's leading Test run-scorers."
        ]
    },

    {
        "name": "AB de Villiers",
        "aliases": [
            "ab",
            "abd",
            "ab de villiers",
            "abd de villiers",
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
            "💪 I was known for both batting and bowling.",
            "🏆 I am regarded as one of cricket's greatest all-rounders."
        ]
    },

    {
        "name": "Quinton de Kock",
        "aliases": ["de kock", "quinton", "quinton de kock"],
        "clues": [
            "🇿🇦 I represented South Africa.",
            "🧤 I am a wicketkeeper-batter.",
            "🏏 I am a left-handed batter.",
            "💥 I am known for aggressive opening batting."
        ]
    },

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
            "🎯 I am known for dangerous swing bowling.",
            "🔥 I have been a key Pakistan pace bowler."
        ]
    },

    {
        "name": "Kumar Sangakkara",
        "aliases": ["sanga", "sangakkara", "kumar sangakkara"],
        "clues": [
            "🇱🇰 I represented Sri Lanka.",
            "🧤 I was a wicketkeeper-batter.",
            "🏏 I was a left-handed batter.",
            "🔥 I was one of Sri Lanka's greatest batters."
        ]
    },

    {
        "name": "Lasith Malinga",
        "aliases": ["malinga", "lasith malinga"],
        "clues": [
            "🇱🇰 I represented Sri Lanka.",
            "⚡ I was a fast bowler.",
            "🎯 I was famous for my yorkers.",
            "🌀 My unusual sling-arm action was instantly recognizable."
        ]
    },

    {
        "name": "Chris Gayle",
        "aliases": ["gayle", "chris gayle", "universe boss"],
        "clues": [
            "🌴 I represented the West Indies.",
            "🏏 I am a powerful left-handed batter.",
            "💥 I am famous for huge sixes.",
            "🔥 Fans know me as the Universe Boss."
        ]
    },

    {
        "name": "Brian Lara",
        "aliases": ["lara", "brian lara"],
        "clues": [
            "🌴 I represented the West Indies.",
            "🏏 I was a left-handed batter.",
            "💯 I am famous for enormous Test innings.",
            "👑 I am considered one of cricket's greatest batters."
        ]
    },

    {
        "name": "Kane Williamson",
        "aliases": ["kane", "williamson", "kane williamson"],
        "clues": [
            "🇳🇿 I represent New Zealand.",
            "🏏 I am a right-handed batter.",
            "🧠 I am known for calm and technically strong batting.",
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

    {
        "name": "Rashid Khan",
        "aliases": ["rashid", "rashid khan"],
        "clues": [
            "🇦🇫 I represent Afghanistan.",
            "🎯 I am a leg-spinner.",
            "⚡ I am known for bowling quickly through the air.",
            "🔥 I have been a major T20 cricket star."
        ]
    }
]


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "started": False,
    "player": None,
    "clue_number": 0,
    "score": 0,
    "round": 1,
    "message": "",
    "game_over": False,
    "round_finished": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# FUNCTIONS
# =========================================================

def start_game():
    st.session_state.started = True
    st.session_state.round = 1
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.round_finished = False
    st.session_state.message = ""
    new_player()


def new_player():
    st.session_state.player = random.choice(players)
    st.session_state.clue_number = 0
    st.session_state.message = ""
    st.session_state.round_finished = False


def next_round():

    if st.session_state.round >= 5:
        st.session_state.game_over = True
        return

    st.session_state.round += 1
    new_player()


def normalize_text(text):

    return "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )


def is_correct_answer(answer, player):

    answer = normalize_text(answer)

    if not answer:
        return False

    possible_answers = [player["name"]] + player["aliases"]

    for possible in possible_answers:

        possible = normalize_text(possible)

        if answer == possible:
            return True

        similarity = SequenceMatcher(
            None,
            answer,
            possible
        ).ratio()

        if similarity >= 0.78:
            return True

    return False


def check_answer(answer):

    player = st.session_state.player

    if is_correct_answer(answer, player):

        points = max(
            10 - (st.session_state.clue_number * 2),
            2
        )

        st.session_state.score += points

        st.session_state.message = (
            f"🎉 CORRECT!<br>"
            f"<strong>{player['name']}</strong><br>"
            f"⭐ +{points} POINTS"
        )

        st.session_state.round_finished = True

    else:

        if st.session_state.clue_number < 3:

            st.session_state.clue_number += 1

            st.session_state.message = (
                "❌ NOT QUITE!<br>"
                "💡 Here's another clue..."
            )

        else:

            st.session_state.message = (
                f"❌ ROUND OVER<br>"
                f"The answer was <strong>{player['name']}</strong>."
            )

            st.session_state.round_finished = True


# =========================================================
# START SCREEN
# =========================================================

if not st.session_state.started:

    st.markdown("""
    <div class="game-title">
        <div class="small-title">🏏 WELCOME TO</div>
        <div class="big-title">GUESS THE<br>CRICKETER</div>
        <div class="game-subtitle">
            Think you know cricket? Prove it! 🔥
        </div>
    </div>

    <div class="stadium"></div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="rules-card">

        <div class="rules-title">
            🎮 HOW TO PLAY
        </div>

        <div class="rule">🕵️ A cricketer is picked randomly.</div>
        <div class="rule">💡 Clues are revealed one by one.</div>
        <div class="rule">⭐ Guess early to earn more points.</div>
        <div class="rule">🏆 Complete 5 rounds.</div>
        <div class="rule">🔥 Small spelling mistakes are allowed.</div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.button(
        "🔥 START THE GAME",
        on_click=start_game,
        use_container_width=True
    )


# =========================================================
# FINAL SCORE
# =========================================================

elif st.session_state.game_over:

    st.balloons()

    st.markdown("""
    <div class="final-card">

        <div class="final-trophy">🏆</div>

        <div class="final-title">
            GAME COMPLETE!
        </div>

        <p>
            You survived all 5 rounds.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-icon">⭐</div>
            <div class="stat-label">FINAL SCORE</div>
            <div class="stat-value">{st.session_state.score} / 50</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.session_state.score >= 45:
        st.success("👑 CRICKET GOD! Absolutely insane!")

    elif st.session_state.score >= 35:
        st.success("🔥 CRICKET MASTER! Outstanding!")

    elif st.session_state.score >= 25:
        st.info("👏 Great job! You really know your cricket!")

    elif st.session_state.score >= 15:
        st.warning("😄 Not bad! Keep watching cricket!")

    else:
        st.error("😂 Looks like you need more cricket!")

    st.write("")

    st.button(
        "🔄 PLAY AGAIN",
        on_click=start_game,
        use_container_width=True
    )


# =========================================================
# GAME SCREEN
# =========================================================

else:

    # Header
    st.markdown("""
    <div class="game-title">
        <div class="small-title">🏏 GUESS THE</div>
        <div class="big-title">CRICKETER</div>
    </div>
    """, unsafe_allow_html=True)

    # Progress
    st.progress(
        st.session_state.round / 5,
        text=f"ROUND {st.session_state.round} / 5"
    )

    # Stats
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-icon">🏏</div>
                <div class="stat-label">ROUND</div>
                <div class="stat-value">
                    {st.session_state.round}/5
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-icon">⭐</div>
                <div class="stat-label">SCORE</div>
                <div class="stat-value">
                    {st.session_state.score}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        points = max(
            10 - (st.session_state.clue_number * 2),
            2
        )

        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-icon">🏆</div>
                <div class="stat-label">POINTS</div>
                <div class="stat-value">
                    {points}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Who am I?
    st.markdown(
        """
        <div class="section-title">
            🔍 WHO AM I?
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="mystery-card">
            <div>
                <div class="mystery-icon">🏏❓</div>
                <div class="mystery-text">
                    Identify the mystery cricketer!
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    player = st.session_state.player

    # Show clues
    for i, clue in enumerate(player["clues"]):

        if i <= st.session_state.clue_number:

            extra_class = "clue-active" if (
                i == st.session_state.clue_number
            ) else ""

            st.markdown(
                f"""
                <div class="clue-card {extra_class}">
                    💡 {clue}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
                <div class="clue-card clue-locked">
                    🔒 Mystery clue locked...
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        f"""
        <div class="clue-counter">
            💡 CLUE {st.session_state.clue_number + 1} / 4
        </div>
        """,
        unsafe_allow_html=True
    )

    # Answer section
    if not st.session_state.round_finished:

        with st.form("guess_form"):

            answer = st.text_input(
                "YOUR ANSWER",
                placeholder="Enter the cricketer's name..."
            )

            submitted = st.form_submit_button(
                "🔥 SUBMIT GUESS",
                use_container_width=True
            )

            if submitted:

                if answer.strip():

                    check_answer(answer)
                    st.rerun()

                else:

                    st.warning(
                        "⚠️ Enter a cricketer's name!"
                    )

        st.write("")

        if st.button(
            "💡 REVEAL NEXT CLUE",
            use_container_width=True
        ):

            if st.session_state.clue_number < 3:

                st.session_state.clue_number += 1
                st.session_state.message = ""

                st.rerun()

            else:

                st.warning(
                    "🚫 All clues are already revealed!"
                )

    # Result
    if st.session_state.message:

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">
                    {st.session_state.message}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Next round
    if st.session_state.round_finished:

        if st.session_state.round < 5:

            st.button(
                "➡️ NEXT ROUND",
                on_click=next_round,
                use_container_width=True
            )

        else:

            st.button(
                "🏆 SEE FINAL SCORE",
                on_click=next_round,
                use_container_width=True
            )

    # Rules
    st.markdown("""
    <div class="rules-card">

        <div class="rules-title">
            🧠 SCORING
        </div>

        <div class="rule">
            🟢 Clue 1 → <strong>10 points</strong>
        </div>

        <div class="rule">
            🟡 Clue 2 → <strong>8 points</strong>
        </div>

        <div class="rule">
            🟠 Clue 3 → <strong>6 points</strong>
        </div>

        <div class="rule">
            🔴 Clue 4 → <strong>4 points</strong>
        </div>

    </div>
    """, unsafe_allow_html=True)
