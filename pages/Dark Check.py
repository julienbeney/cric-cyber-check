import streamlit as st
import requests
import os
# Step 1: Create a sidebar for user inputs

st.header('Cybercheck: Your Darknet Surveillance Ally')

st.markdown('In the hidden corners of the darknet, where anonymity reigns, Cybercheck operates as your watchful ally, unearthing any mentions of your email address amidst the obscured data pools. With each discovery, it delivers a meticulous report outlining the personal details exposed and the specific timeframe of the leak.')
st.markdown('With Cybercheck, you gain an unprecedented level of awareness and the essential tools to protect yourself in the ever-evolving digital landscape.')
st.divider()
col1, col2 = st.columns(2)

with col1:
    email = st.text_input('Enter your email:')
    if st.button('Check Email') and email != '':
        spl = email.split('@')[0]+'@'
        command = f'python3 darkdump/darkdump.py --query="{spl}"'
        st.write(f'### Searching For: {email} and showing 10 results...')
        result = os.popen(command)
        st.write()
        st.divider()
        tester = False
        for line in result.read().split('\n')[:-2][12:]:
            if 'Website:' in line or '.onion' in line or 'No result' in line:
                tester = True
                if '[+]' in line:
                    st.write(line.split('[+]')[1].replace('Website:','**Website:**'))
                else:
                    st.write(line.replace('\x1b[','').replace('\n\n','\n'))
                    st.divider()
        if not tester:
            st.write('No results found.')
with col2:
    name = st.text_input('Enter your name:')
    forname = st.text_input('Enter your forname:')
    if st.button('Check Name') and name != '' and forname != '':
        command = f'python3 darkdump/darkdump.py --query="{name} {forname}"'
        st.write(f'### Searching For: {name} {forname} and showing 10 results...')
        result = os.popen(command)
        st.write()
        st.divider()
        tester = False
        for line in result.read().split('\n')[:-2][12:]:
            if 'Website:' in line or '.onion' in line or 'No result' in line:
                tester = True
                if '[+]' in line:
                    st.write(line.split('[+]')[1].replace('Website:','**Website:**'))
                else:
                    st.write(line.replace('\x1b[','').replace('\n\n','\n'))
                    st.divider()
        if not tester:
            st.write('No results found.')

# Step 2: Create a button to initiate the cyber check


            