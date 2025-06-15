import pytesseract
import pyautogui
from PIL import ImageChops
from gtts import gTTS
from playsound import playsound
import os
import time
import uuid
import tkinter as tk
import json

# --- Tesseractのパス（必要に応じて調整） ---
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# --- 設定ファイル名 ---
REGION_FILE = "capture_region.json"
PREV_TEXT_FILE = "previous_text.txt"

# --- 範囲選択GUI ---
def select_capture_region():
    region_data = {}

    def on_mouse_down(event):
        region_data["x1"] = root.winfo_pointerx()
        region_data["y1"] = root.winfo_pointery()
        canvas.delete("rect")
        region_data["rect"] = canvas.create_rectangle(
            region_data["x1"], region_data["y1"],
            region_data["x1"], region_data["y1"],
            outline="red", width=2
        )

    def on_mouse_drag(event):
        x2 = root.winfo_pointerx()
        y2 = root.winfo_pointery()
        canvas.coords(region_data["rect"], region_data["x1"], region_data["y1"], x2, y2)

    def on_mouse_up(event):
        region_data["x2"] = root.winfo_pointerx()
        region_data["y2"] = root.winfo_pointery()
        root.quit()
        root.destroy()

    print("🖱 キャプチャ範囲をマウスでドラッグして選択してください...")

    root = tk.Tk()
    root.attributes("-alpha", 0.3)
    root.attributes("-fullscreen", True)
    root.config(bg="gray")
    root.lift()
    root.attributes("-topmost", True)

    canvas = tk.Canvas(root, bg="gray", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    root.mainloop()

    x1 = region_data["x1"]
    y1 = region_data["y1"]
    x2 = region_data["x2"]
    y2 = region_data["y2"]

    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    region = (x, y, w, h)

    with open(REGION_FILE, "w") as f:
        json.dump(region, f)

    return region

# --- 前回読み上げたテキストの読み込み ---
def load_previous_text():
    if os.path.exists(PREV_TEXT_FILE):
        with open(PREV_TEXT_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

# --- 前回テキストの保存 ---
def save_previous_text(text):
    with open(PREV_TEXT_FILE, "w", encoding="utf-8") as f:
        f.write(text)

# --- メイン処理 ---
def main():
    region = select_capture_region()
    interval = 2
    prev_text = load_previous_text()

    print("\U0001f4e1 画面変化検知OCR・読み上げツール 起動中（Ctrl+Cで停止）")

    try:
        while True:
            current_img = pyautogui.screenshot(region=region)
            text = pytesseract.image_to_string(
                current_img, lang="jpn", config="--psm 6 --oem 1"
            ).strip()

            if text and text != prev_text:
                print("\U0001f4dd 読み取ったテキスト:\n", text)
                audio_filename = f"screen_audio_{uuid.uuid4().hex}.mp3"
                try:
                    # 1文字目がはっきりしない問題を回避するため空白や改行を前に付ける
                    adjusted_text = " " + text
                    tts = gTTS(text=adjusted_text, lang="ja")
                    tts.save(audio_filename)
                    playsound(audio_filename)
                    os.remove(audio_filename)
                    save_previous_text(text)
                    prev_text = text
                except Exception as e:
                    print("❌ 音声生成エラー:", e)
            else:
                print("✅ テキスト変化なし、または空白（スキップ）")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\U0001f6d1 終了しました")

if __name__ == "__main__":
    main()
