import textwrap
original='abcdefghijklmnopqrstuvwxyz'
wrapper=textwrap.TextWrapper(width=4)
shortened = textwrap.shorten(text=original, width=100) 
shortened_wrapped = wrapper.fill(text=shortened)
print(shortened_wrapped)