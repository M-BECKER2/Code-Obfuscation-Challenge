## Obfuscation Challenge Writeup
These challenges were created as a capstone project for my Malware Analysis and Response class.  Below is the submitted writeup.  

Please note that in Challenge 2, you start with the two images Ch2-cat1.jpg and ch2-cat2.jpg.  The challenge two code challenge_2.py is posted in case one is unable to extract the code from the image.
Secondly, Challenge 3 has an error that will prevent it from being solved.  For now, the flawed code will remain up, for any who wish to determine what the issue is.  And in my defense of this error, this code was written during my finals, sleep was not with me.   


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
![ch1-charcode](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/f7c3ae65-641f-4d55-8944-fb224c469218)

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
![ch1-password](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/2b655206-5e23-4c9b-8695-50ffbb1e60b2)

Let’s test our password to ensure we have the right password:

![ch1-correct](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/89a2d58c-fc5a-4e3e-89cb-0f13a69874d1)

Now we have our message, we have now completed challenge 1.

## Challenge 2:
For challenge 2, we have been given two images: ch2-cat1.jpg and ch-2cat2.jpg. 
![ch2-cat1](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/251257bc-0a5a-4a29-8be4-aab54370b40d)
![ch2-cat2](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/8bf4bef0-7a99-4151-b0bf-fd6fc86248e8)

One of these images has another file- challenge_2.py -embedded into it using Steganography.
Steganography is a method of hiding another file within another- commonly an image or audio
file.
Our goal is to extract the file and then solve it to complete the challenge.
If we try to extract the file without a passphrase, we will receive the error “could not extract
any data with that passphrase!” for both files.
![ch2 steghide fail](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/10253168-19b6-4c45-b18c-84a1b514fc63)

You won’t be able to determine which one by file size, as you do not know the size of the
original image, and stenography does not change the size of the image. Instead, let’s look
somewhere else: strings.
Command: strings <filename>

Strings can give us useful data such as exifdata or other hidden data within the image. In this
case, we found a string password=finally in cat1.jpg. Let’s try that and see if that’s our
passphrase.

![ch2-strings](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/35121335-20ec-4b14-b7a1-8aea627ce443)

Using steghide, or any other stegography tool of your choice, we can extract the file with the
passphrase finally, and we have challenge_2.py

![ch2 extract](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/54fd2034-4d93-42ca-99ff-fb2f4bc2b963)

![ch2 code](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/ed9da96a-d693-4704-a2b7-ed4fe65295e6)

To pass the challenge, we need to find the correct passphrase. Already in the if statement, we
can see that our input is compared to the variable nothing_important.
We can also see that we get the message “et tu, Brute?” if we don’t have the correct password.
It’s a hint for the encryption method used- as those were Caesar’s last words in the play Julius
Caesar. It looks like a type of Caesar cipher that has been used. On the Wikipedia page on the Caesar cipher, we can read that ROT13 is a “modern application” of the cipher, which is in
Cyberchef.

![ch2 rot13](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/e7b12aa7-7836-44ab-b0f6-e4f2e9576bd5)

However, we receive a gibberish string with ROT13. We can either use ROT13 brute force to
find a readable string, or we can take a closer look at the operation used.

![ch2 if statement](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/8ba77755-1ba2-47a9-8e8c-b9398a9112eb)

In Caesar ciphers, the plaintext (the text that will be encrypted) is substituted by x number of
letters to the right in the alphabet. If x = 3, then A becomes C, B becomes D, etc. In this, we can
see that +16 is applied to each letter: each letter is shifted over by 16. In cyberchef, let’s
change the amount. However, since we are decrypting it, we are subtracting 16, or going
backward through the alphabet, so it should be –16

![ch2 cyber 16](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/2d9b13d5-f711-478f-b556-35b6d2ae2535)

We have the password “itsnothalloween”, and if we run it through the program

![ch2 passed](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/982fba7e-ca7a-4bd5-aed2-f52ba3d0f4f6)


We received the “passed challenge 2” message and completed the challenge.

## Challenge 3:
After reviewing the code as I was preparing this for Github, I found that there was an issue in the code that prevented the challenge from being solved.  For now, the code will remained as it is, flawed and inccorect.  Any who come across this is free to try to find what the error could be, and one day this will be fixed.

## Challenge 4:
In challenge 4, we will be looking at some malware obfuscation techniques such as flow control
and dead code insertion. These techniques are used to confuse reverse engineers in
understanding the code execution.
In challenge 4, you have to find the secret that the program asks for, which is one of the four
variables (var1, var2, var3, and var4) at the top of the code to make life easier. However, there
are several functions of encryption processes already seen in the previous challenges, and one
of these functions contains the correct secret as well.
After opening the source code, you can see at the bottom several nested if statements.

![ch4 nested](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/1c5704b9-b090-48c5-aaa7-8d5052e4ed05)


If we input a random string, we can see we receive the message “This is not the correct secret”

![ch4 incorrect](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/77c5d6fa-9a26-46b2-b2ce-ee108b19aeb7)


Now if we look at the if statements, we can see one print statement that doesn’t say “this is not
the correct secret” but “This is the correct secret.” 

![ch4 correct sec](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/dba7ce80-64e7-4478-b058-5e5d37fb869f)

We can see that this only happens if userinput matches var2, which is “notthis.”

![ch4 correct answer](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/29d1f1a1-24c3-4ffe-88db-1e31d63c7057)

So we found the secret, but each encryption function also had a secret that was the same as
one of the varx variables, and we could find that function and the encoding/encryption scheme.
So let’s look further up to the above lines:

![ch4 code 1](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/62e37bb1-db14-488f-9a90-4a1667ed00d8)

We can see that base2 was called for userinput, and before that rot13 was executed. However,
another rot13 was executed 2 lines up, just before the if statement. ROT13, if done twice, will
return the original string after the second round, so base2 just encoded the plaintext userinput.
We can also see that var2, the correct secret, was encoded as well.
Let’s take a look at base2:

![ch4 code 2](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/039f417f-6b42-4753-a482-66d1cf81b46a)

We can see that the userinput is encoded with base64. If we use cyberchef to decode secret.

![ch4 final cyber](https://github.com/M-BECKER2/Code-Obfuscation-Challenge/assets/163598094/3bd2d5b0-ab6e-4d9a-82d3-87c64db9eaa0)

We can confirm that base64 is the encoding function used. Challenge 4 is completed.

That concludes this challenge.

