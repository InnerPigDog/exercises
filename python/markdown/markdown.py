import re


def parse(markdown):
    result = []
    for line in md_to_html_lists(markdown.splitlines()):
        line = md_to_html_heading(line)
        line = md_to_html_bold(line)
        line = md_to_html_italics(line)
        line = md_to_html_paragraphs(line)
        result.append(line)
    return "".join(result)


def md_to_html_heading(md_line):
    # Headings of level i are exactly i times # in a row, followed by a space and any sequence of characters.
    for j in range(1, 7):
        if re.match('#{%s} (.*)' % j, md_line):
            return f"<h{j}>{md_line[j + 1:]}</h{j}>"
    return md_line


def md_to_html_lists(markdown):
    result = []
    for i in range(len(markdown)):
        if is_list_element(markdown[i]):
            # If there is no previous line or the previous line is not a list element, then the current line is the first
            # list entry
            first_list_entry = "<ul>" if i == 0 or not is_list_element(markdown[i - 1]) else ""
            # If there is no next line or the next line is not a list element, then the current line is the last
            # list entry
            last_list_entry = "</ul>" if i == len(markdown) - 1 or not is_list_element(markdown[i + 1]) else ""
            result.append(f"{first_list_entry}<li>{markdown[i][2:]}</li>{last_list_entry}")
        else:
            result.append(markdown[i])
    return result


def is_list_element(md_line):
    # Lists begin with * or - followed by a space
    return re.match(r'^(- (.*)|\* (.*))', md_line)


def md_to_html_bold(md_line):
    m = re.search(r"(.*)__(.*)__(.*)", md_line)
    if m:
        return f"{m.group(1)}<strong>{m.group(2)}</strong>{m.group(3)}"
    else:
        return md_line


def md_to_html_italics(md_line):
    m = re.search(r"(.*)_(.*)_(.*)", md_line)
    if m:
        return f"{m.group(1)}<em>{m.group(2)}</em>{m.group(3)}"
    else:
        return md_line


def md_to_html_paragraphs(md_line):
    if not re.match('<h|<ul|<li', md_line):
        return '<p>' + md_line + '</p>'
    else:
        return md_line
