import streamlit as st

st.set_page_config(
    page_title="Hello from Shreya",
    page_icon="🌷"
)

# Remember the visitor's name and page during their visit.
if "visitor_name" not in st.session_state:
    st.session_state.visitor_name = ""

if "page" not in st.session_state:
    st.session_state.page = "Welcome"


def save_name():
    st.session_state.visitor_name = st.session_state.name_input


def change_page(destination):
    st.session_state.page = destination


descriptions = {
    "January": (
        "You like having something meaningful to work toward, even when "
        "you don't share all your plans with everyone. You often show "
        "care by being dependable, keeping your word, and taking care "
        "of the little things that others might overlook. People may "
        "assume you always have everything under control, but you "
        "appreciate reassurance and support too. When things don't go "
        "as planned, you can be harder on yourself than you would ever "
        "be on a friend. Give yourself permission to learn as you go. "
        "You deserve rest, affection, and good moments along the way—not "
        "just after you reach your next goal."
    ),
    "February": (
        "You enjoy seeing things from your own perspective, and you "
        "don't always feel the need to follow what everyone else is "
        "doing. An unusual idea, an unexpected conversation, or someone "
        "who thinks differently can hold your attention for hours. "
        "You value meaningful connections, but you also appreciate "
        "having space to think and recharge. Sometimes you may struggle "
        "to explain what is happening in your head because there is "
        "so much going on at once. You don't have to make every part "
        "of yourself immediately understandable. Let people get to "
        "know you gradually, and leave room for your ideas to grow."
    ),
    "March": (
        "You have a soft spot for the small details that make life "
        "feel personal—a remembered conversation, a thoughtful message, "
        "or a song that brings back a particular moment. You may find "
        "yourself imagining possibilities or noticing how other people "
        "feel before they say much. That thoughtfulness can make you "
        "wonderful company, but it can also leave you carrying worries "
        "that aren't yours to solve. You are allowed to step back and "
        "protect your energy. Keep making room for the things that "
        "inspire you, whether that is music, creativity, friendship, "
        "or a quiet evening with nothing you need to prove."
    ),
    "April": (
        "When something catches your interest, you want to explore "
        "it rather than spend forever wondering what might happen. "
        "You bring enthusiasm to new beginnings and often find your "
        "confidence by taking action. Waiting, uncertainty, and slow "
        "progress can frustrate you, especially when you care deeply "
        "about the result. Sometimes your honesty arrives before you "
        "have had time to soften the words, but you appreciate people "
        "who are straightforward with you too. Give yourself a moment "
        "to pause when you need it. Your courage can show up in starting "
        "something new, asking for help, or choosing to try again."
    ),
    "May": (
        "You appreciate people and places that help you feel comfortable "
        "being yourself. Loyalty matters to you, and you tend to notice "
        "whether someone's actions match their words. When you commit "
        "to something meaningful, you are willing to give it time and "
        "steady effort. You also know the value of small pleasures: "
        "a good meal, a familiar song, or an unhurried conversation. "
        "Change may take some getting used to, particularly when it "
        "disrupts something you have worked hard to build. You can "
        "keep what matters to you while making space for something "
        "new. Changing your mind can be a thoughtful decision too."
    ),
    "June": (
        "Your curiosity can take a conversation in several interesting "
        "directions. You enjoy discovering what makes people laugh, "
        "what they care about, and how they see the world. There may "
        "be days when you feel talkative and playful, and others when "
        "you would rather keep your thoughts to yourself. Both belong "
        "to you. Because you can see different sides of a situation, "
        "making a decision sometimes takes longer than people expect. "
        "Give yourself space to choose without explaining every step. "
        "The people who care about you can enjoy your company even "
        "when you have no funny story or clever observation to offer."
    ),
    "July": (
        "Feeling comfortable with someone means a great deal to you. "
        "You appreciate relationships where you can relax, speak "
        "honestly, and enjoy the ordinary moments together. Small "
        "gestures may stay with you for a long time because you "
        "remember how they made you feel. You often express affection "
        "by checking in, remembering details, or making someone feel "
        "included. At times, you might hope others will notice what "
        "you need without having to ask. It is okay to tell them "
        "directly. Your feelings deserve attention, and you are "
        "allowed to receive the same patience and care you give."
    ),
    "August": (
        "You enjoy bringing warmth and personality to the things you "
        "do. When you care about someone, you may want them to feel "
        "celebrated, encouraged, and proud of themselves. You can "
        "step forward when a situation needs direction, even if you "
        "are still working things out internally. Being seen as "
        "confident can sometimes make it difficult to admit that you "
        "need reassurance too. You don't have to keep up an impressive "
        "appearance every day. Let yourself be a beginner, laugh "
        "at a mistake, or ask someone else to take the lead. "
        "There is plenty to appreciate about you in those moments."
    ),
    "September": (
        "You often notice the details that could make something "
        "clearer, kinder, or more useful. You may show affection "
        "through practical gestures—helping someone prepare, remembering "
        "what they need, or following through on a promise. Doing "
        "things well matters to you, but that can make it difficult "
        "to recognize when you have already done enough. You might "
        "replay a small mistake long after everyone else has moved "
        "on. Try giving yourself the understanding you would offer "
        "someone you love. Your effort has value even when the "
        "result is imperfect, and you are allowed to enjoy your "
        "progress before everything is finished."
    ),
    "October": (
        "You appreciate good conversation, thoughtful gestures, and "
        "spaces where people feel welcome. You often consider how "
        "a decision will affect everyone involved, which can make "
        "you a considerate friend or teammate. But weighing every "
        "perspective may leave you unsure about what you want. "
        "You are allowed to have a preference even when someone "
        "else would choose differently. A little disagreement does "
        "not have to undo a meaningful connection. Keep making room "
        "for the beauty, humor, and companionship you enjoy, while "
        "remembering that your comfort and opinions deserve attention "
        "alongside the needs of the people around you."
    ),
    "November": (
        "You appreciate honesty and tend to enjoy conversations that "
        "go beyond the usual small talk. You may take time to feel "
        "comfortable opening up, preferring to build trust through "
        "consistent actions rather than big promises. Once something "
        "matters to you, you can give it considerable attention and "
        "commitment. That intensity can be useful, but it is also "
        "okay to step away from a question you cannot solve today. "
        "You don't need to explain every feeling perfectly before "
        "sharing it with someone. Let yourself enjoy lighter moments "
        "too—a silly conversation, an unexpected laugh, or a day "
        "that asks very little of you."
    ),
    "December": (
        "You enjoy having something to look forward to, whether "
        "it is a new experience, a visit with someone you love, "
        "or a small plan for the weekend. Your enthusiasm can "
        "help other people see possibilities they had overlooked. "
        "You appreciate laughter and may use humor to make an "
        "uncomfortable moment feel easier. Still, you don't have "
        "to be the cheerful person in every room. There is space "
        "for disappointment, uncertainty, and quiet days too. Follow "
        "your curiosity at a pace that works for you, and remember "
        "that an ordinary afternoon can be just as worth enjoying "
        "as the next big adventure."
    ),
}

# Sidebar navigation
page = st.sidebar.radio(
    "Explore ✨",
    ["Welcome", "Your Birth Month", "A Note for You"],
    key="page"
)

st.sidebar.caption("Made with ❤️ by Shreya")

# PAGE 1: Welcome
if page == "Welcome":
    st.title("Hey there! 👋")
    st.write(
        "A little hello, a little discovery, "
        "and something to make you smile."
    )

    if "name_input" not in st.session_state:
        st.session_state.name_input = st.session_state.visitor_name

    st.text_input(
        "What should I call you?",
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

# PAGE 2: Birth month
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

# PAGE 3: Encouragement
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
