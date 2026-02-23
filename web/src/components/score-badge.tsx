import { Badge } from "@/components/ui/badge";

export function ScoreBadge({ score }: { score: number }) {
  let variant: "default" | "secondary" | "destructive" | "outline" = "secondary";
  if (score >= 8) variant = "default";
  else if (score >= 6) variant = "outline";

  return (
    <Badge variant={variant} className="text-xs font-mono">
      {score.toFixed(1)}
    </Badge>
  );
}
