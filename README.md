# Typing-Recognition
Biometry POC using keystroke dynamics.

---

## Generating samples
I'ts necessary to generate >=3 train samples for each user. Sample name must be userid_keystrokeid. Now, there are 4 users:

1. Me.
2. Me typing with 2 fingers.
3. Me typing randomly.
4. Me typing with 1 finger.

```python GenerateSamples.py userid_keystrokeid```

<img src="https://i.gyazo.com/e5acf1048f8f93ea695fdae9cf7649c2.gif"/>

---

## Authentication
After training, you can detect your keystroke pattern and authenticate.

```python Authenticate.py```

<img src="https://i.gyazo.com/9a4997e0fa1a9416969c07f61d2289ef.gif/>

