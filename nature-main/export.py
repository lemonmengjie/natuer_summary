CATEGORY_ZH = {
    "Biology": "生物学",
    "Materials Science": "材料学",
    "Computer Science": "计算机科学",
    "Physics": "物理学",
    "Chemistry": "化学",
    "Medicine": "医学",
    "Earth & Environment": "地球与环境",
    "Psychology":"心理学",
    "Other": "其他"
}



# def export_markdown_by_category(groups, label):
#     lines = []

#     lines.append(f"# Nature 月度论文导读（{label}）\n")
#     lines.append("---\n")

#     for cat_en, papers in groups.items():
#         cat_zh = CATEGORY_ZH.get(cat_en, cat_en)
#         lines.append(f"## {cat_zh}（{cat_en}）\n")

#         for idx, p in enumerate(papers, 1):
#             lines.append(f"### {idx}. {p['title']}\n")
#             lines.append(f"**中文标题**：{p['translated_title']}\n\n")
#             lines.append(
#                 f"**第一作者**：{p.get('first_author', 'Unknown')}\n"
#             )
#             lines.append(
#                 f"**作者单位**：{p.get('first_affiliation', 'Unknown')}\n"
#             )
#             lines.append(
#                 f"**国家**：{p.get('country', 'Unknown')}\n\n"
#             )
#             lines.append(
#                 f"**关键词**：{p.get('keywords', '—')}\n\n"
#             )
#             lines.append(f"**导读**：\n{p['summary']}\n\n")
#             lines.append(f"**访问链接**：{p['url']}\n")
#             lines.append("\n---\n")

#     return "\n".join(lines)

CATEGORY_ORDER = [
    "Physics",
    "Chemistry",
    "Materials Science",
    "Biology",
    "Medicine",
    "Earth & Environment",
    "Psychology",
    "Computer Science",
    "Other"
]

def export_markdown_by_category(groups, label):
    lines = []

    lines.append(f"# Nature 月度论文导读（{label}）\n")
    lines.append("---\n")

    for cat_en in CATEGORY_ORDER:
        papers = groups.get(cat_en)
        if not papers:
            continue

        cat_zh = CATEGORY_ZH.get(cat_en, cat_en)
        lines.append(f"## {cat_zh}（{cat_en}）\n")

        for idx, p in enumerate(papers, 1):
            lines.append(f"### {idx}. {p['title']}\n")
            lines.append(f"**中文标题**：{p['translated_title']}\n\n")

            lines.append(
                f"**第一作者**：{p.get('first_author', 'Unknown')}\n"
            )
            lines.append(
                f"**作者单位**：{p.get('first_affiliation', 'Unknown')}\n"
            )
            lines.append(
                f"**国家**：{p.get('country', 'Unknown')}\n\n"
            )
            lines.append(
                f"**关键词**：{p.get('keywords', '—')}\n\n"
            )

            lines.append(f"**导读**：\n{p['summary']}\n\n")
            lines.append(f"**访问链接**：{p['url']}\n")
            lines.append("\n---\n")

    return "\n".join(lines)
