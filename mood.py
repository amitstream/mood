import streamlit as st
import requests
import json
def get_prediction(data={"sentence":"Hello"}):
  url = 'https://askai.aiclub.world/ead40b87-2dde-4e84-bd56-6834d5e57489'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  #print(response)
  return response


def runOne():
  title = st.text_input('How are you doing?', 'I am so happy!!')
  myData={"sentence":title}
  r=get_prediction(myData)
  j=json.loads(r)
  b=j["body"]
  j2=json.loads(b)
  p=j2["predicted_label"]
  st.title(p)

runOne()
