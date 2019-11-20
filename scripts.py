from datacenter.models import Schoolkid, Lesson, Mark, Chastisement, Commendation
from random import choice
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


commendation_phrases = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!"]


def find_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        return schoolkid
    except MultipleObjectsReturned:
        print("С таким именем найдено несколько учеников. Уточните имя")
    except ObjectDoesNotExist:
        print("Учеников с таким именем не найдено. Введите другое имя")


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in marks:
        if mark.points == 2:
            mark.points = 4
        elif mark.points == 3:
            mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid__full_name__contains=schoolkid.full_name).delete()


def create_commendation(schoolkid, lesson_name):
    lesson = Lesson.objects.filter(
        subject__title=lesson_name,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter).order_by('-date')[0]

    Commendation.objects.create(
        text=choice(commendation_phrases),
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher)
