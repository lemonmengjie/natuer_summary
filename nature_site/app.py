import markdown
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from collections import defaultdict
import re

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# ------------------------
# 读取所有 markdown 文件
# ------------------------
DATA_DIR = Path("data")
all_articles = []  # [{"month":..., "category":..., "title":..., "content":...}]

CATEGORY_MAP = {
    "Biology": "生物学",
    "Materials Science": "材料学",
    "Computer Science": "计算机科学",
    "Physics": "物理学",
    "Chemistry": "化学",
    "Medicine": "医学",
    "Earth & Environment": "地球与环境",
    "Psychology": "心理学",
    "Other": "其他"
}
def linkify(text: str) -> str:
    url_pattern = re.compile(r"(https://www\.nature\.com/articles/\S+)")
    return url_pattern.sub(r'<a href="\1" target="_blank">\1</a>', text)


category_pattern = re.compile(r"^(.+?)（.+?）$")  # 匹配 ## 物理学（Physics）这种格式

for md_file in DATA_DIR.glob("*.md"):
    month = md_file.stem.split("_")[-1]
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()
        # 按文章标题拆分，每篇文章以 ## 开头
        articles = md_text.split("## ")
        current_category = "其他"  # 默认分类

        for art in articles[1:]:  # 第一个 split 前是开头文字
            lines = art.strip().splitlines()
            if not lines:
                continue
            title_line = lines[0].strip()

            # 判断是否是分类标题
            cat_match = category_pattern.match(title_line)
            if cat_match and title_line in CATEGORY_MAP.values() or any(k in title_line for k in CATEGORY_MAP.keys()):
                current_category = next((cname for key, cname in CATEGORY_MAP.items() if key in title_line or cname in title_line), "其他")
                continue  # 分类标题不算文章，不增加数量

            # 文章正文
            raw_md = "\n".join(lines[1:])
            raw_md = linkify(raw_md)

            content_md = "## " + raw_md
            html_content = markdown.markdown(content_md, extensions=["extra", "tables"])

            html_content = markdown.markdown(content_md, extensions=["extra", "tables"])

            all_articles.append({
                "month": month,
                "category": current_category,
                "title": title_line,
                "content": html_content
            })


# ------------------------
# 首页 
# ------------------------
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    # 按月份 + 类别分组
    month_groups = defaultdict(lambda: defaultdict(list))
    month_counts = defaultdict(int)

    for article in all_articles:
        month_groups[article["month"]][article["category"]].append(article)
        month_counts[article["month"]] += 1

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "month_groups": dict(month_groups),
            "month_counts": dict(month_counts),
            "categories": CATEGORY_MAP
        }
    )


