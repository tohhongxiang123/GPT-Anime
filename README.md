# Generating anime titles and synopses using GPT-2

### Collecting data
Using [jikan's](https://jikan.docs.apiary.io/#) api, 16142 different anime from 2000 - 2020 were collected. Then these data were used to train GPT-2

### Running
From the root directory,

#### Backend
```
cd server
pip install -r requirements.txt
python api/app.py
```
#### Frontend
```
cd client
npm install
npm run start
```

## Sample responses
### Wonder Garden EX

- Flash anime screened at AnimeJapan Grand Prix Tokyo this April. Episodes happen exclusively on Nico Nico, the official Japanese streaming website. A second trailer was released a day later which shows the Versus against ZONER team again on Niconico stage.

### Jinzou Kanbara to You Enki

- Based on a doujin game where a mysterious dragon swallows the player, using giant horns along the sides of his face. When they meet a high-school student, ryuichi, who leads Shigeo Nanaki's school entrance exams. He is created by Shigeo himself, and together they begin a battle with the high school student Hikaru.

### Popotan!!! Side 4

- With Narvi coming to terms with his pride and Bishory learning to clear his mental picture, Lillie is left second guessing herself as the man she is in hopes of finding a mythical girl named Popot. Now her normal life glitters away and among the students at her school lies a cute little hot redhead boy named Peepot who dreams of being an idol, and who even dreams about trying to kill his crush Megapot. Unfortunately when the danger in her life is right around the corner, she is run over and kidnapped by the nefarious Mi'an. Much to her surprise, her kidnappers are actually Popot, her friends have to be inspired by her, and she ends up fainted while doing the actual rescue work. With reluctant Aya and her partner Shinzo facing off against Mi'an and her wild best friends and rivals, Popot and Popotan must find that elusive "Popotapotan" and save her from grave kidnappers while keeping their support by keeping Mi'an and all her friends by his side.

Links
- https://medium.com/@ngwaifoong92/beginners-guide-to-retrain-gpt-2-117m-to-generate-custom-text-content-8bb5363d8b7f