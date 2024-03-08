#僅把 zh_Hant.po 轉成 Localizable.strings
import os
import polib

# 獲取腳本所在目錄的絕對路徑
script_dir = os.path.dirname(os.path.abspath(__file__))

# 使用 os.path.join 來構建檔案的絕對路徑
ZH_PO_FILE = os.path.join(script_dir, "../locales/zh_Hant.po")
ZH_STRINGS_FILE = os.path.join(script_dir, "../iOSClient/Supporting Files/zh-Hant-TW.lproj/Localizable.strings")

def po_to_localizable_strings():
    po = polib.pofile(ZH_PO_FILE)
    with open(ZH_STRINGS_FILE, 'w', encoding='utf-8') as f:
        for entry in po:
            if entry.msgid and entry.msgstr:
                line = f'"{entry.msgid}" = "{entry.msgstr}";\n'
                f.write(line)

if __name__ == '__main__':
    po_to_localizable_strings()

