# 算法

## 你所拥有的工具：

### 数据结构

list

array

heap

binary search trees

AVL树

stack （`pop`方法用来删除，并返回数值）

### python+数据结构

+ 指针：$ \Theta(1) ​$

+ `list` 类型（RAM）：$ \Theta(1) ​$

  + `L.append(x)`：$ \Theta(1) $ （table doubling）
  + `L = L1+L2`：$ \Theta(1+|L1|+|L2|) $
  + `L.extend(L2)`：$ \Theta(1+|L2|) $
  + `L2 = L1[i:j]`：$ O(|L|) ​$
  + 查找任意元素 `L.find(x)`，`L.index(x)`，`b = x in L`：$ O(|L|) $
  + `len(L)`：$ \Theta(1) ​$
  + `L.sort()`：$ \Theta(|L| \lg |L|) ​$：归并排序

+ `tuple` `str`  类型：差不多的，只是没法改，但是**省内存空间~**

+ `dict` 类型：

  ```python
  D[key] = val
  key in D
  ```

  均花费 $ \Theta(1) ​$ 时间，hashing。

+ `set` 类型：不包含value的 `dict`。

  list可以直接转换为set：`set(list1)`

+ `heap`：push/pop：$ \Theta(\lg n) $

+ `long` ：`x+y`：$O(|x|+|y|)$

  からつば algorithm

### 基础算法

搜索下限 $\Omega(\lg n )$，排序下限 $\Omega (n \lg n)$。

+ 冒泡排序：$ \Theta(n^2) $
+ 归并排序：$ \Theta(n \lg n) $
+ 堆排序：$ \Theta(n \lg n) $
+ BST排序：$\Theta(n \lg n)$ →搜索 $\Theta (\lg n)$，但若极度不平衡 直接变成 $\Theta(n)$
+ AVL排序：$\Theta(n \lg n + n)$ ，（多出了调整为avl的复杂度）搜索时保证 $\Theta (\lg n)$。
+ 计数排序： $O(n)$，针对已知的整数，→radix sort（按基底分数组，$\Theta(n \log_n k)$）
+ 深度搜索+堆栈，可以在保证空间复杂度的情况下进行状态累计。

## 你所拥有的，进阶的工具

+ Kadane算法：解决最大子数列问题，$\Theta (n)$。

