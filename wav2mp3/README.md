# Conversor de WAV para MP3
Converte ficheiros .wav para .mp3 via linha de comandos.

## Instalação
```bash
pip install -r requirements.txt
```
Requer ffmpeg instalado no sistema:

- **Linux:** `sudo apt install ffmpeg`
- **macOS:** `brew install ffmpeg`
- **Windows:** `winget install ffmpeg`

## Uso
```
python converter.py song.wav
python converter.py song.wav -b 320k -o ./out
python converter.py ./pasta_com_wavs
```

## Opções
| Flag | O que faz |
|------|-----------|
| `-b` | Bitrate (128k, 192k, 256k, 320k) |
| `-o` | Pasta de saída |

## License
MIT
