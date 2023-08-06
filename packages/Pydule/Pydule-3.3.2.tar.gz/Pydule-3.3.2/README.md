# Pydule-TM

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.6](https://img.shields.io/badge/python-3.10.7-blue.svg)](https://www.python.org/downloads/release/python-3107/)   

## Functionality of Pydule

- Access ChatGPT
- Encode and Decode a String
- Record Screen,Internal Audio and Microphone
- Seperate String
- Swap Dictionary's Key to Values and Values to Key
- Insert Elements in Tuple & String
- Generate Qrcode
- Copy Text
- Text Translation
- Edit JSON Files
- Replace Letters in String
- Replace Elements in List and Tuple
- Check Weather of any City
- Open any File
- Play Songs
- Get Hex of a any Color
- Convert Text to Speech
- Restart or Shutdown Your System
- Search on Browser

## Usage

- Make sure you have Python installed in your system.
- Run Following command in the CMD.
 ```
  pip install Pydule
  ```
## Example

 ```
# test.py
import Pydule as py

# to Search 
py.search('Youtube')

# to Swap Dictionary
d={1:2,2:3,3:4}
print(py.swapdict(d))

# to Encode String
string,Key=py.codestr('Hello World')

# to Code the String
x,y=py.codestr('Hi') #This Converts Hi to @^&-+*^+^=##&*

# to Decode the String
print(py.dcodestr(x,py.swapdict(y)))

# to Decode String
print(py.dcodestr(string,swapdict(key)))

# to Create Qrcode
text,filename='Hello World','Hello.png'
py.cqrcode(text,filename)

# to Get all Available Functions
py.functions() 

# to Open Calculator
py.openapp('calculator')

# to Copy Text
py.copytext('Hello World')

# to Access ChatGPT
print(py.ChatGPT('Hi There','Your API Key'))
  ```