## Obfuscation Challenge Writeup
These challenges were created as a capstone project for my Malware Analysis and Response class.  Below is the subbmitted writeup (which needs to be better edited at a later date).  

Please note that in Challenge 2, you start with the two images Ch2-cat1.jpg and ch2-cat2.jpg.  The challenge two code challenge_2.py is posted in case one is unable to extract the code from the image.  
Edit note: add picture by drag and dropping

## Challenge 1:

To start, we can cat challenge_1.py and look at the code.
![challenge 1](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/7e3f8b49-15a4-45e3-ba65-c5d1d710e47d)

For challenge 1, the goal is to find the correct password that will give us the message: “correct, you have completed challenge 1”.
Looking at the challenge_1.py code, we can see four encoded strings at in the first lines of the
file. It’s likely that one of the strings contains the passcode, so let's look at the rest of the code
to figure how to decode it. 

We can see that the file calls for base64 in the first line, a binary-to-text encoding scheme; this
matches with the string format. So our next step is to decode the base64 string, and we can do
this with Cyberchef (https://gchq.github.io/CyberChef/)
Cyberchef is called the “Swiss Army knife”, and allows you both encode, decode, encrypt and
decrypt strings, along with additional functions useful for IT purposes. For this challenge, we’re
going to use From Base64 from options on the side menu.
![base64-ch1](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/0bcd2f71-1a5b-497f-b0e2-5c5110f147ca)

From carrot, we decode the string to read: 104,101,108,108,111,44,32,116,104,101,32,34.
Right now, that’s not very useful, as it will give us the “incorrect, please try again” error.
So let’s look at the code.
After we give the code our input, it runs the user_input through
num = ','.join(str(ord(c)) for c in user_input)
The command ord gives us the Unicode number of the letter. So, the input is reformatted into
decimal before being encoded.
Using carrot, let’s go back to cyberchef, and this time we’ll also use the function from charcode:

After changing the delimiter to comma and the base to 10 (decimal is base 10) we have the
output of:
hello, the "
Now we know the encoding scheme, we can find the password.
If we look at the if statement below, we can see the encoded strings concatted together and
compared to the user_input. We can also see that two variables, bean and beans do not match
like the other variables do. In fact, beans contains the user input given, so we can deduce that
bean contains the password.

Taking the string in the bean variable and putting into our cyberchef recipe, we find the
password cant_catch_me 

Let’s test our password to ensure we have the right password:

Now we have our message, we have now completed challenge 1.

## Challenge 2:
For challenge 2, we have been given two images: ch2-cat1.jpg and ch-2cat2.jpg. 
One of these images has another file- challenge_2.py -embedded into it using Steganography.
Steganography is a method of hiding another file within another- commonly an image or audio
file.
Our goal is to extract the file and then solve it to complete the challenge.
If we try to extract the file without a passphrase, we will receive the error “could not extract
any data with that passphrase!” for both files.
You won’t be able to determine which one by file size, as you do not know the size of the
original image, and stenography does not change the size of the image. Instead, let’s look
somewhere else: strings.
Command: strings <filename>

Strings can give us useful data such as exifdata or other hidden data within the image. In this
case, we found a string password=finally in cat1.jpg. Let’s try that and see if that’s our
passphase.

Using steghide, or any other stegography tool of your choice, we can extract the file with the
passphrase finally, and we have challenge_2.py

To pass the challenge, we need to find the correct passphrase. Already in the if statement, we
can see that our input is compared to the variable nothing_important.
We can also see that we get the message “et tu, Brute?” if we don’t have the correct password.
It’s a hint for the encryption method used- as those were Caesar’s last words in the play Julius
Caesar. It looks like a type of Caesar cipher that has been used. On the Wikipedia page on the Caesar cipher, we can read that ROT13 is a “modern application” of the cipher, which is in
Cyberchef. 

However, we receive a gibberish string with ROT13. We can either use ROT13 brute force to
find a readable string, or we can take a closer look at the operation used.

In Caesar ciphers, the plaintext (the text that will be encrypted) is substituted by x number of
letters to the right in the alphabet. If x = 3, then A becomes C, B becomes D, etc. In this, we can
see that +16 is applied to each letter: each letter is shifted over by 16. In cyberchef, let’s
change the amount. However, since we are decrypting it, we are subtracting 16, or going
backward through the alphabet, so it should be –16

We have the password “itsnothalloween”, and if we run it through the program

We received the “passed challenge 2” message and completed the challenge.

## Challenge 3:
In challenge 3, when we cat the file, we see this:

This is morse code, something we’re probably familiar with from spy movies where people tap
out messages to each other or tried to learn with flashlights to communicate. However,
Microsoft report that morse code is also being used by malware creators to hide links to
JavaScript files (https://www.microsoft.com/en-us/security/blog/2021/08/12/attackers-usemorse-code-other-encryption-methods-in-evasive-phishing-campaign/ ).
Luckily, we don’t need to worry about the variable AlphaToMorse to decrypt the file- we can
also use CyberChef to decrypt it. 

Let’s reformat this so it’s easier to read

We can see that in the print function, we’re given an encrypted phrase
gocf`&/~gc|*fy/~go/lckh*ie}*lbnfcoamj*< for us to solve.
We are given three pieces of information, the variable cat, and two definitions- tobinary and
crossed. We can see that crossed calls for cat and a, and uses ^.
With some not so easy googling (sorry about that), we found that ^ is the bitwise XOR. XOR is a
logical operation where it takes two inputs and determines if the input differs or not, and then
determines if it is true or false. If we consider values A and B- if we XOR them, it will always be
true. If XOR A with A and B with B, we will always output false. The XOR cipher is built on this
principle.
We can see that in the print function, we’re given an encrypted phrase
gocf`&/~gc|*fy/~go/lckh*ie}*lbnfcoamj*< for us to solve.
We are given three pieces of information, the variable cat, and two definitions- tobinary and
crossed. We can see that crossed calls for cat and a, and uses ^.
With some not so easy googling (sorry about that), we found that ^ is the bitwise XOR. XOR is a
logical operation where it takes two inputs and determines if the input differs or not, and then
determines if it is true or false. If we consider values A and B- if we XOR them, it will always be
true. If XOR A with A and B with B, we will always output false. The XOR cipher is built on this
principle.

With strings, it is converted into binary and then compared to the other binary, and all bits of
the string will either be one or zero after. So if we take 01000111 and XOR it with 01001000,
we get 00001111. If we have two 0s and two 1s, it is zero. If we have one of each, it is 1.
For our key, we can take the value of cat (final) which serves as the key in crossed. With it, we
find our solution: hello, this is the flag for challenge 3. 

Challenge 3 is now completed.

## Challenge 4:
In challenge 4, we will be looking at some malware obfuscation techniques such as flow control
and dead code insertion. These techniques are used to confuse reverse engineers in
understanding the code execution.
In challenge 4, you have to find the secret that the program asks for, which is one of the four
variables (var1, var2, var3, and var4) at the top of the code to make life easier. However, there
are several functions of encryption processes already seen in the previous challenges, and one
of these functions contains the correct secret as well.
After opening the source code, you can see at the bottom several nested if statements.

If we input a random string, we can see we receive the message “This is not the correct secert”
(With secret incorrectly spelled, of course).

Now if we look at the if statements, we can see one print statement that doesn’t say “this is not
the correct secert” but “This is the correct secert.” 

We can see that this only happens if userinput matches var2, which is “notthis.”

So we found the secret, but each encryption function also had a secret that was the same as
one of the varx variables, and we could find that function and the encoding/encryption scheme.
So let’s look further up to the above lines:

We can see that base2 was called for userinput, and before that rot13 was executed. However,
another rot13 was executed 2 lines up, just before the if statement. ROT13, if done twice, will
return the original string after the second round, so base2 just encoded the plaintext userinput.
We can also see that var2, the correct secret, was encoded as well.
Let’s take a look at base2:

We can see that the userinput is encoded with base64. If we use cyberchef to decode secert (again,
spelt wrong)

We can confirm that base64 is the encoding function used. Challenge 4 is completed.
A piece of malware can employ multiple techniques demonstrated in these challenges in order to avoid
detection. While the challenges present a basic execution of these techniques, in a blue team position
or in malware research, eventually one will encounter these encoding and encryption algorithms and be
able to understand and reverse or work around any obfuscation present. 

