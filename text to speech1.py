#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install ibm_watson


# In[2]:


pip install ibm_cloud_sdk_core

 from ibm_watson import TextToSpeechV1
# In[4]:


from ibm_cloud_sdk_core.authenticators import AIMAuthenticator


# In[6]:


api=AIMAuthenticator("wrOlx2vIgPHKa2OCeU-tI0YrUKRi1mEZaMG9H9v1Rab")


# In[11]:


text_2_speech=TextToSpeechV1(authenticator=api)


# In[ ]:


text_2_speech.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/d858c51d-460f-41c4-9775-4e58bf1eb730")


# In[13]:


with open ("first test","wb") as audiofile:
    audiofile.write(
    text_2_speech.synthesize("I Love IBM Watsron to learn more and More",
                            accept="audio.mp3").get_result().content
    )


# In[ ]:




