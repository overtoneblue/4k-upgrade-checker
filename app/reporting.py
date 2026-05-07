def format_release_summary(summary: dict[str, int]) -> str:
    selected = summary["selected"]
    checked = summary["checked"]
    failed = summary["failed"]

    success_rate = (checked / selected * 100) if selected else 0

    return "\n".join(
        [
            "",
            "========================",
            " Release Check Summary",
            "========================",
            f"Selected:      {selected}",
            f"Checked:       {checked}",
            f"Found 4K:      {summary['found_4k']}",
            f"Not Found:     {summary['not_found']}",
            f"Failed:        {failed}",
            f"Success Rate:  {success_rate:.1f}%",
            "========================",
        ]
    )
