export interface Paper {
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
  chinese_summary: string;
  core_contributions: string[];
  analysis: string;
  md_path: string;
}

export interface PapersData {
  dates: Record<string, Paper[]>;
  available_dates: string[];
}
