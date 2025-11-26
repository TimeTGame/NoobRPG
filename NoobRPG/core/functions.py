__all__ = ('get_filterable_fields')


def get_filterable_fields(model, depth=1, prefix=''):
    fields = set()
    for field in model._meta.get_fields():

        field_full_name = f'{prefix}{field.name}' if prefix else field.name

        fields.add(field_full_name)

        if depth > 0:
            if field.is_relation and not field.auto_created:
                related_model = field.related_model
                if related_model:
                    sub_fields = get_filterable_fields(
                        related_model,
                        depth=depth - 1,
                        prefix=f'{field_full_name}__',
                    )
                    fields.update(sub_fields)
    return fields
