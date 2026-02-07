import streamlit as st
from src.extractor import extract_actions
from src.summareizer import summarize
from src.storage import save_meetings

#Page configuration
st.set_page_config(
    page_title="AI Meeting Memory Assistant",
    page_icon=":-)",
    layout="centered"
)

st.title("AI Meeting Memory Assistant")
st.write("Paste your meeting notes below "
         "This app will extract action items, deadlines and store the meetings.")

#Text
meeting_text = st.text_area("Meeting Notes",
height = 250,
placeholder="Example:\n Amit will prepare budget report by Friday.\nAkshay should contact the vendor next week."
                            )
#Process button
if st.button("Process Meeting"):
    if meeting_text == "":
        st.warning("Please enter your meeting notes.")
    else:
        summary = summarize(meeting_text)
        actions = extract_actions(meeting_text)

        #save_meetings(summary, actions)
        #Output
        st.success("Meeting summarized successfully!")
        st.subheader("Meeting Summary")
        st.write(summary)
        st.subheader("Meeting Actions items")
        if actions:
            for idx, action in enumerate(actions, start=1):
                st.markdown(
                    f""""
                    **{idx}.{action['task']}**
                    Deadline: '{action['deadline']}'
                    """
            )
        else:
            st.info("No actions items found.")

