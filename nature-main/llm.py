import os
from openai import OpenAI



SUMMARY_PROMPT = """
你是一名学术期刊编辑，请为以下 Nature Research Article 撰写【中文论文导读】。

【论文标题】
{title}

【论文摘要】
{abstract}

请按以下四个小标题分别撰写，每一部分 2–4 句话：

【研究背景】
【核心发现】
【方法或机制】
【学术意义】

总体要求：
1. 总字数 150–250 字
2. 学术、客观、克制，不使用宣传性语言
3. 不逐句翻译摘要，而是重组表达
4. 仅输出正文内容，不要额外说明
"""






client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")




def summarize_with_llm(title: str, main_content: str) -> str:
    if not main_content.strip():
        return ""

    prompt = SUMMARY_PROMPT.format(title=title, abstract=main_content)

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role":"user","content":prompt}],
        temperature=0.3,
        stream=False
    )

    return response.choices[0].message.content.strip()

def translate_with_llm(text: str, target_language: str = "Chinese") -> str:
    if not text.strip():
        return ""

    prompt = (
        f"请从下面这段文字中提取最可能的论文标题，并翻译成{target_language}。\n"
        "要求：\n"
        "1. 只输出标题本身\n"
        "2. 不要添加任何解释、前缀或引号\n"
        "3. 如果有多个候选标题，选择最正式、最完整的一个\n\n"
        f"{text}"
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,  # 信息抽取+翻译，低温更稳
        stream=False
    )

    result = response.choices[0].message.content.strip()

    # ---------- 清理结果 ----------
    # 去掉书名号等
    for q in [ "《》" ]:
        if len(q) == 2:
            result = result.replace(q[0], "").replace(q[1], "")
    
    # 去掉 Markdown 加粗符号 **
    result = result.replace("**", "").strip()

    return result





CATEGORIES = [
    "Biology",
    "Materials Science",
    "Computer Science",
    "Physics",
    "Chemistry",
    "Medicine",
    "Earth & Environment",
    "Psychology",
    "Other"
]



def classify_paper_with_llm(title: str, abstract: str) -> str:
    prompt = f"""
你是一名学术期刊编辑。

请将下列论文【且仅能】归类到以下学科之一：
- Biology
- Materials Science
- Computer Science
- Physics
- Chemistry
- Medicine
- Earth & Environment
- Psychology
- Other

【论文标题】
{title}

【论文摘要】
{abstract[:1500]}

要求：
1. 只输出学科英文名
2. 不要输出解释
"""

    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )

    return resp.choices[0].message.content.strip()

KEYWORDS_PROMPT = """
你是一名学术期刊编辑。

请根据以下 Nature Research Article 的标题和摘要，
提取 5–7 个【学术关键词】。

【论文标题】
{title}

【论文摘要】
{abstract}

要求：
1. 关键词应直接来源于论文内容，不得凭空臆造
2. 使用名词或名词短语，不使用完整句子
3. 避免使用“新型”“高效”“创新性”等评价性词语
4. 优先选择具体、专业的技术或研究对象术语
5. 关键词之间用中文分号“；”分隔
6. 不要添加编号、解释或多余说明，只输出关键词本身
"""


def extract_keywords_with_llm(title: str, abstract: str) -> str:
    if not abstract.strip():
        return ""

    prompt = KEYWORDS_PROMPT.format(
        title=title,
        abstract=abstract
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        stream=False
    )

    return response.choices[0].message.content.strip()
