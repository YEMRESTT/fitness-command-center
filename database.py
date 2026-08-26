import sqlite3

DB_NAME = "fitness_tracker.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Günlük Takip Tablosu
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_logs (
        date TEXT PRIMARY KEY,
        taken_calories INTEGER DEFAULT 0,
        weight REAL DEFAULT 0.0,
        water_l REAL DEFAULT 0.0,
        sleep_hours REAL DEFAULT 0.0,
        walk_minutes INTEGER DEFAULT 0,
        walk_steps INTEGER DEFAULT 0,
        walk_calories INTEGER DEFAULT 0
    )
    ''')

    # Egzersiz Kütüphanesi Tablosu
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        sets INTEGER DEFAULT 3,
        reps INTEGER DEFAULT 12,
        cal_per_rep REAL DEFAULT 0.5
    )
    ''')

    # Günlük Egzersiz Kayıtları (Tarih bazlı)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS workout_logs (
        date TEXT,
        exercise_name TEXT,
        sets INTEGER,
        reps INTEGER,
        cal_per_rep REAL,
        total_calories REAL,
        completed INTEGER DEFAULT 0,
        PRIMARY KEY (date, exercise_name)
    )
    ''')

    # Araştırılmış Gerçekçi Varsayılan Kalori Değerleri (Ortalama 70kg birey için)
    # Squat: ~0.32 kcal | Şınav: ~0.45 kcal | Plank: ~0.15 kcal/sn | Lunge: ~0.35 kcal | Burpee: ~1.2 kcal
    default_exercises = [
        ('Squat', 3, 15, 0.35),
        ('Wall Push-up / Şınav', 3, 10, 0.45),
        ('Plank (Saniye)', 3, 30, 0.15),
        ('Lunge', 3, 12, 0.35),
        ('Burpee', 3, 8, 1.20),
        ('Jumping Jack', 3, 20, 0.20)
    ]
    cursor.executemany("INSERT OR IGNORE INTO exercises (name, sets, reps, cal_per_rep) VALUES (?, ?, ?, ?)", default_exercises)
    
    conn.commit()
    conn.close()

def log_daily_data(date_str, data_dict):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    fields = ", ".join([f"{k} = ?" for k in data_dict.keys()])
    values = list(data_dict.values())
    values.append(date_str)
    
    cursor.execute(f"UPDATE daily_logs SET {fields} WHERE date = ?", values)
    if cursor.rowcount == 0:
        cols = ", ".join(list(data_dict.keys()) + ["date"])
        placeholders = ", ".join(["?"] * (len(data_dict) + 1))
        cursor.execute(f"INSERT INTO daily_logs ({cols}) VALUES ({placeholders})", list(data_dict.values()) + [date_str])
        
    conn.commit()
    conn.close()