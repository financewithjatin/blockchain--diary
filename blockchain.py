import streamlit as st
from blockchain import Blockchain

# Initialize blockchain
if "blockchain" not in st.session_state:
    st.session_state.blockchain = Blockchain()

st.title("📖 Blockchain-based Digital Diary")
st.write("Tamper-proof diary entries stored on blockchain")

# User input
entry = st.text_area("Write your daily diary entry:")

if st.button("Add Entry"):
    if entry.strip() != "":
        st.session_state.blockchain.add_block(entry)
        st.success("✅ Entry added to blockchain!")
    else:
        st.warning("Please write something before adding.")

st.subheader("🗂️ Diary Timeline")
for block in st.session_state.blockchain.chain:
    st.markdown(f"""
    **Block {block.index}**  
    - 🕒 Timestamp: {block.timestamp}  
    - 📝 Entry: {block.data}  
    - 🔗 Hash: `{block.hash}`  
    - ⬅️ Prev Hash: `{block.previous_hash}`
    """)
    st.divider()
