export interface QAPair {
  question: string;
  answer: string;
}

// papers.json 中的轻量条目（列表展示用）
export interface PaperMeta {
  arxiv_id: string;
  title: string;
  authors: string[];
  author_count: number;
  categories: string[];
  arxiv_url: string;
  pdf_url: string;
  published: string;
  tags: string[];
  relevance_score: number;
  md_path: string;
  version?: number;
}

// 从 .md 文件解析的完整详情
export interface PaperDetail extends PaperMeta {
  summary: string;
  qa_pairs?: QAPair[];
  chinese_summary?: string;
  core_contributions?: string[];
  analysis?: string;
}

export interface IndexData {
  available_dates: string[];
}
