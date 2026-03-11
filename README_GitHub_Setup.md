# GitHub Actions 新闻摘要系统设置指南

## 🚀 完全免费的云端解决方案

### 优势
- ✅ **完全免费**：GitHub Actions每月2000分钟免费额度
- ✅ **24小时运行**：不受本地电脑开机状态影响
- ✅ **自动定时**：每天北京时间7:00自动发送
- ✅ **邮件推送**：直接发送到您的QQ邮箱

## 📋 设置步骤

### 第一步：创建GitHub仓库
1. 访问 [GitHub.com](https://github.com)
2. 点击右上角"+" → "New repository"
3. 仓库名：`daily-news-email`
4. 选择"Public"（免费）
5. 勾选"Add a README file"

### 第二步：上传代码到GitHub
1. 下载本项目的所有文件
2. 在GitHub仓库页面点击"Upload files"
3. 将所有文件拖拽到上传区域
4. 点击"Commit changes"

### 第三步：配置密钥（重要）
1. 进入仓库 → Settings → Secrets and variables → Actions
2. 点击"New repository secret"
3. 添加以下3个密钥：

**SMTP_USER**
```
289574795@qq.com
```

**SMTP_PASSWORD**
```
mwrihbpgxzeacbbg
```

**RECIPIENT_EMAIL**
```
289574795@qq.com
```

### 第四步：启用Actions
1. 进入仓库 → Actions
2. 点击"I understand my workflows, go ahead and enable them"
3. 系统会自动运行第一次任务

## ⚙️ 定时设置说明

- **运行时间**：每天UTC时间23:00（北京时间第二天7:00）
- **手动触发**：在Actions页面可以手动立即运行
- **运行日志**：可以查看每次执行的详细日志

## 📧 邮件内容预览

**每天自动发送包含：**
- 🌍 15条国际重点新闻
- 💰 财经市场动态分析
- 🔬 科技前沿进展
- ⚡ 风险提示和趋势预测

## 🔧 故障排除

### 如果邮件未收到
1. 检查GitHub Actions运行状态（绿色√表示成功）
2. 检查垃圾邮件文件夹
3. 验证密钥配置是否正确

### 修改发送时间
编辑 `.github/workflows/daily-news.yml` 文件中的cron表达式：
- 每天7:00：`0 23 * * *`（UTC时间）
- 每天8:00：`0 0 * * *`（UTC时间）

## 💡 优势对比

| 方案 | 成本 | 可靠性 | 维护 | 24小时运行 |
|------|------|--------|------|------------|
| 本地电脑 | 免费 | 低 | 高 | ❌ |
| GitHub Actions | 免费 | 高 | 零 | ✅ |
| 云服务器 | 付费 | 高 | 中 | ✅ |

## 🎯 立即开始

按照上述步骤设置后，系统将：
1. ✅ 每天自动收集新闻
2. ✅ 自动生成分析报告
3. ✅ 自动发送到您的邮箱
4. ✅ 无需人工干预

**设置完成后，您就可以享受24小时不间断的新闻摘要服务了！**