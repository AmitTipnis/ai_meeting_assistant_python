import streamlit as st
from src.extractor import extract_actions
from src.summareizer import summarize
from src.llm_extractor import exttract_with_llm
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

ai_mode = st.radio(
    "Choose AI Mode",
    ["Rule-based (Quick & Free)", "LLM-based (AI need to think :-))"]
)
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
        if ai_mode == "Rule-based (Quick & Free)":
            summary = summarize(meeting_text)
            actions = extract_actions(meeting_text)
        else:
            llm_result = exttract_with_llm(meeting_text)
            summary = llm_result
            actions = ""
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

