# Quickstart
## Installation (if you want to change the settings)
```
pip3 install pyyaml
git clone git@github.com:the-real-finnventor/insult.git
echo alias insult-path="$PWD"/insult/insult >> ~/.zprofile
echo alias insult="python3 insult-path" >> ~/.
```

If you are getting errors like:
```
Cloning into 'insult'...
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

Then try:
```
git clone https://github.com/the-real-finnventor/insult.git
echo alias insult-path="$PWD"/insult/insult >> ~/.zprofile
echo alias insult="python3 insult-path" >> ~/.
```

## Installation (if you don't care about the settings)
```
pip3 install finnsult
open ~/.zprofile
```

Now find `${PATH}`. Put your cursor before that and paste this: `/Users/INSERT_YOUR_USERNAME_HERE/Library/Python/3.9/bin:`. Then replace `INSERT_YOUR_USERNAME_HERE` with your username (eg. finneverspaugh). If you are unsure of you username at any time in the terminal (unless the terminal is activly doing something) it should say `username@computername`.

## Run (at any time open a terminal and run)
```
insult
```

# DISCLAIMER: 
If you use pypi to install this package, -u (or --update) will not work.