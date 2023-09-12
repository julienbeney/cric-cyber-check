import streamlit as st
import requests
# Step 1: Create a sidebar for user inputs
st.header('Cybercheck: Your Detailed Data Leak Guardian')
st.markdown('In the expansive digital landscape, Cybercheck emerges as a vigilant guardian, tirelessly monitoring the cyberspace for any leaks associated with your email address. But it goes a step further; for every leak detected, it provides detailed insights including the personal data involved and the exact period it was compromised.')
st.markdown('Armed with Cybercheck, you’re not just informed but empowered, having a clear view of your digital footprint and the guidance to secure it.')
st.divider()
col1, col2 = st.columns(2)

with col1:
    email = st.text_input('Enter your email:')
    
    # Step 2: Create a button to initiate the cyber check
    if st.button('Check Mail') and email != '':
        # Step 3: Display the input email before making the API call
        st.write(f"The email you entered is: {email}")

        # Step 4: Make the API call here (pseudo code)
        # Note: Replace `api_endpoint` and `api_key` with your actual API endpoint and key
        api_endpoint = 'https://leak-lookup.com/api/search'
        response = requests.post(api_endpoint,
            data={
                "key": 'b53f6a8d5d48091321f42ab97989a797',
                "type": 'email_address',
                "query": email,

            }
        )
        if response.status_code == 200:
            api_response = response.json()
            
            # Step 6: Display the API response
            if api_response.get("error") == "false":
                message = api_response.get("message", {})
                try:
                    for breach_site, breach_data in message.items():
                        st.write(f"{breach_site.replace('_', ' ').title()}: {', '.join(breach_data) or 'No data available'}")
                    st.write("####Detailed emails and data columns is only available in production.")
                except: 
                    st.write("No leaks founds")
            
            else:
                st.write("An error occurred while fetching the breach data.")
        else:
            st.write("Failed to retrieve data from the API.")


with col2:
    # Step 2: Create a button to initiate the cyber check
    domain = st.text_input('Enter your domain:')

    if st.button('Check Domain') and domain != '':
        # Step 3: Display the input email before making the API call
        st.write(f"The domain you entered is: {domain}")

        # Step 4: Make the API call here (pseudo code)
        # Note: Replace `api_endpoint` and `api_key` with your actual API endpoint and key
        api_endpoint = 'https://leak-lookup.com/api/search'
        response = requests.post(api_endpoint,
            data={
                "key": 'b53f6a8d5d48091321f42ab97989a797',
                "type": 'domain',
                "query": domain,

            }
        )
        if response.status_code == 200:
            api_response = response.json()
            
            # Step 6: Display the API response
            if api_response.get("error") == "false":
                message = api_response.get("message", {})
                try:
                    for breach_site, breach_data in message.items():
                        st.write(f"{breach_site.replace('_', ' ').title()}: {', '.join(breach_data) or 'No data available'}")
                    st.write("####Detailed emails and data columns is only available in production.")
                except: 
                    st.write("No leaks founds")
                
            else:
                print(api_response)

                st.write("An error occurred while fetching the breach data.")
        else:
            print(api_response)

            st.write("Failed to retrieve data from the API.")
