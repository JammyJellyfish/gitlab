# gitp配置
    # 查看所有配置 以及他们所在文件
    git config --list --show-origin

    # 用户信息
    git config --global user.name "username"
    git config --global user.email "useremail"

    # 设置git编辑器
    git config --global core.editor vim 

    # 检查某一项配置
    git config <key>
    git config user.name

    # 获取帮助
    git help <verb>
    git help config
    
    # 简洁的帮助
    git 命令 -h
    git add -h


# git 基础
    # 初始化创库
    git init

    # 跟踪新文件
    git add

    # 提交更新
    git commit -m '提交信息'

    # 克隆
    git clone <url>

    # 检查当前文件状态
    git status
    git status -s # 状态简览
    
    # 忽略文件
    cat .gitignore

    # 查看已暂存和未暂存的修改
    git diff

    # 对比已暂存文件和最后一次提交的文件差异
    git diff --staged

    # 查看已暂存起来的变化
    git diff --cached

    # 跳过使用暂存区
    git commit -am ""

    # 从暂存区移除文件
    git rm
    git rm -f # 强制删除 force
   
    # 删除所有名字 以~结尾的文件
    git rm \*~

    # 重名了
    git mv file_from file_to

    # 查看提交历史
    git log
    git log -p -n  # -p 或 --patch 显示每次提交所引入得差异 -n 限制显示的日志条目数量
            --stat  # 显示每次提交的文件修改统计信息
            --shortstat  # 只显示 --stat 中最后的行数修改添加移除统计
            --name-only  # 仅在提交信息后显示已修改的文件清单
            --abbrev-commit  # 仅显示 SHA-1 校验和所有 40 个字符中的前几个字符。
            --relative-date  # 使用较短的相对时间而不是完整格式显示日期（比如“2 weeks ago”）。
            --graph  # 在日志旁以 ASCII 图形显示分支与合并历史。
            --pretty  # 使用其他格式显示历史提交信息。可用的选项包括 oneline、short、full、fuller 和 format（用来定义自己的格式）。   
            --oneline  # --pretty=oneline --abbrev-commit 合用的简写。
            --pretty=format:"%h %s" --graph

            --since  # 
            --until  # 限制输出长度
            --since=2.weeks  # 列出最近两周的所有提交
    
    # 撤销操作
    git commit --amend

    # 取消暂存的文件
    git reset HEAD <file>

    # 撤销对文件的修改
    git checkout -- <file>  # 本地的任何修改都会消失 

    # 远程仓库的使用
    git clone <url>
    git remote  # 查看已经配置的远程仓库服务器
               -v  # 显示仓库地址
    
    # 添加远程仓库
    git remote add <shortname> <url>

    # 从远程仓库中抓取与拉取
    git fetch <remote>

    # 推送到远程仓库
    git push origin master

    # 查看某个远程仓库
    git remote show origin

    # 远程仓库的重命名与移除
    git remote rename pb paul # 将pb重命名为paul

    git remote remove paul  # 移除一个远程仓库

    # 打标签
    git tag 
            -l  # 通配符
            --list
    git tag -l "v1.8.5*"

    # 创建标签
        # 轻量标签
            git tag v1.0

    # 附注标签
        git tag -a v1.0 "my version 1.0"
        git show v1.0 #  可以查看到标签信息和与之对应的提交信息
    
    # 后期打标签
        git tag -a v1.2 9fceb02  # 一笔提交的部分 uuid
    
    # 共享标签
    # 删除标签
    # 检出标签
    
    # git 别名
         git config --global alias.co checkout
         git config --global alias.br branch
         git config --global alias.ci commit
         git config --global alias.st status
  

    
















    
