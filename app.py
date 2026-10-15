import streamlit as st

st.set_page_config(
    page_title="Hello from Shreya",
    page_icon="🌷"
)

# Remember the visitor's name and current page.
if "visitor_name" not in st.session_state:
    st.session_state.visitor_name = ""

if "page" not in st.session_state:
    st.session_state.page = "Welcome"


def save_name():
    st.session_state.visitor_name = st.session_state.name_input


def change_page(destination):
    st.session_state.page = destination


# Sidebar navigation
page = st.sidebar.radio(
    "Explore ✨",
    ["Welcome", "Your Birth Month", "A Note for You"],
    key="page"
)

st.sidebar.caption("Made with ❤️ by Shreya")

descriptions = {
    "January": (
        "You like having something to work toward, even if you keep "
        "your plans to yourself. People may see you as dependable, "
        "but you also appreciate someone checking on you. "
        "You deserve rest without having to earn it first."
    ),
    "February": (
        "You enjoy looking at things a little differently and making "
        "choices that feel like you. You value connection, but you "
        "also need space to think. Your quieter moments can hold "
        "some of your most interesting ideas."
    ),
    "March": (
        "You notice little things—a change in someone's tone, a "
        "thoughtful gesture, or a beautiful evening. Your imagination "
        "makes ordinary moments feel special. Give yourself the "
        "same kindness you so readily offer others."
    ),
    "April": (
        "When something excites you, you want to give it a try. "
        "You bring energy and honesty, though waiting can test "
        "your patience. Your courage shines when you take that "
        "first step without having everything figured out."
    ),
    "May": (
        "You appreciate comfort, loyalty, and people who mean what "
        "they say. Once something matters to you, you're willing "
        "to put in the effort. You can hold your ground while "
        "still leaving room to change your mind."
    ),
    "June": (
        "Your curiosity can turn a small conversation into an "
        "unexpected adventure. You enjoy discovering different "
        "sides of people, even when your own feelings are harder "
        "to explain. You don't have to be entertaining to be "
        "good company."
    ),
    "July": (
        "You care deeply about feeling at home with the people "
        "around you. You may remember small moments that others "
        "have forgotten because they meant something to you. "
        "Let yourself receive the care you often give."
    ),
    "August": (
        "You enjoy putting your own stamp on things and making "
        "the people you love feel celebrated. You can take charge "
        "when needed, but you appreciate encouragement too. "
        "You don't have to appear confident every day to be capable."
    ),
    "September": (
        "You notice what could be improved and often show care "
        "through thoughtful actions. You like doing things well, "
        "which can sometimes make you your own toughest critic. "
        "Something can be meaningful without being perfect."
    ),
    "October": (
        "You enjoy warmth, good conversation, and making people "
        "feel included. You often consider more than one side "
        "before deciding what you think. Your own preferences "
        "deserve a place alongside everyone else's."
    ),
    "November": (
        "You prefer connections that feel honest and conversations "
        "with a little depth. You may take your time opening up, "
        "but trust matters greatly once you do. You're allowed "
        "to be both independent and in need of support."
    ),
    "December": (
        "You enjoy having something to look forward to and finding "
        "reasons to laugh along the way. Your enthusiasm can make "
        "new possibilities feel closer. You can love adventure "
        "and still appreciate a quiet, ordinary day."
    ),
}

# PAGE 1
if page == "Welcome":
    st.title("Hey there! 👋")
    st.write(
        "A little hello, a little discovery, "
        "and something to make you smile."
    )

    st.text_input(
        "What should I call you?",
        value=st.session_state.visitor_name,
        key="name_input",
        on_change=save_name,
        placeholder="Type your name and press Enter"
    )

    name = st.session_state.visitor_name.strip()

    if name:
        st.success(f"Hello, {name}! So glad you're here 😊")
        st.button(
            "Next →",
            on_click=change_page,
            args=("Your Birth Month",)
        )

# PAGE 2
elif page == "Your Birth Month":
    st.title("Your Birth Month ✨")
    st.caption(
        "Just for fun—your birth month doesn't determine "
        "your personality."
    )

    month = st.selectbox(
        "Pick your birth month",
        ["Choose a month…"] + list(descriptions)
    )

    if month in descriptions:
        name = st.session_state.visitor_name.strip()

        if name:
            st.subheader(f"{name}, your {month} reading 🌸")
        else:
            st.subheader(f"{month} 🌸")

        st.write(descriptions[month])

        st.button(
            "Next → A note for you",
            on_click=change_page,
            args=("A Note for You",)
        )

    st.button(
        "← Back to welcome",
        on_click=change_page,
        args=("Welcome",)
    )

# PAGE 3
elif page == "A Note for You":
    st.title("A Little Note for You 💌")

    name = st.session_state.visitor_name.strip()
    st.subheader(f"Dear {name}," if name else "Dear you,")

    st.write(
        "You don't need to figure everything out today. "
        "Take one small step, give yourself room to learn, "
        "and notice the things you're already doing well."
    )

    st.write(
        "Some days will feel exciting; others will feel ordinary. "
        "There's room for both. I hope you find one little "
        "reason to smile today."
    )

    st.write("With love,")
    st.write("**Shreya 🌷**")

    if st.button("A little celebration 🎈"):
        st.balloons()

    st.button(
        "← Back to birth month",
        on_click=change_page,
        args=("Your Birth Month",)
    )
