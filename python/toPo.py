import os
import polib

EN_FILE = "../iOSClient/Supporting Files/en.lproj/Localizable.strings"
ZH_FILE = "../iOSClient/Supporting Files/zh-Hant-TW.lproj/Localizable.strings"


def main():

    data = read_localizable_strings(EN_FILE)
    en_po = create(title='English')
    for key, value in data.items():
        new_entry = polib.POEntry(
            msgid=key,
            msgstr=value,  # 初始為空字符串
        )
        # 將新的 entry 添加到 zh.po 中
        en_po.append(new_entry)
    en_po.save("../locales/en.po")

    data = read_localizable_strings(ZH_FILE)
    zh_po = create(title='zh_Hant')
    for key, value in data.items():
        new_entry = polib.POEntry(
            msgid=key,
            msgstr=value,  # 初始為空字符串
        )
        # 將新的 entry 添加到 zh.po 中
        zh_po.append(new_entry)
    zh_po.save("../locales/zh_Hant.po")



def create(title):
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': '1.0',
        'Report-Msgid-Bugs-To': 'you@example.com',
        'POT-Creation-Date': '2007-10-18 14:00+0100',
        'PO-Revision-Date': '2007-10-18 14:00+0100',
        'Last-Translator': 'you <you@example.com>',
        'Language-Team': f'{title} <yourteam@example.com>',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
    }
    return po


def read_localizable_strings(file_path):
    translations = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line.startswith("/*") and "=" in line:
                key, value = line.split("=", 1)
                key = key.strip().strip('"')
                value = value.strip().strip('";')
                translations[key] = value
    return translations


if __name__ == '__main__':
    main()


