from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from core.models.teachers import Teacher

class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher

    id = auto_field(required=False, allow_none=False)
    user_id = auto_field(allow_none=False)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)