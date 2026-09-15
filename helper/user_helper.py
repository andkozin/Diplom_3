# helper/user_helper.py
import allure
import requests

from urls import AUTH

class UserHelper:

# Удаление пользователь через api
    @staticmethod
    def delete_user(access_token: str) -> requests.Response:
       
        headers = {"Authorization": f"{access_token}"}
        url = AUTH["user"]

        with allure.step(f"Удаление - API: DELETE {url}"):
            allure.attach(
                f"URL: {url}\nMethod: DELETE\nToken вывод первые 7: {access_token[:7]}...",
                name="Запрос Удаления",
                attachment_type=allure.attachment_type.TEXT,
            )
            response = requests.delete(url=url, headers=headers)
            allure.attach(
                f"Код: {response.status_code}\nТело: {response.text}",
                name="Ответ Удаления",
                attachment_type=allure.attachment_type.TEXT,
            )
            return response