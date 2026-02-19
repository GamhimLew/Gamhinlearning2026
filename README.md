# 📚 Knowledge Daily - 每日知识推送系统

一个为游戏设计/互联网从业者定制的碎片化学习系统。

## ✨ 功能特点

- 📖 **多学科学习**：高等数学、宏观经济学、炒股、UX/UI设计、游戏系统设计、编曲
- 🔗 **知识关联**：自动回顾之前学过的相关知识，构建知识网络
- 🎯 **行业定制**：习题结合游戏/互联网实际应用场景
- 📧 **定时推送**：GitHub Actions 每天早上8点自动发送邮件
- 📊 **进度追踪**：JSON存储学习进度和知识库

## 📁 项目结构

```
knowledge-daily/
├── config/
│   ├── subjects.json      # 学科配置 & 知识框架
│   └── progress.json      # 学习进度
├── content/
│   └── pending_email.md   # 待发送邮件内容
├── data/
│   └── knowledge_base.json # 知识库存档
├── templates/
│   ├── email_template.md  # 邮件模板
│   └── prompts.md         # AI生成提示词
├── scripts/
│   └── send_email.py      # 邮件发送脚本
├── .github/
│   └── workflows/
│       └── send_daily.yml # GitHub Actions 配置
└── README.md
```

## 🚀 快速开始

### 1. 配置 QQ 邮箱 SMTP

1. 登录 QQ 邮箱网页版
2. 设置 → 账户 → 开启 SMTP 服务
3. 获取 16 位授权码（保存好！）

### 2. 配置 GitHub Secrets

在 GitHub 仓库设置中添加以下 Secrets：

| Secret 名称 | 值 |
|-------------|-----|
| `SMTP_USER` | 你的QQ邮箱地址 |
| `SMTP_PASSWORD` | QQ邮箱授权码 |
| `TO_EMAIL` | 接收邮件的地址 |

### 3. 每日使用流程

```bash
# 1. 与AI对话生成今日学习内容

# 2. 将生成的内容保存到 content/pending_email.md

# 3. 提交并推送到 GitHub
git add .
git commit -m "📚 第X期内容"
git push

# 4. 次日早上8点自动收到邮件！
```

## 📖 当前学科进度

| 学科 | 图标 | 总期数 | 当前进度 |
|------|------|--------|----------|
| 高等数学 | 📐 | 40期 | 0% |
| 宏观经济学 | 📈 | 30期 | 0% |
| 炒股 | 📊 | 35期 | 0% |
| UX/UI设计 | 🎨 | 25期 | 0% |
| 游戏系统设计 | 🎮 | 30期 | 0% |
| 编曲 | 🎵 | 20期 | 0% |

**总计**：180期 ≈ 约6个月（每天学2个学科）

## 📝 内容生成

使用 `templates/prompts.md` 中的提示词模板与 AI 对话，生成符合格式的学习内容。

## 🔧 配置说明

编辑 `config/subjects.json` 可以：
- 添加/删除学科
- 调整每日学科数量
- 修改学习计划和框架

## 📄 License

MIT License
