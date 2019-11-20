# Скрипт для изменения БД «Электронный дневник школы»
Скрипт позволяет исправить оценки, удалить замечания и добавить похвалу конкретному ученику.

## Описание функций

В скрипте несколько функций:
- `find_schoolkid(name)` — находит конкретного ученика по фамилии и имени
- `fix_marks(schoolkid)` — исправляет оценки этого ученика (2→4, 3→5)
- `remove_chastisements(schoolkid)` — удаляет все замечания от учителей
- `create_commendation(schoolkid, lesson_name)` — добавляет похвалу от учителя определённого предмета

## Как использовать

- Положите файл скрипта в корень проекта
- Запустите Django Shell командой `python3 manage.py shell`
- Импортируйте скрипт `import scripts`
- Найдите ученика `schoolkid = scripts.find_schoolkid("Фролов Иван")`
- Запустите нужные вам функции

Код ниже исправляет оценки, удаляет все замечания и добавляет похвалу от учителя истории:
```python
import scripts
schoolkid = scripts.find_schoolkid("Фролов Иван")
scripts.fix_marks(schoolkid)
scripts.remove_chastisements(schoolkid)
scripts.create_commendation(schoolkid, "История")
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
