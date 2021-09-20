import re

import re

# functional improvements:
# can handle any heading levels from 1 to 7

# For each markdown feature there is now a function that parses the feature into the html version.
# This simplifies the markdown parser into a simple sequence of steps. Each function can be maintained on its own.

def parse(markdown):
    tmp = md_to_html_lists(markdown.splitlines())
    tmp = md_to_html_heading(tmp)
    tmp = md_to_html_italics_bold(tmp)
    tmp = md_to_html_paragraphs(tmp)
    return "".join(tmp)


def md_to_html_heading(markdown):
    html = markdown[:]
    for i in range(len(html)):
        for j in range(1, 8):
            # Headings of level i are exactly i times # in a row, followed by a space and any sequence of characters.
            if re.match('#{%s} (.*)' % j, html[i]):  # We can use the truthiness of objects
                html[i] = f"<h{j}>{markdown[i][j + 1:]}</h{j}>"
    return html


def md_to_html_lists(markdown):
    # Lists with * or -
    html = []
    for i in range(len(markdown)):
        if is_list_element(markdown[i]):
            # If there is no previous line or the previous line is not a list element, then the current line is the first
            # list entry
            first_list_entry = "<ul>" if i == 0 or not is_list_element(markdown[i - 1]) else ""
            # If there is no next line or the next line is not a list element, then the current line is the last
            # list entry
            last_list_entry = "</ul>" if i == len(markdown) - 1 or not is_list_element(markdown[i + 1]) else ""
            html.append(f"{first_list_entry}<li>{markdown[i][2:]}</li>{last_list_entry}")
        else:
            html.append(markdown[i])
    return html


def is_list_element(md_line):
    return re.match(r'^(\- (.*)|\* (.*))', md_line)


def md_to_html_italics_bold(markdown):
    for i in range(len(markdown)):
        # Bold
        m = re.search(r"(.*)__(.*)__(.*)", markdown[i])
        if m:
            markdown[i] = f"{m.group(1)}<strong>{m.group(2)}</strong>{m.group(3)}"

        # Italics
        m = re.search(r"(.*)_(.*)_(.*)", markdown[i])
        if m:
            markdown[i] = f"{m.group(1)}<em>{m.group(2)}</em>{m.group(3)}"
    return markdown


def md_to_html_paragraphs(markdown):
    for i in range(len(markdown)):
        if not re.match('<h|<ul|<li', markdown[i]):
            markdown[i] = '<p>' + markdown[i] + '</p>'
    return markdown



def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'
        m = re.match(r'\* (.*)', i) # what is that for?
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res
