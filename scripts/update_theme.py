import re
from datetime import datetime, timezone, timedelta

README_PATH = "README.md"

# IST timezone (UTC+5:30)
ist = timezone(timedelta(hours=5, minutes=30))
today = datetime.now(ist).strftime("%A")  # Monday, Tuesday, etc.

# 7 unique themes, one per day
THEMES = {
    "Monday":    {"grad": "0:1e3c72,50:2a5298,100:00c9ff", "accent": "00C9FF", "stats_theme": "tokyonight",   "graph_theme": "tokyo-night"},
    "Tuesday":   {"grad": "0:0f2027,50:2c5364,100:00c9a7", "accent": "00C9A7", "stats_theme": "dracula",      "graph_theme": "dracula"},
    "Wednesday": {"grad": "0:360033,50:0b8793,100:00ffcc", "accent": "00FFCC", "stats_theme": "radical",      "graph_theme": "radical"},
    "Thursday":  {"grad": "0:1a2980,50:26d0ce,100:26d0ce", "accent": "26D0CE", "stats_theme": "synthwave",    "graph_theme": "react"},
    "Friday":    {"grad": "0:ff512f,50:dd2476,100:ff512f", "accent": "FF512F", "stats_theme": "cobalt",       "graph_theme": "vue-dark"},
    "Saturday":  {"grad": "0:11998e,50:38ef7d,100:11998e", "accent": "38EF7D", "stats_theme": "gruvbox",      "graph_theme": "chartreuse-dark"},
    "Sunday":    {"grad": "0:8e2de2,50:4a00e0,100:8e2de2", "accent": "8E2DE2", "stats_theme": "merko",        "graph_theme": "github-compact"},
}

theme = THEMES[today]

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# --- Update Banner ---
banner_block = f'''<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color={theme['grad']}&height=220&section=header&text=Aamit%20Kumar&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Data%20Scientist%20%7C%20GenAI%20%7C%20LLMs%20%7C%20MLOps%20Engineer&descAlignY=55&descSize=20"/>
</p>'''
content = re.sub(
    r"(<!--THEME_BANNER_START-->)(.*?)(<!--THEME_BANNER_END-->)",
    lambda m: f"{m.group(1)}\n{banner_block}\n{m.group(3)}",
    content, flags=re.DOTALL
)

# --- Update Typing SVG color ---
typing_block = f'''<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=1000&color={theme['accent']}&center=true&vCenter=true&width=650&lines=Data+Scientist+%40+India+%7C+8%2B+Years+Experience;Building+%26+Deploying+AI%2FML+Models;Exploring+Generative+AI+%26+LLMs;Turning+Data+into+Actionable+Stories" alt="Typing SVG" />
  </a>
</p>'''
content = re.sub(
    r"(<!--THEME_TYPING_START-->)(.*?)(<!--THEME_TYPING_END-->)",
    lambda m: f"{m.group(1)}\n{typing_block}\n{m.group(3)}",
    content, flags=re.DOTALL
)

# --- Update Stats + Activity Graph theme ---
stats_block = f'''<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=amitmakode&theme={theme['stats_theme']}&hide_border=true&background=0D1117"/>
</p>
<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=amitmakode&theme={theme['graph_theme']}&hide_border=true&bg_color=0D1117"/>
</p>'''
content = re.sub(
    r"(<!--THEME_STATS_START-->)(.*?)(<!--THEME_STATS_END-->)",
    lambda m: f"{m.group(1)}\n{stats_block}\n{m.group(3)}",
    content, flags=re.DOTALL
)

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Theme updated for {today}")
