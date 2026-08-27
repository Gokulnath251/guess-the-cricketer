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
    {
        "name": "MS Dhoni",
        "aliases": ["dhoni", "msd", "ms dhoni"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🧤 I am famous for my wicketkeeping.",
            "🏆 I have captained India to a World Cup victory.",
            "🦁 I am strongly associated with Chennai Super Kings."
        ]
    },
    {
        "name": "Virat Kohli",
        "aliases": ["kohli", "virat", "virat kohli"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🏏 I am a right-handed batsman.",
            "👑 I am often called the King of Indian cricket.",
            "🔥 I have scored many international centuries."
        ]
    },
    {
        "name": "Rohit Sharma",
        "aliases": ["rohit", "rohit sharma", "hitman"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🏏 I am an opening batsman.",
            "💯 I have scored multiple ODI double centuries.",
            "🏆 I have captained India."
        ]
    },
    {
        "name": "Suresh Raina",
        "aliases": ["raina", "suresh raina", "mr ipl"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🏏 I am known mainly as a white-ball cricketer.",
            "💛 I am strongly associated with Chennai Super Kings.",
            "👑 I am popularly called Mr. IPL."
        ]
    },
    {
        "name": "Sachin Tendulkar",
        "aliases": ["sachin", "tendulkar", "sachin tendulkar"],
        "clues": [
            "🇮🇳 I am an Indian cricket legend.",
            "🏏 I was known as a technically gifted batsman.",
            "💯 I scored 100 international centuries.",
            "🏆 I was part of India's 2011 World Cup-winning team."
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
            "🌍 I represented South Africa.",
            "🏏 I was famous for innovative batting.",
            "⚡ I could score extremely quickly.",
            "🔥 Fans often called me Mr. 360."
        ]
    },
    {
        "name": "Chris Gayle",
        "aliases": ["gayle", "chris gayle", "universe boss"],
        "clues": [
            "🌴 I represented the West Indies.",
            "🏏 I am a powerful left-handed batsman.",
            "💥 I am famous for huge sixes.",
            "🔥 I am known as the Universe Boss."
        ]
    },
    {
        "name": "Jasprit Bumrah",
        "aliases": ["bumrah", "jasprit", "jasprit bumrah"],
        "clues": [
            "🇮🇳 I am an Indian cricketer.",
            "🎯 I am a fast bowler.",
            "⚡ I have an unusual bowling action.",
            "🔥 I am known for deadly yorkers."
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
    """
    Remove spaces, punctuation and capitalization
    so small formatting differences don't matter.
    """
    return "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )


def is_correct_answer(answer, player):
    """
    Accept:
    - Exact name
    - Aliases
    - Small spelling mistakes
    """

    answer = normalize_text(answer)

    if not answer:
        return False

    possible_answers = [player["name"]] + player["aliases"]

    for possible in possible_answers:

        possible = normalize_text(possible)

        # Exact match
        if answer == possible:
            return True

        # Similar spelling
        similarity = SequenceMatcher(
            None,
            answer,
            possible
        ).ratio()

        # Accept minor spelling mistakes
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

        if st.session_state.clue_number < len(player["clues"]) - 1:

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
    "Can you identify the cricketer using the fewest clues?"
)


# -----------------------------
# START SCREEN
# -----------------------------
if not st.session_state.started:

    st.markdown("## 🎮 How to Play")

    st.write(
        """
        🕵️ A cricketer will be selected randomly.

        💡 You will receive clues one by one.

        ⭐ The fewer clues you need, the more points you earn.

        🏆 There are 5 rounds.

        🔥 Try to get the highest score!
        """
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
        text=f"Round {st.session_state.round} / 5"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "⭐ Score",
            st.session_state.score
        )

    with col2:

        points_left = max(
            10 - (st.session_state.clue_number * 2),
            2
        )

        st.metric(
            "🏆 Points",
            points_left
        )

    st.divider()

    st.subheader("🔍 Who am I?")

    player = st.session_state.player

    current_clue = player["clues"][
        st.session_state.clue_number
    ]

    st.info(current_clue)

    st.caption(
        f"Clue {st.session_state.clue_number + 1} "
        f"of {len(player['clues'])}"
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
                        "⚠️ Enter a cricketer's name first!"
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
                    "No more clues available!"
                )

    # -----------------------------
    # RESULT
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

    if st.session_state.score >= 40:

        st.success(
            "🔥 CRICKET MASTER! Outstanding!"
        )

    elif st.session_state.score >= 25:

        st.info(
            "👏 Great job! You know your cricket!"
        )

    else:

        st.warning(
            "😄 Good try! Time for a rematch!"
        )

    st.divider()

    st.write(
        "Ready for another game?"
    )

    st.button(
        "🔄 PLAY AGAIN",
        on_click=start_game,
        use_container_width=True
    )
