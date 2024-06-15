#!/usr/bin/env python3

from pwn import *

if args.DOCKER:
    p = remote('localhost', 1337)
elif args.REMOTE:
    p = remote('localhost', 1337)
else:
    p = process(['./game.py'])

p.sendlineafter(b'(y/n) > ', b'yes')

for i in range(1000):
    p.recvuntil(b'What is ')
    todo = p.recvuntil(b'?')
    todo = todo[:-1]
    todo = todo.split()
    x, y = int(todo[0]), int(todo[2])
    result = x+y 
    p.sendline(str(result).encode())

p.interactive()

