import tkinter as tk
from googletrans import Translator
import threading

input_text_buffer = ""
input_lock = threading.Lock()

def translate_to_english(event=None):
    global input_text_buffer
    with input_lock:
        input_text_buffer = input_text_box.get("1.0", "end-1c")
    start_translation()

def start_translation():
    threading.Thread(target=do_translation).start()

def do_translation():
    global input_text_buffer
    with input_lock:
        input_text = input_text_buffer
    translator = Translator()
    try:
        translation = translator.translate(input_text, src='zh-CN', dest='en')
        if translation is not None and translation.text:
            translated_text = translation.text
            translated_text_box.delete("1.0", "end")
            translated_text_box.insert("1.0", translated_text)
        else:
            print("Translation failed or returned empty result.")
    except Exception as e:
        print("An error occurred during translation:", e)


def exit_program():
    root.destroy()

root = tk.Tk()
root.title("实时中译英")

input_label = tk.Label(root, text="请输入中文:")
input_label.pack(anchor="w", padx=10, pady=10)

input_text_box = tk.Text(root, height=5, width=50)
input_text_box.pack(padx=10, pady=10)
input_text_box.bind("<KeyRelease>", translate_to_english)

translated_text_box = tk.Text(root, height=5, width=50)
translated_text_box.pack(padx=10, pady=10)

exit_button = tk.Button(root, text="退出", command=exit_program)
exit_button.pack(side="right", padx=10, pady=10)

root.mainloop()