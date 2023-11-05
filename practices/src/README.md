## 编译C为动态库
```sh
 gcc -shared -o demo.dylib -fPIC demo.c 
```

## 监听C文件改变编译
```sh
pyhton3 watch.py
```

## C文件引入其他库
```sh
# 需要一起执行
gcc main.c demo.c -o <target>
```
## Python With C
通过在 Python 中调用 C，你可以利用 C 的高性能特性来执行一些有趣的任务。以下是一些你可以做的事情：

- 加速计算： C 通常比 Python 运行得更快，特别是对于复杂的数值计算。你可以将一些计算密集型任务委托给 C，从而提高程序的执行速度。
- 访问硬件： 如果你需要与硬件进行交互，如传感器、摄像头、音频设备等，C 可以更好地直接访问底层硬件。
- 图像处理： C 可以用于实现高性能的图像处理算法，如滤波、边缘检测等。
- 游戏开发： 如果你对游戏开发感兴趣，C 可以用于实现游戏引擎和高性能游戏逻辑。
- 编写扩展模块： 你可以将一些核心功能用 C 实现，然后将其封装为 Python 扩展模块，从而在 Python 中调用高性能的 C 代码。
- 并行计算： C 可以用于编写多线程和多进程的代码，以实现并行计算，充分利用多核处理器的能力。
- 加密和安全性： C 可以用于实现加密算法和安全性功能，如密码学算法和身份验证。
- 嵌入式系统开发： C 通常用于嵌入式系统开发，如物联网设备、嵌入式控制器等。
- 优化和调试： 通过在 C 中实现一些关键部分，你可以更方便地进行性能优化和调试，从而提高整体代码质量。

总之，通过在 Python 中调用 C，你可以将 Python 的高级特性和易用性与 C 的高性能和底层控制结合起来，实现更多有趣和复杂的任务。

## python执行原理
是的，Python 和 PHP 在某些执行机制方面的确有相似之处，因为它们都属于解释型语言，并且都具有动态类型、脚本语言的特性。以下是一些 Python 和 PHP 相似的执行机制：

1. **解释型语言：** Python 和 PHP 都是解释型语言，不需要预先编译成机器代码，而是由解释器逐行解释和执行。

2. **动态类型：** Python 和 PHP 都是动态类型语言，变量的类型在运行时确定，而不是在编译时。

3. **脚本语言：** Python 和 PHP 都被广泛用作脚本语言，用于快速开发、自动化和网页开发。

4. **执行单元：** 在交互式环境中，Python 和 PHP 的执行单位都是单个语句。在脚本中，它们的执行单位是一行代码。

5. **模块和导入：** Python 和 PHP 都支持模块的概念，允许代码组织成不同的文件，并在其他代码中导入和使用。

6. **异常处理：** Python 和 PHP 都提供异常处理机制，用于捕获和处理在运行时发生的错误。

7. **动态解释器：** Python 和 PHP 都使用动态解释器来处理代码，解释器会根据代码的上下文和执行路径进行逐行解释。

虽然 Python 和 PHP 有相似的执行机制，但它们的语法、标准库和应用领域可能有所不同。然而，这些相似之处使得从一种语言切换到另一种语言变得相对容易，因为你可以将一些基本的编程概念和技能应用到不同的语言中。

### 字节码

Python 的字节码通常被存储在 `.pyc` 文件中，这些文件是由 Python 解释器在首次运行一个脚本时自动生成的。`.pyc` 文件包含了 Python 源代码编译后的字节码，这样在以后的运行中，Python 解释器可以直接加载字节码而不必重新编译源代码。

当你运行一个 `.py` 脚本时，Python 解释器会检查是否已经存在对应的 `.pyc` 文件。如果存在，解释器将尝试加载并执行该 `.pyc` 文件的字节码，从而提高执行速度。如果 `.pyc` 文件不存在或过期（即源代码已经更改），Python 解释器会重新编译源代码并生成新的 `.pyc` 文件。

`.pyc` 文件通常存储在与源代码文件相同的目录中，但是在 Python 的 `__pycache__` 子目录中。这是为了防止不同版本的 Python 解释器之间的冲突。

需要注意的是，`.pyc` 文件不是在每次运行脚本时都会生成的，而是根据需要进行生成和更新。如果你希望强制重新生成 `.pyc` 文件，你可以删除对应的文件，然后重新运行脚本。

## codewars
[Link](https://www.codewars.com/kata/search/my-languages?q=&r%5B%5D=-5&xids=played&beta=false&order_by=popularity%20desc)