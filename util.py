import re


def remove_extra_line(source):
    return re.sub('\n\n+', '\n', source)


def get_output_regex(regex, source):
    try:
        return re.search(regex, source, re.IGNORECASE).group()
    except:
        return ""


def tokenize(string):
    regex = '\w+'
    data = []
    for match in re.finditer(regex, string, re.IGNORECASE):
        data.append(match.group())
    return data


def read_line(filename, line_num):
    class BreakIt(Exception):
        pass

    ar = None
    try:
        with open(filename) as f:
            i = 0
            for line in f:
                if (i == line_num):
                    ar = line
                    raise BreakIt
                i += 1
    except BreakIt:
        pass

    return ar


# This function reads a files
def read_file(file_path):
    data = ''
    with open(file_path, 'r') as myfile:
        data = data + myfile.read()
    return data


def get_regex_groups(regex, source, groups):
    data = ['', '']
    extr = re.search(regex, source, re.IGNORECASE)
    i = 0
    for group in groups:
        data[i] = extr.group(groups[i]).strip()
        i += 1

    return data


def get_all_regex_one_group(regex, source, group):
    data = []
    for match in re.finditer(regex, source, re.IGNORECASE):
        data.append(match.group(group))
    return data


def get_all_regex_multiple_group(regex, source, groups):
    data = []
    for match in re.finditer(regex, source, re.IGNORECASE):
        current_data = {}
        for group in groups:
            current_data[group] = match.group(group)
        data.append(current_data)
    return data


def remove_html(source):
    return re.sub('<[^<]+?>', '', source)


def rl(source):
    return re.sub('\n', ' ', source)


def parse_date(date):
    split = date.split(',')
    year = split[1].strip()

    split2 = split[0].split(' ')

    day = split2[1].strip()
    if (len(day) == 1):
        day = "0" + day
    alpha_month = split2[0].lower()
    month = ''
    array = ["jan", "feb", "mar", "apr", "may", "june", "july", "august", "sept", "oct", "nov", "dec"]
    output = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    for i in range(12):
        if (alpha_month.startswith(array[i])):
            month = output[i]
            break
    return [day, month, year]