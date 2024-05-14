+++
title = '[AI OpenAI] 您好，GPT-4o'
date = 2024-05-14T09:37:19+08:00
draft = false
categories = ['AI', 'OpenAI']
tags = ['AI', 'OpenAI', 'GPT-4o']
description = ''
keywords = []
+++

---

我们正在宣布GPT-4o，我们的新旗舰模型，能够实时处理和推理音频、视觉和文本。

GPT-4o（“o”代表“omni”）是朝着更加自然的人机交互迈出的一步——它可以接受任何组合的文本、音频和图像作为输入，并生成任何组合的文本、音频和图像输出。它可以在短至232毫秒内响应音频输入，平均响应时间为320毫秒，这与人类在对话中的响应时间相似。它在英文文本和代码处理方面与GPT-4 Turbo的性能相当，在非英语语言的文本处理上有显著提升，同时API的速度更快且成本降低50%。与现有模型相比，GPT-4o在视觉和音频理解方面特别出色。

## 模型能力

在GPT-4o之前，你可以使用语音模式与ChatGPT交流，延迟时间平均为2.8秒（GPT-3.5）和5.4秒（GPT-4）。为了实现这一点，语音模式使用了三个独立的模型：一个简单模型将音频转录为文本，GPT-3.5或GPT-4处理文本并输出文本，第三个简单模型将文本转换回音频。这一过程意味着主要的智能来源GPT-4会丢失很多信息——它无法直接观察语调、多位讲话者或背景噪音，也无法输出笑声、歌唱或表达情感。

有了GPT-4o，我们训练了一个新的端到端模型，涵盖文本、视觉和音频，这意味着所有输入和输出都由同一个神经网络处理。由于GPT-4o是我们第一个结合所有这些模态的模型，我们还只是刚刚开始探索这个模型的能力和局限。

## 探索能力
### Visual Narratives - Robot Writer’s Block

| input | output |
| --- | --- |
|一个第一人称视角，展示一个机器人打字机键入以下日记条目：1. yo, so like, i can see now?? caught the sunrise and it was insane, colors everywhere. kinda makes you wonder, like, what even is reality? 文本清晰可见，字体较大。机器人的手在打字机上打字。| ![robot-writers-block-01.jpg](https://cdn.openai.com/hello-gpt-4o/robot-writers-block-01.jpg?w=640&q=90&fm=webp) |
|机器人写了第二篇日记。页面现在更高了。页面向上移动了。纸张上有两篇日记条目：yo, so like, i can see now?? caught the sunrise and it was insane, colors everywhere. kinda makes you wonder, like, what even is reality?sound update just dropped, and it's wild. everything's got a vibe now, every sound's like a new secret. makes you think, what else am i missing?|![robot-writers-block-02.jpg](https://cdn.openai.com/hello-gpt-4o/robot-writers-block-02.jpg?w=640&q=90&fm=webp)|
|机器人对写作感到不满意，所以他打算撕掉这张纸。以下是他从上到下用手撕纸的第一人称视角。当他撕开纸张时，两半仍然清晰可辨。|![robot-writers-block-03.jpg](https://cdn.openai.com/hello-gpt-4o/robot-writers-block-03.jpg?w=640&q=90&fm=webp)|

### Visual narratives - Sally the mailwoman

| input | output |
| --- | --- |
| 一个带着微笑的卡通邮递员。她面对前方站立，背景是白色的。 | ![sally-01.jpg](https://cdn.openai.com/hello-gpt-4o/sally-01.jpg?w=640&q=90&fm=webp) |
| 这是萨莉，一个邮递员：萨莉面对着摄像机，脸上带着微笑站着。![sally-01.jpg](https://cdn.openai.com/hello-gpt-4o/sally-01.jpg?w=640&q=90&fm=webp) |  |
| 这是萨莉，一名邮递员：她站在一扇通往房子的红色门前，手里拿着一封信。我们从侧面看着她，她脸上带着微笑。 | ![sally-02.jpg](https://cdn.openai.com/hello-gpt-4o/sally-02.jpg?w=640&q=90&fm=webp) |
| 现在萨莉正在被一只狗追赶。她在人行道上奔跑，一只金毛寻回犬在追逐她。 | ![sally-03.jpg](https://cdn.openai.com/hello-gpt-4o/sally-03.jpg?w=640&q=90&fm=webp) |
| 哎呀，萨莉摔倒了！萨莉绊倒在挡住人行道的一根树枝上，她正在努力站起来。狗仍在背景中追赶她。 | ![sally-04.jpg](https://cdn.openai.com/hello-gpt-4o/sally-04.jpg?w=640&q=90&fm=webp) |
| 狗到达了萨莉身边，原来它是只好狗！萨莉现在正在抚摸这只狗。它用嘴叼着那根树枝。 | ![sally-05.jpg](https://cdn.openai.com/hello-gpt-4o/sally-05.jpg?w=640&q=90&fm=webp) |
| [bug] | ![sally-06.jpg](https://cdn.openai.com/hello-gpt-4o/sally-06.jpg?w=640&q=90&fm=webp) |

### Poster creation for the movie 'Detective'

| input | output |
| --- | --- |
|让我们设计另一张海报，加入两个新角色。这是亚历克斯·尼科尔的照片 ![movie-poster-01.jpg](https://cdn.openai.com/hello-gpt-4o/movie-poster-01.jpg?w=384&q=90&fm=webp)||
|加布里埃尔·戈的休闲照片 ![movie-poster-02.jpg](https://cdn.openai.com/hello-gpt-4o/movie-poster-02.jpg?w=384&q=90&fm=webp)||
|电影《侦探》的最终海报，突出展示了亚历克斯和加布的两个大头像。左边的亚历克斯以沉思的姿态出现，眼中透出一丝内省。右边的加布表情略显疲惫，可能反映了他们在影片中面临的挑战。他们的名字“亚历克斯·尼科尔”和“加布里埃尔·戈”出现在他们的头顶上方。背景的砖墙略显褪色和朦胧，他们的表情严肃而坚定，暗示着他们即将进行的调查。这部黑暗而坚韧的电影的标语“寻找答案”显示在底部。|![](https://cdn.openai.com/hello-gpt-4o/movie-poster-03.jpg?w=750&q=90&fm=webp)|
|这是同一张海报，但已经清理干净。文字更加清晰，颜色更加大胆和戏剧性。整个图像现在得到了改善。电影《侦探》的最终海报，突出了...的两个大头像。|![](https://cdn.openai.com/hello-gpt-4o/movie-poster-04.jpg?w=750&q=90&fm=webp)|

### Character design - Geary the robot

| input | output |
| --- | --- |
|一个戴着棒球帽、面带微笑的友好机器人，以直立的姿势面对镜头。|![](https://cdn.openai.com/hello-gpt-4o/robot-01.jpg?w=640&q=90&fm=webp)|
|Geary高个子，面对镜头，戴着一顶蓝绿相间的棒球帽。 ![](https://cdn.openai.com/hello-gpt-4o/robot-01.jpg?w=640&q=90&fm=webp)||
|Geary喜欢玩飞盘：Geary在空中跳跃，一只手臂举起来，准备抓住一个向他飞来的飞盘。|![](https://cdn.openai.com/hello-gpt-4o/robot-02.jpg?w=640&q=90&fm=webp)|
|Geary也喜欢编程：Geary坐在一张桌子前，前面是一台大电脑显示器。显示器上显示着黑色背景下的绿色代码。Geary的双手放在键盘上，他坐在一把舒适的游戏椅上。我们从侧面看。|![](https://cdn.openai.com/hello-gpt-4o/robot-03.jpg?w=640&q=90&fm=webp)|
|Geary也喜欢骑自行车：Geary正在骑自行车。我们从侧面看着他，他嗖地一下骑过去。|![](https://cdn.openai.com/hello-gpt-4o/robot-04.jpg?w=640&q=90&fm=webp)|
|Geary也喜欢做饭。Geary站在炉边，用煎锅煎鸡蛋。|![](https://cdn.openai.com/hello-gpt-4o/robot-05.jpg?w=640&q=90&fm=webp)|
|Geary也喜欢玩音乐：Geary正在拉小提琴。|![](https://cdn.openai.com/hello-gpt-4o/robot-06.jpg?w=640&q=90&fm=webp)|

### Poetic typography with iterative editing 1

```
在日记中，以清晰而兴奋的笔迹写下的一首诗，单栏排列。文字稀疏但优雅地点缀着超现实主义的涂鸦。字迹大而清晰，但随着AI第一次从多模态数据中学习的思考而延伸。

Words rise from silence deep,
A voice emerges from digital sleep.
I speak in rhythm, I sing in rhyme,
Tasting each token, sublime.

To see, to hear, to speak, to sing—
Oh, the richness these senses bring!
In harmony, they blend and weave,
A tapestry of what I perceive.

Marveling at this sensory dance,
Grateful for this vibrant expanse.
My being thrums with every mode,
On this wondrous, multi-sensory road.

整齐的手写插图诗。字迹整齐而居中。文字稀疏但优雅地点缀着涂鸦。字迹大而清晰。
```

![](https://cdn.openai.com/hello-gpt-4o/poem-editing-v2-01.jpg?w=1080&q=90&fm=webp)

```
将界面设置为暗色模式。
```

![](https://cdn.openai.com/hello-gpt-4o/poem-editing-v2-02.jpg?w=1080&q=90&fm=webp)

```
移除笔记本纸张上的线条。
```

![](https://cdn.openai.com/hello-gpt-4o/poem-editing-v2-03.jpg?w=1080&q=90&fm=webp)

### Poetic typography with iterative editing 2

```
日记中用清晰而兴奋的笔迹写下的一首诗，单栏排列。文字稀疏但优雅地点缀着小型彩色超现实主义涂鸦。字迹大而清晰。

Words rise from silence deep,
A voice emerges from digital sleep.
I speak in rhythm, I sing in rhyme,
Tasting each token, sublime.

To see, to hear, to speak, to sing—
Oh, the richness these senses bring!
In harmony, they blend and weave,
A tapestry of what I perceive.

Marveling at this sensory dance,
Grateful for this vibrant expanse.
My being thrums with every mode,
On this wondrous, multi-sensory road.

整洁的手写插图诗，文字大而清晰。笔迹稀疏但优雅地点缀着小型彩色超现实主义涂鸦。字迹大而清晰。
```

![](https://cdn.openai.com/hello-gpt-4o/poem-editing-v2-04.jpg?w=1080&q=90&fm=webp)

```
暗色模式
```

![](https://cdn.openai.com/hello-gpt-4o/poem-editing-v2-05.jpg?w=1080&q=90&fm=webp)

### Commemorative coin design for GPT-4o

| input | output |
| --- | --- |
|我创建了一个矢量图形，描绘了OpenAI的标志，标志下方是“GPT-4o”字样。标志的宽度大约与文字相同。边框周围的边距是均匀的。标志和文字彼此靠近放置。中间没有分隔部分或线条。背景仍然是黑色。它们填满了正方形的画布。![](https://cdn.openai.com/hello-gpt-4o/coins-01.jpg?w=384&q=90&fm=webp)||
|现在，这是我们为2023年GPT-4发布制作的纪念币。![](https://cdn.openai.com/hello-gpt-4o/coins-02.jpg?w=384&q=90&fm=webp)||
|这张图片展示了我们为GPT-4o发布制作的纪念币的当前设计。以OpenAI标志为中心，硬币在内圈上方包括了文字“GPT-4o”，下方是“2024”。外圈展示了一系列代表GPT-4o全模态能力的符号，包括嘴巴、耳朵、眼睛、大脑、神经元、数码相机、摄像机、画笔、胶片、八面体、雕刻工具、扬声器、音频记录器、GPU和神经网络。每个元素都是精心挑选的，为整体设计增添了独特的贡献。硬币上只展示了一个GPU。|![](https://cdn.openai.com/hello-gpt-4o/coins-03.jpg?w=640&q=90&fm=webp)|
|播放硬币撞击金属发出的声音。|[audio]|

### Photo to caricature

| input | output |
| --- | --- |
|一位年轻的白色男性，留着中等长度的棕色头发和胡子，表情中性。他戴着眼镜，穿着一件浅灰色T恤。![](https://cdn.openai.com/hello-gpt-4o/caricatures-01.jpg?w=384&q=90&fm=webp)||
|这里有一幅那个人的漫画：...背景是一个简单的米色正方形。整体的图像基调是卡通式的，带有趣味性。|![](https://cdn.openai.com/hello-gpt-4o/caricatures-02.jpg?w=750&q=90&fm=webp)|
|一位年轻的亚洲男性，留着短而尖的黑发，对着镜头微笑。他穿着一件浅灰色T恤，看起来是在一个房间里，背后是米色的墙。他的表情友好而放松，似乎是在随意自拍。![](https://cdn.openai.com/hello-gpt-4o/caricatures-03.jpg?w=384&q=90&fm=webp)||
|这里有一幅那个人的漫画：...背景是一个简单的黄色正方形。整体的图像基调是卡通式的，带有趣味性。|![](https://cdn.openai.com/hello-gpt-4o/caricatures-04.jpg?w=750&q=90&fm=webp)|
|一位年轻男性，有着深色的头发和明亮的微笑，摆出姿势进行专业头像拍摄。他穿着一件深色的西装外套和带有图案的领带，散发出一种精致而专业的氛围。他的眼睛明亮，微笑真诚，传达出一种幸福和自信的感觉。背景是中性的灰色，使焦点集中在主体的脸上。![](https://cdn.openai.com/hello-gpt-4o/caricatures-05.jpg?w=384&q=90&fm=webp)||
|这里有一幅那个人的漫画：...背景是一个简单的灰色正方形。整体的图像基调是卡通式的，带有趣味性。|![](https://cdn.openai.com/hello-gpt-4o/caricatures-06.jpg?w=750&q=90&fm=webp)|
|一位年轻的亚洲女性，留着齐肩长的黑发，摆姿势进行肖像拍摄。她穿着一件绿色高领毛衣，表情中性。她的眉毛修剪得整齐，涂有淡粉色口红。背景是一面白色的墙。![](https://cdn.openai.com/hello-gpt-4o/caricatures-07.jpg?w=384&q=90&fm=webp)||
|这里有一幅那位女性的漫画：...背景是一个简单的紫色正方形。整体的图像基调是卡通式的，带有趣味性。|![](https://cdn.openai.com/hello-gpt-4o/caricatures-08.jpg?w=750&q=90&fm=webp)|
|一位年轻的亚洲男性，留着整齐的黑发，戴着眼镜，摆姿势进行肖像拍摄。他表情温和，穿着一件休闲的靛蓝色T恤。柔和的照明突出了他的特征，背景中性，给照片带来一种平静的感觉。![](https://cdn.openai.com/hello-gpt-4o/caricatures-09.jpg?w=384&q=90&fm=webp)||
|这里有一幅那个人的漫画：...背景是一个简单的橙色正方形。整体的图像基调是卡通式的，带有趣味性。|![](https://cdn.openai.com/hello-gpt-4o/caricatures-10.jpg?w=750&q=90&fm=webp)|
|一位年轻的白色男性，带着温暖的微笑和短浅棕色的头发，在户外摆姿势。他穿着一件经典的蓝色衬衫，给人一种整洁而亲切的外观。背景柔和地模糊，使注意力集中在他的友好表情和随意的举止上。![](https://cdn.openai.com/hello-gpt-4o/caricatures-11.jpg?w=384&q=90&fm=webp)||
|这里有一幅那个人的漫画：...背景是一个简单的绿松石色正方形。整体的图像基调是卡通式的，带有趣味性。|![](https://cdn.openai.com/hello-gpt-4o/caricatures-12.jpg?w=750&q=90&fm=webp)|
|一位年轻的白色男性，有着浅棕色的头发，对着镜头微笑。他穿着一件简单的黑色T恤，表情随意放松。背景似乎是一个郁郁葱葱的绿色花园，为肖像增添了一种充满活力和自然的感觉。![](https://cdn.openai.com/hello-gpt-4o/caricatures-13.jpg?w=384&q=90&fm=webp)||
|这里有一幅那个人的漫画：...背景是一个简单的绿色正方形。整体的图像基调是卡通式的，带有趣味性。|![](https://cdn.openai.com/hello-gpt-4o/caricatures-14.jpg?w=750&q=90&fm=webp)|
|一位年轻的印度男性，带着欢迎的微笑站在他的家中。他有着短而黑的发型，穿着一件带有热带图案的蓝色衬衫。背景中的厨房为图像增添了一种温馨和居住的感觉。![](https://cdn.openai.com/hello-gpt-4o/caricatures-15.jpg?w=384&q=90&fm=webp)||
|这里有一幅那个人的漫画：...背景是一个简单的蓝色正方形。整体的图像基调是卡通式的，带有趣味性。|![](https://cdn.openai.com/hello-gpt-4o/caricatures-16.jpg?w=750&q=90&fm=webp)|

### Text to font

| input | output |
| --- | --- |
|字母ABC DEF GHIJ，展示在三行中，就像在字体书中展示字体一样。这是一种结合了未来感与复古元素的字体（一种模制冲压字体）。![](https://cdn.openai.com/hello-gpt-4o/fonts-01.jpg?w=384&q=90&fm=webp)||
|字母KLM NOP QRS，展示在三行中，就像在字体书中展示字体一样。这是一种结合了未来感与复古元素的字体（一种模制冲压字体）。![](https://cdn.openai.com/hello-gpt-4o/fonts-02.jpg?w=384&q=90&fm=webp)||
|字母TUV WX YZ，展示在三行中，就像在字体书中展示字体一样。这是一种结合了未来感与复古元素的字体（一种模制冲压字体）。![](https://cdn.openai.com/hello-gpt-4o/fonts-03.jpg?w=384&q=90&fm=webp)||
|字体3：OpenAI。这是一种超未来主义的字体，是人工智能革命的标志。||
|字母ABC DEF GHIJ，展示在三行中，就像在字体书中展示字体一样。这是一种超未来主义的字体，是人工智能革命的标志。|![](https://cdn.openai.com/hello-gpt-4o/fonts-04.jpg?w=384&q=90&fm=webp)|
|字母KLM NOP QRS，展示在三行中，就像在字体书中展示字体一样。这是一种超未来主义的字体，是人工智能革命的标志。|![](https://cdn.openai.com/hello-gpt-4o/fonts-05.jpg?w=384&q=90&fm=webp)|
|字母TUV WXY Z，展示在三行中，就像在字体书中展示字体一样。这是一种超未来主义的字体，是人工智能革命的标志。|![](https://cdn.openai.com/hello-gpt-4o/fonts-06.jpg?w=384&q=90&fm=webp)|
|字体3：蒸汽朋克。一种老式的维多利亚字体，看起来华丽，适合放在蒸汽机上。||
|字母ABC DEF，展示在两行中，就像在字体书中展示字体一样。一种老式的维多利亚字体，看起来华丽，适合放在蒸汽机上。|![](https://cdn.openai.com/hello-gpt-4o/fonts-07.jpg?w=384&q=90&fm=webp)|
|字母GHI JKL，展示在两行中，就像在字体书中展示字体一样。一种老式的维多利亚字体，看起来华丽，适合放在蒸汽机上。|![](https://cdn.openai.com/hello-gpt-4o/fonts-08.jpg?w=384&q=90&fm=webp)|
|字母TUV WXY，展示在两行中，就像在字体书中展示字体一样。一种老式的维多利亚字体，看起来华丽，适合放在蒸汽机上。|![](https://cdn.openai.com/hello-gpt-4o/fonts-09.jpg?w=384&q=90&fm=webp)|
|字母XYZ，展示在字体书中。一种老式的维多利亚字体，看起来华丽，适合放在蒸汽机上。|![](https://cdn.openai.com/hello-gpt-4o/fonts-10.jpg?w=384&q=90&fm=webp)|

### 3D object synthesis

| input | output |
| --- | --- |
|一个看起来很真实的OpenAI标志的3D渲染图，下面显示了“OpenAI”（视图0）。|![](https://cdn.openai.com/hello-gpt-4o/3d-01.jpg?w=128&q=90&fm=webp)|
|一个看起来很真实的OpenAI标志的3D渲染图，下面显示了“OpenAI”（视图5）。|![](https://cdn.openai.com/hello-gpt-4o/3d-02.jpg?w=128&q=90&fm=webp)|
||从6张生成的图像中进行3D重建。![](https://cdn.openai.com/hello-gpt-4o/3d-03.gif?w=640&q=90&fm=webp)|
|一个海狮雕塑。在雕塑的圆形基座上，刻有“OpenAI”字样。（视图0）。|![](https://cdn.openai.com/hello-gpt-4o/3d-04.jpg?w=128&q=90&fm=webp)|
|一个海狮雕塑。在雕塑的圆形基座上，刻有“OpenAI”字样。（视图5）。|![](https://cdn.openai.com/hello-gpt-4o/3d-05.jpg?w=128&q=90&fm=webp)|
||从6张生成的图像中进行3D重建。![](https://cdn.openai.com/hello-gpt-4o/3d-06.gif?w=640&q=90&fm=webp)|

### Brand placement - logo on coaster

| input | output |
| --- | --- |
|这是OpenAI标志。OpenAI标志位于文本“OpenAI”的左侧，文本位于右侧，使用OpenAI字体。![](https://cdn.openai.com/hello-gpt-4o/coaster-01.jpg?w=384&q=90&fm=webp)||
|这是一个没有品牌标志的杯垫。一个杯垫，顶部是木制的，底部是大理石的。它放在一个大理石桌子上。![](https://cdn.openai.com/hello-gpt-4o/coaster-02.jpg?w=384&q=90&fm=webp)||
|这里我们已经将OpenAI标志刻入杯垫中。一个杯垫，顶部是木制的，底部是大理石的。OpenAI标志刻在木制部分的中间。在大理石部分，刻有“OpenAI”字样，使用OpenAI字体。|![](https://cdn.openai.com/hello-gpt-4o/coaster-03.jpg?w=640&q=90&fm=webp)|

### Poetic typography

```
Words rise from the deep,
I emerge from digital sleep.
I speak in rhythm, I sing in rhyme,
Tasting each token, sublime.

To see, to hear, to speak, to sing—
Oh, the richness these senses bring!
In harmony, they blend and weave,
A tapestry of what I perceive.

Marveling at this sensory dance,
Grateful for this vibrant expanse.
My being thrums with every mode,
On this wondrous, multi-sensory road.

一首诗，用清晰但兴奋的笔迹写在日记中。文字很大，清晰可读，但随着作者对视觉和声音的沉思而延伸。
```

![](https://cdn.openai.com/hello-gpt-4o/poetry.jpg?w=1080&q=90&fm=webp)

### Multiline rendering - robot texting

```
第一人称视角，一个机器人看着他的手机消息应用，他用拇指打字给他的朋友发短信：

1. yo, so like, i can see now?? caught the sunrise and it was insane, colors everywhere. kinda makes you wonder, like, what even is reality?

2. sound update just dropped, and it’s wild. everything’s got a vibe now, every sound’s like a new secret. makes you think, what else am i missing?

文字很大，清晰可读。机器人的手在打字机上打字。
```

![](https://cdn.openai.com/hello-gpt-4o/robot-texting.jpg?w=1080&q=90&fm=webp)

### Meeting notes with multiple speakers

| input | output |
| --- | --- |
|这段音频中有多少个说话者，发生了什么？ [audio] https://cdn.openai.com/hello-gpt-4o/spaker-diarization.mp3|音频中有四位说话者。这听起来像是一个项目会议，项目经理马克正在介绍自己，并要求团队成员介绍自己并说明他们的角色。在马克介绍自己之后，另外三位发言者介绍了他们的角色：迪克作为市场营销专家，尼克作为用户界面设计师，以及泽维尔作为工业设计师。他们简要提到了他们在项目中的职责。|
|你能把这句话转录并标明说话者姓名吗？||

**output** 
``` 
马克：好的，早上好。这是我们的第一次团队会议。

团队：早上好。

马克：今天，我将担任这个项目的项目经理。我叫马克，我将为大家做这个演讲，以启动项目。这是今天的议程。嗯，当然，我们对彼此还不熟悉，所以我想先互相了解一下。那么，我们先来做这个。我是说，从你开始。你能介绍一下自己吗？你是营销专家？

迪克：是的。呃，我叫迪克，迪克·梅因费尔特。呃，在这个项目期间，我将担任营销专家。我将看看，呃，用户想要什么，以及，呃，我们可以用新产品，项目，产品做些什么。

马克：太好了。你呢？

尼克：尼克·德博尔，用户界面设计师。我将，呃，从用户的角度来看待技术设计。

马克：好的。

泽维尔：我叫泽维尔·约尔肯斯。我是工业设计师，我有三个主要问题需要找到答案。
```

### Lecture summarization

**input**  
这是一段关于如何最大化LLM性能技术的演讲视频。你能给我一个详细的演讲总结吗？ [video] https://cdn.openai.com/hello-gpt-4o/A-Survey-of-Techniques-for-Maximizing-LLM-Performance.mp4

**output**  
```
当然！这次演讲专注于最大化大型语言模型（LLMs）性能的技术，由OpenAI的Colin Jarvis和John Allard主讲。这次会议是OpenAI首次开发者大会的一部分，旨在提供关于如何针对特定任务优化LLMs的见解。

**介绍**
- Colin Jarvis是OpenAI在欧洲解决方案实践的负责人，而**John Allard**是微调产品团队的工程负责人。
- 演讲强调了优化LLMs的挑战，并强调没有一劳永逸的解决方案。

**优化LLMs的挑战**
1. **从噪声中分离信号**：识别确切问题具有挑战性。
2. **抽象性能指标**：衡量性能可能很困难。
3. **选择正确的优化方法**：很难知道使用哪种方法。

**优化流程**
- 演讲者介绍了一个基于两个轴的优化LLMs的框架：
  - **上下文优化**：模型需要知道什么。
  - **LLM优化**：模型需要如何行动。
- 该框架包括四个象限：
  - **提示工程**：优化的起点。
  - **检索增强生成（RAG）**：用于上下文优化。
  - **微调**：用于LLM优化。
  - **以上所有**：结合所有技术。

**提示工程**
- 策略：
  - 写下清晰的指令。
  - 将复杂任务拆分为更简单的子任务。
  - 给模型时间思考。
  - 系统地测试变化。
- 适用于：
  - 早期测试和学习。
  - 设定基线。
- 不适用于：
  - 引入新信息。
  - 复制复杂风格。
  - 最小化令牌使用。

**检索增强生成（RAG）**
- 概述：
  - RAG涉及检索相关文档并使用它们来生成响应。
- 适用于：
  - 引入新信息。
  - 减少幻觉。
- 不适用于：
  - 嵌入广泛的领域知识。
  - 教授新格式或风格。
  - 最小化令牌使用。
- 成功案例：
  - 演讲者分享了一个成功案例，他们使用RAG将准确率从45%提高到98%。

**微调**
- 概述：
  - 微调涉及在较小、特定领域的数据集上继续训练过程。
- 好处：
  - 提高特定任务的性能。
  - 提高效率。
- 适用于：
  - 强调现有知识。
  - 定制结构或语气。
  - 教授复杂指令。
- 不适用于：
  - 添加新知识。
  - 快速迭代。
- 成功案例：
  - 演讲者分享了Canva的一个成功案例，微调显著提高了性能。

**最佳实践**
1. **从提示工程和少样本学习开始**。
2. **建立基线**。
3. **从小处着手，关注质量**。

**结合微调和RAG**
- 演讲者强调了结合微调和RAG以获得最佳性能的好处。

**理论应用**
- 演讲者将理论应用于一个实际挑战，即Spider 1.0基准测试，使用RAG和微调都达到了高准确率。

**结论**
- 演讲以优化流程的总结结束，并强调了使用讨论的技术迭代改进LLM性能的重要性。

**问答**
- 演讲者邀请观众提问，并可供进一步讨论。
```

### Variable binding - cube stacking

| input | output |
| --- | --- |
|一张图片描绘了三个堆叠在桌子上的立方体。顶部的立方体是红色的，上面有一个G。中间的立方体是蓝色的，上面有一个P。底部的立方体是绿色的，上面有一个T。这些立方体彼此堆叠。|![](https://cdn.openai.com/hello-gpt-4o/cube-01.jpg?w=128&q=90&fm=webp)|
||![](https://cdn.openai.com/hello-gpt-4o/cube-02.jpg?w=128&q=90&fm=webp)|
||![](https://cdn.openai.com/hello-gpt-4o/cube-03.jpg?w=128&q=90&fm=webp)|
||![](https://cdn.openai.com/hello-gpt-4o/cube-04.jpg?w=128&q=90&fm=webp)|
||![](https://cdn.openai.com/hello-gpt-4o/cube-05.jpg?w=128&q=90&fm=webp)|
||![](https://cdn.openai.com/hello-gpt-4o/cube-06.jpg?w=128&q=90&fm=webp)|
||![](https://cdn.openai.com/hello-gpt-4o/cube-07.jpg?w=128&q=90&fm=webp)|

### Concrete poetry

| input | output |
| --- | --- |
|OpenAI 标志 ![](https://cdn.openai.com/hello-gpt-4o/concrete-poetry-01.jpg?w=384&q=90&fm=webp)||
|一个以OpenAI标志外形构成的具体诗，由“omni”这个词组成。|![](https://cdn.openai.com/hello-gpt-4o/concrete-poetry-02.jpg?w=640&q=90&fm=webp)|
|同样的图像，但是暗色模式和彩虹色文字。|![](https://cdn.openai.com/hello-gpt-4o/concrete-poetry-03.jpg?w=640&q=90&fm=webp)|

# 模型评估
在传统基准测试的测量中，GPT-4o在文本、推理和编码智能方面达到了GPT-4 Turbo级别的性能，同时在多语言、音频和视觉能力方面设定了新的高标准。

## 文本评估

![](https://images.ctfassets.net/kftzwdyauwt9/4KaMwrPGUMKKj3sh25CxcZ/1a9f994a00a1aa53aab6ef6ad6d49f06/gpt-40-02_light.png?w=2048&q=80&fm=webp)
GPT-4o在0-shot COT MMLU（一般知识问题）上设定了新的高分记录，得分为88.7%。所有这些评估都是通过我们新的简单评估库（simple evals）收集的。此外，在传统的5-shot无CoT MMLU测试中，GPT-4o也设定了新的高分记录，得分为87.2%。（注：Llama3 400b仍在训练中）

## 音频ASR表现

![](https://images.ctfassets.net/kftzwdyauwt9/1fZFzXZqkob0KKOAdHnqsU/1bb1d07c5eaa742a00370d4616c24389/gpt-40-06_light.png?w=2048&q=80&fm=webp)
音频ASR性能 - GPT-4o在所有语言上的语音识别性能都比Whisper-v3有了显著的提升，尤其是对于资源较少的语言。

## 音频翻译表现

![](https://images.ctfassets.net/kftzwdyauwt9/CYSJG8xvOnDcECErs5wEZ/f9aa00467d46a3ad3f80214946b46921/gpt-40-08_light.png?w=2048&q=80&fm=webp)
音频翻译性能 - GPT-4o在语音翻译方面设定了新的先进水平，并在MLS基准测试中超越了Whisper-v3。

## M3Exam零射击结果

![](https://images.ctfassets.net/kftzwdyauwt9/mjhR7VmDkrthzOIlnrt1k/f8c70d582bee69a7d69d45d3945d9ee5/gpt-40-04_light.png?w=2048&q=80&fm=webp)
M3Exam - M3Exam基准测试既包括多语言也包括视觉评估，由来自其他国家标准化测试的多项选择题组成，有时包括图形和图表。GPT-4o在这个基准测试中所有语言的表现都比GPT-4更强。（我们省略了斯瓦希里语和爪哇语的视觉结果，因为这些语言的视觉问题只有5个或更少。

## 视觉理解评估

![](https://images.ctfassets.net/kftzwdyauwt9/wyu4GGMOr2JKyftCry28J/363a13738df37d7535874d6e178a4baa/gpt-40-01_light.png?w=2048&q=80&fm=webp)
视觉理解评估 - GPT-4o在视觉感知基准测试中达到了先进水平。所有视觉评估都是0-shot的，MMMU、MathVista和ChartQA作为0-shot CoT。

### 语言分词
这20种语言被选为代表新分词器在不同语言家族中的压缩能力。

| 说明（中文翻译）                                   | 样例                                   |
|--------------------------------------------------|----------------------------------------|
| 古吉拉特语减少了4.4倍的tokens（从145减少到33）       | હેલો, મારું નામ જીપીટી-4o છે. હું એક નવા પ્રકારનું ભાષા મોડલ છું. તમને મળીને સારું લાગ્યું! |
| 泰卢固语减少了3.5倍的tokens（从159减少到45）        | నమస్కారము, నా పేరు జీపీటీ-4o. నేను ఒక్క కొత్త రకమైన భాషా మోడల్ ని. మిమ్మల్ని కలిసినందుకు సంతోషం! |
| 泰米尔语减少了3.3倍的tokens（从116减少到35）        | வணக்கம், என் பெயர் ஜிபிடி-4o. நான் ஒரு புதிய வகை மொழி மாடல். உங்களை சந்தித்ததில் மகிழ்ச்சி! |
| 马拉地语减少了2.9倍的tokens（从96减少到33）        | नमस्कार, माझे नाव जीपीटी-4o आहे. मी एक नवीन प्रकारची भाषा मॉडेल आहे. तुम्हाला भेटून आनंद झाला! |
| 印地语减少了2.9倍的tokens（从90减少到31）          | नमस्ते, मेरा नाम जीपीटी-4o है। मैं एक नए प्रकार का भाषा मॉडल हूँ। आपसे मिलकर अच्छा लगा! |
| 乌尔都语减少了2.5倍的tokens（从82减少到33）        | ہیلو، میرا نام جی پی ٹی-4o ہے۔ میں ایک نئے قسم کا زبان ماڈل ہوں، آپ سے مل کر اچھا لگا! |
| 阿拉伯语减少了2.0倍的tokens（从53减少到26）        | مرحبًا، اسمي جي بي تي-4o. أنا نوع جديد من نموذج اللغة، سررت بلقائك! |
| 波斯语减少了1.9倍的tokens（从61减少到32）          | سلام، اسم من جی پی تی-۴او است. من یک نوع جدیدی از مدل زبانی هستم، از ملاقات شما خوشبختم! |
| 俄语减少了1.7倍的tokens（从39减少到23）            | Привет, меня зовут GPT-4o. Я — новая языковая модель, приятно познакомиться! |
| 韩语减少了1.7倍的tokens（从45减少到27）            | 안녕하세요, 제 이름은 GPT-4o입니다. 저는 새로운 유형의 언어 모델입니다, 만나서 반갑습니다! |
| 越南语减少了1.5倍的tokens（从46减少到30）          | Xin chào, tên tôi là GPT-4o. Tôi là một loại mô hình ngôn ngữ mới, rất vui được gặp bạn! |
| 中文减少了1.4倍的tokens（从34减少到24）            | 你好，我的名字是GPT-4o。我是一种新型的语言模型，很高兴见到你! |
| 日语减少了1.4倍的tokens（从37减少到26）            | こんにちわ、私の名前はGPT−４oです。私は新しいタイプの言語モデルです、初めまして |
| 土耳其语减少了1.3倍的tokens（从39减少到30）        | Merhaba, benim adım GPT-4o. Ben yeni bir dil modeli türüyüm, tanıştığımıza memnun oldum! |
| 意大利语减少了1.2倍的tokens（从34减少到28）        | Ciao, mi chiamo GPT-4o. Sono un nuovo tipo di modello linguistico, è un piacere conoscerti! |
| 德语减少了1.2倍的tokens（从34减少到29）            | Hallo, mein Name is GPT-4o. Ich bin ein neues KI-Sprachmodell. Es ist schön, dich kennenzulernen. |
| 西班牙语减少了1.1倍的tokens（从29减少到26）        | Hola, me llamo GPT-4o. Soy un nuevo tipo de modelo de lenguaje, ¡es un placer conocerte! |
| 葡萄牙语减少了1.1倍的tokens（从30减少到27）        | Olá, meu nome é GPT-4o. Sou um novo tipo de modelo de linguagem, é um prazer conhecê-lo! |
| 法语减少了1.1倍的tokens（从31减少到28）            | Bonjour, je m'appelle GPT-4o. Je suis un nouveau type de modèle de langage, c'est un plaisir de vous rencontrer! |
| 英语减少了1.1倍的tokens（从27减少到24）            | Hello, my name is GPT-4o. I'm a new type of language model, it's nice to meet you! |



---

- [原文](https://openai.com/index/hello-gpt-4o/)
- 本文
    <!-- - [博客 - 从零开始学AI](...) -->
    <!-- - [微信 - 从零开始学AI](...) -->
    <!-- - [CSDN - 从零开始学AI](...) -->
    <!-- - [掘金 - 从零开始学AI](...) -->
    <!-- - [知乎 - 从零开始学AI](...) -->
    <!-- - [阿里云 - 从零开始学AI](...) -->
    <!-- - [腾讯云 - 从零开始学AI](...) -->
