# Paul Graham博客合集

[English Version](Readme.md)

经典文章值得反复阅读，在网页上看太麻烦了，所以制作成了电子书。

网页爬到本地后，又做了这些工作：

 - 设计封面
 - 网页由cp1252转码为utf-8，防止乱码
 - 添加Favorite、Latest、Hackers and Painters
 - 按照标题首字母分章节，方便查找
 - 添加非作者原创但在作者网站的几篇文章
 - 纠正正文中部分不对称的标点符号（破折号和引号）
 - 删除2个失效链接和1个年代久远内容过短的文章
 - 修正网页中不对称的tag，防止在Kindle上阅读出现异常

如果您熟悉python和html，那么您可以通过编辑**calibre.recipe**或**index.html**轻松添加或删除文章/章节，制作属于自己的电子书。 编辑完成后，您可以按照以下步骤制作kindle电子书：

## 1. 启动本地 Web 服务器

在当前文件夹中运行以下命令：

```sh
python3 -m http.server 8000
```

## 2. 测试程序

使用以下命令调试您的程序

```sh
ebook-convert calibre.recipe .mobi --test -vv --debug-pipeline debug
```

## 3. 使用Calibre制作电子书

打开 Calibre，右键单击 **Fetch news**，然后选择 **Add or edit a custom news source**，单击 **New recipe**，然后选择 **Switch to advanced mode** 并将您的程序粘贴到新的页面，点击**Save**并选择**Download this recipe**。用本地服务器制作一本 Kindle 电子书只需不到一分钟。

## 资源

 [最新版的Kindle电子书](https://t.me/master_thyself/285)
 [Custom news fetching](https://blog.calibre-ebook.com/custom-news-fetching/)
