# customer-journey-analytics
аналитика пути пользователя. Событийная модель, воронки с drop-off, топ-путей, common next events, граф переходов. Дашборд для Product Manager.  Стек: FastAPI, PostgreSQL, pandas, Streamlit, Plotly, NetworkX, Docker.
# customer-journey-analytics

Аналитика пути пользователя: воронки, топ-путей, граф переходов.

## Возможности
- Запись событий пользователя
- Воронка с drop-off по шагам
- Топ-путей пользователей
- Common next events
- Граф переходов
- Streamlit-дашборд

## Быстрый старт
cp .env.example .env
docker-compose up --build

API: http://localhost:8000/docs
Dashboard: http://localhost:8501

## Тесты
pytest tests/ -v

## Лицензия
MIT
