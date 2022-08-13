# bof_badchar_finder
Buffer Overflow - Bad Character Finder with Python 2

---

Firstly, run the application and 1_find_offset.py

```
python2 1_find_offset.py ip port len
```

Example: `python2 1_find_offset.py 127.0.0.1 1337 10000`

If the application crashed, then you can go to the chapter 2_get_offset!

If not, upper the length size like 10000 to 15000.

---

You don't need to run the application for get offset.

```
python2 2_find_offset.py len EIP
```

Example: `python2 2_find_offset.py 10000 23423889`

If EIP value is correct, offset will be printed.

---

Now, we know the offset, we can manipulate the EIP with the answer to life the universe and everything(42424242).

Re-run the application and start the script like below.

```
python2 3_correct_offset.py ip port offset
```

Example: `python2 3_correct_offset.py 127.0.0.1 1337 2306`

If the EIP value is 42424242 then our offset value is correct, we can find the badchars.

---

For finding badchars, firstly we can use the last script without any badchar.

```
python2 4_bad_chars_first.py ip port offset badchars?
```

Example: `python2 4_bad_chars_first.py 127.0.0.1 1337 2306`

Then we have to find each badchar by manually and we can re-use the script for the end.

Example: `python2 4_bad_chars_first.py 127.0.0.1 1337 2306 \x0a`

Example: `python2 4_bad_chars_first.py 127.0.0.1 1337 2306 \x0a \xb2`

Example: `python2 4_bad_chars_first.py 127.0.0.1 1337 2306 \x0a \xb2 \xd7`


After all, if there is not any badchar on Debugger, we found all.
