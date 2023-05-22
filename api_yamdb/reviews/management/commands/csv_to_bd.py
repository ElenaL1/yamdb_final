# Файл вызывается командой python manage.py csv_to_bd
import os

from django.conf import settings
from django.core.management.base import BaseCommand

import pandas as pd
from sqlalchemy import create_engine

from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title
from api_yamdb.settings import CSV_FILES_DIR

FILES_MODELS = {
    'category.csv': Category,
    'comments.csv': Comment,
    'genre_title.csv': GenreTitle,
    'genre.csv': Genre,
    'review.csv': Review,
    'titles.csv': Title,
}


class Command(BaseCommand):
    help = 'Загрузка данных в базу из csv-файлов'

    def handle(self, *args, **options):
        for csv_file, model in FILES_MODELS.items():
            csv_path = os.path.join(CSV_FILES_DIR, csv_file)
            data = pd.read_csv(csv_path)
            if csv_file == 'titles.csv':
                data.insert(2, 'description', None)
                data.rename(columns={'category': 'category_id'}, inplace=True)
            if csv_file == 'comments.csv' or csv_file == 'review.csv':
                data.rename(columns={'author': 'author_id'}, inplace=True)
            # engine = create_engine('sqlite:///db.sqlite3')

            user = settings.DATABASES['default']['USER'],
            password = settings.DATABASES['default']['PASSWORD'],
            database_name = settings.DATABASES['default']['NAME'],

            database_url = ('postgresql://{user}:{password}@db:5432/\
                            {database_name}'.format
                            (user=user, password=password,
                                database_name=database_name,)
                            )
            engine = create_engine(database_url, echo=False)
            data.to_sql(model._meta.db_table, if_exists='replace',
                        con=engine, index=False)
        print('Данные из csv-файлов записаны в базу?')
