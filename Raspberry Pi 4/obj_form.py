from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class ObjForm(FlaskForm):
    obj = SelectField(
        'Object',
        choices=[('perf_btl', 'Perfume bottle'), ('cup', 'Cup')]
    )
    submit = SubmitField('Find')
