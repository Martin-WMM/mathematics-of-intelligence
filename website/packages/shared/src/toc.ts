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
    id: "foundations",
    title: "Mathematical Foundations",
    chapters: [
      { id: "spaces-and-inner-products", title: "Spaces, Vectors, and Inner Products" },
      { id: "operators-and-spectra", title: "Linear Maps, Spectra, and Decompositions" },
      { id: "probability", title: "Probability and Expectation" },
      { id: "information", title: "Information and Compression" },
      { id: "optimization", title: "Optimization as Geometry" },
      { id: "dynamics", title: "Dynamics and Iteration" },
      { id: "beyond-vectors", title: "Structure Beyond Vectors" },
    ],
  },
  {
    id: "mathematics-of-ai",
    title: "Mathematics of AI",
    chapters: [
      { id: "representation", title: "Representation" },
      { id: "learning-and-risk", title: "Learning, Loss, and Risk" },
      { id: "generalization", title: "Generalization" },
      { id: "deep-learning", title: "From Classical Learning to Deep Learning" },
      { id: "modeling-distributions", title: "Modeling Distributions" },
      { id: "autoregressive", title: "Autoregressive Factorization" },
      { id: "latent-variables", title: "Latent Variable Models" },
      { id: "adversarial", title: "Adversarial and Implicit Generation" },
      { id: "diffusion", title: "Diffusion, Scores, and Flows" },
    ],
  },
  {
    id: "intelligence-and-beyond",
    title: "Intelligence and Beyond",
    chapters: [
      { id: "prediction-and-reasoning", title: "Prediction versus Reasoning" },
      { id: "memory", title: "Memory and Retrieval" },
      { id: "planning", title: "Planning and Control" },
      { id: "world-models", title: "World Models" },
      { id: "agents", title: "Agents" },
      { id: "beyond", title: "Beyond" },
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
