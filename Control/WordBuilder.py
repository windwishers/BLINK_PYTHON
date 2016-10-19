import re


# 문자열중 () 안의 글자를 추출 한 후 해당 문자열이 제거된 문자열 과 추출된 문자열으로 나눠 반환 해준다.
from model.Word import Word


def extract_assist(string):
    pattern = "\\(.+\\)"
    r = re.compile(pattern)
    assist = ""
    match = r.search(string)
    if match:
        startIndex = match.start()
        endIndex = match.end()

        assist = string[startIndex:endIndex]

    string = string.replace(assist, "")
    return string, assist


# 문자열을 , 를 기준으로 나눠 준다 단, () 나 "" 안의 문자열은 한 파트로 인식한다.
def split_phase(line):
    string = ""
    quoting = False
    list = []
    for ch in line:
        # check quoting.
        if ch == '"':
            quoting = not quoting
        elif ch == '(':
            quoting = True
        elif ch == ')':
            quoting = False

        if ch == ',' and not quoting:
            if string:
                list.append(string.strip())
            string = ""
        else:
            string += ch
    return list


# 문자열을 파싱하여 Word 리스트를 반환 한다.
def build(line):
    phases = split_phase(line)
    if phases.__len__() < 4:
        return []
    means = phases[3:]
    list = []
    for mean_phase in means:
        mean, assist = extract_assist(mean_phase)
        list.append(Word(phases[0], phases[1], phases[2], mean, assist))

    return list
