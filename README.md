# Diplom_3: Автотесты UI для Stellar Burgers

Автотесты для Stellar Burgers (stellarburgers.education-services.ru) по заданию 3.  
Page Object. Браузеры: Chrome, Firefox. Отчёт: Allure.

---

## Что протестировано

**Конструктор бургеров:**
- переходы между разделами (Конструктор - Лента заказов);
- открытие и закрытие модального окна ингредиента;
- увеличение счётчика ингредиента при добавлении в корзину (drag‑and‑drop).

**Лента заказов:**
- рост счётчиков Выполнено за всё время и Выполнено за сегодня после заказа
- появление номера заказа в секции В работе

---

## Как запустить

rm -rf allure-results/

pytest tests/ -v --alluredir=allure-results

allure serve allure-results

zip -r allure-results.zip allure-results/
