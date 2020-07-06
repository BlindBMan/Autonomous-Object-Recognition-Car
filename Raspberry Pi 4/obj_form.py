from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, validators


class ObjForm(FlaskForm):
    obj = SelectField(
        'Object',
        [validators.input_required()],
        choices=[('perfume_bottle', 'Perfume bottle'), ('cup', 'Cup')]
    )
    submit = SubmitField('Find')
