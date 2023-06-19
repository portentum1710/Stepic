m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
note1, note2, note3 = map(int, input().split())
note1 = f"#{m[note1 - 1]}" if m[note1 - 1] in ("до", "фа") else f"{m[note1 - 1]}"
note2 = f"#{m[note2 - 1]}" if m[note2 - 1] in ("до", "фа") else f"{m[note2 - 1]}"
note3 = f"#{m[note3 - 1]}" if m[note3 - 1] in ("до", "фа") else f"{m[note3 - 1]}"

print(note1, note2, note3)

