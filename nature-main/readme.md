# Nature Research Articles 月度抓取与导出

## 功能简介
- 抓取 Nature（`/nature/research-articles`）列表页的论文条目
- 支持：
  - 默认抓取**当前月**
  - 或通过参数指定月份（`YYYY-MM`）
- 对每篇论文：
  - 获得一作姓名，机构，国家
  - 捕捉关键词
  - 抽取 Abstract + 正文首段（按当前实现）
  - 调用 LLM：学科分类、标题翻译、中文导读生成
- 按学科分组导出 Markdown：`nature_{YYYY-MM}.md`

## 部署环境
- Python：建议 3.10+（代码使用了 `str | None` 类型注解）
- 依赖安装（项目根目录执行）：
  ```bash
  pip install -r requirement.txt
  ```

> 备注：依赖文件名是 `requirement.txt`（不是常见的 `requirements.txt`）。

## 运行命令
### 1) 默认抓取当前月
```bash
python main.py
```

### 2) 指定月份（YYYY-MM）
```bash
python main.py --month 2025-12
```

### 3) 限制最多扫描页数（安全上限）
```bash
python main.py --month 2025-12 --max-pages 50
```

## 输出
- 运行结束后会在当前目录生成：
  - `nature_{YYYY-MM}.md`

## 环境变量（必须先自行定义）
本项目通过 `llm.py` 调用 DeepSeek（OpenAI SDK 兼容接口），需要你本地先设置：
- `DEEPSEEK_API_KEY`

示例：

**Windows PowerShell**
```powershell
$env:DEEPSEEK_API_KEY="your_key_here"
python main.py --month 2025-12
```

**Windows CMD**
```bat
set DEEPSEEK_API_KEY=your_key_here
python main.py --month 2025-12
```

**macOS / Linux (bash/zsh)**
```bash
export DEEPSEEK_API_KEY="your_key_here"
python main.py --month 2025-12
```

## 注意事项

### 网络环境
请确保网络环境稳定，抓取大量页面可能耗时较长。

### 抓取频率
建议不要频繁抓取大量页面，以免被 Nature 网站限制访问。

### Markdown 文件用途
生成的 Markdown 文件可直接用于：
- 网站数据展示
- 本地阅读

## 邮件发送（可选）

### 必填环境变量
- `EMAIL_SMTP_SERVER`
- `EMAIL_PORT`（默认 587）
- `EMAIL_USER`
- `EMAIL_PASS`
- `EMAIL_TO`

### 示例

#### Windows PowerShell
```powershell
$env:EMAIL_SMTP_SERVER="smtp.example.com"
$env:EMAIL_USER="your@example.com"
$env:EMAIL_PASS="yourpassword"
$env:EMAIL_TO="recipient@example.com"
python main.py --month 2025-12
```

#### Windows
```
set EMAIL_SMTP_SERVER=smtp.example.com
set EMAIL_USER=your@example.com
set EMAIL_PASS=yourpassword
set EMAIL_TO=recipient@example.com
python main.py --month 2025-12
```

#### macOS / Linux (bash/zsh)
```
export EMAIL_SMTP_SERVER="smtp.example.com"
export EMAIL_USER="your@example.com"
export EMAIL_PASS="yourpassword"
export EMAIL_TO="recipient@example.com"
python main.py --month 2025-12
```
