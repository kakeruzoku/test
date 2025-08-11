import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

os.makedirs("docs", exist_ok=True)
output_path = "docs/index.md"

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

r = requests.get("https://httpbin.org/user-agent")

# Markdown生成
content = f"""\

# 自動生成テスト

生成時刻 {now}

github's useragent: `{r.json()["user-agent"]}`
"""

# 保存
with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Markdownファイルを生成しました: {output_path}")
