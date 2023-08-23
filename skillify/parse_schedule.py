import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillify.settings')
django.setup()

from bs4 import BeautifulSoup
from education.models import Schedule, Subject

# Пример HTML с таблицей (замените на свою таблицу)
html = """
<div class="content_box">
  <h1 data-attr="title" data-guid="45071">Расписание 1 класс</h1>  <div class="html_block post"><h1><span style="color: #003366;">Расписание учебных занятий в&nbsp;I классах на II полугодие 2022/2023 учебного года</span></h1>
<table border="2">
<tbody>
<tr>
<td style="text-align: center;">
<p><span style="color: #003366;"><strong>&nbsp;</strong></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #003366;"><strong>I А</strong></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #003366;"><strong>I Б</strong></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #003366;"><strong>I В</strong></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #003366;"><strong>I Г</strong></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #003366;"><strong>I Д</strong></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #003366;"><strong>I Е</strong></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #003366;"><strong>I Ж</strong></span></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПН</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПН</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПН</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПН</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПН</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПН</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПН</em></span></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>0</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>КЛ. ЧАС</p>
</td>
<td style="text-align: center;">
<p>КЛ. ЧАС</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>1</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ЧЕЛ.И МИР</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>2</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p></p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>3</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ТРУД.ОБУЧ.</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>ТРУД . ОБУЧ.</p>
</td>
<td style="text-align: center;">
<p></p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>4</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ЧЕЛ.И МИР</p>
</td>
<td style="text-align: center;">
<p>ЧЕЛ. И МИР</p>
</td>
<td style="text-align: center;">
<p>ЧЕЛ. И МИР</p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>5</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>КЛ. ЧАС</p>
</td>
<td style="text-align: center;">
<p>КЛ. ЧАС</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>КЛ. ЧАС</p>
</td>
<td style="text-align: center;">
<p>КЛ. ЧАС</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>&nbsp;</strong></span></em></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ВТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ВТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ВТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ВТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ВТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ВТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ВТ</em></span></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>0</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>1</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>БЕЛ. ЯЗЫК</p>
</td>
<td style="text-align: center;">
<p>БЕЛ. ЯЗЫК</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>МУЗЫКА</p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
<td style="text-align: center;">
<p>БЕЛ. ЯЗЫК</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>2</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>МУЗЫКА</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>3</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>БЕЛ. ЯЗЫК</p>
</td>
<td style="text-align: center;">
<p>МУЗЫКА</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>4</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>5</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>ПЗ</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
<td style="text-align: center;">
<p>СЗ</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>&nbsp;</strong></span></em></p>
</td>
<td style="text-align: center;">
<p><em><span style="color: #008080;">СР</span></em></p>
</td>
<td style="text-align: center;">
<p><em><span style="color: #008080;">СР</span></em></p>
</td>
<td style="text-align: center;">
<p><em><span style="color: #008080;">СР</span></em></p>
</td>
<td style="text-align: center;">
<p><em><span style="color: #008080;">СР</span></em></p>
</td>
<td style="text-align: center;">
<p><em><span style="color: #008080;">СР</span></em></p>
</td>
<td style="text-align: center;">
<p><em><span style="color: #008080;">СР</span></em></p>
</td>
<td style="text-align: center;">
<p><em><span style="color: #008080;">СР</span></em></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>0</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>СЗ</p>
</td>
<td style="text-align: center;">
<p>СЗ</p>
</td>
<td style="text-align: center;">
<p>ПЗ</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>1</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
<td style="text-align: center;">
<p>БЕЛ. ЯЗЫК</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>2</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>БЕЛ. ЯЗЫК</p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>3</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>4</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>ТРУД. ОБУЧ.</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>БЕЛ. ЯЗЫК</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>5</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>СЗ</p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
<td style="text-align: center;">
<p>ПЗ</p>
</td>
<td style="text-align: center;">
<p>ПЗ</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>&nbsp;</strong></span></em></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ЧТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ЧТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ЧТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ЧТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ЧТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ЧТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ЧТ</em></span></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>0</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ПЗ</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>1</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ЧЗС</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>МУЗЫКА</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>2</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>МУЗЫКА</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>3</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ФИЗ. К. И ЗД.</p>
</td>
<td style="text-align: center;">
<p>МУЗЫКА</p>
</td>
<td style="text-align: center;">
<p>ЧЕЛ.И МИР</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>4</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
<td style="text-align: center;">
<p>ТРУД. ОБУЧ.</p>
</td>
<td style="text-align: center;">
<p>МУЗЫКА</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>ЧЕЛ. И МИР</p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
<td style="text-align: center;">
<p>ТРУД. ОБУЧ.</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>5</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>ИНФ.Ч</p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>&nbsp;</strong></span></em></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПТ</em></span></p>
</td>
<td style="text-align: center;">
<p><span style="color: #008080;"><em>ПТ</em></span></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>0</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>ПЗ</p>
</td>
<td style="text-align: center;">
<p>СЗ</p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>1</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ЧЗС</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ЧТЕНИЕ</p>
</td>
<td style="text-align: center;">
<p>ЧЕЛ.И МИР</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>2</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ЧЗС</p>
</td>
<td style="text-align: center;">
<p>ПИСЬМО</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ЧЗС</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>3</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ЧЗС</p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>МАТЕМ.</p>
</td>
<td style="text-align: center;">
<p>ЧЗС</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>4</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>ИЗОБР. ИСК.</p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
<td style="text-align: center;">
<p>ТРУД. ОБУЧ.</p>
</td>
<td style="text-align: center;">
<p>ЧЗС</p>
</td>
<td style="text-align: center;">
<p>ТРУД. ОБУЧ.</p>
</td>
<td style="text-align: center;">
<p>ФЗ</p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><em><span style="color: #008080;"><strong>5</strong></span></em></p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
<td style="text-align: center;">
<p>СЗ</p>
</td>
<td style="text-align: center;">
<p>СЗ</p>
</td>
<td style="text-align: center;">
<p>&nbsp;</p>
</td>
</tr>
</tbody>
</table>
<p></p></div>

</div>
"""


soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')[1:]


for row in rows:
    columns = row.find_all('td')
    day_of_week = columns[0].text
    lesson_number = columns[1].text
    subject_name = columns[2].text


    subject, created = Subject.objects.get_or_create(name=subject_name)


    schedule_entry = Schedule.objects.create(
        day=day_of_week,
        lesson_number=lesson_number,
    )
    schedule_entry.subject.add(subject)
