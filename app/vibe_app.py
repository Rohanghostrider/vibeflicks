import streamlit as st
import random
from data.vibe_data import vibe_dict

st.set_page_config(page_title="VibeFlicks", page_icon="🎬", layout="centered")
st.title("VibeFlicks 🎬")
st.markdown("Curated Bollywood movies and music to match your mood. Select a vibe and start exploring!")

# Surprise Me feature
if st.button("🎲 Surprise Me"):
    selected_mood = random.choice(list(vibe_dict.keys()))
else:
    selected_mood = st.selectbox("Select your mood:", options=list(vibe_dict.keys()), index=0)

if selected_mood:
    movies = vibe_dict[selected_mood]["movies"]
    songs = vibe_dict[selected_mood]["songs"]

    st.subheader(f"🎬 Movies that match the '{selected_mood.capitalize()}' vibe")

    for movie in movies:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(movie["image"], width=150)
        with col2:
            st.markdown(f"**{movie['name']}**")
        st.markdown("---")

    st.subheader("🎧 Music Recommendations")
    st.markdown("Enjoy the soundtrack that fits your mood:")

    # Embed first video
    st.video(songs[0]["link"])

    # Link the rest
    for song in songs[1:]:
        st.markdown(f"- [{song['name']}]({song['link']})")

st.caption("Powered by Rohan’s Mood Engine 💫")
