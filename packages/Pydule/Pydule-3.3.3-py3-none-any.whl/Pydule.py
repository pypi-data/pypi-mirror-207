import datetime
import os
import tkinter as tk
import pyttsx3 

engine = pyttsx3.init() 

err='\n\U0000274C Something Went Wrong \U0000274C\n'

def openapp(appname):
	from AppOpener import open
	open(appname)

def resizeimg(size,path):
	from PIL import Image

	img = Image.open(path)

	img_resized = img.resize(size)

	fname="Pydule Resize Image -" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".png"

	img_resized.save(fname)

def GetWebHTML(url):
	import requests

	page = requests.get(url)

	return page.text

def screenshot(sec=0):
	import pyautogui
	import time as t
	import datetime

	t.sleep(sec)

	myScreenshot = pyautogui.screenshot()

	fname="Pydule Screen Shot -" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".png"

	myScreenshot.save(fname)

def SpeechtoText(string=''):
	if isinstance(string,str):
		import speech_recognition as sr

		r = sr.Recognizer()

		mic = sr.Microphone()

		with mic as source:
			print(string,end='')
			audio = r.listen(source)

		try:
			return r.recognize_google(audio)
		except:
			print(err)
	else:
		print(err)	    

def recintaudio(sec):
	if isinstance(sec,int):
		if sec>0:
			import soundcard as sc
			import soundfile as sf
			import datetime

			out = "Pydule Recorded Internel Audio -" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".wav"
			rate=48000

			with sc.get_microphone(id=str(sc.default_speaker().name),include_loopback=True).recorder(samplerate=rate) as mic:
				data=mic.record(numframes=rate*sec)
				sf.write(file=out,data=data[:,0],samplerate=rate)
		else:
			print(err)
	else:
		print(err)		

def recscreen():
	import pyautogui
	import cv2
	import numpy as np
	import datetime

	screen_size = pyautogui.size()

	filename = "Pydule Recorded Screen -" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".avi"

	fourcc = cv2.VideoWriter_fourcc(*"XVID")

	out = cv2.VideoWriter(filename, fourcc, 20.0, screen_size)

	cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)

	cv2.resizeWindow("Recording", 480, 270)

	while True:
		img = pyautogui.screenshot()

		frame = np.array(img)

		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		out.write(frame)

		cv2.imshow('Live', frame)

		if cv2.waitKey(1) == ord('q'):
			break

	out.release()
	cv2.destroyAllWindows()

def recmic(sec):
	import pyaudio
	import wave
	audio=pyaudio.PyAudio()
	stream=audio.open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=1024)
	frames=[]

	fn = "Pydule Recorded Microphone-" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".wav"
	for i in range(0,int(44100/1024*(sec+1))):
		data=stream.read(1024)
		frames.append(data)

	stream.stop_stream()
	stream.close()
	audio.terminate()

	sound_file=wave.open(fn,'wb')
	sound_file.setnchannels(1)
	sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
	sound_file.setframerate(44100) 
	sound_file.writeframes(b''.join(frames))
	sound_file.close()   

def mulmatrix(x,y):
	import numpy as np

	return np.dot(np.array(x), np.array(y))

def swapdict(d):
	if isinstance(d,dict):
		new={}
		for i in d:
			new[d.get(i)]=i
		return new
	else:
		print(err)

def sepstr(st,n):
	l,s=[],''
	for i in st:
		if len(s)!=n:
			s+=i
		else:
			l+=[s]
			s=''
			s+=i
	if len(s)>0:
		l+=[s]          
	return l 

def dcodestr(st,k):
	s,key='',{}
	if isinstance(st,str):
		for j in k:
			n=chr(k[j])
			key[j]=n
		sr=sepstr(st,7)
		for i in range(len(sr)):
			s+=key[sr[i]]
		return s
	else:
		print(err)    

def codestr(string):
	import random as r
	ex=['!','@','#','$','%','^','&','*','_','=','-','+']
	s,Ans,d,e='',[],{'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None, 'H': None, 'I': None, 'J': None, 'K': None, 'L': None, 'M': None, 'N': None, 'O': None, 'P': None, 'Q': None, 'R': None, 'S': None, 'T': None, 'U': None, 'V': None, 'W': None, 'X': None, 'Y': None, 'Z': None, 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None, 'j': None, 'k': None, 'l': None, 'm': None, 'n': None, 'o': None, 'p': None, 'q': None, 'r': None, 's': None, 't': None, 'u': None, 'v': None, 'w': None, 'x': None, 'y': None, 'z': None,'1':None,'2':None,'3':None,'4':None,'5':None,'6':None,'7':None,'8':None,'9':None,'0':None,'!':None,'@':None,'#':None,'$':None,'%':None,'^':None,'&':None,'*':None,'_':None,'=':None,'-':None,'+':None,'(':None,')':None,'[':None,']':None,'`':None,'~':None,'{':None,'}':None,'?':None,'\\':None,'\'':None,'/':None,';':None,':':None,'\"':None,'<':None,'>':None,'.':None,',':None,' ':None},{}
	while True:
		if len(Ans)!=95:
			n=''
			for i in range(7):
				n+=ex[r.randint(0,11)]
			if n not in Ans:
				Ans+=[n]
		else:
			break
	for i,j in zip(d,Ans):
		d[i]=j

	for i in string:
		s+=d[i]

	for i in d:
		n=ord(i)
		e[n]=d[i]

	return s,e

def ChatGPT(prompt,api_key,engine="text-davinci-003",max_tokens=1024,temperature=0.7):
	import openai

	openai.api_key = api_key

	completions = openai.Completion.create(engine=engine,prompt=prompt,max_tokens=max_tokens,n=1,stop=None,temperature=temperature)

	return completions.choices[0].text.strip()

def wjson(data,path):
	import json

	with open(path,'w') as json_file:
		json.dump(data,json_file)

def askfile():
	from tkinter.filedialog import askopenfilename

	filepath = askopenfilename()

	return filepath

def delfile(filename):
	if isinstance(filename,str):
		if filename=='askfile':
			import os
			from tkinter.filedialog import askopenfilename
			
			filename = askopenfilename()
			os.remove(filename)

		else:	
			import os

			os.remove(filename)
	else:
		print(err)

def deljsonele(path):
	import json

	jsonfile=json.load(open(path))
	copy=jsonfile.copy()

	k=eval(input('Enter the Key : '))

	del copy[k]

	with open(path,'w') as json_file:
		json.dump(copy,json_file)	

def upjson(path):
	import json
	jsonfile=json.load(open(path))
	copy=jsonfile.copy()

	k=eval(input('Enter the Key : '))
	v=eval(input('Enter the Value : '))
	copy[k]=v

	with open(path,'w') as json_file:
		json.dump(copy,json_file)

def num(n):
	if isinstance(n,int):
		if str(n).endswith('1') and not(str(n).endswith('11')):
			s=str(n)+'st'
		elif str(n).endswith('2') and not(str(n).endswith('12')):
			s=str(n)+'nd'
		elif str(n).endswith('3') and not(str(n).endswith('13')):
			s=str(n)+'rd'        
		else:
			s=str(n)+'th'
		return s 
	else:
		print(err)	
def intuple(x,index,element):
	if isinstance(x,tuple):
		new=()
		if len(x)<=index:
			new+=x+(element,)
		else:	
			for i,j in zip(range(len(x)),x):
				if i==index:
					new+=(element,)+(j,)
				else:
					new+=(j,)
		return new	
	else:
		print(err)

def instr(x,index,element):
	if isinstance(x,str):
		new=''
		if len(x)<=index:
			new+=x+element
		else:	
			for i,j in zip(range(len(x)),x):
				if i==index:
					new+=element+j
				else:
					new+=j
		return new
	else:
		print(err)			

def askfolder():
	from tkinter import filedialog

	folder = filedialog.askdirectory()

	return folder

def msgbox(type,title='Pydule',text='YOUR TEXT HERE'):
	if isinstance(type,str) and isinstance(title,str) and isinstance(text,str):
		from tkinter import messagebox
		if type=='info':
			return messagebox.showinfo(title,text)
		elif type=='error':
			return messagebox.showerror(title,text)
		elif type=='warning':
			return messagebox.showwarning(title,text)
		elif type=='question':
			return messagebox.askquestion(title,text)
		elif type=='okcancel':
			return messagebox.askokcancel(title,text)
		elif type=='retrycancel':
			return messagebox.askretrycancel(title,text)
		elif type=='yesno':
			return messagebox.askyesno(title,text)
		elif type=='yesnocancel':
			return messagebox.askyesnocancel(title,text)							
		else:
			print(err)
	else:
		print(err)			

def functions():
	def lower(s):
		return s.lower()
	l=['msgbox(<type>,<title>,<text>)','askfolder()','askfile()','delfile(<filename>)','resizeimg(<size>,<path>)','GetWebHTML(<url>)','TrackLocation(<phone_number>)','num(<numbers>)','screenshot(<seconds>)','SpeechtoText(<str>)','ChatGPT(<content>,<api>)','recintaudio(<seconds>)','recmic(<seconds>)','recscreen()','mulmatrix(<matrix a>,<matrix b>)','codestr(<str>)','dcodestr(<str>,<dict>)','swapdict(<dict>)','sepstr(<str>)','wjson(<dict>,<path>)','deljsonele(<path>)','upjson(<path>)','copytext(<text_to_copy>)','translate(<sentence>,<language>)','cqrcode(<link>)','summatrix(<matrix a>,<matrix b>)','submatrix(<matrix a>,<matrix b>)','intuple(<tuple>,<index>,<new_element>)','instr(<str>,<index>,<new_element>)','reSet(<old_set>,<new_element>,<old_element>)','reStr(<old_str>,<index>,<new_str>)','reDict(<old_dict>,<old_key>,<new_key>)','reList(<old_list>,<index>,<new_element>)','reTuple(<old_tuple>,<index>,<new_element>)','clist(<length_of_the_list>)','ctuple(<length_of_the_tuple>)','cdict(<length_of_the_dict>)','cset(<length_of_the_set>)','pickcolor()','search(<content>)','playmusic(<path>)','restart_system()','shutdown_system()','datetoday()','timenow()','say(<content>)','openfile(<path>)','weathernow(<city_name>)','setvoice(<number>)','voicerate(<any_number>)']
	l1=list(map(lower,l))
	l2,final=l1.copy(),[]
	l1.sort()
	for i in range(len(l)):
		for j in range(len(l)):
			if l1[i]==l2[j]:
				final.append(l[j])

	print('Available Functions : \n')

	for i in range(len(l)):
		print(f'\t{i+1}.{final[i]}')

def summatrix(x,y):
	import numpy as np
	result = np.array(x) + np.array(y)
	
	return result

def submatrix(x,y):
	import numpy as np
	result = np.array(x) - np.array(y)

	return result

def reDict(x,oele,nele):
	if isinstance(x,dict):
		new={}
		for i in x:
			if i==oele:
				new[nele]=x.get(i)
			else:
				new[i]=x.get(i)
		return new		
	else:
		print(err)

def translate(content,language):
	from deep_translator import GoogleTranslator
	translated = GoogleTranslator(source='auto', target=language.lower()).translate(content)
	return translated
	
def cqrcode(data,filename):
	import qrcode

	img = qrcode.make(data)

	img.save(filename)
	print('\nQrcode Saved Successfully \U00002714\n')
	
def Author():
	print('\nThis Pydule is Created by D.Tamil Mutharasan \U0001F608\n')

def reStr(oldstr,index,newstr):
	if isinstance(oldstr,str):
		new=''
		for i in range(len(oldstr)):
			if i==index:
				new+=newstr
			else:
				new+=oldstr[i]
		return new
	else:
		print(err)	

def reSet(oldset,element,newelement):
	if isinstance(oldset,set):
		new=set()
		for i in oldset:
			if i==element:
				new.add(newelement)
			else:
				new.add(i)
		return new				
	else:
		print(err)	

def reList(oldlist,index,newlist):
	if isinstance(oldlist,list):
		new=[]
		for i in range(len(oldlist)):
			if i==index:
				new+=[newlist]
			else:
				new+=[oldlist[i]]
		return new
	else:
		print(err)	

def reTuple(oldtup,index,newtup):
	if isinstance(oldtup,tuple):
		new=tuple()
		for i in range(len(oldtup)):
			if i==index:
				new+=(newtup,)
			else:
				new+=(oldtup[i],)
		return new
	else:
		print(err)	

def clist(mx):
	if isinstance(mx,int):
		List=[]
		print('Enter Values One by One \U0001F447\n')
		for i in range(mx):
			l=eval(input(f'Enter {num(i+1)} Value :'))
			List.append(l)
		print('\nList Created Successfully \U00002714')
		return List
	else:
		print(err)	

def ctuple(mx):
	if isinstance(mx,int):
		Tuple=()
		print('Enter Values One by One \U0001F447\n')
		for i in range(mx):
			t=eval(input(f'Enter {num(i+1)} Value :'))
			Tuple+=(t,)
		print('\nTuple Created Successfully \U00002714')
		return Tuple
	else:
		print(err)

def cdict(mx):
	if isinstance(mx,int):
		Dict={}
		print('Enter Values One by One \U0001F447\n')
		for i in range(mx):
			key=eval(input(f'Enter the Key of No.{num(i+1)} Element :'))
			value=eval(input(f'Enter the Value of {key} Element :'))
			print()
			Dict[key]=value
		print('Dictionary Created Successfully \U00002714')	
		return Dict
	else:
		print(err)	

def cset(mx):
	if isinstance(mx,int):
		Set=set()
		print('Enter Values One by One \U0001F447\n')
		for i in range(mx):
			s=eval(input(f'Enter {num(i+1)} Values : '))
			Set.add(s)
		print('\nSet Created Successfully \U00002714')	
		return Set
	else:
		print(err)	

def copytext(string):
	import pyperclip
	pyperclip.copy(string)

def pickcolor():
	from tkinter import colorchooser
	c=colorchooser.askcolor(title='Pydule Color Picker \U00002714')
	copytext('\''+str(c[-1])+'\'')
	print(f'Choosen Color ({c[-1]}) is Copied \U00002714')
	
def search(content):
	import pywhatkit as kt
	kt.search(content)	
	print('\nSearching \U0001F50E...\n')		
	
def playmusic(path):
	if isinstance(path,str):
		if path=='askfile':
			import os
			from tkinter.filedialog import askopenfilename
			import time
			import pyglet

			filename = askopenfilename()

			media_player = pyglet.media.Player()

			song = pyglet.media.load(filename)

			media_player.queue(song)

			media_player.play()

			time.sleep(song.duration)

			media_player.pause()
		else:
			import os
			from tkinter.filedialog import askopenfilename
			import time
			import pyglet

			media_player = pyglet.media.Player()

			song = pyglet.media.load(path)

			media_player.queue(song)

			media_player.play()

			time.sleep(song.duration)

			media_player.pause()
	else:
		print(err)

def restart_system():
	print('\nRestarting the System \U0001F4BB...\n')		
	os.system("shutdown /r /t 1")
	
def shutdown_system():
	print('\nShutting Down Your System \U0001F4BB...\n')
	return os.system("shutdown /s /t 1")
	
def datetoday():
	from datetime import date
	d=date.today()
	return d
	
def timenow():
	from datetime import datetime
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S %p")
	return current_time
	
def say(content,save=False):
	if isinstance(content,str):	
		engine.say(content)
		if save==True:
			engine.save_to_file(text=content,filename=content+'.mp3')
		engine.runAndWait()  
	else:
		print(err)

def openfile(path):
	if isinstance(path,str):	
		if path=='askfile':
			from tkinter import filedialog
			filename = filedialog.askopenfilename()
			os.startfile(filename)
		else:	
			os.startfile(path)
	else:
		print(err)		

def weathernow(place):
	if isinstance(place,str):
		import requests
		from bs4 import BeautifulSoup
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

		def weather(city,place):
			city = city.replace(" ", "+")
			res = requests.get(
				f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
			soup = BeautifulSoup(res.text, 'html.parser')
			time = soup.select('#wob_dts')[0].getText().strip()
			info = soup.select('#wob_dc')[0].getText().strip()
			weather = soup.select('#wob_tm')[0].getText().strip()
			details=['City Name : '+place,info,weather+'°C']
			return details
		city = place+" weather"
		return weather(city,place)
	else:
		print(err)	

def TrackLocation(string):
	if isinstance(string,str) and len(string)==13:
		import phonenumbers
		from phonenumbers import geocoder

		number = phonenumbers.parse(string)

		location = geocoder.description_for_number(number, "en")

		return location
	else:
		print(err)	

def setvoice(num):
	if isinstance(num,int):
		voices=engine.getProperty('voices')
		engine.setProperty('voice',voices[num].id)	
	else:
		print(err)	

def voicerate(num):
	if isinstance(num,int):
		engine.setProperty('rate',num)
	else:
		print(err)	