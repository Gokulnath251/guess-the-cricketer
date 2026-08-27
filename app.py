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

st.html("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% 0%, #173f72 0%, #081b36 38%, #020914 100%);
    color: white;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* TITLE */

.game-title {
    text-align: center;
    margin-bottom: 20px;
}

.welcome-text {
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 4px;
    color: white;
}

.main-title {
    font-size: clamp(48px, 9vw, 82px);
    line-height: 0.95;
    font-weight: 900;
    letter-spacing: 2px;
    color: #8cff2e;
    text-shadow:
        0 3px 0 #176000,
        0 7px 15px rgba(0,0,0,0.7);
}

.tagline {
    display: inline-block;
    margin-top: 15px;
    padding: 9px 25px;
    border-radius: 30px;
    background: linear-gradient(90deg, #ffb300, #ffd740);
    color: #111;
    font-weight: 900;
    font-size: 14px;
}

/* STADIUM */

.stadium {
    height: 100px;
    margin: 25px 0;
    border-radius: 60% 60% 0 0;

    background:
        radial-gradient(circle at 15% 60%, white 0 4px, transparent 6px),
        radial-gradient(circle at 85% 60%, white 0 4px, transparent 6px),
        radial-gradient(circle at 30% 30%, white 0 3px, transparent 5px),
        radial-gradient(circle at 70% 30%, white 0 3px, transparent 5px),
        linear-gradient(to bottom, #102a50, #08182f 65%, #126125);

    border-bottom: 4px solid #42a82e;
}

/* RULES */

.rules-card {
    background: linear-gradient(145deg, #29175d, #120b2d);
    border: 1px solid #8b5cff;
    border-radius: 20px;
    padding: 24px;
    margin: 20px 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}

.rules-title {
    text-align: center;
    font-size: 24px;
    font-weight: 900;
    margin-bottom: 18px;
}

.rule {
    padding: 9px 0;
    color: #e9ddff;
    font-size: 15px;
    font-weight: 600;
}

/* STATS */

.stat-card {
    background: linear-gradient(145deg, #12345d, #07182d);
    border: 1px solid #3478b9;
    border-radius: 18px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}

.stat-icon {
    font-size: 24px;
}

.stat-label {
    color: #a9c6e7;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
}

.stat-value {
    color: white;
    font-size: 31px;
    font-weight: 900;
}

/* WHO AM I */

.section-title {
    background: linear-gradient(90deg, #147ad8, #083e76);
    border: 2px solid #37aaff;
    border-radius: 18px 18px 5px 5px;
    padding: 13px;
    text-align: center;
    font-size: 25px;
    font-weight: 900;
    margin-top: 28px;
}

.mystery-card {
    min-height: 145px;

    background:
        radial-gradient(
            circle at 50% 30%,
            rgba(38,110,180,0.35),
            transparent 45%
        ),
        linear-gradient(145deg, #071b38, #031020);

    border: 1px solid #285b91;
    border-radius: 5px 5px 18px 18px;

    display: flex;
    align-items: center;
    justify-content: center;

    text-align: center;
    margin-bottom: 15px;
}

.mystery-icon {
    font-size: 62px;
}

.mystery-text {
    color: #8fa9c7;
    font-weight: 600;
    font-size: 14px;
}

/* CLUES */

.clue-card {
    background: linear-gradient(145deg, #102b4d, #07182e);
    border: 1px solid #2d557d;
    border-radius: 14px;
    padding: 15px 18px;
    margin: 10px 0;
    color: white;
    font-size: 16px;
    font-weight: 600;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.clue-active {
    border: 2px solid #ffd400;
    box-shadow: 0 0 18px rgba(255,212,0,0.2);
}

.clue-locked {
    color: #637c99;
}

.clue-counter {
    text-align: center;
    color: #ffd400;
    font-size: 19px;
    font-weight: 900;
    margin: 18px 0;
}

/* RESULT */

.result-card {
    background: linear-gradient(145deg, #063f35, #031f1c);
    border: 2px solid #16d3a0;
    border-radius: 18px;
    padding: 20px;
    margin: 20px 0;
    text-align: center;
    color: white;
    font-size: 19px;
    font-weight: 700;
}

/* FINAL */

.final-card {
    background:
        radial-gradient(
            circle at 50% 15%,
            rgba(255,196,0,0.18),
            transparent 45%
        ),
        linear-gradient(145deg, #102b4d, #050e1c);

    border: 2px solid #ffd400;
    border-radius: 25px;
    padding: 35px 20px;
    margin: 30px 0;
    text-align: center;
}

.final-trophy {
    font-size: 70px;
}

.final-title {
    font-size: 44px;
    font-weight: 900;
    color: #ffd400;
}

/* MOBILE */

@media (max-width: 700px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .main-title {
        font-size: 52px;
    }

    .welcome-text {
        font-size: 14px;
    }

    .stat-value {
        font-size: 26px;
    }

    .clue-card {
        font-size: 14px;
    }

    .final-title {
        font-size: 36px;
    }
}

</style>
""")

# =========================================================
# PLAYER DATABASE
# =========================================================

players = [

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
        "aliases": ["kohli", "virat", "virat kohli"],
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

# =========================================================
# SESSION STATE
# =========================================================

if "started" not in st.session_state:
    st.session_state.started = False

if "player" not in st.session_state:
    st.session_state.player = None

if "clue_number" not in st.session_state:
    st.session_state.clue_number = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "round" not in st.session_state:
    st.session_state.round = 1

if "message" not in st.session_state:
    st.session_state.message = ""

if "round_finished" not in st.session_state:
    st.session_state.round_finished = False

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# =========================================================
# FUNCTIONS
# =========================================================

def new_player():
    st.session_state.player = random.choice(players)
    st.session_state.clue_number = 0
    st.session_state.message = ""
    st.session_state.round_finished = False


def start_game():
    st.session_state.started = True
    st.session_state.score = 0
    st.session_state.round = 1
    st.session_state.game_over = False
    st.session_state.round_finished = False
    new_player()


def next_round():

    if st.session_state.round >= 5:
        st.session_state.game_over = True
    else:
        st.session_state.round += 1
        new_player()


def normalize_text(text):
    return "".join(
        char.lower()
        for char in text
        if char.isalnum()
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
            f"🎉 CORRECT!<br><br>"
            f"🏏 <strong>{player['name']}</strong><br><br>"
            f"⭐ +{points} POINTS"
        )

        st.session_state.round_finished = True

    else:

        if st.session_state.clue_number < 3:

            st.session_state.clue_number += 1

            st.session_state.message = (
                "❌ NOT QUITE!<br><br>"
                "💡 Here's another clue..."
            )

        else:

            st.session_state.message = (
                f"❌ ROUND OVER<br><br>"
                f"The answer was "
                f"<strong>{player['name']}</strong>."
            )

            st.session_state.round_finished = True


# =========================================================
# START SCREEN
# =========================================================

if not st.session_state.started:

    st.html("""
    <div class="game-title">

        <div class="welcome-text">
            🏏 WELCOME TO
        </div>

        <div class="main-title">
            GUESS THE<br>
            CRICKETER
        </div>

        <div class="tagline">
            THINK YOU KNOW CRICKET? PROVE IT! 🔥
        </div>

    </div>

    <div class="stadium"></div>

    <div class="rules-card">

        <div class="rules-title">
            🎮 HOW TO PLAY
        </div>

        <div class="rule">
            🕵️ A cricketer is picked randomly.
        </div>

        <div class="rule">
            💡 Clues are revealed one by one.
        </div>

        <div class="rule">
            ⭐ Guess early to earn more points.
        </div>

        <div class="rule">
            🏆 Complete 5 rounds.
        </div>

        <div class="rule">
            🔥 Small spelling mistakes are allowed.
        </div>

    </div>
    """)

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

    st.html(f"""
    <div class="final-card">

        <div class="final-trophy">
            🏆
        </div>

        <div class="final-title">
            GAME COMPLETE!
        </div>

        <p>
            You survived all 5 rounds!
        </p>

        <div class="stat-card">

            <div class="stat-icon">
                ⭐
            </div>

            <div class="stat-label">
                FINAL SCORE
            </div>

            <div class="stat-value">
                {st.session_state.score} / 50
            </div>

        </div>

    </div>
    """)

    score = st.session_state.score

    if score >= 45:
        st.success("👑 CRICKET GOD! Absolutely insane!")

    elif score >= 35:
        st.success("🔥 CRICKET MASTER! Outstanding!")

    elif score >= 25:
        st.info("👏 Great job! You really know your cricket!")

    elif score >= 15:
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

    # TITLE
    st.html("""
    <div class="game-title">

        <div class="welcome-text">
            🏏 GUESS THE
        </div>

        <div class="main-title">
            CRICKETER
        </div>

    </div>
    """)

    # PROGRESS
    st.progress(
        st.session_state.round / 5,
        text=f"🏏 ROUND {st.session_state.round} / 5"
    )

    # STATS
    col1, col2, col3 = st.columns(3)

    points = max(
        10 - (st.session_state.clue_number * 2),
        2
    )

    with col1:
        st.html(f"""
        <div class="stat-card">
            <div class="stat-icon">🏏</div>
            <div class="stat-label">ROUND</div>
            <div class="stat-value">
                {st.session_state.round}/5
            </div>
        </div>
        """)

    with col2:
        st.html(f"""
        <div class="stat-card">
            <div class="stat-icon">⭐</div>
            <div class="stat-label">SCORE</div>
            <div class="stat-value">
                {st.session_state.score}
            </div>
        </div>
        """)

    with col3:
        st.html(f"""
        <div class="stat-card">
            <div class="stat-icon">🏆</div>
            <div class="stat-label">POINTS</div>
            <div class="stat-value">
                {points}
            </div>
        </div>
        """)

    # WHO AM I
    st.html("""
    <div class="section-title">
        🔍 WHO AM I?
    </div>

    <div class="mystery-card">

        <div>
            <div class="mystery-icon">
                🏏❓
            </div>

            <div class="mystery-text">
                IDENTIFY THE MYSTERY CRICKETER
            </div>
        </div>

    </div>
    """)

    player = st.session_state.player

    # CLUES
    for index, clue in enumerate(player["clues"]):

        if index <= st.session_state.clue_number:

            if index == st.session_state.clue_number:
                class_name = "clue-card clue-active"
            else:
                class_name = "clue-card"

            st.html(f"""
            <div class="{class_name}">
                {clue}
            </div>
            """)

        else:

            st.html("""
            <div class="clue-card clue-locked">
                🔒 Mystery clue locked...
            </div>
            """)

    st.html(f"""
    <div class="clue-counter">
        💡 CLUE {st.session_state.clue_number + 1} / 4
    </div>
    """)

    # ANSWER
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

    # RESULT
    if st.session_state.message:

        st.html(f"""
        <div class="result-card">
            {st.session_state.message}
        </div>
        """)

    # NEXT ROUND
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

    # SCORING
    st.html("""
    <div class="rules-card">

        <div class="rules-title">
            🧠 SCORING
        </div>

        <div class="rule">
            🟢 Clue 1 → 10 points
        </div>

        <div class="rule">
            🟡 Clue 2 → 8 points
        </div>

        <div class="rule">
            🟠 Clue 3 → 6 points
        </div>

        <div class="rule">
            🔴 Clue 4 → 4 points
        </div>

    </div>
    """)
