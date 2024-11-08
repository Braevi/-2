
# 测试文档

### 第一关: 基本测试

根据S-AES算法编写和调试程序, 提供GUI解密支持用户交互. 输入可以是16bit的数据和16bit的密钥，输出是16bit的密文.

##### 加密:

![]([-2/1_1.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/1_1.png))

##### 解密:

![]([-2/1_2.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/1_2.png))

### 第二关: 交叉测试

考虑到是"**算法标准"**，所有人在编写程序的时候需要使用相同算法流程和转换单元(替换盒、列混淆矩阵等)，以保证算法和程序在异构的系统或平台上都可以正常运行。设有A和B两组位同学(选择相同的密钥K)；则A、B组同学编写的程序对明文P进行加密得到相同的密文C；或者B组同学接收到A组程序加密的密文C，使用B组程序进行解密可得到与A相同的P。

我们与其他组进行交叉测试，双方采用相同的密钥1111111100000000对明文1111111111111111进行加密：

##### 我们的测试结果:

![]([-2/2_1.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/2_1.png))

##### 他们的测试结果:

![]([-2/2_2.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/2_2.png))

（十进制密文12420转换成二进制为0011000010000100与我们的结果一样）

测试结果：得到了相同结果，测试通过。

### 第三关: 扩展功能

 考虑到向实用性扩展，加密算法的数据输入可以是ASCII编码字符串(分组为2 Bytes)，对应地输出也可以是ASCII字符串(很可能是乱码)。对于奇数长度的字符串，我们采取才字符串末尾加上一个空格来保障加解密的正常进行。程序设计了使用字符串的形式进行输入和输出的模式，只需要切换到String模式即可将字符串加密或将密文（字符串形式）解密为明文字符串：

![]([-2/3_1.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/3_1.png))

### 第四关: 多重加密

*双重加密*：

 将S-AES算法通过双重加密进行扩展，分组长度仍然是16 bits，但使用两个16bits的密钥。

![]([-2/4_1.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/4_1.png))

![]([-2/4_2.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/4_2.png))

*中间相遇攻击*：

假设找到了使用相同密钥的明、密文对(一个或多个)，请尝试使用中间相遇攻击的方法找到正确的密钥Key(K1+K2)。

![]([-2/4_3.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/4_3.png))

*多重加密*：

将S-AES算法通过三重加密进行扩展，使用一组三个16bits的密钥(K1+K2+K3)的模式进行三重加解密。

![]([-2/4_4.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/4_4.png))

![]([-2/4_5.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/4_5.png))

### 第五关: 工作模式

基于S-AES算法，使用密码分组链(CBC)模式对较长的明文消息进行加密。注意初始向量(16 bits) 为随机生成。

 在CBC模式下进行加密，并尝试对密文分组进行替换或修改，然后进行解密，请对比篡改密文前后的解密结果。

*CBC模式加解密*：

![]([-2/5_1.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/5_1.png))

*CBC模式混淆*：

![]([-2/5_2.png at main · Braevi/-2](https://github.com/Braevi/-2/blob/main/5_2.png))
