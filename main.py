import random
import streamlit as st

# 平假名與羅馬字的對應表
hiragana_chart = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "を": "wo", "ん": "n"
}

katakana_chart = {
    "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
    "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
    "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
    "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
    "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
    "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
    "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
    "ヤ": "ya", "ユ": "yu", "ヨ": "yo",
    "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro",
    "ワ": "wa", "ヲ": "wo", "ン": "n"
}

# Streamlit App
st.title("日語五十音測驗")

# 輸入題目數量
num_questions = st.number_input("請輸入每種題目的題數：", min_value=1, step=1, value=5)

if st.button("開始測驗"):
    hiragana_quiz = random.sample(list(hiragana_chart.items()), num_questions)
    katakana_quiz = random.sample(list(katakana_chart.items()), num_questions)
    quiz_data = hiragana_quiz + katakana_quiz
    random.shuffle(quiz_data)

    score = 0

    for i, (character, correct_answer) in enumerate(quiz_data, start=1):
        user_answer = st.text_input(f"{i}. {character}", key=f"q{i}")
        if user_answer:
            if user_answer.strip().lower() == correct_answer:
                st.write(f"\u2714 正確! ({correct_answer})")
                score += 1
            else:
                st.write(f"\u274C 錯誤! 正確答案是: {correct_answer}")

    st.write(f"測驗結束！你的得分是 {score}/{len(quiz_data)}")
