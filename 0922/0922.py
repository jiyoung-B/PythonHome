#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('ls')


# In[2]:


get_ipython().system('cat test.d')


# In[3]:


get_ipython().system('cat test.dat')


# In[8]:


fread = None
try :
    fread = open('test.dat', 'r')
except :
    print('File Not Foud')
finally :
    fread.close()


# In[14]:


fread = None
try :
    fread = open('test.dat', 'r')
    #result = fread.read()
    #result = fread.readline() # 초기값
    #while result :
    #    print(result, end='')
    #    result = fread.readline()
    for line in fread.readlines() :
        print(line, end='')
except :
    print('File Not Foud')
finally :
    fread.close()


# In[20]:


poet = """
죽는 날까지 하늘을 우르러
한점 부끄럼이 없기를、
잎새에 이는 바람에도
나는 괴로워했다。
별을 노래하는 마음으로
모든 죽어가는것을 사랑해야지
그리고 나한테 주어진 길을
거러가야겠다。

오늘밤에도 별이 바람에 스치운다。
"""


# In[21]:


fwrite = None
try :
    fwrite = open('서시.txt', 'w')
    fwrite.write(poet)
    print("File Save Successfully.")
except Exception as err:
    print('File Not Found')
    print(err)
    # Not Found 일 경우는 잘 없어
    # 보통 디스크 용량, 권한 문제 발생 가능
finally :
    fwrite.close()



# In[25]:


with open('서시.txt', 'r') as fread :
    try :
        count = 1
        for line in fread.readlines() : 
        # readlines는 리스트를 리턴한다.
            print(f'{count} : {line}', end='')
            count += 1
    except :
        print('File Not Found')


# In[98]:


import json


# In[31]:


list_ = ['Hello, world', 5, True, 89.5]
type(list_)


# In[33]:


str_ = json.dumps(list_)
type(str_)


# In[34]:


print(str_)


# In[36]:


obj = json.loads(str_)
type(obj)


# In[37]:


obj[2]


# In[39]:


student = {
    "hakbun" : "2023-003",
    "name" : "한지민",
    "age" : 24,
    "address" : "서울시 강남구 역삼동"
}
type(student)


# In[62]:


str_ = json.dumps(student, ensure_ascii=False, indent='\t')
print(type(str_))
print(str_)


# In[44]:


with open('student.dat', 'wt') as fwrite :
    fwrite.write(str_)
    print("File Save Successfully.")


# In[ ]:





# In[ ]:





# In[99]:


with open('student.dat', "rt") as fread :
    result = fread.read()
    #print(type(result))
    obj = json.loads(result)
    #print(type(obj))
    print(f"name = {obj['name']}, age = {obj['age']}")


# In[97]:


with open('student.dat', "rt") as fread :
    result = fread.read()
    obj = json.loads(result)
    print(type(obj))
    print(obj)
    print(f"name = {obj['name']}, age = {obj['age']}")


# In[56]:


with open('sungjuk.json', 'rt') as fread :
    result = json.load(fread) # load = read() -> loads()
    #print(type(result)) # list
    #print(len(result)) #12
    #print(type(result[0])) # dict
    print(result[0]['irum'])


# In[63]:


import os
print(os.name)


# In[65]:


print(os.getcwd())


# In[64]:


get_ipython().system('pwd')


# In[66]:


os.chdir('/')
print(os.getcwd())


# In[71]:


import sys


# In[72]:


print(f"Version : {sys.version}")
print(f"Version Info : {sys.version_info}")
print(f"Platform : {sys.platform}")


# In[74]:


import platform


# In[75]:


print(f"OS name : {platform.system()}")


# In[76]:


print(f"OS name : {platform.uname()}")


# In[77]:


import socket


# In[78]:


print(f"Host name : {socket.gethostname()}")


# In[79]:


hostname = socket.gethostname()
print(socket.gethostbyname(hostname))


# In[80]:


print(socket.gethostbyname('www.google.com'))


# In[81]:


os.chdir("/home/ubuntu")
print(os.getcwd())

#print(os.system("date"))
import subprocess
# In[85]:


import subprocess
print(subprocess.run(["ls", "-a"]))


# In[86]:


get_ipython().system('pip list')


# In[87]:


get_ipython().system('pip install pymysql')


# In[100]:


get_ipython().system('pip install nbconvert')


# In[105]:


get_ipython().system('jupyter nbconvert --to script 0922.ipynb')


# In[103]:


os.getcwd()

