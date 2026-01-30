# Nature Markdown 网站

这个仓库包含用于生成 Nature 论文摘要网站的 Python 脚本。脚本会读取 `data` 文件夹下的 Markdown 文件，将论文按照月份和类别分组，并生成 HTML 页面展示。

## 功能

* 解析 Markdown 文件中的文章内容
* 自动识别文章类别
* 中文和英文标题都显示
* Nature 文章链接可点击访问
* 按月份和类别折叠显示论文

## 使用方法

1. 克隆仓库并进入目录：

```bash
git clone <仓库地址>
cd nature_site
```

2. 安装依赖：

```bash
pip install fastapi uvicorn markdown jinja2
```

3. 确保 `data` 文件夹下有按月份命名的 Markdown 文件，如 `nature_2025-12.md`。

4. 运行网站：

```bash
python -m uvicorn app:app --reload
```

5. 在浏览器打开 [http://127.0.0.1:8000](http://127.0.0.1:8000) 即可访问网站。

## Markdown 文件格式示例

```markdown
## 物理学（Physics）

## 光学调控莫尔材料中的拓扑陈数

**作者与单位**
第一作者：Zhang et al.
单位：Tsinghua University

**研究背景**
莫尔材料为研究强关联量子态提供了新的平台，但其拓扑性质的可控调节仍是挑战。

**核心发现**
本文通过光学调控实现了拓扑陈数的连续调节。

**方法**
作者采用超快激光泵浦-探测技术结合理论建模。

**学术意义**
该工作为可编程拓扑量子器件提供了新思路。

https://www.nature.com/articles/s41586-025-09864-5
```

文章标题和正文将自动渲染为 HTML，并将 URL 转换为可点击链接。
