import os
from datetime import datetime, timezone

# ============== ROLES & TECH STACK (with % expertise) ==============
ROLES = [
    {
        "title": "Data Analyst",
        "skills": [
            ("Python", 80), ("SQL", 90), ("Power BI", 85),
            ("Advanced Excel", 90), ("Tableau", 70),
        ],
    },
    {
        "title": "Data Scientist",
        "skills": [
            ("Python", 90), ("Statistics", 85), ("Pandas / NumPy", 90),
            ("Scikit-learn", 85), ("SQL", 80),
        ],
    },
    {
        "title": "Data Engineer",
        "skills": [
            ("Python", 80), ("SQL", 85), ("Apache Spark", 75),
            ("Airflow", 70), ("Docker", 75),
        ],
    },
    {
        "title": "AI / ML Engineer",
        "skills": [
            ("Python", 90), ("TensorFlow", 85), ("PyTorch", 85),
            ("Scikit-learn", 80), ("Docker", 75),
        ],
    },
    {
        "title": "ML Engineer",
        "skills": [
            ("Python", 85), ("MLflow", 75), ("Docker", 80),
            ("Kubernetes", 70), ("Model Deployment", 80),
        ],
    },
    {
        "title": "MLOps Engineer",
        "skills": [
            ("Docker", 85), ("Kubernetes", 80), ("MLflow", 80),
            ("CI/CD Pipelines", 75), ("Cloud (AWS/GCP)", 80),
        ],
    },
    {
        "title": "GenAI Engineer",
        "skills": [
            ("Python", 85), ("LangChain", 80), ("Hugging Face", 80),
            ("OpenAI / LLM APIs", 85), ("Vector Databases", 75),
        ],
    },
    {
        "title": "GenAI Cloud Engineer",
        "skills": [
            ("AWS / Azure / GCP", 85), ("LangChain", 75), ("Docker", 75),
            ("Kubernetes", 70), ("Vector Databases", 75),
        ],
    },
    {
        "title": "Business Analyst",
        "skills": [
            ("SQL", 85), ("Advanced Excel", 90), ("Power BI", 90),
            ("Data Storytelling", 85), ("Stakeholder Communication", 80),
        ],
    },
]

PALETTE = ["#00C9A7", "#FF512F", "#8E2DE2", "#26D0CE", "#38EF7D", "#00C9FF", "#DD2476"]

# Rotation cadence: pick a new role every N minutes (must match the workflow's cron).
MINUTES_PER_ROLE = 10

OUTPUT_PATH = "assets/role-card.svg"

# ---- pick current role based on UTC time (deterministic, no state needed) ----
now = datetime.now(timezone.utc)
minutes_since_epoch = int(now.timestamp() // 60)
slot = (minutes_since_epoch // MINUTES_PER_ROLE) % len(ROLES)
role = ROLES[slot]

WIDTH = 700
BAR_X = 190
BAR_MAX_W = 430
BAR_H = 14
ROW_H = 46
TOP_PAD = 90
BOTTOM_PAD = 46
HEIGHT = TOP_PAD + len(role["skills"]) * ROW_H + BOTTOM_PAD

svg_parts = []
svg_parts.append(f'''<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f2027"/>
      <stop offset="50%" stop-color="#12222b"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" rx="16" fill="url(#bg)" stroke="#233240" stroke-width="1"/>

  <text x="{WIDTH/2}" y="42" text-anchor="middle" font-family="'Segoe UI', Verdana, sans-serif" font-size="26" font-weight="700" fill="#00C9A7">
    {role["title"]}
  </text>
  <text x="{WIDTH/2}" y="66" text-anchor="middle" font-family="'Segoe UI', Verdana, sans-serif" font-size="13" fill="#8b98a5">
    Tech Stack &amp; Expertise Level
  </text>
''')

for i, (skill, pct) in enumerate(role["skills"]):
    y = TOP_PAD + i * ROW_H
    color = PALETTE[i % len(PALETTE)]
    bar_w = round(BAR_MAX_W * pct / 100)
    svg_parts.append(f'''
  <text x="30" y="{y + BAR_H - 1}" font-family="'Segoe UI', Verdana, sans-serif" font-size="15" fill="#e6edf3">{skill}</text>
  <rect x="{BAR_X}" y="{y}" width="{BAR_MAX_W}" height="{BAR_H}" rx="7" fill="#1c2733"/>
  <rect x="{BAR_X}" y="{y}" width="{bar_w}" height="{BAR_H}" rx="7" fill="{color}"/>
  <text x="{BAR_X + BAR_MAX_W + 14}" y="{y + BAR_H - 1}" font-family="'Segoe UI', Verdana, sans-serif" font-size="13" font-weight="600" fill="{color}">{pct}%</text>
''')

footer_y = HEIGHT - 18
svg_parts.append(f'''
  <text x="{WIDTH/2}" y="{footer_y}" text-anchor="middle" font-family="'Segoe UI', Verdana, sans-serif" font-size="11" fill="#5b6773">
    Role {slot + 1} of {len(ROLES)} &#8226; refreshes every {MINUTES_PER_ROLE} min
  </text>
</svg>
''')

svg = "".join(svg_parts)

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Generated static role card for: {role['title']} -> {OUTPUT_PATH}")
