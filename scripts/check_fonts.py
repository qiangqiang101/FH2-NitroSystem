# Checks that every translation in l10n/*.po only uses characters the game's fonts for that language have, so none
# of them shows as a box in game. Also checks the English in l10n/NitroSystem.pot.
#   python scripts/check_fonts.py "<Mount>/media/ui/Fonts.zip"
#
# The game picks fonts by language (fontsettings.xml in Fonts.zip): the Anthem fonts for Latin text, with Verdana
# behind them for Russian, and a Japanese, Korean or Chinese font that holds only the characters the game's own
# text uses. A .vfont has its glyph count at 0x80 and, from 0xC0, a 28-byte record per glyph starting with its code
# point (see ANNA Drone Mode's gamefont.cpp). The PO files are read with the platform's own reader
# (platform/tools/l10n/pofile.py), so what's checked is what the platform reads.
import struct
import sys
import zipfile
from pathlib import Path

sys.dont_write_bytecode = True   # no __pycache__ in the platform submodule
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "platform" / "tools" / "l10n"))
import pofile  # noqa: E402

# The font behind the Latin one, by PO file (language) name
FALLBACK = {"ja": "DFGHSGothic-W5", "ko": "MalgunBdGm", "zh_Hant": "DFYuanMedium-B5", "ru": "verdana"}


def code_points(data):
    count = struct.unpack_from("<I", data, 0x80)[0]
    return {struct.unpack_from("<I", data, 0xC0 + 28 * i)[0] for i in range(count)}


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: check_fonts.py <Fonts.zip>")
    fonts = zipfile.ZipFile(sys.argv[1])
    glyphs = {Path(n).stem: code_points(fonts.read(n)) for n in fonts.namelist() if n.endswith(".vfont")}
    latin = glyphs["Anthem_A"]

    files = [ROOT / "l10n" / "NitroSystem.pot"] + sorted((ROOT / "l10n").glob("*.po"))
    problems = texts = 0
    for path in files:
        lang = path.stem if path.suffix == ".po" else "en"
        have = latin | glyphs.get(FALLBACK.get(lang, ""), set())
        for e in pofile.parse(path.read_text(encoding="utf-8"), path.name):
            if e.is_header():
                continue
            for text in (e.forms() if lang != "en" else [e.msgid]):
                texts += 1
                missing = sorted({c for c in text if ord(c) not in have})
                if missing:
                    print(f"{path.name} {e.ctxt}: {''.join(missing)} not in its font, in {text[:60]!r}")
                    problems += 1
    print(f"{texts} texts in {len(files)} files: {problems} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
