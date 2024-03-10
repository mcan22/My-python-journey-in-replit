import random

def choose_word():
    words = ["parkur", "gizemli", "kitaplık", "takvim", "gökyüzü", "sandık"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Hoş geldiniz! Hangman oyununa başlıyoruz.")
    selected_word = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    while True:
        current_display = display_word(selected_word, guessed_letters)
        print("\nKelime:", current_display)

        if current_display == selected_word:
            print("Tebrikler! Kelimeyi doğru tahmin ettiniz. Kazandınız!")
            break

        guess = input("Bir harf tahmin edin: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("Bu harfi zaten tahmin ettiniz. Lütfen başka bir harf deneyin.")
            elif guess in selected_word:
                print("Harika! Doğru tahmin ettiniz.")
                guessed_letters.append(guess)
            else:
                print("Üzgünüm, yanlış tahmin. Bir hakkınız gitti.")
                attempts += 1
                if attempts == max_attempts:
                    print("Üzgünüm, hakkınız bitti. Doğru kelime '{}' idi. Kaybettiniz.".format(selected_word))
                    break
        else:
            print("Geçersiz giriş. Lütfen sadece bir harf girin.")

if __name__ == "__main__":
    hangman()
