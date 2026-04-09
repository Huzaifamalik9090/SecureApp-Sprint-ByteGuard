from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="cp1252", errors="replace")


def _wrap_lines(text: str, max_chars: int = 96):
    lines = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line:
            lines.append("")
            continue
        while len(line) > max_chars:
            split_at = line.rfind(" ", 0, max_chars)
            if split_at <= 0:
                split_at = max_chars
            lines.append(line[:split_at].rstrip())
            line = line[split_at:].lstrip()
        lines.append(line)
    return lines


def write_pdf(title: str, text: str, output: Path):
    c = canvas.Canvas(str(output), pagesize=A4)
    width, height = A4
    margin = 2 * cm
    y = height - margin

    try:
        pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))
        font_name = "Arial"
    except Exception:
        font_name = "Helvetica"

    c.setTitle(title)
    c.setAuthor("Team ByteGuard")

    c.setFont(font_name, 15)
    c.drawString(margin, y, title)
    y -= 0.9 * cm

    c.setFont(font_name, 10.5)
    for line in _wrap_lines(text):
        if y <= margin:
            c.showPage()
            c.setFont(font_name, 10.5)
            y = height - margin
        c.drawString(margin, y, line if line else " ")
        y -= 0.5 * cm

    c.save()


def main():
    threat_md = ROOT / "threat-model" / "THREAT_MODEL.md"
    final_md = ROOT / "docs" / "Final_Report_ByteGuard.md"

    threat_pdf = ROOT / "THREAT_MODEL.pdf"
    final_pdf = ROOT / "Final_Report_ByteGuard.pdf"

    write_pdf(
        "THREAT MODEL - BYTEGUARD SECURE BLOG",
        _read_text(threat_md),
        threat_pdf,
    )
    write_pdf(
        "FINAL REPORT - BYTEGUARD SECURE BLOG",
        _read_text(final_md),
        final_pdf,
    )
    print(f"Generated: {threat_pdf}")
    print(f"Generated: {final_pdf}")


if __name__ == "__main__":
    main()
