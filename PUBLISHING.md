# GitHub 发布状态

首版的本地仓库内容已经准备；远端仓库尚未创建或推送。

建议仓库名：`scaling-law-survey`。可见性待用户选择。当前检查到 GitHub 网页未登录，环境中没有可用 `gh` 命令或 GitHub token；因此不能把本地准备完成写成发布成功。

完成 GitHub 登录后，可以在用户账户下创建空仓库、绑定 `origin`、正常推送并核验网页显示。本项目不要求在聊天中提供密码或 token。若用 CLI，可安装官方 GitHub CLI，并由用户完成 `gh auth login`。

发布前运行构建检查；只发布本仓库文件。参考 survey 的原始源码、原论文全文、社区网页镜像均不包含在发布内容中。远端 URL 确认后，更新 README 与 data/state.json。
