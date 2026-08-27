import streamlit as st
import random
from difflib import SequenceMatcher

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Guess The Cricketer 🏏",
    page_icon="🏏",
    layout="centered"
)

# -----------------------------
# CRICKETER DATABASE
# -----------------------------
players = [

    # 🇮🇳 INDIA
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
            "🔥 I once hit six sixes in an over in T20 cricket.",
            "🏆 I was Player of the Tournament at the 2011 World Cup."
        ]
    },

    # 🇦🇺 AUSTRALIA
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
            "🔥 I have played for Sunrisers Hyderabad in the IPL."
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

    # 🏴 ENGLAND
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

    # 🇿🇦 SOUTH AFRICA
    {
        "name": "AB de Villiers",
        "aliases": [
            "ab",
            "abd",
            "abd de villiers",
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

    # 🇵🇰 PAKISTAN
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

    # 🇱🇰 SRI LANKA
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

    # 🌴 WEST INDIES
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

    # 🇳🇿 NEW ZEALAND
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

    # 🇦🇫 AFGHANISTAN
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

# -----------------------------
# SESSION STATE
# -----------------------------
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

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "round_finished" not in st.session_state:
    st.session_state.round_finished = False


# -----------------------------
# FUNCTIONS
# -----------------------------
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

        # Exact match
        if answer == possible:
            return True

        # Minor spelling mistakes
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
            f"🎉 CORRECT!\n\n"
            f"🏏 It was **{player['name']}**!\n\n"
            f"⭐ You earned **{points} points**."
        )

        st.session_state.round_finished = True

    else:

        if st.session_state.clue_number < 3:

            st.session_state.clue_number += 1

            st.session_state.message = (
                "❌ Not quite!\n\n"
                "💡 Here's another clue..."
            )

        else:

            st.session_state.message = (
                f"❌ You couldn't get it this time.\n\n"
                f"🏏 The answer was **{player['name']}**."
            )

            st.session_state.round_finished = True


# -----------------------------
# TITLE
# -----------------------------
st.title("🏏 Guess The Cricketer")

st.caption(
    "Think you know cricket? Prove it!"
)


# -----------------------------
# START SCREEN
# -----------------------------
if not st.session_state.started:

    st.markdown("## 🎮 GUESS THE CRICKETER")

    st.write(
        """
        🕵️ A random cricketer will be selected.

        💡 You'll get clues one by one.

        ⭐ Guess early to earn more points.

        🏆 Complete 5 rounds.

        🔥 Try to become the Cricket Master!
        """
    )

    st.info(
        "💡 Small spelling mistakes are allowed!"
    )

    st.button(
        "🚀 START GAME",
        on_click=start_game,
        use_container_width=True
    )


# -----------------------------
# GAME SCREEN
# -----------------------------
elif not st.session_state.game_over:

    st.progress(
        st.session_state.round / 5,
        text=f"🏏 ROUND {st.session_state.round} / 5"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "⭐ SCORE",
            st.session_state.score
        )

    with col2:

        points_left = max(
            10 - (st.session_state.clue_number * 2),
            2
        )

        st.metric(
            "🏆 POINTS",
            points_left
        )

    st.divider()

    st.subheader("🔍 WHO AM I?")

    player = st.session_state.player

    current_clue = player["clues"][
        st.session_state.clue_number
    ]

    st.info(current_clue)

    st.caption(
        f"💡 Clue {st.session_state.clue_number + 1} / 4"
    )

    # -----------------------------
    # ANSWER INPUT
    # -----------------------------
    if not st.session_state.round_finished:

        with st.form("guess_form"):

            answer = st.text_input(
                "Your answer:",
                placeholder="Enter the cricketer's name..."
            )

            submitted = st.form_submit_button(
                "🔥 GUESS",
                use_container_width=True
            )

            if submitted:

                if answer.strip():

                    check_answer(answer)

                    st.rerun()

                else:

                    st.warning(
                        "⚠️ Enter a name first!"
                    )

        # -----------------------------
        # NEXT CLUE
        # -----------------------------
        if st.button(
            "💡 NEXT CLUE",
            use_container_width=True
        ):

            if st.session_state.clue_number < 3:

                st.session_state.clue_number += 1
                st.session_state.message = ""

                st.rerun()

            else:

                st.warning(
                    "🚫 No more clues!"
                )

    # -----------------------------
    # RESULT MESSAGE
    # -----------------------------
    if st.session_state.message:

        st.divider()

        if "CORRECT" in st.session_state.message:

            st.success(
                st.session_state.message
            )

        else:

            st.error(
                st.session_state.message
            )

    # -----------------------------
    # NEXT ROUND
    # -----------------------------
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


# -----------------------------
# GAME OVER
# -----------------------------
else:

    st.balloons()

    st.header("🏆 GAME COMPLETE!")

    st.metric(
        "FINAL SCORE",
        f"{st.session_state.score} / 50"
    )

    if st.session_state.score >= 45:

        st.success(
            "👑 CRICKET GOD! Absolutely insane!"
        )

    elif st.session_state.score >= 35:

        st.success(
            "🔥 CRICKET MASTER! Outstanding!"
        )

    elif st.session_state.score >= 25:

        st.info(
            "👏 Great job! You know your cricket!"
        )

    elif st.session_state.score >= 15:

        st.warning(
            "😄 Not bad! Time to sharpen your cricket knowledge!"
        )

    else:

        st.error(
            "😂 Looks like you need to watch more cricket!"
        )

    st.divider()

    st.write(
        "Think you can beat your score?"
    )

    st.button(
        "🔄 PLAY AGAIN",
        on_click=start_game,
        use_container_width=True
    )
