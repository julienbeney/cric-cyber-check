import streamlit as st
import requests
# Step 1: Create a sidebar for user inputs

st.header('Cybercheck: Your Website Intelligence Tool')
st.markdown('In the vast sea of websites, Cybercheck stands as your intelligent navigator, delving deep to extract all the crucial information surrounding any website you wish to explore. From security assessments to data leaks, it offers a comprehensive view, granting you the insights you need to navigate the web safely and knowledgeably.')
st.markdown('Cybercheck doesn’t just provide information; it equips you with a powerful lens to scrutinize the digital terrain, ensuring a secure and informed online journey.')
st.divider()
st.markdown('We are working tirelessly to bring this tool to this server. In the meantime, we are thrilled to announce that Cybercheck is available for use at a specific location.')
web = st.text_input('Enter your website url:')
if st.button('Check the website') and web != '':
    st.write(f'[Access {web} data result](https://web-check.as93.net/results/globaz.ch)')

