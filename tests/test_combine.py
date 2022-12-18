import json

import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure import attachment_type


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Oleg Malyshev")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_create_issue_auth_user():
    pass


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Oleg Malyshev")
@allure.feature("Задачи в репозитории")
@allure.story("Не авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_cant_create_issue_not_auth_user():
    pass
    allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Hello, world</h1>", name="Html", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Oleg Malyshev")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь успешно находит задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_search_issue_positive():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")
    allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Hello, world</h1>", name="Html", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
