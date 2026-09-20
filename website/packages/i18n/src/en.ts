export const en = {
  meta: {
    title: "Mathematics of Intelligence",
    tagline: "From mathematical foundations to intelligence and beyond",
  },
  nav: {
    home: "Home",
    read: "Read",
    mathematics: "Mathematics",
    ai: "AI",
    topics: "Topics",
    resources: "Resources",
  },
  home: {
    kicker: "English monograph · two PDF editions",
    lead: "A working map of AI theory: symbols and arguments on one thread, models and engineering on the other. Other fields enter only when a structure is genuinely shared.",
    spine: "Mathematical Foundations → Mathematics of AI → Intelligence and Beyond",
    threadsTitle: "Two threads",
    mathTitle: "Mathematics",
    mathBody: "The start is a first course in calculus. Part I then collects the ideas that keep returning: linear structure, probability, stochastic processes, convex optimisation, information, and dynamics.",
    aiTitle: "Artificial intelligence",
    aiBody: "Models and algorithms are the second thread. Missing mathematics is filled in when a chapter needs it, and tied to engineering where that is honest.",
    topicsTitle: "Later topics",
    topicsBody: "Physics, finance, and related fields can appear once a bridge is real. They do not sit at the top of the repository.",
    ctaRead: "Read the book",
    ctaResources: "Animations, slides, examples",
  },
  read: {
    title: "Read",
    subtitle: "The site embeds the compiled PDFs. The source of truth is the LaTeX tree in book/.",
    light: "Light edition",
    dark: "Dark edition",
    missing: "PDF not found. From the book/ directory run scripts/build.ps1 all (or build.sh) so the files are copied into apps/web/public/pdfs/.",
    openTab: "Open in a new tab",
  },
  thread: {
    mathematics: {
      title: "Mathematics",
      body: "The mathematical thread runs through every part. Use this page as an index into the narrative, not as a second textbook.",
    },
    ai: {
      title: "Artificial intelligence",
      body: "The AI thread is the laboratory: representation learning, optimisation, generative models, and agents.",
    },
    topics: {
      title: "Topics",
      body: "Optional bridges. Folders exist so finance and physics can be added without changing the top-level layout.",
    },
  },
  resources: {
    title: "Resources",
    subtitle: "Companion artifacts. They illustrate the book; they do not replace it.",
    animations: "Manim animations",
    animationsBody: "Reusable scenes under animations/, grouped by mathematics, AI, and topics.",
    ppts: "Slide decks",
    pptsBody: "PowerPoint files under ppts/, same grouping.",
    examples: "Examples",
    examplesBody: "Small programs under examples/ that answer a conceptual question.",
  },
  footer: {
    note: "Book text is English. This interface is available in English and Chinese.",
  },
} as const;
