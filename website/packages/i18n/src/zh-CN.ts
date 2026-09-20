export const zhCN = {
  meta: {
    title: "Mathematics of Intelligence",
    tagline: "从数学基础到智能及其之外",
  },
  nav: {
    home: "首页",
    read: "阅读",
    mathematics: "数学",
    ai: "人工智能",
    topics: "话题",
    resources: "资源",
  },
  home: {
    kicker: "英文专著 · 浅色 / 深色两份 PDF",
    lead: "一份可修订的 AI 理论地图：一条线是符号与论证，一条线是模型与工程。其他学科只在结构真正共享时进入。",
    spine: "数学基础 → 人工智能的数学 → 智能及其之外",
    threadsTitle: "两条主线",
    mathTitle: "数学",
    mathBody: "起点是高等教育里的微积分。第一部收集反复出现的想法：线性结构、概率、随机过程、凸优化、信息与动力学。",
    aiTitle: "人工智能",
    aiBody: "模型与算法是第二条线。缺的数学随章节补上；能诚实接到工程上的，就接到工程上。",
    topicsTitle: "后续话题",
    topicsBody: "物理、金融等可以在桥接成立后作为话题出现，它们不占据仓库顶层。",
    ctaRead: "阅读全书",
    ctaResources: "动画、课件、示例",
  },
  read: {
    title: "阅读",
    subtitle: "站点嵌入编译后的 PDF。正文以 book/ 下的 LaTeX 为准。",
    light: "浅色版",
    dark: "深色版",
    missing: "未找到 PDF。请在 book/ 目录运行 scripts/build.ps1 all（或 build.sh），文件会复制到 apps/web/public/pdfs/。",
    openTab: "在新标签打开",
  },
  thread: {
    mathematics: {
      title: "数学",
      body: "数学主线贯穿每一部。本页是叙事索引，不是第二本教材。",
    },
    ai: {
      title: "人工智能",
      body: "人工智能主线是实验室：表示学习、优化、生成模型与智能体。",
    },
    topics: {
      title: "话题",
      body: "可选桥接。目录已留好，金融与物理可以后加，不必改顶层结构。",
    },
  },
  resources: {
    title: "资源",
    subtitle: "配套工件。它们说明这本书，并不代替这本书。",
    animations: "Manim 动画",
    animationsBody: "animations/ 下的可复用场景，按数学、人工智能、话题分组。",
    ppts: "课件",
    pptsBody: "ppts/ 下的 PowerPoint 文件，分组方式相同。",
    examples: "示例",
    examplesBody: "examples/ 下回答概念问题的小程序。",
  },
  footer: {
    note: "书的正文是英文。本站界面提供英文与中文。",
  },
} as const;
