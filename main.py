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


# 重置測驗的功能
if st.button("重來一次"):
    st.session_state.clear()


# 初始化 Session State
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = []
    st.session_state.answers = {}
    st.session_state.score = 0



# 輸入題目數量
num_questions = st.number_input("請輸入平假名與片假名題目的個別題數：", min_value=1, step=1, value=2)

if st.button("開始測驗"):
    hiragana_quiz = random.sample(list(hiragana_chart.items()), num_questions)
    katakana_quiz = random.sample(list(katakana_chart.items()), num_questions)
    st.session_state.quiz_data = hiragana_quiz + katakana_quiz
    random.shuffle(st.session_state.quiz_data)
    st.session_state.answers = {}
    st.session_state.score = 0

# 顯示測驗問題
if st.session_state.quiz_data:
    st.write("請輸入你的答案：")
    for i, (character, correct_answer) in enumerate(st.session_state.quiz_data, start=1):
        user_input = st.text_input(f"{i}. {character}", key=f"q{i}")
        st.session_state.answers[f"q{i}"] = user_input

    if st.button("提交答案"):
        st.session_state.score = 0
        for i, (character, correct_answer) in enumerate(st.session_state.quiz_data, start=1):
            user_input = st.session_state.answers.get(f"q{i}", "")
            if user_input.strip().lower() == correct_answer:
                st.write(f"{i}. {character}: ✔ 正確! ({correct_answer})")
                st.session_state.score += 1
            else:
                st.write(f"{i}. {character}: ❌ 錯誤! 正確答案是: {correct_answer}")

        st.write(f"測驗結束！你的得分是 {st.session_state.score}/{len(st.session_state.quiz_data)}")
        if st.button("再次挑戰！"):
            st.session_state.answers = {}
            st.session_state.clear()
