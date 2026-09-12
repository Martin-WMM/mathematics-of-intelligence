export type ThreadId = "mathematics" | "ai" | "topics";

export type TopicId = "finance" | "physics";

export interface ChapterMeta {
  id: string;
  title: string;
}

export interface PartMeta {
  id: string;
  title: string;
  chapters: ChapterMeta[];
}

export const BOOK_TITLE = "Mathematics of Intelligence";

export const PARTS: PartMeta[] = [
  {
    id: "representation",
    title: "Representation",
    chapters: [
      { id: "signal-to-vector", title: "From Signal to Vector" },
      { id: "beyond-vectors", title: "Structure Beyond Vectors" },
      { id: "information", title: "Information and Compression" },
      { id: "representations-in-ai", title: "Representations in Modern AI" },
    ],
  },
  {
    id: "learning",
    title: "Learning",
    chapters: [
      { id: "loss-and-risk", title: "Loss, Risk, and Empirical Risk" },
      { id: "optimization", title: "Optimization as Geometry" },
      { id: "generalization", title: "Generalization" },
      { id: "learning-dynamics", title: "Learning Algorithms as Dynamics" },
      { id: "classical-to-deep", title: "From Classical Learning to Deep Learning" },
    ],
  },
  {
    id: "generation",
    title: "Generation",
    chapters: [
      { id: "modeling-distributions", title: "Modeling Distributions" },
      { id: "autoregressive", title: "Autoregressive Factorization" },
      { id: "latent-variables", title: "Latent Variable Models" },
      { id: "adversarial", title: "Adversarial and Implicit Generation" },
      { id: "diffusion", title: "Diffusion, Scores, and Flows" },
    ],
  },
  {
    id: "intelligence",
    title: "Intelligence",
    chapters: [
      { id: "prediction-vs-reasoning", title: "Prediction versus Reasoning" },
      { id: "memory", title: "Memory and Retrieval" },
      { id: "planning", title: "Planning and Control" },
      { id: "world-models", title: "World Models" },
      { id: "agents", title: "Agents" },
    ],
  },
];

export const THREADS: { id: ThreadId; label: string }[] = [
  { id: "mathematics", label: "Mathematics" },
  { id: "ai", label: "Artificial Intelligence" },
  { id: "topics", label: "Topics" },
];

export const TOPICS: { id: TopicId; label: string }[] = [
  { id: "finance", label: "Finance" },
  { id: "physics", label: "Physics" },
];
