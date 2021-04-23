import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

st.title('Status of Survey about Campaigns of Tirupati PC Elections')
st.write("It shows ***PC level analysis*** in Tirupati PC")
st.sidebar.title("Selector")
image = Image.open("PC.jpg")
st.image(image,use_column_width=False)
st.markdown('<style>body{background-color: lightblue;}Survey</style>',unsafe_allow_html=True)
#container=st.beta_container()
st.markdown("## **Actual data of survey**")

#Reading data from CSV file using Pandas
@st.cache
def load_data():
    Survey_data = pd.read_csv("Survey_5_Responses .csv")
    return Survey_data

Survey_data = load_data()


#Created dropdown to select constituency
select_constituency = st.sidebar.selectbox('Select a Constituency',Survey_data['AC'].unique())


#Created dropdown to select Mandal under a specific constituency which was selected in the above dropdown
if len(select_constituency)> 0:
    types = select_constituency
    #st.write(types)
    mandal = sorted(set(Survey_data['Mandal'].loc[Survey_data['AC']==(types)]))
    #st.write(mandal)
    select_mandal = st.sidebar.selectbox('Select Mandal',mandal)
else:
    types = []
    mandal = sorted(set(Survey_data['Mandal'].loc[Survey_data['AC']==(types)]))
    #st.write(mandal)
    select_mandal = st.sidebar.selectbox('Select Mandal',mandal)



#Extracted data under a specific constituency and Mandal 
selected_state = Survey_data[Survey_data['AC']==select_constituency]
selected_state = Survey_data[Survey_data['Mandal']==select_mandal]
st.write(selected_state)
#st.write(selected_state1)


#Extracted Data of call responded in Survey from CSV file under a specific constituency and Mandal which were selected in dropdowns
st.markdown("## **Data of responded**")
respond_data = selected_state[selected_state['Status of the call']=='Call responded']
st.write(respond_data)


#Pie chart for the TDP CAMPAIGNS Question in survey of call responded
st.title("TDP campaigns ")
TDP_camp_data  =  pd.DataFrame(respond_data['How many time have TDP people campaigned in your area?'].value_counts())
count_campof_TDP,Mandal_camp_TDP = st.beta_columns(2)
TDP_camp_data = TDP_camp_data.reset_index()
TDP_camp_data.columns = ['How many time have TDP people campaigned in your area?','count_campof_TDP']
#st.write(TDP_camp_data)
fig_TDP_camp = px.pie(TDP_camp_data,values = TDP_camp_data['count_campof_TDP'], names = TDP_camp_data['How many time have TDP people campaigned in your area?'])
#st.write(fig_TDP_camp)
st.plotly_chart(fig_TDP_camp)


#Pie chart for the YCP CAMPAIGNS Question in survey of call responded
st.title("YCP campaigns ")
YCP_camp_data = pd.DataFrame(respond_data['How many time have YCP people campaigned in your area?'].value_counts())
count_campof_YCP,Mandal_camp_YCP = st.beta_columns(2)
YCP_camp_data = YCP_camp_data.reset_index()
YCP_camp_data.columns = ['How many time have YCP people campaigned in your area?','count_campof_YCP']
#st.write(YCP_camp_data)
fig_YCP_camp = px.pie(YCP_camp_data,values=YCP_camp_data['count_campof_YCP'], names = YCP_camp_data['How many time have YCP people campaigned in your area?'])
#st.write(fig_YCP_camp)
st.plotly_chart(fig_YCP_camp)

    
#Pie chart for the VOTE FOR THE SAME PARTY Question in survey of call responded
st.title("vote for last time party")
vote_Sparty_data = pd.DataFrame(respond_data['Will you vote for the same party you voted for the last time?'].value_counts())
count_vote_Sparty,Mandal_Sparty = st.beta_columns(2)
vote_Sparty_data = vote_Sparty_data.reset_index()
vote_Sparty_data.columns = ['Will you vote for the same party you voted for the last time?','count_vote_Sparty']
#st.write(data)
fig_Sparty_vote = px.pie(vote_Sparty_data,values = vote_Sparty_data['count_vote_Sparty'], names = vote_Sparty_data['Will you vote for the same party you voted for the last time?'])
st.plotly_chart(fig_Sparty_vote)


#Pie chart for the WHOM WILL YOU VOTE Question in survey of call responded
st.title("whom will you vote ")
whom_vote_data = pd.DataFrame(respond_data['Whom will you vote in the upcoming Tirupati bypoll elections?'].value_counts())
count_whom_vote,Mandal_whom_vote = st.beta_columns(2)
whom_vote_data = whom_vote_data.reset_index()
whom_vote_data.columns = ['Whom will you vote in the upcoming Tirupati bypoll elections?','count_whom_vote']
#st.write(data)
fig_whom_to_vote = px.pie(whom_vote_data,values = whom_vote_data['count_whom_vote'], names = whom_vote_data['Whom will you vote in the upcoming Tirupati bypoll elections?'])
st.plotly_chart(fig_whom_to_vote)



# Table of Data which was used to plot the above Charts       
def get_table():
    datatable = Survey_data[['AC', 'Mandal', 'How many time have TDP people campaigned in your area?',
                    'How many time have YCP people campaigned in your area?',
                    'Will you vote for the same party you voted for the last time?',
                    'Whom will you vote in the upcoming Tirupati bypoll elections?']].sort_values(by=['AC'],ascending =True)
    return datatable

datatable = get_table()
st.markdown("***Data which was used for plot***")
st.dataframe(datatable)

