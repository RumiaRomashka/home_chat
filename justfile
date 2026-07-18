#Just будет выполнять команды через PowerShell
set shell := ["powershell.exe", "-NoLogo", "-Command"]

# Запуск FastAPI приложения через Docker Compose
up:
    docker compose -f compose.yml up --build -d

# Остановка контейнеров
down:
    docker compose down

# Просмотр логов
logs:
    docker compose logs -f

# Перезапуск
restart: 
    docker compose restart

#Отображение списка запущенных контейнеров и их статусов
ps:
    docker compose ps