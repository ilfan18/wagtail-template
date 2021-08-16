# Мой шаблон для Wagtail проектов.

## Документация

### Глобальные настройки сайта

В глобальных настройках сайта содержится информация доступная и используемая на всех страницах сайта. Доступны в разделе "Настройки".

В шаблонах удобно пользоваться тегом `setvar` для сокращения:

```sh
{% load custom_template_tags %} # Загрузка кастомных тегов
{% setvar settings.site_settings.SiteSettings as site_settings %} # "Переименовывание" глобальных настроек
```

Глобальные настроки включают в себя:

Название | Имя переменной | Тип
---------|----------------|-----
Название компании | company_name | text
Описание компании | description | text
Слоган компании | tagline | text
Логотип | logo | image
Телефоны в шапке | header_phones | orderable
Адреса в шапке | header_adresses | orderable
Соц. сети в шапке | header_socials | orderable
Эмейлы в шапке | header_emails | orderable
Телефоны в подвале | footer_phones | orderable
Адреса в подвале | footer_adresses | orderable
Соц. сети подвале | footer_socials | orderable
Эмейлы подвале | footer_emails | orderable
Копирайт | site_copyright | text
Фавикон | favicon | image

Пример использования копирайта в шаблоне:
```sh
{% load custom_template_tags %} # Загрузка кастомных тегов
{% setvar settings.site_settings.SiteSettings as site_settings %} # "Переименовывание" глобальных настроек
<div>
    # Так же доступны и все остальные глобальные настройки
    {{ site_settings.site_copyright }} 
</div>
```

### Глобальные шаблоны

Глобальные шаблоны предназначены для быстрой верстки шаблонов. Они расположены в директории `[project_name]\templates\global_templates` .

Доступны следеющие глобыльные шаблоны:

Название | Принимаемые параметры | Пояснение
---------|-----------------------|----------
logo.html | class | Группа из логотипа, названия и описания компании
phones.html | phones, class | Список из номеров
adresses.html | adresses, class | Список из адресов
socials.html | socials, class | Список из иконок соц. сетей
emails.html | emails, class | Список из эмейлов
favicon.html | icon | Фавиконы разного формата

### Внутряняя страница
Приложение стандартной внутренней страницы наполняется контентом из StreamField, блоки которого поределены в приложении `streams`. Стили и скрипты страницы должны быть в вайлах `css/inner_page.css` и `js/inner_page.js` соответсвенно. 

### Блоки StreamField
Блоки StreamField описаны в приложении `streams` в файле `streams\blocks.py`. Для корректной работы необходимо добавить файлы зависимостей в блоки `extra_css` и `extra_js`:

```sh
{% block extra_css %}
<link rel="stylesheet" type="text/css" href="{% static 'css/swiper-bundle.min.css' %}">
<link rel="stylesheet" type="text/css" href="{% static 'css/streams.css' %}">
{% endblock extra_css %}

{% block extra_js %}
<script type="text/javascript" src="{% static 'js/streams.js' %}"></script>
<script type="text/javascript" src="{% static 'js/swiper-bundle.min.js' %}"></script>
<script type="text/javascript" src="{% static 'js/fslightbox.js' %}"></script>
{% endblock extra_js %}
```