import os
from flask import Flask, render_template_string, url_for

app = Flask(__name__, static_folder="static")

HER_NAME = "Mrs Naaz"
YOUR_NAME = "Naaz's Birthday"

BIRTHDAY_MESSAGE = """Happy Birthday, my sweetest Mrs Naaz! 💗

You make ordinary days feel special just by being in them. If I could give
you one thing today, it would be the ability to see yourself through my eyes,
so you could understand just how special you are to me.

I hope this new chapter brings you happiness, peaceful days, exciting dreams,
and countless reasons to smile. Thank you for being you and for making so
many ordinary moments feel unforgettable.

I made this little corner of the internet just for you, with all my love.
Happy Birthday, my love. You deserve all the beautiful things in life. 💖"""

CAPTIONS = [
    ("My favorite person", "Every moment with you becomes a memory I want to keep. 💗"),
    ("Us, always", "My favorite place is wherever I get to be with you. 🫶"),
    ("A little piece of forever", "If I could relive a moment, I'd choose one with you. ✨"),
    ("My happy place", "You make my world softer, brighter, and sweeter. 🌷"),
    ("Just you and me", "Some memories are little treasures I keep close to my heart. 💌"),
    ("My favorite smile", "I hope I get to see this smile a million more times. ❤️"),
]
ALLOWED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".gif")

PAGE = r"""
<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Happy Birthday, {{ her_name }} 💗</title><meta name="theme-color" content="#fff0f6">
<style>
:root{--pink:#f45f9a;--deep:#963d6d;--ink:#63374f}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;color:var(--ink);font-family:Georgia,"Times New Roman",serif;background:linear-gradient(145deg,#fff6fa,#ffe0ed 48%,#f0e6ff);overflow-x:hidden}
.glow{position:fixed;width:270px;height:270px;border-radius:50%;filter:blur(75px);opacity:.35;z-index:-1;pointer-events:none;background:#ff83b4;top:7%;left:-100px}.glow.two{background:#b8a0ff;top:58%;left:auto;right:-100px}
.wrap{width:min(100% - 34px,1000px);margin:auto}nav{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:22px 0;font:700 .82rem Arial,sans-serif;color:var(--deep);letter-spacing:.08em}.pill{border:1px solid #f4b2ce;background:#ffffffb8;border-radius:999px;padding:10px 13px;letter-spacing:0;font-weight:500}
.hero{min-height:75vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:25px 0 55px}.eyebrow{text-transform:uppercase;letter-spacing:.22em;font:700 .73rem Arial,sans-serif;color:#b24e7d}
h1{font-size:clamp(2.8rem,9vw,6.4rem);line-height:.98;margin:22px 0;letter-spacing:-.05em;color:#923765}h1 span{display:block;color:#ec639b;font-style:italic;font-weight:400;margin-top:10px}
.sub{font:1.02rem/1.85 Arial,sans-serif;max-width:620px;color:#80546d}.heart{font-size:2.1rem;display:inline-block;animation:beat 1.25s infinite;margin:10px}@keyframes beat{0%,100%{transform:scale(1)}50%{transform:scale(1.18)}}
.btn{cursor:pointer;border:0;border-radius:999px;padding:14px 22px;background:linear-gradient(100deg,#f45b98,#bb68d8);color:white;font:700 .94rem Arial,sans-serif;box-shadow:0 12px 28px #d65d9b42}
section{padding:42px 0}.title{text-align:center;font-size:clamp(2rem,5vw,3.15rem);margin:0 0 12px;color:#913c6b}.section-sub{text-align:center;font:.94rem/1.75 Arial,sans-serif;color:#80546d;margin:0 auto 30px;max-width:650px}
.gallery{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;align-items:start}.polaroid{min-width:0;background:#fffdfb;padding:11px 11px 18px;box-shadow:0 12px 28px #713b5a26;transform:rotate(var(--tilt));transition:transform .25s;border-radius:3px}.polaroid:hover{transform:rotate(0deg) translateY(-5px)}
.photo,.placeholder{width:100%;aspect-ratio:4/4.6;display:block;object-fit:cover;background:linear-gradient(145deg,#ffd0e2,#e7d8ff)}.placeholder{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:16px;color:#8b4a70;font:.88rem/1.6 Arial,sans-serif}.placeholder span{font-size:2rem;margin-bottom:9px}
.caption-title{text-align:center;font-size:1.1rem;color:#913c6b;margin:13px 4px 5px}.caption-text{text-align:center;font:.83rem/1.5 Arial,sans-serif;color:#80546d;margin:0 5px}
.note{max-width:760px;margin:0 auto;padding:clamp(23px,5vw,43px);background:#ffffffc7;border:1px solid white;border-radius:27px;box-shadow:0 18px 50px #9f47751c}.note p{white-space:pre-line;font-size:1.08rem;line-height:1.95;margin:0}.signature{margin-top:24px;text-align:right;color:#bd4f86;font-size:1.35rem;font-style:italic}
.center{text-align:center}#letter{display:none;margin-top:23px}#letter.show{display:block;animation:appear .7s ease both}@keyframes appear{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.music{max-width:520px;margin:20px auto 0;padding:17px;background:#ffffffa8;border:1px solid #fff;border-radius:18px;text-align:center;font:.9rem/1.6 Arial,sans-serif}audio{width:100%;margin-top:10px}
footer{text-align:center;padding:25px 0 42px;font:.84rem Arial,sans-serif;color:#96627d}.float-heart{position:fixed;bottom:-30px;pointer-events:none;z-index:5;animation:floatUp 4.5s linear forwards}@keyframes floatUp{to{transform:translateY(-110vh) rotate(25deg);opacity:0}}
@media(max-width:700px){.gallery{grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.polaroid{padding:8px 8px 13px}.caption-title{font-size:1rem}.caption-text{font-size:.78rem}}@media(max-width:420px){.pill{font-size:.72rem;padding:8px 10px}.hero{min-height:68vh}}
</style></head><body><div class="glow"></div><div class="glow two"></div><div class="wrap">
<nav><div>♡ MADE JUST FOR YOU</div><div class="pill">A birthday surprise ✨</div></nav>
<main><div class="hero"><div class="eyebrow">Today is all about you</div><div class="heart">💗</div><h1>Happy Birthday,<span>{{ her_name }}!</span></h1>
<p class="sub">A little corner of the internet, made just for you. If I could wrap up all the reasons you make me smile, this page still wouldn't be big enough. But I made it with all my heart.</p>
<button class="btn" onclick="document.getElementById('memories').scrollIntoView({behavior:'smooth'})">Our little scrapbook ↓</button>
{% if music_file %}<div class="music"><strong>🎵 A song for you</strong><br>Press play for your birthday soundtrack.<audio controls loop preload="none"><source src="{{ url_for('static', filename='music/' + music_file) }}">Your browser does not support audio.</audio></div>{% else %}<div class="music">🎵 Add an audio file to <code>static/music/</code> to show a music player here.</div>{% endif %}
</div>
<section id="memories"><h2 class="title">A scrapbook of you 📸</h2><p class="section-sub">Little moments, big feelings. Every frame is a reminder of how special you are. 💗</p>
<div class="gallery">{% for photo in photos %}<article class="polaroid" style="--tilt:{{ photo.tilt }}deg">
{% if photo.exists %}<img class="photo" src="{{ url_for('static', filename='photos/' + photo.filename) }}" alt="{{ photo.title }}" loading="lazy">{% else %}<div class="placeholder"><span>💞</span><strong>Add your photo here</strong><br>{{ photo.filename }}</div>{% endif %}
<h3 class="caption-title">{{ photo.title }}</h3><p class="caption-text">{{ photo.caption }}</p></article>{% endfor %}</div></section>
<section><h2 class="title">A letter for you 💌</h2><p class="section-sub">Something to read whenever you need a reminder of how loved you are.</p><div class="center"><button class="btn" id="reveal" onclick="revealLetter()">Tap to open your letter 💖</button></div>
<div class="note" id="letter"><p>{{ message }}</p><div class="signature">With all my love,<br>{{ your_name }} 💗</div></div></section>
<section class="center"><div class="heart">🎂</div><h2 class="title">Make a wish, birthday girl!</h2><p class="section-sub">May this year bring you peaceful days, exciting dreams, countless reasons to smile, and love that makes you feel special.</p><button class="btn" onclick="celebrate()">Sending you a thousand hearts 💕</button></section>
</main><footer>Made with love for {{ her_name }} · Happy Birthday ♡</footer></div>
<script>
function revealLetter(){document.getElementById('letter').classList.add('show');document.getElementById('reveal').textContent='A message from my heart 💗';document.getElementById('letter').scrollIntoView({behavior:'smooth',block:'center'});celebrate();}
function celebrate(){const e=['💗','💖','💕','💘','✨','🌸'];for(let i=0;i<30;i++){const n=document.createElement('span');n.className='float-heart';n.textContent=e[Math.floor(Math.random()*e.length)];n.style.left=Math.random()*100+'vw';n.style.fontSize=(16+Math.random()*22)+'px';n.style.animationDuration=(3+Math.random()*3)+'s';document.body.appendChild(n);setTimeout(()=>n.remove(),6500);}}setTimeout(celebrate,800);
</script></body></html>
"""

@app.route("/")
def home():
    photo_dir = os.path.join(app.static_folder, "photos")
    os.makedirs(photo_dir, exist_ok=True)
    files = sorted(
        f for f in os.listdir(photo_dir)
        if f.lower().endswith(ALLOWED_EXTENSIONS) and os.path.isfile(os.path.join(photo_dir, f))
    )
    photos = []
    for i in range(6):
        if i < len(files):
            filename = files[i]
            title, caption = CAPTIONS[i]
            photos.append({"filename": filename, "exists": True, "title": title, "caption": caption, "tilt": [-3, 2, -2, 3, -1, 2][i]})
        else:
            expected = f"photo{i+1}.jpg"
            title, caption = CAPTIONS[i]
            photos.append({"filename": expected, "exists": False, "title": title, "caption": caption, "tilt": [-3, 2, -2, 3, -1, 2][i]})
    music_dir = os.path.join(app.static_folder, "music")
    music_file = next((f for f in os.listdir(music_dir) if f.lower().endswith((".mp3", ".ogg", ".wav", ".m4a"))), None) if os.path.isdir(music_dir) else None
    return render_template_string(PAGE, her_name=HER_NAME, your_name=YOUR_NAME, message=BIRTHDAY_MESSAGE, photos=photos, music_file=music_file)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
