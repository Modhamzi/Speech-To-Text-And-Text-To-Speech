#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


pip install ibm_watson


# In[2]:


from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[3]:


apikey='1k1bvzTPHNz4We7u65Zi4vvzcRIlqDq2_GOE78VYW9L8'
url= 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/782301c7-993f-4c9a-90b9-72612c6731f8'


# In[12]:


authenticator=IAMAuthenticator(apikey)
stt=SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)


# In[23]:


with open('ee_126.mp3','rb') as f:
    res=stt.recognize(audio=f, content_type= 'audio/mp3', model='en-US_NarrowbandModel',continous=True).get_result()
    


# In[19]:


res


# In[21]:


text=res['results'][0]['alternatives'][0]['transcript']
text


# In[22]:


confidance=res['results'][0]['alternatives'][0]['confidance']
confidance


# In[ ]:


with open ('output.txt','w') as out:
    out.writelines(text)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




