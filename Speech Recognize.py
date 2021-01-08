
# coding: utf-8

# In[35]:


import speech_recognition as sr


# In[36]:


engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ""

with mic as source:
    print("Silahkan Bicara..")
    rekaman = engine.listen(source)
    print("Waktu Selesai")
    
    try:
        hasil = engine.recognize_google(rekaman, language = "id-ID")
        print(hasil)
    except engine.UnknownValueError:
        print("Maaf tidak terdeteksi, Coba lagi")
    except Exeption as E:
        print(E)


# In[32]:


text_file = open("hasil.txt", "w")
text_file.write(hasil)
text_file.close()                 

