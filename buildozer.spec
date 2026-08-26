[app]

# Назва твого додатку
title = AstroApp

# Ім'я папки пакету
package.name = astroapp
package.domain = org.astro

# Які файли включати у збірку
source.dir = .
source.exts = py,png,jpg,kv,atlas

# Версія додатку
version = 0.1

# Головні залежності (обов'язково вказуємо kivymd і фіксуємо сумісний cython)
requirements = python3,kivy,https://github.com/kivymd/KivyMD/archive/master.zip,pillow,requests

# Фіксуємо стабільну версію cython, щоб уникнути помилок компіляції
cython_version = 0.29.36

# Орієнтація екрана (портретна)
orientation = portrait

# Дозволи для інтернету (потрібні для зв'язку з малинкою/Astroberry)
android.permissions = INTERNET

# Версії Android API (рекомендовані для стабільної збірки)
android.api = 33
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.accept_sdk_license = True
