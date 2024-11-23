import eel

eel.init("web")

@eel.expose
def calculate_damage(damage):
    try:
        damage = float(damage)
        if damage < 0:
            return {"error": "Число не может быть меньше нуля!"}
        
        return {
            "damage1": round(damage * 2.4),
            "damage2": round(damage * 4.2),
            "damage3": round(damage * 6.4),
            "damage4": round(damage * 9),
            "damage5": round(damage * 12),
            "damage6": round(damage * 15.39),
            "damage7": round(damage * 20),
        }
    except ValueError:
        return {"error": "Введите корректное число!"}

try:
    eel.start("main.html", size=(100, 100), mode="chrome")
except Exception:
    print("Chrome не найден, открываем в браузере по умолчанию...")
    eel.start("main.html", size=(100, 100), mode="None")