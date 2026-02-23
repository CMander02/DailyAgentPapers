"use client";

import { useEffect, useState, useCallback } from "react";
import { PapersData, Paper } from "@/types/paper";
import { fetchPapersData, getPapersForDate, getAvailableDates, formatDateStr } from "@/lib/data";
import { DatePicker } from "@/components/date-picker";
import { PaperList } from "@/components/paper-list";
import { ThemeToggle } from "@/components/theme-toggle";
import { Separator } from "@/components/ui/separator";
import { Button } from "@/components/ui/button";
import { ChevronLeft, ChevronRight } from "lucide-react";

export default function Home() {
  const [data, setData] = useState<PapersData | null>(null);
  const [selectedDate, setSelectedDate] = useState<Date | undefined>();
  const [papers, setPapers] = useState<Paper[]>([]);
  const [dateStr, setDateStr] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchPapersData().then((d) => {
      setData(d);
      setLoading(false);
      // Auto-select the latest available date
      if (d.available_dates && d.available_dates.length > 0) {
        const latest = d.available_dates[0];
        const date = new Date(latest + "T00:00:00");
        setSelectedDate(date);
        setDateStr(latest);
        setPapers(getPapersForDate(d, latest));
      }
    });
  }, []);

  const handleDateSelect = useCallback(
    (date: Date | undefined) => {
      if (!date || !data) return;
      setSelectedDate(date);
      const str = formatDateStr(date);
      setDateStr(str);
      setPapers(getPapersForDate(data, str));
    },
    [data]
  );

  const navigateDate = useCallback(
    (direction: -1 | 1) => {
      if (!data || !dateStr) return;
      const dates = data.available_dates;
      const idx = dates.indexOf(dateStr);
      const nextIdx = idx - direction; // dates are sorted descending
      if (nextIdx >= 0 && nextIdx < dates.length) {
        const nextStr = dates[nextIdx];
        const nextDate = new Date(nextStr + "T00:00:00");
        setSelectedDate(nextDate);
        setDateStr(nextStr);
        setPapers(getPapersForDate(data, nextStr));
      }
    },
    [data, dateStr]
  );

  const availableDates = data ? getAvailableDates(data) : [];

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="sticky top-0 z-50 border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="max-w-7xl mx-auto flex h-14 items-center justify-between px-4">
          <div className="flex items-center gap-2">
            <h1 className="text-lg font-bold tracking-tight">DailyAgentPapers</h1>
            <span className="text-xs text-muted-foreground hidden sm:inline">
              每日 Arxiv Agent 论文摘要
            </span>
          </div>
          <div className="flex items-center gap-2">
            {dateStr && (
              <div className="flex items-center gap-1">
                <Button
                  variant="ghost"
                  size="icon"
                  className="h-8 w-8"
                  onClick={() => navigateDate(-1)}
                  disabled={
                    !data ||
                    data.available_dates.indexOf(dateStr) >=
                      data.available_dates.length - 1
                  }
                >
                  <ChevronLeft className="h-4 w-4" />
                </Button>
                <span className="text-sm font-mono min-w-[6.5rem] text-center">
                  {dateStr}
                </span>
                <Button
                  variant="ghost"
                  size="icon"
                  className="h-8 w-8"
                  onClick={() => navigateDate(1)}
                  disabled={
                    !data || data.available_dates.indexOf(dateStr) <= 0
                  }
                >
                  <ChevronRight className="h-4 w-4" />
                </Button>
              </div>
            )}
            <ThemeToggle />
          </div>
        </div>
      </header>

      {/* Main content */}
      <div className="max-w-7xl mx-auto px-4 py-6">
        {loading ? (
          <div className="flex items-center justify-center py-20 text-muted-foreground">
            <p>加载中...</p>
          </div>
        ) : (
          <div className="flex flex-col lg:flex-row gap-6">
            {/* Sidebar: Calendar */}
            <aside className="lg:w-[300px] shrink-0">
              <div className="sticky top-20">
                <DatePicker
                  selected={selectedDate}
                  onSelect={handleDateSelect}
                  availableDates={availableDates}
                />
                {data && data.available_dates.length > 0 && (
                  <div className="mt-4 text-xs text-muted-foreground">
                    <p>共 {data.available_dates.length} 天数据</p>
                    <p>
                      {data.available_dates[data.available_dates.length - 1]} ~{" "}
                      {data.available_dates[0]}
                    </p>
                  </div>
                )}
              </div>
            </aside>

            <Separator orientation="vertical" className="hidden lg:block" />

            {/* Main: Paper list */}
            <main className="flex-1 min-w-0">
              <PaperList papers={papers} dateStr={dateStr} />
            </main>
          </div>
        )}
      </div>
    </div>
  );
}
