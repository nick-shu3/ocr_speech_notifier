````markdown
## 🇯🇵 日本語版 README.md

# 📡 OCR画面変化検知・読み上げツール

このツールは、指定した画面領域を定期的にキャプチャし、OCR（光学文字認識）を使って文字を抽出、前回と違う内容が検出された場合に日本語で読み上げるデスクトップユーティリティです。

## 🔧 機能概要

- キャプチャ範囲はマウスで自由に選択可能
- 画面の変化を自動的に検知
- 変化があった場合にOCRで文字抽出し、TTSで音声読み上げ
- Google Text-to-Speech（gTTS）を使用

## 🖥 使用方法

### 1. 環境構築

```bash
pip install -r requirements.txt
````

### 2. 実行

```bash
python ocr_speech_notifier.py
```

起動後、画面上でマウスをドラッグしてキャプチャ範囲を選択してください。

## 📦 必要ライブラリ

* pytesseract
* pyautogui
* Pillow
* gTTS
* playsound

## ⚠ 前提条件

* Windows 環境での動作を想定
* Tesseract OCR がインストールされており、パスが正しく設定されている必要があります

## 📝 ライセンス

MIT License

---

## 🇺🇸 English Version README.md

# 📡 OCR Screen Change Detector and Text-to-Speech Notifier

This is a desktop utility that periodically captures a selected screen region, performs OCR to extract any visible text, and uses text-to-speech (TTS) to read it aloud — but only if the content has changed since the last scan.

## 🔧 Features

* Freely select the screen capture area with your mouse
* Automatically detects changes in the screen
* Performs OCR and reads new content aloud
* Uses Google Text-to-Speech (gTTS)

## 🖥 Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the tool

```bash
python ocr_speech_notifier.py
```

Upon starting, you'll be prompted to drag and select the screen region to monitor.

## 📦 Required Libraries

* pytesseract
* pyautogui
* Pillow
* gTTS
* playsound

## ⚠ Prerequisites

* Works on Windows
* Tesseract OCR must be installed and correctly referenced in the script

## 📝 License

MIT License

````
