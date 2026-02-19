# 📚 每日知识 | 第{{global_episode}}期
**{{date}} · {{weekday}}**

---

{{#each subjects}}
## {{icon}} {{name}} | 第{{current}}/{{total}}期
### {{title}}

#### 🔗 知识关联（Callback）

{{#if callbacks}}
{{#each callbacks}}
> 📌 **回顾第{{episode}}期**：{{summary}}
{{/each}}
> 
> 🔗 **本期关联**：{{callback_relation}}
{{else}}
> 📌 这是本学科的第一期，让我们开始这段学习之旅！
{{/if}}

---

#### 引入故事

{{story_intro}}

---

#### 核心概念

{{core_concept}}

---

#### 深入分析

{{deep_analysis}}

---

#### 重点记忆

{{key_points}}

---

> 💡 **一句话带走**：{{takeaway}}

---

#### 📝 课后习题（游戏/互联网应用向）

{{#each exercises}}
**{{index}}. {{type}}**
{{question}}

{{/each}}

---

<details>
<summary>🔑 点击查看参考答案</summary>

---

{{#each answers}}
**第{{index}}题 解析：{{type}}**

{{content}}

---

{{/each}}

</details>

---

{{/each}}

## 📊 今日学习统计

| 学科 | 进度 | 状态 |
|------|------|------|
{{#each subjects}}
| {{icon}} {{name}} | {{current}}/{{total}} ({{progress}}%) | {{status_emoji}} |
{{/each}}

🎯 **累计进度**：已完成 {{global_episode}} 期
⏰ **预计完成**：{{estimated_completion_date}}

---

## 📦 本期知识存档

```json
{{knowledge_json}}
```

---

## 📈 知识脉络

```
{{knowledge_tree}}
```

---

> 📮 本邮件由 **Knowledge Daily** 自动生成
> 🔧 如需调整学科或进度，请修改配置文件后重新生成
> 📅 生成时间：{{generate_time}}
