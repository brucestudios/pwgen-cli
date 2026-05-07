import json
import csv
from datetime import datetime
from typing import Any, Dict, List


def format_output(data: Any, format: str = 'text') -> str:
    """Format data as specified output format."""
    if format == 'json':
        return json.dumps(data, indent=2, default=str)
    elif format == 'csv':
        if isinstance(data, list) and len(data) > 0:
            # Flatten if necessary? For simplicity, we assume data is a list of dicts.
            output = []
            writer = csv.DictWriter(output, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            return output.getvalue()
        else:
            return str(data)
    elif format == 'markdown':
        if isinstance(data, dict):
            return _dict_to_markdown(data)
        elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            return _list_of_dicts_to_markdown(data)
        else:
            return f"```\n{str(data)}\n```"
    else:  # text
        return str(data)


def _dict_to_markdown(d: Dict[str, Any]) -> str:
    lines = []
    for key, value in d.items():
        lines.append(f"**{key}**: {_format_value(value)}")
    return "\n".join(lines)


def _list_of_dicts_to_markdown(data: List[Dict[str, Any]]) -> str:
    if not data:
        return ""
    headers = data[0].keys()
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in data:
        lines.append("| " + " | ".join(str(row.get(h, "")) for h in headers) + " |")
    return "\n".join(lines)


def _format_value(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return f"```json\n{json.dumps(value, indent=2)}\n```"
    elif isinstance(value, datetime):
        return value.isoformat()
    else:
        return str(value)


def parse_date(date_str: str) -> datetime:
    """Parse a date string into a datetime object.
    Supports ISO format and simple relative dates like '6 months ago'.
    """
    # This is a simplified version. In a real project, use dateutil or similar.
    from datetime import datetime, timedelta
    try:
        return datetime.fromisoformat(date_str)
    except ValueError:
        pass
    now = datetime.now()
    if date_str.endswith(" ago"):
        value_str = date_str[:-4].strip()
        parts = value_str.split()
        if len(parts) == 2:
            try:
                value = int(parts[0])
                unit = parts[1]
                if unit.startswith("month"):
                    return now - timedelta(days=30 * value)
                elif unit.startswith("week"):
                    return now - timedelta(weeks=value)
                elif unit.startswith("day"):
                    return now - timedelta(days=value)
                elif unit.startswith("year"):
                    return now - timedelta(days=365 * value)
            except ValueError:
                pass
    # If we can't parse, raise an error
    raise ValueError(f"Unable to parse date string: {date_str}")