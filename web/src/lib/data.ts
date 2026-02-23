import { PapersData, Paper } from "@/types/paper";

const BASE_PATH = process.env.NEXT_PUBLIC_BASE_PATH || "";

let cachedData: PapersData | null = null;

export async function fetchPapersData(): Promise<PapersData> {
  if (cachedData) return cachedData;

  try {
    const res = await fetch(`${BASE_PATH}/data/papers.json`);
    if (!res.ok) {
      return { dates: {}, available_dates: [] };
    }
    const data: PapersData = await res.json();
    cachedData = data;
    return data;
  } catch {
    return { dates: {}, available_dates: [] };
  }
}

export function getPapersForDate(
  data: PapersData,
  dateStr: string
): Paper[] {
  return data.dates[dateStr] || [];
}

export function getAvailableDates(data: PapersData): Date[] {
  return (data.available_dates || []).map((d) => new Date(d + "T00:00:00"));
}

export function formatDateStr(date: Date): string {
  const y = date.getFullYear();
  const m = String(date.getMonth() + 1).padStart(2, "0");
  const d = String(date.getDate()).padStart(2, "0");
  return `${y}-${m}-${d}`;
}
