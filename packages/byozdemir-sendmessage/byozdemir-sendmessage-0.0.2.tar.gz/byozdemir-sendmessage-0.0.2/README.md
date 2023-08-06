# byozdemir-sendmessage

This is the library that you can send messages via telegram,discord and email. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install byozdemir-sendmessage.

```bash
pip install byozdemir-sendmessage
```

## Usage

```python
import byozdemir_sendmessage

# Returns 'provider which is you selected'
# You can select telegram,discord,mail,skype
messager = byozdemir_sendmessage.getProvider('discord',key="discord key here")

#Send Message
messager.sendMessage('receiver_id','This is a test message')

#Help. This method returns how to use the selected provider.
messager.help()

#TODO
```bash
signal
line
netgsm
```
