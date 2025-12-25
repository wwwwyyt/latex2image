# LaTex2Image

这是一个简单的可视化转化 LaTex 公式为图片的小工具。在点击“转化”按钮后，可以将文本框中的 LaTex 公式转为图片。图片会显示在下方的图片框里，也会在工作目录下生成一个 png 图片。

但是，它无法显示中文，也无法支持多行 LaTex ，无法支持某些语法。有些公式也有显示问题。

## 依赖环境

需要安装 pygubu 、pillow 和 matplotlib ：

```
pip install -U pygubu pillow matplotlib
```

## 使用方式

在命令行运行：

```
python latex2image.py
```

或者

```
python3 latex2image.py
```

总之，将它当作一个正常的 Python 脚本运行起来。

