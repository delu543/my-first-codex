# my-first-codex

这是一个非常精简的 Python 入门仓库，目前包含：

- `README.md`：项目说明文档。
- `hello.py`：第一个示例（打印一句话）。
- `test.py`：第二个示例（变量 + 简单计算 + 打印）。

## 第一步：运行 hello.py

在仓库根目录打开终端，执行：

```bash
python3 hello.py
```

你会看到：

```text
Hello, world!
```

## hello.py 是怎么运行的（最简单理解）

`hello.py` 代码只有一行：

```python
print("Hello, world!")
```

你可以这样理解：

1. `python3 hello.py` 的意思是：让 **Python 解释器** 打开并执行这个文件。
2. Python 会从上到下读代码。
3. 读到 `print(...)` 时，就把括号里的文字输出到终端。

## 第二步：运行 test.py

执行：

```bash
python3 test.py
```

你会看到类似输出：

```text
This is test.py
name = beginner
2 + 3 = 5
```

这个例子说明了三件事：

- 可以用变量保存内容（如 `name`）。
- 可以做简单计算（如 `2 + 3`）。
- 也可以用 `print()` 把变量和结果显示出来。
