from dash import dcc
from datetime import date

dcc.DatePickerSingle(
    date=date(2017, 6, 21),
    display_format='MMMM Y, DD'
)