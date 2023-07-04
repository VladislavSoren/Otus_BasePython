## Advanced work with django

Summary:
- `CBV` (Class-based views)
- CamelCase (plugin for change case): `Shift + Alt + U`
- `extra_context` is useful attr of `ContextMixin` class
- success_url (redirection when request is success)
- reverse/reverse_lazy = immediately/on call
Notes:


Commands:

Install main dependencies and delete others
```shell
poetry install --only-main --sync
```

Create auto empty migration
```shell
python manage.py makemigrations shop_projects --empty
```
