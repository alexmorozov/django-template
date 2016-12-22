from kupola.fabric_class import DjangoFabric,\
    add_class_methods_as_functions


class Fabric(DjangoFabric):
    host = '{{ cookiecutter.production_host }}'
    app_name = '{{ cookiecutter.project_name }}'
    repository = 'git@repo.kupo.la:kupola/{{ cookiecutter.project_name }}.git'
    remote_db_name = '{{ cookiecutter.project_name }}'
    local_db_name = '{{ cookiecutter.local_db_name }}'
    use_bower = True


__all__ = add_class_methods_as_functions(Fabric(), __name__)
