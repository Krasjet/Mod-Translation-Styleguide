# Minecraft Mod翻译规范与指南

为了Minecraft中Mod翻译的统一，玩家良好的体验，以及中文Minecraft Mod社区的统一，本文档将对Mod翻译事项进行规定，同时也会提供翻译所需的相关资料以及工具。希望各位Mod翻译者能尽量遵守本文档中的一些指示，将翻译文件标准化。

对规范或者例子中提到的译文如果有改进的欢迎提交Pull Request。

本文档采用[WTFPL](http://www.wtfpl.net/about/)协议，但对本文档的传播请链接至本工程。

## 01.普适原则

- **以原文为准**，除非原文实在无法简明翻译，不要存在意译
	- 原文一般为 `en_US.lang` 文件内的内容
	- 但如果是日站mod或者其它语言的mod请参考对应的语言文件
- 符合中文表达习惯，如果无法转换则改写句子形式
	- 比如手册中存在的定语从句
	- 原文：`The Red Cedar Tree is a large tree that has magical properties.`([Totemic](https://github.com/TeamTotemic/Totemic)，TeamTotemic)
	- 译文：`高大无比的红柏树有着魔法的属性。`
- 不需要保留英文原文

## 02.保留字符

- 在每一个词条中等于号 `=` 作为分隔符，在等于号两旁请**不要**留空格，除非原文中就已经包含了空格
- 某些词条中出现的 `%s`、`%d` 等格式字符或以 `%` 围起来的字符串（如 `%msg%`），请保留这些字符串，并可以根据中文语序做出调整，它们会在代码中被替换为对应的文本，如果不确定最终效果，请打开游戏进行测试
- 在某些mod的手册中会使用 `<br>` 作为换行符，遇到时请保留
- 某些mod使用 `&` 或者 `§` 后加一个字符或者数字表示颜色或者格式，在此标识出现后的文字都将变成对应的颜色或者格式，一般使用 `&0` 或者 `§0` 恢复默认颜色，`&r` 或者 `§r` 恢复默认格式。遇到时请保留，并将其放到对应文本两侧
	- 具体字符含义请参考Minecraft Wiki：[http://minecraft.gamepedia.com/Formatting_codes](http://minecraft.gamepedia.com/Formatting_codes)
- 在遇到JSON字符串的时候，请**仅**翻译 `"text"` 项的值，对于其它的键和值请保留均不翻译
	- 原文：`{"text":" has shared a ","color":"blue"}`([Botania](https://github.com/Vazkii/Botania)，Vazkii)
	- 译文：`{"text":"分享了一本","color":"blue"}`
- 少数mod使用XML格式的语言文件，对于这种文件请保留以 `<` 和 `>` 开头结尾的标签
- 能量单位（EU、MJ等）请保留不翻译

## 03.标点符号

- 请与原版Minecraft保持统一，使用中文的标点符号
	- 原文：`Weighted Pressure Plate (Heavy)`(Minecraft, Mojang)
	- 译文：`测重压力板（重质）`
- 遵守《标点符号用法》：[http://people.ubuntu.com/~happyaron/l10n/GB(T)15834-2011.html](http://people.ubuntu.com/~happyaron/l10n/GB(T)15834-2011.html)
- 对于英文标点符号前或后的空格，请在修改标点符号为中文时删除
- 仅修改文本当中的标点符号，对于JSON的格式标点符号请保留

## 04.专有名词

- 除非有通用翻译以外的外文人名请保留不要翻译
	- 如牛顿、阿基米德等
- 对于原版中出现过的词语请根据Minecraft Wiki上的[译名标准列表](http://minecraft-zh.gamepedia.com/Minecraft_Wiki:%E8%AF%91%E5%90%8D%E6%A0%87%E5%87%86%E5%8C%96)进行翻译（注意默认方块、实体、物品是隐藏的，需要手动点击显示）
- 参考本工程的[译名标准化列表]()进行翻译
- 如果还没有找到，请自行拟定翻译，并发送PR更新本工程的译名标准化列表

## 05.署名

- 除非作者在语言文件中专门提供了翻译者署名的地方，请不要添加任何其它标识标明翻译者的名字，特别是作者让你签署CLA的情况。你的贡献将会在文件上方的Contribution处显示