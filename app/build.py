"""Собирает простой сайт в папку site/ — его и задеплоит CD."""
import datetime
import os

from app.calc import add, multiply, divide

os.makedirs("site", exist_ok=True)
now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
commit = os.getenv("GITHUB_SHA", "local")[:7]

html = f"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><title>CI/CD demo</title></head>
<body style="font-family:sans-serif;max-width:600px;margin:40px auto">
<h1>Мой первый CI/CD test1 🚀</h1>
<p>2 + 3 = {add(2, 3)}</p>
<p>4 × 5 = {multiply(4, 5)}</p>
<p>10 / 4 = {divide(10, 4)}</p>
<hr><small>Собрано: {now}, коммит: {commit}</small>
</body></html>"""

with open("site/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("site/index.html готов")
