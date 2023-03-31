# Getting-Started

## step

```shell
# 1.fork 目标仓库 -> 个人项目
# 2.git clone 个人项目
# 3.添加上游仓库例：
git remote add upstream git@github.com:microsoft/playwright.git
# 4.切换个人项目分支 
git checkout main
# 5.更新上游代码
git fetch upstream
# 6.合并代码至指定分支
git merge upstream/main
# 7.更新代码 保持目标库与个人库一致
git push

# 8.新建分支
git checkout -b xxx
# 9.开发 -> push 至个人仓库
# 10.提交pr  等待 review 通过合并至主分支
# 11.删除本地分支,同步上游 main 分支
```
