"""
wav to mp3 converter
by Daniel Luis
github.com/danieldluis
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from pydub import AudioSegment
except ImportError:
    sys.exit("pydub nao instalado. corre: pip install pydub")


BITRATES = ["128k", "192k", "256k", "320k"]


def convert(wav_path, output_dir=None, bitrate="192k"):
    wav_path = Path(wav_path)
    if not wav_path.exists():
        print(f"  [!] nao encontrado: {wav_path}")
        return False

    out_dir = Path(output_dir) if output_dir else wav_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    mp3_path = out_dir / (wav_path.stem + ".mp3")

    print(f"  [>] {wav_path.name} -> {mp3_path.name} ({bitrate})")
    audio = AudioSegment.from_wav(str(wav_path))
    audio.export(str(mp3_path), format="mp3", bitrate=bitrate)
    print(f"  [ok] {mp3_path}")
    return True


def batch(input_dir, output_dir=None, bitrate="192k"):
    # converte todos os .wav de uma pasta
    input_dir = Path(input_dir)
    wav_files = sorted(input_dir.glob("*.wav"))

    if not wav_files:
        print(f"[!] nenhum .wav em {input_dir}")
        return

    print(f"\npasta: {input_dir}")
    print(f"ficheiros: {len(wav_files)}\n")

    ok, fail = 0, 0
    for f in wav_files:
        if convert(str(f), output_dir, bitrate):
            ok += 1
        else:
            fail += 1

    print(f"\n{'=' * 30}")
    print(f"  {ok} ok, {fail} falharam")


def main():
    parser = argparse.ArgumentParser(
        description="wav to mp3 converter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
exemplos:
  python converter.py song.wav
  python converter.py song.wav -b 320k -o ./out
  python converter.py ./musicas
        """
    )
    parser.add_argument("input", help="ficheiro .wav ou pasta")
    parser.add_argument("-b", "--bitrate", default="192k", choices=BITRATES)
    parser.add_argument("-o", "--output", default=None)

    args = parser.parse_args()

    if os.path.isdir(args.input):
        batch(args.input, args.output, args.bitrate)
    else:
        convert(args.input, args.output, args.bitrate)


if __name__ == "__main__":
    main()   