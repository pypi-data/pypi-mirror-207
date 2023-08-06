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
# You can select telegram,discord,mail
messager = byozdemir_sendmessage.getProvider('discord',key="discord key here")

#Send Message
messager.sendMessage('receiver_id','This is an test message')

