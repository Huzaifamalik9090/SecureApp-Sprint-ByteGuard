from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="cp1252", errors="replace")


def _escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def _build_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "TitleStyle",
            parent=base["Title"],
            fontSize=20,
            leading=24,
            textColor=colors.HexColor("#0f172a"),
            spaceAfter=14,
        ),
        "h1": ParagraphStyle(
            "H1Style",
            parent=base["Heading1"],
            fontSize=15,
            leading=19,
            textColor=colors.HexColor("#0f172a"),
            spaceBefore=10,
            spaceAfter=6,
        ),
        "h2": ParagraphStyle(
            "H2Style",
            parent=base["Heading2"],
            fontSize=12.5,
            leading=16,
            textColor=colors.HexColor("#1e293b"),
            spaceBefore=8,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "BodyStyle",
            parent=base["BodyText"],
            fontSize=10.5,
            leading=15,
            spaceAfter=5,
        ),
        "bullet": ParagraphStyle(
            "BulletStyle",
            parent=base["BodyText"],
            fontSize=10.3,
            leading=14,
            leftIndent=14,
            bulletIndent=4,
            spaceAfter=3,
        ),
        "meta": ParagraphStyle(
            "MetaStyle",
            parent=base["BodyText"],
            fontSize=10,
            leading=13,
            textColor=colors.HexColor("#334155"),
            alignment=1,
            spaceAfter=4,
        ),
    }


def _is_table_line(line: str) -> bool:
    return line.strip().startswith("|") and line.strip().endswith("|")


def _table_from_lines(lines):
    rows = []
    for line in lines:
        if not _is_table_line(line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append([_escape(cell) for cell in cells])
    if len(rows) >= 2 and all(set(x) <= {"-", ":"} for x in rows[1]):
        rows.pop(1)
    return rows


def _add_title_page(story, title, subtitle, styles):
    story.append(Spacer(1, 4 * cm))
    story.append(Paragraph(_escape(title), styles["title"]))
    story.append(Spacer(1, 0.8 * cm))
    story.append(Paragraph(_escape(subtitle), styles["meta"]))
    story.append(Paragraph("Course: CYC386 Secure Software Design and Development", styles["meta"]))
    story.append(Paragraph("Team: ByteGuard", styles["meta"]))
    story.append(Paragraph("Institution: COMSATS University Islamabad", styles["meta"]))
    story.append(Spacer(1, 1.6 * cm))
    story.append(Paragraph("Spring 2026", styles["meta"]))
    story.append(PageBreak())


def _markdown_to_story(markdown_text: str, styles):
    story = []
    lines = markdown_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            story.append(Spacer(1, 0.18 * cm))
            i += 1
            continue

        if stripped.startswith("# "):
            story.append(Paragraph(_escape(stripped[2:].strip()), styles["h1"]))
            i += 1
            continue

        if stripped.startswith("## "):
            story.append(Paragraph(_escape(stripped[3:].strip()), styles["h2"]))
            i += 1
            continue

        if stripped.startswith("### "):
            story.append(Paragraph(_escape(stripped[4:].strip()), styles["h2"]))
            i += 1
            continue

        if _is_table_line(stripped):
            table_block = []
            while i < len(lines) and _is_table_line(lines[i].strip()):
                table_block.append(lines[i].strip())
                i += 1
            data = _table_from_lines(table_block)
            if data:
                col_count = len(data[0])
                col_width = (A4[0] - 4 * cm) / max(col_count, 1)
                table = Table(data, colWidths=[col_width] * col_count, repeatRows=1)
                table.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#94a3b8")),
                            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
                            ("FONTSIZE", (0, 0), (-1, -1), 9.2),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                            ("TOPPADDING", (0, 0), (-1, -1), 5),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                        ]
                    )
                )
                story.append(table)
                story.append(Spacer(1, 0.25 * cm))
            continue

        if stripped.startswith("- "):
            story.append(Paragraph(_escape(stripped[2:].strip()), styles["bullet"], bulletText="•"))
            i += 1
            continue

        if stripped[:2].isdigit() and ". " in stripped:
            story.append(Paragraph(_escape(stripped), styles["body"]))
            i += 1
            continue

        story.append(Paragraph(_escape(stripped), styles["body"]))
        i += 1

    return story


def write_pdf(title: str, markdown_text: str, output: Path):
    styles = _build_styles()
    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        topMargin=1.8 * cm,
        bottomMargin=1.6 * cm,
        leftMargin=2.0 * cm,
        rightMargin=2.0 * cm,
        title=title,
        author="Team ByteGuard",
    )

    story = []
    _add_title_page(story, title, "DevSecOps Security Sprint Final Artifact", styles)
    story.extend(_markdown_to_story(markdown_text, styles))
    doc.build(story)


def main():
    threat_md = ROOT / "threat-model" / "THREAT_MODEL.md"
    full_final_md = ROOT / "docs" / "Final_Report_ByteGuard_FULL.md"
    final_md = full_final_md if full_final_md.exists() else (ROOT / "docs" / "Final_Report_ByteGuard.md")
    threat_pdf = ROOT / "THREAT_MODEL.pdf"
    final_pdf = ROOT / "Final_Report_ByteGuard.pdf"

    write_pdf("THREAT MODEL - BYTEGUARD SECURE BLOG", _read_text(threat_md), threat_pdf)
    write_pdf("FINAL REPORT - BYTEGUARD SECURE BLOG", _read_text(final_md), final_pdf)

    print(f"Generated: {threat_pdf}")
    print(f"Generated: {final_pdf}")


if __name__ == "__main__":
    main()
