import streamlit as st
import random
from difflib import SequenceMatcher

# =========================================================
# PAGE
# =========================================================

st.set_page_config(
    page_title="Guess The Cricketer",
    page_icon="🏏",
    layout="centered"
)

# =========================================================
# SIMPLE PAGE STYLE
# =========================================================

st.markdown("""
<style>
.stApp {
    background: #07182d;
}

.block-container {
    max-width: 700px;
    padding-top: 1rem;
    padding-bottom: 1rem;
}

h1 {
    color: #7CFF21 !important;
}

h2, h3 {
    color: white !important;
}

p, label {
    color: #e6edf5 !important;
}

.stCaption {
    color: #9bb5cf !important;
}

/* Input */
input {
    color: white !important;
}

/* Buttons */
button {
    min-height: 40px !important;
}

/* Mobile */
@media (max-width: 600px) {
    .block-container {
        padding: 0.5rem;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# PLAYERS
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

if "clue" not in st.session_state:
    st.session_state.clue = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "round" not in st.session_state:
    st.session_state.round = 1

if "finished" not in st.session_state:
    st.session_state.finished = False

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "message" not in st.session_state:
    st.session_state.message = ""


# =========================================================
# FUNCTIONS
# =========================================================

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
        c.lower()
        for c in text
        if c.isalnum()
    )


def is_correct(answer, player):

    answer = normalize(answer)

    if not answer:
        return False

    answers = [player["name"]] + player["aliases"]

    for option in answers:

        option = normalize(option)

        if answer == option:
            return True

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

        points = 10 - (st.session_state.clue * 2)

        if points < 4:
            points = 4

        st.session_state.score += points

        st.session_state.message = (
            f"🎉 Correct! **{player['name']}** "
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
                f"❌ The answer was **{player['name']}**."
            )

            st.session_state.finished = True


def next_round():

    if st.session_state.round >= 5:
        st.session_state.game_over = True

    else:
        st.session_state.round += 1
        choose_player()


# =========================================================
# START SCREEN
# =========================================================

if not st.session_state.started:

    st.title("🏏 Guess The Cricketer")

    st.caption("Think you know cricket? Prove it! 🔥")

    st.info(
        "💡 Guess early to score more points!"
    )

    st.subheader("🎮 How to Play")

    st.write("🕵️ A cricketer is selected randomly.")
    st.write("💡 You get 4 clues.")
    st.write("⭐ Fewer clues = more points.")
    st.write("🔥 Small spelling mistakes are allowed.")
    st.write("🏆 Complete 5 rounds.")

    st.button(
        "🔥 START GAME",
        on_click=start_game,
        use_container_width=True
    )


# =========================================================
# FINAL SCREEN
# =========================================================

elif st.session_state.game_over:

    st.title("🏆 Game Complete!")

    st.success(
        f"You completed all 5 rounds!"
    )

    st.metric(
        "FINAL SCORE",
        f"{st.session_state.score} / 50"
    )

    score = st.session_state.score

    if score >= 45:
        st.balloons()
        st.success("👑 CRICKET GOD!")

    elif score >= 35:
        st.success("🔥 CRICKET MASTER!")

    elif score >= 25:
        st.info("👏 Great job!")

    elif score >= 15:
        st.warning("😄 Not bad!")

    else:
        st.error("😂 Time to watch more cricket!")

    st.button(
        "🔄 PLAY AGAIN",
        on_click=start_game,
        use_container_width=True
    )


# =========================================================
# GAME SCREEN
# =========================================================

else:

    st.title("🏏 Guess The Cricketer")

    st.caption("Can you identify the mystery player?")

    # -------------------------
    # STATS
    # -------------------------

    col1, col2, col3 = st.columns(3)

    points = 10 - (
        st.session_state.clue * 2
    )

    if points < 4:
        points = 4

    with col1:
        st.metric(
            "ROUND",
            f"{st.session_state.round}/5"
        )

    with col2:
        st.metric(
            "⭐ SCORE",
            st.session_state.score
        )

    with col3:
        st.metric(
            "🏆 POINTS",
            points
        )

    st.progress(
        st.session_state.round / 5
    )

    # -------------------------
    # GAME
    # -------------------------

    st.divider()

    st.subheader("🔍 WHO AM I?")

    st.caption("🏏 Mystery player")

    player = st.session_state.player

    current_clue = player["clues"][
        st.session_state.clue
    ]

    st.info(current_clue)

    st.caption(
        f"💡 Clue {st.session_state.clue + 1} / 4"
    )

    # -------------------------
    # ANSWER
    # -------------------------

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
                        "Please enter a cricketer's name."
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
                    "All clues are already revealed!"
                )

    # -------------------------
    # RESULT
    # -------------------------

    if st.session_state.message:

        st.success(
            st.session_state.message
            if "Correct" in st.session_state.message
            else st.session_state.message
        )

    # -------------------------
    # NEXT ROUND
    # -------------------------

    if st.session_state.finished:

        st.divider()

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
