"use client";

import { Calendar } from "@/components/ui/calendar";

interface DatePickerProps {
  selected: Date | undefined;
  onSelect: (date: Date | undefined) => void;
  availableDates: Date[];
}

export function DatePicker({ selected, onSelect, availableDates }: DatePickerProps) {
  // Build a set of date strings that have papers
  const availableSet = new Set(
    availableDates.map(
      (d) =>
        `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`
    )
  );

  const isDisabled = (date: Date) => {
    const dateStr = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}`;
    return !availableSet.has(dateStr);
  };

  return (
    <Calendar
      mode="single"
      selected={selected}
      onSelect={onSelect}
      disabled={isDisabled}
      className="rounded-md border"
      modifiers={{
        available: availableDates,
      }}
      modifiersClassNames={{
        available: "font-bold text-primary",
      }}
    />
  );
}
